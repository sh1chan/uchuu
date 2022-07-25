#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
  import asyncio

  from src.networking.server import ATCPServer

  async_tcp_server = ATCPServer()

  asyncio.run(async_tcp_server.main())
