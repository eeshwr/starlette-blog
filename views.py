
from starlette.responses import JSONResponse


async def homepage(request):
    return JSONResponse({'hello': 'home page'})


async def about(request):
    return JSONResponse({'hello': 'about page'})
