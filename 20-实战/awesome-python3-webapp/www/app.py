#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'VectorX'

import logging;

from aiohttp import web

logging.basicConfig(level=logging.INFO)

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    # return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
    # 用谷歌没问题，非谷歌得用上面写法指明内容类型
    return web.Response(body=b'<h1>Awesome</h1>')


async def init():
    app = web.Application()
    app.add_routes(index)
    logging.info('server started at http://localhost:9000...')
    return app


web.run_app(init(), host='localhost', port=9000)
