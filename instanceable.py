'''
设置一个对象是否能被实例化
'''

# 设置不能被实例化
cmds.instanceable(allow=0, shape=True)

# 设置允许被实例化
cmds.instanceable(allow=1, shape=True)

