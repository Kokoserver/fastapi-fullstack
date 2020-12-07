from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
template = Jinja2Templates(directory="template").TemplateResponse
app.mount("/static", StaticFiles(directory="static"), name="static")

from server import account





