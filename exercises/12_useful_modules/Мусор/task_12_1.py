# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import ipaddress


input_str = input('Введите адреса(,): ')

input_list = [i.strip() for i in input_str.split(',')]

def check_ip(input_ip):
    output = []
    for ip in input_ip:
        try:
            ipaddress.ip_address(ip)
            output.append(ip)
        except ValueError:
            print(ip + " is not IP")
    return(output)

def ping_ip_addresses(ip):
    reach=[]
    unreach=[]
                   # stdout=subprocess.PIPE,
                   # stderr=subprocess.PIPE,
                   # encoding='utf-8')
    for ip in ip:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip])
        if reply.returncode == 0:
            reach.append(ip)
        else:
            unreach.append(ip)
    return reach, unreach



ip=check_ip(input_list)
reach, unreach = ping_ip_addresses(ip)
print("доступны: " + ', '.join(reach))
print("недоступны: " + ', '.join(unreach))






