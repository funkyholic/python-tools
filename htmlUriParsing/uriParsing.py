#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding: utf-8-*-
import re
import os,sys


class UriFormattingFactory(object):
	source = []
	pattern = ""
	
	def __init__(self, pattern):
		self.pattern = pattern
	
	def setSource(self,*k):
		self.source = k
			
	
	def doFormat(self, filename, replacement):
		pt = re.compile(self.pattern, re.IGNORECASE)
		with open(filename, "rb" ) as file:
			data = file.read().decode("gb18030")	#二进制读入文件，以gb18030编码解读
			k = pt.search(data)
			if(k):
				print(k.group())
				result = pt.sub(replacement,data)
				with open("./output/" + filename, "w", encoding="gb18030") as outputFile:
					outputFile.write(result)	#保存为gb18030编码
					print("success")
					return True
			else:
				print("no match")
				return False
	
	def doMultiFormats(self, replacement):
		for file in self.source:
			self.doFormat(file, replacement)
			
		
			
	def setPattern(self):
		pass
		
	


if __name__ == "__main__":
	
	pattern = r"(?P<pre><\s*(link|img|script)\s+(.*?)(href|src)\s*=\s*\")(?P<uri>/?.*?)(?P<post>\"(.*?)/?(.*?)>)"
	
# 	pattern = r'<\s*script[^>]*>[^<]*<\s*/\s*script\s*>'
	
	#自定义替换函数
	def replacement(matched):
		pre = matched.group("pre")
		post = matched.group("post")
		uri = matched.group("uri")
		if(uri.startswith("/")):
			return pre+uri[1:]+post	#如果有斜杠去掉斜杠
		else:
			return matched.group()
	
	files = []
	content = os.listdir(os.getcwd())
	for item in content:
		if(os.path.isfile(item) and item.split(".")[-1]=="html"):	#过滤出当前文件夹下".html"文件
			files.append(item)
	print(files)
	
	UFF = UriFormattingFactory(pattern)	#初始化pattern
	UFF.setSource(*files)
	UFF.doMultiFormats(replacement)
	
	print("success")