
import asyncio
import websockets

peers = set()

async def handler(ws):
    peers.add(ws)
    try:
        async for msg in ws:
            for peer in peers:
                if peer != ws:
                    await peer.send(msg)
    finally:
        peers.remove(ws)

def start():
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(handler, "0.0.0.0", 9200)
    )
    asyncio.get_event_loop().run_forever()
