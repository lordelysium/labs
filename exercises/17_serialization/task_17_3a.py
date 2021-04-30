# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import re
import glob
import yaml
from pprint import pprint


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    all_result={}
    for file in list_of_files:
        with open(file) as txt_file:
            input_from_file=txt_file.read()
            device_result={}
            device_dict={}
            hostname=re.search((r'(?P<hostname>\S+)>'), input_from_file).group('hostname')
            regex =(r"(?P<dev_id>\w+)  +(?P<local_int>\S+ \S+)"
                    r" +\d+  +[\w ]+  +\S+ +(?P<port_id>\S+ \S+)")
            result=re.findall(regex, input_from_file)
            for match in result:
                dev_id, local_int , port_id = match
                device_id={}
                device_id[dev_id]=port_id
                device_dict[local_int] = device_id
        all_result[hostname] = device_dict
    if save_to_filename:    
        with open(save_to_filename, 'w') as yaml_file:        
            yaml.dump(all_result, yaml_file, default_flow_style=False)
    return all_result    
    
  
   
if __name__ == "__main__":
    sh_cdp_n_files = glob.glob("sh_cdp_n_*")
        
    list_of_files=sh_cdp_n_files
    save_to_filename="topology.yaml"
    generate_topology_from_cdp(list_of_files, save_to_filename)
           
    with open(save_to_filename) as yaml_file:        
        print(yaml_file.read())    

 
          