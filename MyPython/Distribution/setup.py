from distutils.core import setup
setup(
	name="MoviesNester",
	version="2.0.2",
	py_modules=["MoviesNester"],
	author="Guo.yang",
	author_email="gyang973256@gmail.com",
	url="https://github.com/holyTornado",
	description="保存文件时，由于是递归操作，每次重新写入，导致文件只存了最后一个列表的内容。"
				"修改为追加写入，但没有加入文件权限的判断",
)
