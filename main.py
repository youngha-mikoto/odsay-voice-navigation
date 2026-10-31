from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI")


@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health():
    return {"status": "ok"}
