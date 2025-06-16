import asyncio
import json

import websockets

_server: websockets.Server | None = None


def send_action(action: str):
    assert _server is not None
    websockets.broadcast(_server.connections, json.dumps({"action": action}))


async def handler(websocket: websockets.ServerConnection):
    assert _server is not None
    print("client connected", len(_server.connections))
    await websocket.wait_closed()
    print("client disconnected", len(_server.connections))


async def create_dummy():
    async for websocket in websockets.connect("ws://localhost:22708"):
        try:
            print("dummy connected")
            async for _ in websocket:
                pass
        except websockets.ConnectionClosed:
            print("dummy disconnected")


async def start():
    global _server
    async with websockets.serve(handler, "localhost", 22708) as server:
        _server = server
        await asyncio.gather(server.serve_forever(), create_dummy())
