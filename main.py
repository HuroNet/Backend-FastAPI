from fastapi import FastAPI

app=FastAPI(title='Proyecto para peliculas',
            description='en este poryecto seremos capaces de rese;ar pelis',
            version='1')


@app.get('/')
async def index():
    return 'Hola mundo'

@app.get('/about')
async def about():
    return 'About'