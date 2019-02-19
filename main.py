# -*- coding: utf-8 -*-
from lark import Lark
from twisets.executor import Visitor
from twisets.twitter import MockTwitterClient
from twisets.twloader import TwiLoader
from twisets.environment import Environment
from twisets.db import OnMemoryDB

rule = open('config/grammer.txt').read()
# 文法規則をパーサジェネレータに渡してパーサを生成(字句解析もやってくれる)
parser = Lark(rule, start='program', parser='lalr')
# visitor を定義
visitor = Visitor()
# 初期環境を定義
client = MockTwitterClient()
db = OnMemoryDB
twiloader = TwiLoader(twitter=client, db=db)
env = Environment(twiloader=twiloader)

try:
    while True:
        program = input(">> ")
        try:
            # プログラムを字句解析＆構文解析
            tree = parser.parse(program)
            visitor.program(tree, env, interactive=True)
        except Exception as e:
            print(e)

except EOFError:
    pass
