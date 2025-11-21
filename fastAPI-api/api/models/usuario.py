from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int | None = None

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    edad: int | None = None