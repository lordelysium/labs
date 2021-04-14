# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

def get_ints_without_description(filename):
    with open(filename) as file:
        regex=re.compile(r"!\ninterface (?P<int>\S+)\n"
                     r"(?P<descr> description \S+)?")
        match=regex.finditer(file.read())
        result=[m.group('int') for m in match if m.lastgroup == 'int']
        return(result)

if __name__ == "__main__":   
    filename="config_r1.txt"
    print (get_ints_without_description(filename))
   
    
   
   
    