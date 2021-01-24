# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

filename=argv[1]

ignorelist = ["duplex", "alias", "Current configuration"]

with open (filename) as file:
    for line in file:
        skipfile = False
        for ignore in ignorelist:
            if ignore in line:
                skipfile = True
                break
        if not line.startswith('!') and not skipfile:
            print(line.rstrip())
