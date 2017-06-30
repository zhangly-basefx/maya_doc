# 返回maya版本号
cmds.about(v=True)

# 返回maya api版本
cmds.about(apiVersion=True)

# 返回maya运行时的编码
cmds.about(codeset=True)

# 返回用户是否存在网络链接
cmds.about(connected=True)

# 返回当前时间与日期，格式为 Wed Jan 02 02:03:55 1980\n\0
cmds.about(ctime=True)

# 返回maya环境配置文件
cmds.about(environmentFile=True)

# 返回帮助文件路径
cmds.about(helpDateDirectory=True)

# 返回产品版本
cmds.about(installedVersion=True)

# 返回maya版本是否是64位
cmds.about(x64=True)

# 返回当前的使用语言
cmds.about(languageResources=True)

# 返回操作系统是否为xxx
cmds.about(linux=True)
> linux

cmds.about(mac=True)
> macOS

cmds.about(ntOS=True)
> windows

# 返回Autodesk格式产品信息
cmds.about(liveUpdate)
>>> ("MAYA","2016","Linux64","201603180400-990260")

