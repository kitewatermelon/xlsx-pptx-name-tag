from fastapi import FastAPI, APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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