# -*- coding: utf-8 -*-
"""
Задание 4.7
mac = "AAAA:BBBB:CCCC"
Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
#print(mac1)
mac1=mac.replace(':','')
#print(mac1)
mac1=int(mac1,16)
#print(mac1)
mac1_bin="{:b}".format(mac1)
print(mac1_bin)