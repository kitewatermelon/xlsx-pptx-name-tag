from fastapi import FastAPI, APIRouter, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from nameplate import make_nameplate
import time
import os
UPLOAD_DIR = "./files"

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
    return templates.TemplateResponse("index.html", {"request":request})

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
async def process_files(timestamp: str, excel_filename: str , pptx_filename: str):

    ppt = make_nameplate(f"{UPLOAD_DIR}/{excel_filename}", f"{UPLOAD_DIR}/{pptx_filename}")
    ppt_path = os.path.join(UPLOAD_DIR, f"{timestamp}_nameplate.pptx")
    ppt.save(ppt_path)
    return FileResponse(path=ppt_path, filename=f"{timestamp}_nameplate.pptx")
