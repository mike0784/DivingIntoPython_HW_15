import sys
import os
from pathlib import Path
import logging

import pack.ListDir as ld
import pack.WriteJsonFile as jf

FORMAT = '{asctime} {levelname:<8}  {funcName}() {lineno:03d}: {msg}'

logging.basicConfig(format=FORMAT, style='{', filename="project.log", filemode="w", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger("основной файл проекта")
logger.warning("Опасный момент")

def validationDir(dir: str) -> bool:
    logger.info(f'Проверка наличия каталога "{dir}"')
    if Path(dir).exists():
        return True
    else:
        logger.error(f'Каталог "{dir}" не найден')
        return False

def work(file: str, dir: str) -> None:
    logger.info("Выполнение функции")
    if validationDir(dir):
        result = list()
        file = os.getcwd() + "/" + file
        result = ld.listDirectories(dir)
        logger.info("Создан список каталогов и файлов")
        jf.writeToJSON(result, file)
        logger.info(f"Запись списка файлов в файл: {file}")
    else:
        logger.info("Завершение функции work без результата")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logger.error("Должно быть как минимум два аргумента")
    else:
        work(sys.argv[1], sys.argv[2])
    