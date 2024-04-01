from datetime import datetime
import json


def get_lst():
    """
    Получает неотфильтрованный список из json файла
    """
    with open("operations.json") as file:
        lst = json.load(file)
    return lst


def filter_lst(lst):
    """
    Создаёт отфильтрованный список: без пустых каталогов и отменённых операций
    """
    lst_2 = list()
    i = 0
    for i in range(len(lst)):
        if len(lst[i]) < 1:
            i += 1
        elif lst[i]["state"] == "EXECUTED":
            lst_2.append(lst[i])
            i += 1
        else:
            i += 1
    return lst_2

def mask_kard(operation):
    """
    Маскирует номер карты в формат
    XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом).
    """

    for k, v in operation.items():
        if k == "from" and v[-16:].isdigit() and "Счет" not in v:
            operation["from"] = (operation["from"][:-12] + " " +
                                 operation["from"][-12:-10] +
                                 "** **** " + operation["from"][-4:])
        elif k == "to" and v[-16:].isdigit() and "Счет" not in v:
            operation["to"] = (operation["to"][:-12] + " " +
                               operation["to"][-12:-10] +
                               "** **** " + operation["to"][-4:])
    return operation


def mask_account(operation):
    """
    Маскирует номер счёта в формат
    **XXXX  (видны только последние 4 цифры номера счета)..
    """

    for k, v in operation.items():

        if k == "from" and v[-20:].isdigit():
            operation["from"] = "Счет **" + operation["from"][-4:]

        elif k == "to" and v[-20:].isdigit():
            operation["to"] = "Счет **" + operation["to"][-4:]

    return operation


def print_operation(operation):
    """ Выводит на экран операции с поправкой на отсутствие или наличие ключа откуда ["from"]
    """
    if "from" in operation.keys():
        return (f'{operation["date"]} {operation["description"]}'
                f'\n{operation["from"]} -> {operation["to"]}'
                f'\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
    else:
        return (f'{operation["date"]} {operation["description"]} '
                f'\n-> {operation["to"]}'
                f'\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')


def reformat_date(operation):
    """
    Форматирование даты в формат ДД.ММ.ГГГГ
    """
    operation["date"] = datetime.strptime(operation["date"][:10], '%Y-%m-%d').strftime("%d.%m.%Y")
    return operation









