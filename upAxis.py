'''
改变世界坐标轴的上轴
'''

# 将y轴变为世界坐标轴的上轴
cmds.upAxis(ax='y')

# 将x轴变为世界坐标轴的上轴,并旋转视图
cmds.upAxis(ax='x', rv=True)

# 查询当前的世界坐标轴的上轴
cmds.upAxis(q=True, axis=True)
