from urllib import request
#导入python ssl模块
import ssl
#利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context=ssl._create_unverified_context
url="https://www.12306.cn/mormhweb/"
rep=request.urlopen(url)
html=rep.read().decode()
print(html)