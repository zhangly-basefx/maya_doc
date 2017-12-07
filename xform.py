'''
这个命令用于查询或设置变换节点的属性元素
'''

# 为物体的Y旋转属性添加90
cmds.xform(r=True, ro=(0,90,0))

# 改变物体选择轴向的顺序，但不影响物体的变换属性
cmds.xform(p=True, roo='yzx')

# 返回对象的边界框，按以下顺序排列:xmin,ymin,zmin,xmax,ymax,zmax
cmds.xform(q=True, bb=True)

# 将轴心设置到物体中心
cmds.xform(cp=1)


