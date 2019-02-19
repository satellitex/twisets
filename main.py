# -*- coding: utf-8 -*-
from lark import Lark

program = open('example/program.txt').read()
rule = open('config/grammer.txt').read()

# 文法規則をパーサジェネレータに渡してパーサを生成(字句解析もやってくれる)
parser = Lark(rule, start='program', parser='lalr')

# プログラムを字句解析＆構文解析
tree = parser.parse(program)
print(tree.pretty())

