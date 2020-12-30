# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.


"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
print(command1)
print(command2)

com1_split=command1.split()
#print(com1_split)
vlan1=com1_split[-1].split(',')
#print(vlan1)

com2_split=command2.split()
#print(com2_split)
vlan2=com2_split[-1].split(',')
#print(vlan2)

vlan1_set=set(vlan1)
vlan2_set=set(vlan2)
Merge=sorted(vlan1_set.union(vlan2_set))



print(Merge)
