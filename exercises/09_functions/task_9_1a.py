# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд
   port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template и шаблона port_security_template,
если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config, с генерацией конфигурации
port-security и без.

Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}



intf_vlan_mapping = access_config
access_template = access_mode_template
psecurity = port_security_template

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None, result_list=None):
    result_list=[]
    for interface, vlan in intf_vlan_mapping.items():
        result='interface ' + interface
        result_list.append(result)
        for command in access_template:
            if command.endswith('vlan') is True:
                result=command + ' ' + str(vlan)
                result_list.append(result)
            else:
                result=command
                result_list.append(result)
        if not psecurity:
                pass
        else:
            for command_secure in psecurity:
                result=command_secure
                result_list.append(result)
    return result_list



stringsall=generate_access_config(intf_vlan_mapping, access_template, psecurity)

for string in stringsall:
    print(string)