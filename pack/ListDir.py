import os
__all__ = ["listDirectories"]
result = list()
def listDirectories(dir: str) -> list:
    """Данная функция создает список каталогов и файлов
    """
    global result
    os.chdir(dir)
    content = os.listdir()
    for obj in content:
        if os.path.isfile(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "file", "size": size}
            #print(temp)
            result.append(temp)
        if os.path.isdir(obj):
            size = os.path.getsize(obj)
            temp = {"file": obj, "parent": dir, "type": "directories", "size": size}
            #print(temp)
            result.append(temp)
            listDirectories(obj)
    os.chdir("..")
    return result