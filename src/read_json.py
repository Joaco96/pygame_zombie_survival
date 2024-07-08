import json

def cargar_json(path:str):
    with open(path, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_score(path: str, score: int):
  datos = cargar_json(path)
  datos['scores'].append(score)
  with open(path, 'w') as archivo:
    json.dump(datos, archivo, indent=2)