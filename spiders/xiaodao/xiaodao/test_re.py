import re

import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

strs = '''
百度：https://pan.baidu.com/s/1-shzVDlAx4iK8UkS7AOqEw 提取码: 2333

天翼：https://cloud.189.cn/t/IB3ieymQJ7re（访问码：uf34）
'''

print(strs)
res = re.match(r'https://pan.baidu.*', strs)
print(res)  