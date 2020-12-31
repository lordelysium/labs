# -*- coding: utf-8 -*-
"""
Задание 4.1

Используя подготовленную строку nat, получить новую строку, в которой
в имени интерфейса вместо FastEthernet написано GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
"""

"""
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
commands=nat.split()
interface=commands.index('FastEthernet0/1')
commands[interface]='GigabitEthernet0/1'
nat = ' '.join(commands)
print(nat)
"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
nat = nat.replace('Fast','Gigabit')
print(nat)

