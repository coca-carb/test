#将本地的test.py文件上传到远程（Github）仓库
一. 首先克隆远程仓库到本地仓库
git clone 远程仓库地址链接

二. 在本地仓库创建编辑文件并同步
1.创建文件         touch (test.py)文件名.后缀
2.编辑修改         vi test.py    进入之后按 (i) 键，编辑完后按 (Esc) 键，之后英文状态下输入 (:wq)
3.添加文件到暂存区  git add test.py
4.添加到本地仓库    git commit -m '将a.py添加到本地仓库（添加描述）'
5.添加到远程仓库    git push
