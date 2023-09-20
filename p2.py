import math
import csv
import random
import json
import os
import sys
from pathlib import Path

import logging

dmt = ";"
fields = ["a", "b", "c"]
file = "pp.csv"

FORMAT = '{asctime} {levelname:<8}  {funcName}() {lineno:03d}: {msg}'

logging.basicConfig(format=FORMAT, style='{', filename="project.log", filemode="w", encoding="utf-8", level=logging.INFO)
logger = logging.getLogger("основной файл проекта")
logger.warning("Опасный момент")

def genCSV(count: int, file: str) -> None:
    max = 100
    min = -100
    logger.info(f'Создание файла {file} и запись переменных')
    try:
        with open(file, "w", encoding="utf8") as f:
            writer = csv.DictWriter(f, delimiter=dmt, fieldnames=fields, lineterminator="\r")
            writer.writeheader()
            for _ in range(0, count):
                writer.writerow({fields[0]: random.randint(min, max), fields[1]: random.randint(min, max), fields[2]: random.randint(min, max)})
    except OSError:
        logger.critical(f'Невозможно создать файл {file}')

def verificationFile(file: str) -> bool:
    logger.info(f'Проверка наличия файла "{file}"')
    if Path(file).exists():
        return True
    else:
        logger.error(f'Файл "{file}" не найден')
        return False


def my_decorator(func):
    result = {}
    if verificationFile(file):
        with open(file, "r", encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=dmt)
            count = 0
            for row in reader:
                temp = []
                a = int(row[fields[0]])
                b = int(row[fields[1]])
                c = int(row[fields[2]])
                temp = func(a, b, c)
                result[count] = {fields[0]: a, fields[1]: b, fields[2]: c, "result": temp}
                count += 1
    return result


@my_decorator
def equation(a: int, b: int, c: int) -> list:
    result = []
    if a == 0:
        return None
    D = b ** 2 - 4 * a * c
    if D < 0:
        return None
    elif D == 0:
        x = -b / (2 * a)
        result.append(x)
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        result.append(x1)
        result.append(x2)
    return result



def readCSVFile(file: str) -> list:
    logger.info(f'Чтение файла "{file}"')
    try:
        result = []
        with open(file, "r", encoding="utf8") as f:
            reader = csv.DictReader(f, delimiter=dmt)
            for row in reader:
                a = int(row[fields[0]])
                b = int(row[fields[1]])
                c = int(row[fields[2]])
                result.append([a, b, c])
        return result
    except OSError:
        logger.critical(f'Невозможно прочитать файл {file}')


def toWrite(func):
    def wrapper_toWrite(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_toWrite


@toWrite
def writeJsonFile(file: str, data: dict) -> None:
    logger.info(f'Запись в файл "{file}"')
    if Path(file).exists():
        a = input(f'Указанный вами файл "{file}" уже существует.\nХотите его перезаписать (Y or N): ')
        if a.upper() == "N" or a.upper() == "NO":
            b = input("Укажите новый файл: ")
            file = b
            logger.info(f'Введен новый файл "{file}"')
    with open(file, "w", encoding="utf8") as f:
        json.dump(data, f, indent=2)

def verificationInt(a: str) -> bool:
    logger.info(f'Проверка введенного значения "{a}"')
    if a.isdigit():
        return True
    else:
        logger.critical(f'Введенное значение "{a}" содержит что ещё, кроме цифр')
        return False

if __name__ == "__main__":
    if len(sys.argv) != 4:
        logger.error("Неверное количество аргументов")
    elif not verificationInt(sys.argv[1]):
        logger.critical("Программа завершилась с ошибкой")
    else:
        genCSV(int(sys.argv[1]), sys.argv[2])
        temp = equation
        writeJsonFile(sys.argv[3], temp)