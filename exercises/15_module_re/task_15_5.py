# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать
на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов,
а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""
import re


def generate_description_from_cdp(filename):
    with open(filename) as file:
        result={}
        regex=(r'(?P<dev>\S+) +(?P<local_int>Eth \S+) .* (?P<id_int>Eth \S+)')
        for line in file:
            match=re.search(regex, line)
            if match:
                local=match.group("local_int")
                result[local]="description Connected to " + match.group("dev") + " port " + match.group("id_int")
        return result
            
if __name__ == "__main__":   
    filename="sh_cdp_n_sw1.txt"
    print (generate_description_from_cdp(filename))            
        