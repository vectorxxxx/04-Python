#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'VectorX'

import asyncio

import orm
from models import User


async def test():
    password = input('Enter your password: ')
    loop = asyncio.get_event_loop()
    await orm.create_pool(loop=loop, user='root', password=password, db='test')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()


async def main():
    await test()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())