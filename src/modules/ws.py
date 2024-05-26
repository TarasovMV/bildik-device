import asyncio
import websockets
import json

import shared


async def ws_handler(uri, ws_receive_stack):
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                # Получение данных по вебсокетам
                json_string = await websocket.recv()
                data = json.loads(json_string)
                with shared.ws_receive_lock:
                    ws_receive_stack.append(data)

            except Exception as e:
                print(f"Error: {e}")

def init_ws(ws_receive_stack):
    websocket_uri = "wss://bildik.m-tarasov.com/ws"
    # websocket_uri = "ws://localhost:3333/ws"
    asyncio.get_event_loop().run_until_complete(ws_handler(websocket_uri, ws_receive_stack))