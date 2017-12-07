'''
为节点添加动态属性。必须指定属性的longName或简称。如果没有制定，则添加一个双精度属性。
'''

# 添加一个属性mass，默认值1,最大值10000,最小值0.001
cmds.addAttr(shortName='ms', longName='mass', defaultValue=1.0, minValue=0.001, maxValue=10000)


