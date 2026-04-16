import os
import threading
import time
import random

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from contextlib import asynccontextmanager

from backend.db import init_db

DIST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend", "dist")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


if os.path.exists(DIST_DIR):
    app.mount(
        "/static",
        StaticFiles(directory=os.path.join(DIST_DIR, "assets")),
        name="static",
    )

    @app.get("/")
    def serve_index():
        index_path = os.path.join(DIST_DIR, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        return HTMLResponse("<h1>RetroReel MP</h1><p>Build frontend first</p>")
else:

    @app.get("/")
    def serve_placeholder():
        return HTMLResponse("""
        <html>
        <head><title>RetroReel MP</title>
        <body style="background:#16171d;color:#fff;font-family:sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;">
            <div style="text-align:center;">
                <h1>RetroReel MP</h1>
                <p>Run <code>cd frontend && npm run build</code> to build the frontend</p>
            </div>
        </body>
        </html>
        """)


def run_server(port: int):
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="error")


def get_free_port():
    while True:
        port = random.randint(10000, 65535)
        try:
            import socket

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("127.0.0.1", port))
            sock.close()
            return port
        except:
            continue


if __name__ == "__main__":
    import webview

    port = get_free_port()
    server_thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()
    time.sleep(1)

    webview.create_window(
        "RetroReel MP",
        f"http://127.0.0.1:{port}",
        width=1200,
        height=800,
        resizable=True,
    )
    webview.start()
