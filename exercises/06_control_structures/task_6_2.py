# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip=input ("Введите ip адресс в виде 10.0.1.1: ")
print('Ваш ввод - ' + ip)

octet_list=ip.split(".") #Разбить "ввод ip" в список octet_list по разделителю ТОЧКА



#проверка списка octet_list на "каждый элемент число"
for octet in octet_list:              #Для элемента октет в списке octet_list:
    if octet.isdigit()==False:        #если элемент октет не соответствует числу т.е .isdigit() возвр False
        valid_ip=False

if valid_ip:
    octet_list_int=[]
    for octet in octet_list:              #Для элемента октет в списке octet_list:
        octet_list_int.append(int(octet)) #Перевести его в формат int и добавить в новый список octet_list_int

    if  0<octet_list_int[0]<224:
        print('unicast - первый байт в диапазоне 1-223')
    elif 223<octet_list_int[0]<240:
        print ('multicast - первый байт в диапазоне 224-239')
    elif ip=="255.255.255.255":
        print('local broadcast если IP-адрес равен 255.255.255.255')
    elif ip=="0.0.0.0":
        print('unassigned - если IP-адрес равен 0.0.0.0')
    else:
        print ('unused - во всех остальных случаях')
else:
    print ('Неправильный ip адрес')







