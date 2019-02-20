# -*- coding: utf-8 -*-
from lark import Lark
from twisets.executor import Visitor
from twisets.twitter import TwitterAPIClient
from twisets.twloader import TwiLoader
from twisets.environment import Environment
from twisets.db import SQLiteDB
from twisets.config import YamlConfig
import argparse

if __name__ == '__main__':
    # Parse settings
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--config', type=str, default='config/act_config.yaml', help='Path name to config file.')
    parser.add_argument(
        '--use_cache', type=str, default='True', help='use cache flag [(True), False]')

    FLAGS, unparsed = parser.parse_known_args()

    config_path = FLAGS.config
    use_cache = True
    if FLAGS.use_cache == 'False':
        use_cache = False

    rule = open('config/grammer.txt').read()
    # 文法規則をパーサジェネレータに渡してパーサを生成(字句解析もやってくれる)
    parser = Lark(rule, start='program', parser='lalr')
    # visitor を定義
    visitor = Visitor()
    # 初期環境を定義
    conf = YamlConfig(config_path)
    client = TwitterAPIClient(conf)
    db = SQLiteDB(conf)
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
