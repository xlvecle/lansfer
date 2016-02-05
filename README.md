# lansfer

---

一款使用 http 来传输文件的命令行工具

使用场景:

+ 局域网传文件

安装:

+ pip install lansfer

使用方法:

> sf [-h] [-p PORT] filename
> rf [-h] filename
> 在一个命令行下输入 sf [你需要发送的文件], 在另一台机器的终端输入rf [刚才sf 生成的 url 或者生成的那一串 code]

特色:

+ 交互式操作, 体验人机互动快感, 还算好用
+ 轻量简洁

友情提示:

+ 本工具不适合用来替代 rsync, sftp, scp等
+ 本工具不适合用来做自动化
+ 本工具不适合在 windows 下使用