# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress




def convert_ranges_to_ip_list(input_ip):
    output = []
    for ip in input_ip:
        try:
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
        except:
            print(ip + " is not IP")
    return output


if __name__ == "__main__":
    input_str = input('Введите адреса(,): ')
    input_list = [i.strip() for i in input_str.split(',')]
    print(convert_ranges_to_ip_list(input_list))