from pydantic import BaseModel

class Documento(BaseModel):
    id_documento: int
    nombre_doc:str
    id_dependencia: int
    prioridad: int
    fecha_venc: str   

documentos = {
    1: Documento(id_documento=1, nombre_doc="cotizacion_1", id_dependencia=3, prioridad= 1, fecha_venc="10-10-2020"),
    2: Documento(id_documento=2, nombre_doc="cuenta_cobro_1", id_dependencia=2, prioridad= 2, fecha_venc="25-11-2020"),
    3: Documento(id_documento=3, nombre_doc="citacion_1", id_dependencia=3, prioridad= 3, fecha_venc="15-12-2020")
}

def obtener_docs():
    lista_docs = []
    for d in documentos:
        lista_docs.append(documentos[d])
    return lista_docs

def docs_dep(dep):
    lista_dep = []    
    for Documento in documentos:
        if documentos[Documento].id_dependencia==dep:
            lista_dep.append(documentos[Documento])
    return lista_dep

def crear_docs(doc: Documento):
    if doc.id_documento in documentos:
        return False
    else:
        documentos[doc.id_documento]=doc
        return True