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




def convert_ranges_to_ip_list(input_ip):
    output = []
    try:
        for ip in input_ip:
            if '-' in ip:
                first_ip, second_ip = ip.split("-")
                if not '.' in second_ip:
                    second = list(map(int, first_ip.split(".")))
                    second = second[:-1] + [int(second_ip)]
                    second_ip = list(map(str, second))
                    second_ip = ipaddress.ip_address('.'.join(second_ip))
                first_ip = ipaddress.ip_address(first_ip)
                second_ip = ipaddress.ip_address(second_ip)
                for ip in range(int(first_ip), int(second_ip) + 1):
                    output.append(str(ipaddress.ip_address(ip)))
            else:
                output.append(str(ipaddress.ip_address(ip)))
        return output
    except:
        print(ip + " is not IP")


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


input_str = input('Введите адреса(,): ')

input_list = [i.strip() for i in input_str.split(',')]

ip=convert_ranges_to_ip_list(input_list)
reach, unreach = ping_ip_addresses(ip)
print("доступны: " + ', '.join(reach))
print("недоступны: " + ', '.join(unreach))






