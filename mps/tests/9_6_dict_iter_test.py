"""
deep comprehension of dictionary through the demo
"""


web_dict = {
    "baidu": "https://www.baidu.com/",
    "HG": "https://www.huggingface.co/",
    "bibi": "https://www.bilibili.com/",
}

for i in web_dict:
    print(i, "\n", web_dict[i])
print(web_dict.values(), "\n", "\n", web_dict.keys())

# 得到的输出如下：
"""
baidu 
 https://www.baidu.com/
HG 
 https://www.huggingface.co/
bibi 
 https://www.bilibili.com/
dict_values(['https://www.baidu.com/', 'https://www.huggingface.co/', 'https://www.bilibili.com/']) 
 
 dict_keys(['baidu', 'HG', 'bibi'])
"""