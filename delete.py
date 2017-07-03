'''
用于删除的命令,如all=True，则对象是场景所有
'''

# 删除选择的物体
cmds.delete()

# 删除选择物体的约束节点
cmds.delete( constraints=True)

# 删除选择物体的构造历史记录
cmds.delete(constructionHistory=True)

# 删除选择物体上的表达式
cmds.delete(expressions=True)

