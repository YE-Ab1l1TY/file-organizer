# File Organizer

一个早期练手用的简单文件整理工具。

程序会让用户选择一个文件夹，然后根据文件扩展名自动将其中的文件分类到不同目录中，例如：

- 文档
- 图片
- 代码
- 压缩包
- 音频
- 视频

> 这是一个较早期的个人练习项目，功能比较基础，主要用于熟悉 Python、文件操作、Tkinter 文件夹选择以及程序打包流程。

## 使用方法

### 方式一：直接下载可执行程序

如果只是想使用程序，可以直接前往 GitHub Releases 下载已经打包好的 Windows 可执行文件：

[Download from Releases](https://github.com/YE-Ab1l1TY/file-organizer/releases)

当前 Release 中提供：

```text
YE.exe
```

下载后直接运行即可，不需要另外安装 Python。

运行程序后：

1. 在弹出的窗口中选择需要整理的文件夹
2. 程序会自动创建对应的分类文件夹
3. 文件会按照扩展名移动到对应分类中

例如：

```text
原文件夹
├── report.pdf
├── photo.png
├── test.py
├── music.mp3
└── video.mp4
```

整理后大致会变成：

```text
原文件夹
├── 文档/
│   └── report.pdf
├── 图片/
│   └── photo.png
├── 代码/
│   └── test.py
├── 音频/
│   └── music.mp3
└── 视频/
    └── video.mp4
```

## 源码运行

项目主要使用 Python 编写。

```bash
python organizer.py
```

主要使用的标准库包括：

```text
os
shutil
tkinter
```

因此源码本身不依赖额外的第三方 Python 包。

## 说明

这是我较早期完成的一个小工具，目前功能还比较简单，对文件类型和异常情况的处理也不算完善，但用于日常做一些基础的文件分类已经足够。

建议在重要文件上使用前先做好备份。

## License

MIT License
