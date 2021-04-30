# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
import glob
import csv


filename='sh_cdp_n_sw1.txt'



def parse_sh_cdp_neighbors(input_from_file):
# with open(filename) as file_txt:
#     input_from_file=file_txt.read()
    device_result={}
    device_dict={}
    
    hostname=re.search((r'(?P<hostname>\S+)>'), input_from_file).group('hostname')
    regex =(r"(?P<dev_id>\w+)  +(?P<local_int>\S+ \S+)"
            r" +\d+  +[\w ]+  +\S+ +(?P<port_id>\S+ \S+)")
    result=re.findall(regex, input_from_file)
    for match in result:
        dev_id, local_int , port_id = match
        device_id={}
        device_id[dev_id]=port_id
        device_dict[local_int] = device_id
    device_result[hostname] = device_dict   
    return device_result
        

        
    
if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_sh_cdp_neighbors(f.read()))   
