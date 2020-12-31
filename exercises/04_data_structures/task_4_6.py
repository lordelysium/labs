# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
#print(ospf_route)
ospf=ospf_route.replace(',',' ').replace(']',' ').replace('[',' ').split()
#print(ospf)

output = "\n{:25} {}" * 5



print(output.format ('Prefix', ospf[0], 'AD/Metric' , ospf[1], 'Next-Hop', ospf[3],'Last update', ospf[4],
'Outbound Interface', ospf[5]))

"""
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
print(command1)
print(command2)

com1_split=command1.split()
print(com1_split)
vlan1=com1_split[-1].split(',')
print(vlan1)

com2_split=command2.split()
print(com2_split)
vlan2=com2_split[-1].split(',')
print(vlan2)

vlan1_set=set(vlan1)
vlan2_set=set(vlan2)
Merge=sorted(vlan1_set.union(vlan2_set))
print(Merge)
"""