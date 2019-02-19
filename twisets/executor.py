# -*- coding: utf-8 -*-


# ツリーをたどって実行コードを生成するVisitorクラス
class Visitor(object):
    def __default__(self, tree, env):
        raise NotImplementedError

    def program(self, tree, env):
        for sub_tree in tree.children:
            self.visit(sub_tree, env)

    def state(self, tree, env):
        ret = self.visit(tree.children[0], env)
        if tree.children[0].data == 'expr':
            print(ret)

    def assignment(self, tree, env):
        left = self.visit(tree.children[0], env)
        right = self.visit(tree.children[1], env)
        env.set(left, right)

    def new_symbol(self, tree, env):
        return tree.children[0].value

    def expr(self, tree, env):
        return tree.visit(tree, env)

    def sum(self, tree, env):
        left = tree.visit(tree.children[0], env)
        right = tree.visit(tree.children[1], env)
        return left | right

    def intersection(self, tree, env):
        left = tree.visit(tree.children[0], env)
        right = tree.visit(tree.children[1], env)
        return left & right

    def difference(self, tree, env):
        left = tree.visit(tree.children[0], env)
        right = tree.visit(tree.children[1], env)
        return left - right

    def symmetric_difference(self, tree, env):
        left = tree.visit(tree.children[0], env)
        right = tree.visit(tree.children[1], env)
        return left ^ right

    def term(self, tree, env):
        return self.visit(tree, env)

    def id(self, tree, env):
        ff = tree.children[0].data
        twitter_id = tree.children[1].data
        return env.twiloader.load(ff, twitter_id)

    def symbol(self, tree, env):
        return env.get(tree.children[0].data)

    def visit(self, tree, env):
        f = getattr(self, tree.data, self.__default__(tree, env))
        return f(tree, env)