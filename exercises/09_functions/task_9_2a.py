# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result_list=[]
    result_dict={}
    for interface, vlan in intf_vlan_mapping.items():
        interface_com=interface
        result_list=[]
        for command in trunk_template:
            if command.endswith('vlan') is True:
                result=command + ' ' + ','.join(str(vlans) for vlans in vlan)
                result_list.append(result)
            else:
                result=command
                result_list.append(result)
        result_dict[interface_com]=result_list
    return result_dict
    #return result_list


print (generate_trunk_config(trunk_config, trunk_mode_template ))