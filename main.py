from fastapi import FastAPI

app = FastAPI(title="project", description="peliculas", version="1")


@app.get("/")
async def index():
    return "Hola mundo"


@app.get("/about")
async def about():
    return "About"
