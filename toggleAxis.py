'''
在世界坐标原点显示坐标轴
'''

# 开启显示
cmds.toggleAxis(o=True)

# 关闭显示
cmds.toggleAxis(o=False)

# 查询显示状态
cmds.toggleAxis(q=True, o=True)

# 显示与关闭切换
cmds.toggleAxis()
