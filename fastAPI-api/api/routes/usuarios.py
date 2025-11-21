from fastapi import APIRouter, HTTPException
from api.models.usuario import Usuario, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

# "Base de datos" en memoria
db: dict[int, dict] = {}
contador_id = 0

@router.post("/")
def crear_usuario(usuario: Usuario):
    global contador_id
    contador_id += 1
    db[contador_id] = usuario.model_dump()
    return {"id": contador_id, **db[contador_id]}

@router.get("/")
def obtener_usuarios():
    return [{"id": id, **data} for id, data in db.items()]

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    if usuario_id not in db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"id": usuario_id, **db[usuario_id]}

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: Usuario):
    if usuario_id not in db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db[usuario_id] = usuario.model_dump()
    return {"id": usuario_id, **db[usuario_id]}

@router.patch("/{usuario_id}")
def actualizar_parcial(usuario_id: int, usuario: UsuarioUpdate):
    if usuario_id not in db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    datos_actuales = db[usuario_id]
    datos_nuevos = usuario.model_dump(exclude_unset=True)
    db[usuario_id] = {**datos_actuales, **datos_nuevos}
    return {"id": usuario_id, **db[usuario_id]}

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    if usuario_id not in db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    eliminado = db.pop(usuario_id)
    return {"mensaje": "Usuario eliminado", "usuario": eliminado}