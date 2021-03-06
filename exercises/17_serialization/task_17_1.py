# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv


def write_dhcp_snooping_to_csv(filename, output):
    head=['switch', "mac","ip", "vlan","interface"]
    result=[]
    result.append(head)
    print(head)
    regex = (r'(?P<mac>^\S\S\:\S\S\:\S\S\:\S\S\:\S\S\:\S\S) +' #MAC
             r'(?P<IP>\S+) +'   #IP           
             r'\S+ +' #trash lease
             r'\S+ +' #trash type
             r'(?P<VLAN>\S+) +' #vlan
             r'(?P<Interface>\S+)') #interface
    for file in filename:
        with open(file) as file_in:
            switch=[file.split("_")[0]]
            print(switch)
            
            for line in file_in:         
                match=re.search(regex, line)        
                if match:
                    pre_result=switch + list(match.groups())
                    result.append(pre_result)
            print(result)

        


if __name__ == "__main__":

    filename=["sw1_dhcp_snooping.txt", "sw2_dhcp_snooping.txt"]
    output="sw1_dhcp_snooping.csv" 
  

    write_dhcp_snooping_to_csv (filename, output)        