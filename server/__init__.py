from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .setting import debug
template = Jinja2Templates(directory="./server/template").TemplateResponse
app = FastAPI(debug=debug, root_path="/api/v1")
app.mount("/static", StaticFiles(directory="./server/static"), name="static")


@app.get("/")
def home(request: Request):
    return template("index.html", {"request": request})
from server.user import account

