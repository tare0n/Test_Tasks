import json
import io


def from_json_to_dicts(file):
    """
    opens json-file
    :param file: .json file
    :return: list of dicts
    """
    with io.open(file, encoding='utf-8') as f:
        dicts = json.load(f)
    return dicts


def date_to_normal(date_str):
    """
    converts data to format DD.MM.YYYY
    :param date_str:
    :return:
    """
    dates_list = date_str[:10].split('-')
    return '.'.join(dates_list[::-1])


def encryption(payment_info):
    """encrypts cards and bank account numbers"""
    if payment_info[:4] == "Счет":
        return "Cчет **" + payment_info[-4:]
    else:
        return payment_info[:-12] + " " + payment_info[-12:-10] + "** **** " + payment_info[-4:]


def print_5_top(dicts):
    dicts.sort(key=lambda dictionary: dictionary['date'] if dictionary else '1040', reverse=True)
    counter = 0
    while counter < 5:
        for dictionary in dicts[1:]:
            try:
                if dictionary['state'] == 'EXECUTED':
                    print(f"{date_to_normal(dictionary['date'])}  {dictionary['description']}\n"
                          f"{encryption(dictionary['from'])} -> {encryption(dictionary['to'])}\n"
                          f"{dictionary['operationAmount']['amount']} {dictionary['operationAmount']['currency']['name']}\n")
                    counter += 1
            except KeyError:
                pass
            if counter >= 5:
                break
