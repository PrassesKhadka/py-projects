# FASTAPI concurrency

Example with websockets:

```
@app.websocket("/ws/")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    while True:
        data=await websocket.receive_text()
        await websocket.send_text(f"Message text wat: {data}")
```

Example with StreamingResponse

- Response Streaming

```
def generate_data():
    for i in range(10):
        yield f"data:{i}\n\n"
        time.sleep(1)

@app.get("/stream/")
def stream_data():
    return StreamingResponse(generate_data(),media_type="text/plain")

```

- Request Streaming

```
@app.post("/upload/")
async def upload_data(request:Request):
    async for chunk in request.stream():
        process_chunk(chunk)
```
