import requests


def main():
    name = input("enter ur name: ")
    # 发送post请求到服务器
    response = requests.post("http://127.0.0.1:8080/greet", data={"name": name})
    print(response.text)


if __name__ == "__main__":
    main()