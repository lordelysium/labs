# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

filename_input=CAM_table.txt


ignorelist = ["duplex", "alias", "Current configuration"]

with open (filename_input) as source
    for line in source:
        skipfile = False
        for ignore in ignorelist:
            if ignore in line:
                skipfile = True
                break
        #if not line.startswith('!') and not skipfile:
            #print(line.rstrip())

        if not skipfile:
            output.write(line)

print("Done!")