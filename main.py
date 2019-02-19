# -*- coding: utf-8 -*-
from lark import Lark
from twisets.executor import Visitor
from twisets.twitter import MockTwitterClient
from twisets.twloader import TwiLoader
from twisets.environment import Environment



program = open('example/program.txt').read()
rule = open('config/grammer.txt').read()

# 文法規則をパーサジェネレータに渡してパーサを生成(字句解析もやってくれる)
parser = Lark(rule, start='program', parser='lalr')

# プログラムを字句解析＆構文解析
tree = parser.parse(program)

# visitor を定義
visitor = Visitor()

# 初期環境を定義
client = MockTwitterClient()
twiloader = TwiLoader(twitter=client)
env = Environment(twiloader=twiloader)
visitor.program(tree, env)
