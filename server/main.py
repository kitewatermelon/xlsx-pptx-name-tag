from fastapi import FastAPI, APIRouter, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from nameplate import make_nameplate
from starlette.background import BackgroundTasks

import time
import os

router = APIRouter(
    prefix="/nameplate",
    tags=['nameplate'],
    responses={404: {"description": "Not found"}}
)
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") 


@app.get("/", response_class=HTMLResponse)
async def read_all_by_user(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})

@app.get("/help",response_class=HTMLResponse)
async def get_help(request: Request):
    return templates.TemplateResponse("help.html", {"request":request})

UPLOAD_DIR = "./files"

@app.post("/upload")
async def upload_files(excel_file: UploadFile = File(...), pptx_file: UploadFile = File(...)):
    timestamp = str(time.time())
    # 엑셀 파일 처리
    excel_contents = await excel_file.read()
    pptx_contents = await pptx_file.read()
    with open(f"{UPLOAD_DIR}/{timestamp + excel_file.filename}", "wb") as excel_fp:
        excel_fp.write(excel_contents)

    # PPTX 파일 처리
    with open(f"{UPLOAD_DIR}/{timestamp + pptx_file.filename}", "wb") as pptx_fp:
        pptx_fp.write(pptx_contents)

    # 리디렉션할 때 쿼리 매개변수를 함께 전달
    return RedirectResponse(url=f'/process?timestamp={timestamp}&excel_filename={excel_file.filename}&pptx_filename={pptx_file.filename}')

@app.post("/process")
async def process_files(timestamp: str, excel_filename: str , pptx_filename: str, bg_tasks: BackgroundTasks):
    try:
        ppt = make_nameplate(f"{UPLOAD_DIR}/{timestamp+excel_filename}", f"{UPLOAD_DIR}/{timestamp+pptx_filename}")
        ppt_path = os.path.join(UPLOAD_DIR, f"{timestamp}_nameplate.pptx")
        ppt.save(ppt_path)
        
        os.remove(f"{UPLOAD_DIR}/{timestamp + excel_filename}")
        os.remove(f"{UPLOAD_DIR}/{timestamp + pptx_filename}")
        
        bg_tasks.add_task(os.remove, ppt_path)

        return FileResponse(path=ppt_path, 
                            filename=f"nameplate.pptx")
        
    except FileNotFoundError as e:
        error_message = f"파일이 없습니다. 다시 시도해주세요. "
        return JSONResponse(status_code=404, content={"error": error_message})
    except Exception as e:
        error_message = f"파일이 선택되지 않았습니다. 다시 시도하세요. 그래도 에러 발생 시 관리자에게 문의 주세요."
        return JSONResponse(status_code=500, content={"error": error_message})
 