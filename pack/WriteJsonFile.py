import json
def writeToJSON(ls: list, file: str) -> None:
    """Функция сохранеет результат работы функции listDirectories в json файл"""
    json_object = json.dumps(ls, indent=4)
    with open(file, "w") as f:
        f.write(json_object)