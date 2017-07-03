'''
设置线框在没有被选择时的颜色
'''

# 为sphere1设置指定线框颜色
cmds.color('sphere1',rgb=(1,0,0))

# 还原默认的线框颜色
cmds.color('sphere1')

