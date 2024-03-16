from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 정적 파일을 제공하기 위해 디렉터리 지정

# 루트 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def read_index():
    # HTML 파일의 내용을 읽어 반환
    with open("index.html", "r") as file:
        content = file.read()
    return content

@app.post("/upload")
async def upload_files(excel_file: UploadFile = File(...), ppt_file: UploadFile = File(...)):
    excel_file, ppt_file
    # 업로드된 파일을 처리하는 코드를 여기에 추가
    return {"excel_file_size": len(await excel_file.read()), "ppt_file_size": len(await ppt_file.read())}
