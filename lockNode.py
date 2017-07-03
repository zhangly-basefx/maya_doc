'''
锁定一个对象的节点。锁定状态下受到以下限制：
它可能不会被删除
它可能不会被重命名
其父级可能不会改变
属性可能不会被删除或锁定
未锁定的属性可能不会被锁定
'''

# 锁定对象节点
cmds.lockNode('sphere1')

# 取消锁定
cmds.lockNode('sphere1', lock=False)