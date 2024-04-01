from src.functions import *

def test_main():
    assert print_operation({"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",

lst_2 = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

def test_filter():
    assert print("\n".join(map(print_operation,
                    map(reformat_date,
                        map(mask_kard,
                            map(mask_account,
                                sorted(lst_2, reverse=True, key=lambda x: x["date"])[:5])))))) == None

