import json

def importar_json(path:str):
    with open(path, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def actualizar_scores(path: str, score:tuple[str,int]):
  datos = importar_json(path)
  datos['scores'].append(score)
  with open(path, 'w') as archivo:
    json.dump(datos, archivo, indent=4)