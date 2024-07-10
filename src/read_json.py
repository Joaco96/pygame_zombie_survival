import json

def importar_json(path:str):
    """Lee e importa un archivo json en el path especificado.

    Args:
        path (str): Ruta para extrar los datos.

    Returns:
        _type_: Devuelve contenido del archivo especificado.
    """
    with open(path, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def actualizar_scores(path: str, score:tuple[str,int]):
  """Lee el archivo destino y agrega el ultimo puntaje de la partida al archivo.

  Args:
      path (str): Ruta del archivo para leer y agregar puntaje.
      score (tuple[str,int]): Tupla con ultimo puntaje y nombre del dueño.
  """
  datos = importar_json(path)
  datos['scores'].append(score)
  with open(path, 'w') as archivo:
    json.dump(datos, archivo, indent=4)