
import asyncio
import websockets

connected = set()

async def handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            for ws in connected:
                if ws != websocket:
                    await ws.send(message)
    finally:
        connected.remove(websocket)

def start():
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handler, "0.0.0.0", 8765)
    )
    asyncio.get_event_loop().run_forever()
