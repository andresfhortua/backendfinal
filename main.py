from fastapi import FastAPI, HTTPException
import db_doc
import db_dep
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:8080", "https://frontendsprint3.herokuapp.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dependencias/")
async def obtener_deps():
    dep = db_dep.obtener_deps()
    return dep


@app.post("/dependencias/nuevo")
async def crear_dep(dep: db_dep.Dependencia):
    ok = db_dep.crear_deps(dep)
    if ok:
        return {"mensaje": "Dependencia creada"}
    else:
        raise HTTPException(status_code=400, detail="Dependencia existente")

@app.get("/documentos/")
async def obtener_docs():
    doc = db_doc.obtener_docs()
    return doc


@app.post("/documentos/nuevo/")
async def crear_doc(doc: db_doc.Documento):
    ok = db_doc.crear_docs(doc)
    if ok:
        return {"mensaje": "Documento creado"}
    else:
        raise HTTPException(status_code=400, detail="Documento existente")

@app.get("/dependencias/documentos/{id_dep}")
async def buscarDoc(id_dep:int):
    doc_dep = db_doc.docs_dep(id_dep)
    return doc_dep

@app.get("/dependencias/verificar/{id_dep}")
async def verificar_id(id_dep:int):   
    ok = db_dep.existe_dep(id_dep) 
    return ok
