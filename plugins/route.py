#rymme
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("CRYSTAL TELEGRAM | https://t.me/Crystal_Anime_Index")
