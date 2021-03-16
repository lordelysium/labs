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




def ping_ip_addresses(list_of_ips):
    reach=[]
    unreach=[]
                   # stdout=subprocess.PIPE,
                   # stderr=subprocess.PIPE,
                   # encoding='utf-8')
    for ip in list_of_ips:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip])
        if reply.returncode == 0:
            reach.append(ip)
        else:
            unreach.append(ip)
    return reach, unreach

if __name__ == "__main__":
    reach, unreach = ping_ip_addresses(["1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"])
    print(reach)
    print(unreach)







