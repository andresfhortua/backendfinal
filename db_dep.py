from pydantic import BaseModel


class Dependencia(BaseModel):
    id_dependencia: int
    nombre_dep: str


dependencias = {
    1: Dependencia(id_dependencia=1, nombre_dep="Contabilidad"),
    2: Dependencia(id_dependencia=2, nombre_dep="Juridico"),
}


def obtener_deps():
    lista_deps = []
    for d in dependencias:
        lista_deps.append(dependencias[d])
    return lista_deps


def crear_deps(dep: Dependencia):
    if dep.id_dependencia in dependencias:
        return False
    else:
        dependencias[dep.id_dependencia] = dep
        return True


def existe_dep(id_dep:int):
    if id_dep in dependencias.keys():
        return True
    else:
        return False