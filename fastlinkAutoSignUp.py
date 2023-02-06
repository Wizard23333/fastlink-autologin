import requests
import time
import os

check_in_data = [
    {
        "email": os.getenv("EMAIL"),
        "passwd": os.getenv("PASSWORD")
    },
]
MAX_RETRY_TIME = 3


def auto_check_in(data):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    login_url = "https://www.fastlink.pro/auth/login"
    check_in_url = "https://www.fastlink.pro/user/checkin"

    login_req = requests.post(url=login_url, data=data)
    print(login_req.json())

    cookies = login_req.cookies
    check_in_req = requests.post(url=check_in_url, cookies=cookies)
    print(check_in_req.json())


if __name__ == '__main__':
    print("fastlink: ")
    for data in check_in_data:
        is_succeed = False
        for _ in range(0, MAX_RETRY_TIME):
            if is_succeed:
                break
            try:
                auto_check_in(data)
                is_succeed = True
            except Exception as e:
                print(e)
