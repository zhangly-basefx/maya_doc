'''
创建locator
'''

# 在指定位置创建locator
cmds.spaceLocator( p=(1,1,1) )

# 以英寸为单位创建locator
cmds.spaceLocator( p=('1in','1in','1in') )
