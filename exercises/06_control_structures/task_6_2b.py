# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
valid_ip=False

while not valid_ip:
    ip=input ("Введите ip адресс в виде 10.0.1.1: ")
    print('Ваш ввод - ' + ip)
    octet_list=ip.split(".") #Разбить "ввод ip" в список octet_list по разделителю ТОЧКА
#состоит из 4 чисел
#проверка списка на "количество элементов"
#(не букв или других символов)
#проверка списка octet_list на "каждый элемент число"
    for octet in octet_list:              #Для элемента октет в списке octet_list:
        if octet.isdigit()==False:        #если элемент октет не соответствует числу т.е .isdigit() возвр False
            valid_ip=False
            print ('Неправильный ip адрес')
            break
        elif len(octet_list)!=4:        #если количество элементов в списке octet_list не соответствует числу
            valid_ip=False
            print ('Неправильный ip адрес')
            break
        elif 0>int(octet) or int(octet)>255 :  #если элемент октет меньше ноля или больше 255
            valid_ip=False
            print ('Не в диапазоне0-255')
            print ('Неправильный ip адрес')
            break

        else:
            valid_ip=True

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







