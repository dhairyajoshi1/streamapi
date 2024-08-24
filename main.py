import json
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio


app = FastAPI()


async def fake_data_streamer():
    for i in range(10):
        yield json.dumps({"name": "stream"})
        await asyncio.sleep(0.5)     
    
    print("done")

    
@app.get('/')
async def main():
    return StreamingResponse(fake_data_streamer(), media_type='text/event-stream')