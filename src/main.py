from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("", response_class=HTMLResponse)
def index():
    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """
