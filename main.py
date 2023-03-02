# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import requests


from lxml import etree
url = 'https://cs.nju.edu.cn/lwz/networks/index.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

page_text = requests.get(url=url, headers=headers)
tree = etree.HTML(page_text.text)


print(page_text.text)
tr_list = tree.xpath('/html/body/ul[3]/h3[2]/table/tr')
print(tr_list)
'/html/body/ul[3]/h3[2]/table/tbody/tr[1]'
result = []
#'/html/body/ul[3]/h3[2]/table/tbody/tr[2]/td[2]/a[1]'
#'/html/body/ul[3]/h3[2]/table/tbody/tr[2]/td[2]/a[2]'
#'/html/body/ul[3]/h3[2]/table/tbody/tr[4]/td[2]/a'
#'/html/body/ul[3]/h3[2]/table/tbody/tr[28]/td[2]/a'
label = '/html/body/ul[3]/h3[2]/table/tbody/tr[2]/td[2]/a[1]/text()'
tmp = tr_list[1].xpath(label)
print(tmp[0])
# for i in range(1, 15):
#     label = '/html/body/ul[3]/h3[2]/table/tbody/tr[' + str(2*i) + ']/td[2]/a[text()="slides"]/@href'
#     tmp = tr_list[i-1].xpath(label)
#     result.append(tmp[0])
# print(result)

