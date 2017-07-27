'''
吸附模式的查询与开关
'''

# 开启吸附
cmds.snapMode(currve=True)
cmds.snapMode(grid=True)
cmds.snapMode(point=True)

# 查询是否开启吸附
cmds.snapMode(q=True, point=True)
