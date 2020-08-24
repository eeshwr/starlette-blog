
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
import pathlib
HERE = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=str(HERE/'templates'))


async def homepage(request):
    context = {
                    "request": request,
                    "title": "hello post",
                    "id": 1,
                    "name": "ishmaira",
                    "content": "this is content",
                    "date_posted": "this is posted date"
                }
    return templates.TemplateResponse('home.html', context=context)


async def about(request):
    return JSONResponse({'hello': 'about page'})
