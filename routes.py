from starlette.routing import Route 
from views import homepage, about
routes = [
    Route("/", endpoint=homepage),
    Route("/home", endpoint=homepage),
    Route("/about", endpoint=about),
]
