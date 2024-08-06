from fastapi import FastAPI

app = FastAPI(title="project", description="peliculas", version="1")


@app.get("/")
async def index():
    return "Project of backend"


@app.get("/about")
async def about():
    return "About"
