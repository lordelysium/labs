# -*- coding: utf-8 -*-
"""
Задание 6.1

Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX
Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX

Написать код, который преобразует MAC-адреса в формат cisco
и добавляет их в новый список mac_cisco

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""
#Вариант №1
#Через джойн-реплейс-сплит
mac=["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac_cisco=' '.join(mac) #объединяет список в строку с разделителем "пробел"
mac_cisco=mac_cisco.replace(':','.') #заменяет в строке двоеточия на точки
mac_cisco=mac_cisco.split(' ') #разбивает строку на список с разделителем "пробел"
print(mac_cisco)
"""

#Вариант №2
#Через цикл

mac=["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

mac_cisco=[] #Новый list (список) с именем mac_cisco

for mac_item in mac:  #для каждого элемента с именем mac_item в списке mac
    mac_cisco.append(mac_item.replace(':','.')) #append - добавить в список mac_cisco,
                                                #replace - заменить в mac_item ДВОЕТОЧИЕ на ТОЧКУ
print(mac_cisco)

