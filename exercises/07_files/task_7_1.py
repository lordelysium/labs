# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
out="\n{:20} {}" *5
with open ('ospf.txt', 'r') as ospf:
    for line in ospf:
        attributes=line[1:].replace('[','').replace(']','').replace(',','').strip().split()
        print(out.format(
               'Prefix',                attributes[0],
               'AD/Metric',             attributes[1],
               'Next-Hop',              attributes[3],
               'Last update',           attributes[4],
               'Outbound Interface',    attributes[5]))