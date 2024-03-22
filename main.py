from fastapi import FastAPI, APIRouter, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
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
async def read_all_by_user(request: Request, file: UploadFile):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/upload")
async def upload_files(excel_file: UploadFile = File(...), pptx_file: UploadFile = File(...)):
    UPLOAD_DIR = "./files"
    
    # 엑셀 파일 처리
    excel_contents = await excel_file.read()
    with open(f"{UPLOAD_DIR}/{excel_file.filename}", "wb") as excel_fp:
        excel_fp.write(excel_contents)

    # PPTX 파일 처리
    pptx_contents = await pptx_file.read()
    with open(f"{UPLOAD_DIR}/{pptx_file.filename}", "wb") as pptx_fp:
        pptx_fp.write(pptx_contents)

    return {"message": "Files uploaded successfully"}
