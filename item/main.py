import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from item_api.item_handler import router

app = FastAPI()
app.include_router(router)

#Mounting the static files for the templates
template = Jinja2Templates(directory="item/templates")
app.mount("/static", StaticFiles(directory="item/static"), name="static")

#Adding the cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

#Adding the templates files to the routes of the application
@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return template.TemplateResponse("login.html", {"request":request})

@app.get('/item-page', response_class=HTMLResponse)
async def read_root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get('/summary', response_class=HTMLResponse)
async def read_summary(request: Request):
    return template.TemplateResponse("summary.html", {"request": request})

#Running the uvicorn server

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)