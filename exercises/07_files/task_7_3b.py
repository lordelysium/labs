# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

config_table_vlan=[]

with open ('CAM_table.txt', 'r') as source:
    for line in source:
        items=line.split()
        if items and items[0].isdigit():
            vlan, mac, _, interface = items
            vlan = int(vlan)
            config_table_vlan.append(vlan)




allvlans=''.join(str(sorted(set(config_table_vlan))))
inputvlan = input("Выберите vlan" + allvlans + ": " )

with open ('CAM_table.txt', 'r') as source:
    for line in source:
        items=line.split()
        if items and items[0].isdigit() and items[0]==inputvlan:
            vlan, mac, _, interface = items
            print(f'{vlan:5}{mac:15}{interface}')


