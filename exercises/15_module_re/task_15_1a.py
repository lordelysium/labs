# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
import re 

#filename=input('Введите название файла(config_r1.txt):')
filename='config_r1.txt'


def get_ip_from_cfg (filename):
    ip_mask_dict={}
    file=open(filename, 'r')
    for line in file:
        line=line.strip()
        interface_check=re.match(r'interface (\S+)', line)
        ip_mask=re.match(r'ip address (\S+) (\S+)', line)
        if interface_check != None:
            interface=interface_check.group(1)
        if ip_mask != None and interface != None:
            ip_mask_dict[interface]=ip_mask.group(1, 2)
    return ip_mask_dict        
            

if __name__ == "__main__":
    list_cort=get_ip_from_cfg (filename)
    print(list_cort)


