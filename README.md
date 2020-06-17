UI、APP、接口通用自动化测试框架
====
1.项目概述
-------
python3+unittest+beautiful报告，UI、APP、接口共用一套框架，excel编写测试用例，暂时不支持多线程，

###
2.目录简介
-------
- **[app]()**：封装app的方法 
- **[web]()**：web方法的封装
- **[interface]()**：接口方法的封装 
- **[utest]()**：封装的datadriven和WebTest方法，datadriven封装反射法，WebTest组织脚本执行读取用例、执行用例、统计用例结果、发送测试报告
- **[common]()**：公共模块，日志、excel的读写、结果用例统计、邮件的配置、数据库的配置  
- **[conf]()**：配置信息，如yaml文件，邮件模板
- **[data/case]()**：用于excel用例存放,及准备的其他辅助测试数据
- **[lib]()**：浏览器驱动、autoit封装的exe文件等
- **[outputs]()**：存放报告、结果用例、日志、错误截图
- **[runUnitTestWEB]()**：脚本主入口，采用了unittest框架和beautiful报告，暂不支持多线程
- **[mainruner]()**：脚本主入口，纯代码框架，已支持多线程



3、不足和优化
-------
app、web、和接口封装的方法偏少，后续需要不断完善，报告需要优化