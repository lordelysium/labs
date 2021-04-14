# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

filename='sh_ip_int_br_2.txt'
    

'''
def parse_sh_ip_int_br(filename):
    with open(filename, 'r') as file:
        list_tup=[]
        for line in file:
            regex=(r'(\S+) +(\S+) +\S+ +\S+ +(up|down|administratively down) +(up|down)')
            result=re.search(regex, line)
            if result:                
                list_tup.append(result.groups())
        return list_tup
'''


def parse_sh_ip_int_br(filename):
    with open(filename, 'r') as file:
        regex=(r'(\S+) +(\S+) +\S+ +\S+ +(up|down|administratively down) +(up|down)')
        result=[m.groups() for m in re.finditer(regex, file.read())]   
    return result

if __name__ == '__main__': 
    a=parse_sh_ip_int_br(filename)
    print (a)
    
    