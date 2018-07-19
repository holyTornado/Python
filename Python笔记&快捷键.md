# 目录
## [**Python学习笔记**](#学习笔记)
1. [构建发布](#构建发布)
2. [GitHub的使用](#GitHub的使用)
    1. [注册GitHub帐号](#注册GitHub帐号)
    2. [通过PyCharm（2018.1.4）初始化Git环境](#通过PyCharm（2018.1.4）初始化Git环境)
    3. [分支操作(待写)](#分支操作)
3. [待添加](#待添加)


## [**Python快捷键**](#快捷键)
- [常用快捷键](#常用快捷键)
- [全部快捷键](#全部快捷键)
    - [01、编辑(Editing)](#1、编辑)
    - [02、查找/替换(Search/Replace)](#2、查找/替换)
    - [03、运行(Running)](#3、运行)
    - [04、调试(Debugging)](#4、调试)
    - [05、导航(Navigation)](#5、导航)
    - [06、搜索相关(Usage Search)](#6、搜索相关)
    - [07、重构(Refactoring)](#7、重构)
    - [08、控制(VCS/Local History)](#8、控制)
    - [09、模版(Live Templates)](#9、模版)
    - [10、基本(General)](#10、基本)

---
---

# 学习笔记

## 构建发布
1. **首先为模块创建一个文件夹**。创建了文件夹之后，将 demo.py （示例，扩展名为py的文件）模块文件复制到这个文件夹中。
2. **在新文件夹中创建一个名为“setup.py”的文件**。这个文件包含有关发布的元数据。编辑这个文件，代码如下：

>
    from distutils.core import setup
    setup(
        name = "name",
        versin = "1.0.0",
        py_modules = ["modules"],
        author = "author",
        author_email = "author_email@hotmail.com",
        url = "url",
        description = "description...",
    )

3. **构建一个发布文件**。发布工具包含有构建一个发布所需的所有功能。在创建的文件夹中打开一个终端窗口，（进入模块所在目录，本机所在位置：D:\\Python\\MyPython\\Distribution），键入一行命令：<font color="red">python.exe setup.py sdist</font>（注意“python.exe”的系统路径。）
4. **将发布安装到你的Python本地副本中**。仍然在终端窗口中，键入以下命令：<font color="red">python.exe setup.py install</font>（注意“python.exe”的系统路径。）
5. **发布到PyPi**。首先，在PyPi注册帐号，<font color="red">【**注意**：Windows系统，首次上传，检查系统用户文件夹下（C:\Users\GYang）是否有文件“**.pypirc**”，如果没有，创建一个空文件名的文件，扩展名是“pypirc”。文件内容如下：

>
    [distutils]
    index-servers = pypi
    [pypi]
    repository = https://upload.pypi.org/legacy/
    username:<username>   #这里是PyPi网站的用户名
    password:<password>   #这里是PyPi网站的密码
】</font>；然后在终端进入需要上传的文件夹，执行命令：<font color="red">python.exe setup.py sdist upload</font>；最后显示“<font color="red">Server response(200)：OK</font>”，上传成功（不再出现<font color="red">**403**</font>的错误提示）

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

---

## GitHub的使用

### **注册GitHub帐号**
这个不多说，网有一大堆。

### **通过PyCharm（2018.1.4）初始化Git环境**
1. **连接设置**，通过菜单：VCS->Checkout from Version Control->Git，打开“Clone Repository”窗口。URL栏输入Git的仓库地址，Directory栏选择本地的同步Git文件夹，点击“Clone”按钮完成初始化。Checkout之后，可能PyCharm识别不到，这时候通过菜单：VCS->Enable Version Control Integration，启动一下。
2. **状态颜色说明：**
    - <font color=red>红色：新建文件（目录），表示还未add；</font>
    - <font color=LawnGreen>绿色：add之后，变成绿色；</font>
    - <font color=DodgerBlue>蓝色：做过修改的，变为蓝色；</font>
    - <font color=Gray>灰色：被忽略的文件是灰色的。</font>
3. **提交**，（可以不用add，而直接提交），通过“VCS”菜单，或者直接目录/文件鼠标右键弹出菜单，下的Git->Commit Directory，打开“CommitChanges”窗口，在这里选择在提交的文件或文件夹，在“Commit Message”中添写提交说明，然后点击“Commit and Push……”按钮，完成提交操作。过程中会很明确的，这是从本地的master上传到Origin远端的master上。push之后，就可以在GitHub上看到了。

### **分支操作**
<font color=red>下次再写，参考网址[通过pycharm使用git[图文详解]](http://www.cnblogs.com/caseast/p/6085837.html)</font>


>>>[**<p align="right">>>返回目录<<</p>**](#目录)

---

## 待添加

### 这里是待添加的笔记内容：
>这里是……

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

---
---

# 快捷键
## 常用快捷键
|快捷键|功能|
|-|-|
|Ctrl + Q|快速查看文档|
|Ctrl + F1|显示错误描述或警告信息|
|Ctrl + /|行注释|
|Ctrl + Alt + L|代码格式化|
|Ctrl + Alt + O|自动导入|
|Ctrl + Alt + I|自动缩进|
|Tab/Shift + Tab|缩进、不缩进当前行|
|Ctrl + C/Ctrl + Insert|复制当前行或选定的代码块到剪贴板|
|Ctrl + D|复制选定的区域或行到后面或下一行|
|Ctrl + Y|删除当前行|
|Shift + Enter|下一行另起一行|
|Ctrl + J|插入模版|
|Ctrl + Numpad+/-|展开折叠代码块|
|Ctrl + Numpad+|全部展开|
|Ctrl + Numpad-|全部折叠|
|Ctrl + Delete|删除到字符结束|
|Ctrl + Backspace|删除到字符开始|
|Ctrl + Shift + F7|将当前单词在整个文件中高亮，F3移动到下一个，ESC取消高亮。|
|Alt + up/down|方法上移或下移动|
|Alt + Shift + up/down|当前行上移或下移动|
|Ctrl + B/鼠标左键|转到方法定义处|
|Ctrl + W|选中增加的代码块|
|Shift + F6|方法或变量重命名|
|Ctrl + E|最近访问的文件|
|Esc|从其他窗口回到编辑窗口|
|Shift + Esc|隐藏当前窗口，焦点到编辑窗口|
|F12|回到先前的工具窗口|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

---

## 全部快捷键
### 1、**编辑**
>**编辑 (Editing)**

|快捷键|功能|
|-|-|
|Ctrl + Space|基本的代码完成（类、方法、属性）|
|Ctrl + Alt + Space|快速导入任意类|
|Ctrl + Shift + Enter|语句完成|
|Ctrl + P|参数信息（在方法中调用参数）|
|Ctrl + Q|快速查看文档|
|Shift + F1|外部文档|
|Ctrl + 鼠标|简介|
|Ctrl + F1|显示错误描述或警告信息|
|Alt + Insert|自动生成代码|
|Ctrl + O|重新方法|
|Ctrl + Alt + T|选中|
|Ctrl + /|行注释|
|Ctrl + Shift + /|块注释|
|Ctrl + W|选中增加的代码块|
|Ctrl + Shift + W|回到之前状态|
|Ctrl + Shift + ]/[|选定代码块结束、开始|
|Alt + Enter|快速修正|
|Ctrl + Alt + L|代码格式化|
|Ctrl + Alt + O|自动导入|
|Ctrl + Alt + I|自动缩进|
|Tab/Shift + Tab|缩进、不缩进当前行|
|Ctrl + X/Shift + Delete|剪切当前行或选定的代码块到剪贴板|
|Ctrl + C/Ctrl + Insert|复制当前行或选定的代码块到剪贴板|
|Ctrl + V/Shift + Insert|从剪贴板粘贴|
|Ctrl + Shift + V|从最近的缓冲区粘贴|
|Ctrl + D|复制选定的区域或行到后面或下一行|
|Ctrl + Y|删除当前行|
|Ctrl + Shift + J|添加智能线|
|Ctrl + Enter|智能线切割|
|Shift + Enter|下一行另起一行|
|Ctrl + Shift + U|在选定的区域或代码块间切换|
|Ctrl + Delete|删除到字符结束|
|Ctrl + Backspace|删除到字符开始|
|Ctrl + Numpad+/-|展开折叠代码块|
|Ctrl + Numpad+|全部展开|
|Ctrl + Numpad-|全部折叠|
|Ctrl + F4|关闭运行的选项卡|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 2、**查找/替换**
>**查找/替换 (Search/Replace)**

|快捷键|功能|
|-|-|
|F3|下一个|
|Shift + F3|前一个|
|Ctrl + R|替换|
|Ctrl + Shift + F|全局查找|
|Ctrl + Shift + R|全局替换|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 3、**运行**
>**运行 (Running)**

|快捷键|功能|
|-|-|
|Alt + Shift + F10|运行模式配置|
|Alt + Shift + F9|调试模式配置|
|Shift + F10|运行|
|Shift + F9|调试|
|Ctrl + Shift + F10|运行编辑器配置|
|Ctrl + Alt + R|运行manage.py任务|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 4、**调试**
>**调试 (Debugging)**

|快捷键|功能|
|-|-|
|F8|跳过|
|F7|进入|
|Shift + F8|退出|
|Alt + F9|运行游标|
|Alt + F8|验证表达式|
|Ctrl + Alt + F8|快速验证表达式|
|F9|恢复程序|
|Ctrl + F8|断点开关|
|Ctrl + Shift + F8|查看断点|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 5、**导航**
>**导航 (Navigation)**

|快捷键|功能|
|-|-|
|Ctrl + N|跳转到类|
|Ctrl + Shift + N|跳转到符号|
|Alt + Right/Left|跳转到下一个、前一个编辑的选项卡|
|F12|回到先前的工具窗口|
|Esc|从其他窗口回到编辑窗口|
|Shift + Esc|隐藏当前窗口，焦点到编辑窗口|
|Ctrl + Shift + F4|关闭主动运行的选项卡|
|Ctrl + G|查看当前行号、字符号|
|Ctrl + E|最近访问的文件|
|Ctrl + Alt + Left/Right|后退、前进|
|Ctrl + Shift + Backspace|导航到最近编辑区域|
|Alt + F1|查找当前文件或标识|
|Ctrl + B/Ctrl + Click|跳转到声明|
|Ctrl + Alt + B|跳转到实现|
|Ctrl + Shift + I|查看快速定义|
|Ctrl + Shift + B|跳转到类型声明|
|Ctrl + U|跳转到父方法、父类|
|Alt + Up/Down|跳转到上一个、下一个方法|
|Ctrl + ]/[|跳转到代码块结束、开始|
|Ctrl + F12|弹出文件结构|
|Ctrl + H|类型层次结构|
|Ctrl + Shift + H|方法层次结构|
|Ctrl + Alt + H|调用层次结构|
|F2/Shift + F2|下一条、前一条高亮的错误|
|F4/Ctrl + Enter|编辑资源、查看资源|
|Alt + Home|显示导航条F11书签开关|
|Ctrl + Shift + F11|书签助记开关|
|Ctrl + #[0-9]|跳转到标识的书|
|Shift + F11|显示书签|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 6、**搜索相关**
>**搜索相关 (Usage Search)**

|快捷键|功能|
|-|-|
|Alt + F7/Ctrl + F7|文件中查询用法|
|Ctrl + Shift + F7|文件中用法高亮显示|
|Ctrl + Alt + F7|显示用法|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 7、**重构**
>**重构 (Refactoring)**

|快捷键|功能|
|-|-|
|F5|复制|
|F6|剪切|
|Alt + Delete|安全删除|
|Shift + F6|方法或变量重命名|
|Ctrl + F6|更改签名|
|Ctrl + Alt + N|内联|
|Ctrl + Alt + M|提取方法|
|Ctrl + Alt + V|提取属性|
|Ctrl + Alt + F|提取字段|
|Ctrl + Alt + C|提取常量|
|Ctrl + Alt + P|提取参数|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 8、**控制**
>**控制 (VCS/Local History)**

|快捷键|功能|
|-|-|
|Ctrl + K|提交项目|
|Ctrl + T|更新项目|
|Alt + Shift + C|查看最近的变化|
|Alt + BackQuote(’)VCS|快速弹出|
|Ctrl + Alt + J|当前行使用模版|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 9、**模版**
>**模版 (Live Templates)**

|快捷键|功能|
|-|-|
|Ctrl + Alt + J|当前行使用模版|
|Ctrl + J|插入模版|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)

### 10、**基本**
>**基本 (General)**

|快捷键|功能|
|-|-|
|Alt + #[0-9]|打开相应编号的工具窗口|
|Ctrl + Alt + Y|同步|
|Ctrl + Shift + F12|最大化编辑开关|
|Alt + Shift + F|添加到最喜欢|
|Alt + Shift + I|根据配置检查当前文件|
|Ctrl + BackQuote(’)|快速切换当前计划|
|Ctrl + Alt + S　|打开设置页|
|Ctrl + Shift + A|查找编辑器里所有的动作|
|Ctrl + Tab|在窗口间进行切换|

>>>[**<p align="right">>>返回目录<<</p>**](#目录)
