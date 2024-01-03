"""this is a cp demo for web page information acquiring"""


from multiprocessing import Process, Queue
import requests

web_dict = {
    "baidu": "https://www.baidu.com/",
    "HG": "https://www.huggingface.co/",
    "bibi": "https://www.bilibili.com/",
}


# for i in web_dict:
#     print(i, web_dict[i])
# 注意这里字典数据类型的遍历方法

def producer(name, url, q):
    ret = requests.get(url)
    """
    ret变量将包含一个Response对象，该对象包含了从服务器返回的HTTP响应的信息，包括响应状态码、响应头部和响应正文等。
    要访问响应的内容，您可以使用ret对象的不同属性和方法，例如：
    ret.status_code：获取响应的状态码，如200表示成功，404表示未找到等。
    ret.headers：获取响应的头部信息。
    ret.text：获取响应的文本内容，如果响应是HTML页面或纯文本，则可以使用这个属性。
    ret.json()：如果响应是JSON格式的数据，则可以使用这个方法解析JSON数据。
    """

    q.put((name, ret.text))


def consumer(q):
    while 1:
        tup = q.get()
        if tup is None: # 注意这里不能使用 == 而是要使用is.
            break
        with open(f"{tup[0]}.html", mode="w", encoding="utf-8") as f:
            f.write(tup[1])


if __name__ == "__main__":
    q = Queue()
    p_list = []
    for k in web_dict:
        p = Process(target=producer, args=(k, web_dict[k], q))
        p.start()
        p_list.append(p)
    Process(target=consumer, args=(q, )).start()
    for p in p_list:
        p.join()
    q.put(None)