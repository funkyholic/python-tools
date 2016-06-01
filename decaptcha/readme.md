# 文档说明

## 外部依赖
执行tesseract识别需要在系统安装tesseract，并且能用tesseract命令

mac下安装tesseract

brew install tesseract

## 目录
char 存放预处理后的验证码图片

capthca 存放urllib抓取的验证码图片

## py文件

rof.py python计算机视觉一书提供的rof降噪算法

algorithm.py 定义各种算法

decaptcha.py 调用tesseract识别经过预处理的图片

floodfill.py flood fill算法

preprocess.py 对captcha目录中抓取的验证码进行图像预处理

getcaptcha.py 通过urllib抓取captcha图片

## 项目教程
简书: [http://www.jianshu.com/p/41127bf90ca9](http://www.jianshu.com/p/41127bf90ca9)