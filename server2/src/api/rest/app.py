from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.exception_handler(Exception)
def handle_any_exception(request: Request, exception: Exception):
    return JSONResponse(content={
        "exception": exception.__class__.__name__,
        "message": str(exception)
    })


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
