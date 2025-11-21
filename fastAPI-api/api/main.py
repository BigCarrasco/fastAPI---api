from fastapi import FastAPI
from api.routes import usuarios

app = FastAPI(title="Mi API", version="1.0.0")

# Registrar routers 
app.include_router(usuarios.router)

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

#  Correr: uvicorn api.main:app --reload 

# uv venv 
# uv pip install 
# uv pip install fastapi uvicorn[standard]
 