# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re

filename="cisco_nat_config.txt"
filename2="cisco_asa_cfg.txt"

def convert_ios_nat_to_asa(filename, filename2):
    with open(filename, 'r') as file, open(filename2, 'w') as asa_cfg_writefile:
        asa_cfg_list=[]
        regex=(r' tcp (?P<ip>\S+) +(?P<local_port>\S+) +interface +\S+ +(?P<out_port>\S+)')
        asa_nat_template = (
                    "object network LOCAL_{ip}\n"
                    " host {ip}\n"
                    " nat (inside,outside) static interface service tcp {local_port} {out_port}\n")
       
        for line in file:
           
            inventory=re.search(regex, line) 
            ip, local_port, out_port = inventory.groups()
            asa_cfg=asa_nat_template.format(ip=ip, local_port=local_port, out_port=out_port).strip(" ")
            asa_cfg_list.append(asa_cfg)
            
            asa_cfg_writefile.write(asa_cfg)
       
  
 
    
    
              
              
if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_cfg.txt")
            
            
            
