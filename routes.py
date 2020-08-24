from starlette.routing import Route, Mount
from views import homepage, about
from starlette.staticfiles import StaticFiles
import pathlib
HERE = pathlib.Path(__file__).parent
routes = [
    Route("/", endpoint=homepage),
    Route("/home", endpoint=homepage),
    Route("/about", endpoint=about),
    Mount('/static', StaticFiles(directory=str(HERE/'static')), name='static')
]
