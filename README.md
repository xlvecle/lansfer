# lansfer

---

一款使用 python SimpleHTTPServer 来传输文件的命令行工具

>[http://xlvecle.github.io/lansfer/](http://xlvecle.github.io/lansfer/)

使用场景:

+ 局域网传文件

安装:

+ pip install lansfer

使用方法:

> sf [-h] [-p PORT] [-a] filename

> rf [-h] filename

> 在一台机器的终端输入 sf [你需要发送的文件], 在另一台机器的终端输入rf [刚才sf 生成的 url 或者生成的那一串 code]

> **多次传输或者大文件(传输时间大于20s)请使用 -a 选项, 保持服务不中断**

特色:

+ 交互式操作, 体验人机互动快感, 还算好用
+ 轻量简洁
+ 不加 -a 选项会自动停止, 加上 -a 需要手动停止

友情提示:

+ 本工具不适合用来替代 rsync, sftp, scp等
+ 本工具不适合用来做自动化
+ 本工具不适合在 windows 下使用