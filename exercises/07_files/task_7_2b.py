# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

filename_input=argv[1]


ignorelist = ["duplex", "alias", "Current configuration"]

with open (filename_input) as source, open ('config_sw1_cleared.txt', 'w') as output:
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