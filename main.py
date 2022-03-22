from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional, List
import uvicorn


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')


templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
def index(request: Request):

    context = {'request': request, 'message':'Hello World from FastAPI'}

    return templates.TemplateResponse('index.html', context)

if __name__ == '__main__':
    uvicorn.run(app)
