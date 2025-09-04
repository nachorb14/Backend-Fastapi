from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#ROUTERS
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

#Recursos Estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

#Url local: http://127.0.0.1:8000

@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }

#Url local mas url de curso: http://127.0.0.1:8000/url


#Inicia el server: uvicorn main:app --reload
#Detener el server: CTRL + C

#Documentación con Swagger: http://127.0.0.1:8000/docs
#Documentación con Redocly: http:77127.0.0.1:8000/redoc