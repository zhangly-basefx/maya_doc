'''
改变outline面板给对象名称的顺序
'''

# 将指定对象向下移一位
cmds.reorder('sphere1',r=-1)

# 将指定对象排在顺序第一位
cmds.rerder('sphere1',front=True)

