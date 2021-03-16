# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate
from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list

def print_ip_table(reach, unreach):
    table = {"Reachable": reach, "Unreachable": unreach}
    tabulated_table=tabulate(table, headers='keys')
    print(table)
    return tabulated_table





if __name__ == "__main__":
    input_str = input('Введите адреса(,): ')
    input_list = [i.strip() for i in input_str.split(',')]
    list_of_ips=(convert_ranges_to_ip_list(input_list))
    reach, unreach = ping_ip_addresses(list_of_ips)
    print(print_ip_table(reach, unreach))


