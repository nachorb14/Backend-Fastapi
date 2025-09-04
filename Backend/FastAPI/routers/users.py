from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user",tags=["user"])

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id= 1,name="Ignacio", surname="Romero", url="https://nacho.dev", age=24),
              User(id= 2,name="Iara", surname="Sanchez", url="https://iaras.com", age=25),
              User(id= 3,name="Lorenzo", surname="Romero", url="https://lolo.com.ar", age=6)]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Ignacio", "surname": "Romero", "url": "https://nacho.dev", "age": 24},
            {"name": "Iara", "surname": "Sanchez", "url": "https://iaras.com", "age": 25},
            {"name": "Lorenzo", "surname": "Romero", "url": "https://lolo.com.ar", "age": 6},]
    
@router.get("/users")
async def users():
    return users_list


@router.get("/{id}") #Path
async def user(id: int):
    return search_user(id)
    

@router.get("/") #Query
async def user(id: int, name: str):
    return search_user(id)


@router.post("/", response_model=User, status_code=201) #Post
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    users_list.append(user)
    return user
    
#Put
@router.put("/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    
    return user

@router.delete("/{id}") #Delete
async def user(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    

