
请使用python3
在uriRegex.py 的首行 指定python3的路径
以顶层模块运行.py 不要导入

使用:
1 定义将要匹配的正则模式:pattern
2 初始化工厂类 UriFormattingFactory(pattern)
3 设置文件路径 UriFormattingFactory.setSource(...)
4 处理文件 UriFormattingFactory.doMultiFormats(...)

遇到文件编码问题请到UriFormattingFactory.doFormat(...)函数中修改文件读取的编码
要自定义替换规则 请修改 replacement函数

默认pattern:
pattern = r"(?P<pre><\s*(link|img|script)\s+(.*?)(href|src)\s*=\s*\")(?P<uri>/?.*?)(?P<post>\"(.*?)/?(.*?)>)"

匹配html标签<script>，<img>，<link>中带有的href，src属性，对属性值进行修改

修改函数:
def replacement(matched):
		pre = matched.group("pre")
		post = matched.group("post")
		uri = matched.group("uri")
		if(uri.startswith("/")):
			return pre+uri[1:]+post	#如果有斜杠去掉斜杠
		else:
			return matched.group()	#没有斜杠就不修改