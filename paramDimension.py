'''
在curve上创建一个拽点，用于显示指定点在曲线上的参数值
'''

# 创建一个曲线，再在这个曲线上创建拽点
cmds.circle(r=2.206276)
cmds.paramDimension('nurbscircleShape1.u[0.5]')

