'''
对对象的旋转操作
'''

# 将对象x轴选择45度
cmds.rotate('45deg',0,0,r=True)

# 指定旋转时的的轴心位置
cmds.rotate(0,'180deg',0,'circle1', pivot=(1,0,0))

