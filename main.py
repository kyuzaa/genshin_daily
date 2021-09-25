import requests
import os

cookies = os.environ.get('COOKIES')
print(cookies)
# url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?act_id=e202102251931481&lang=en-us"

# cookies = {'ltuid': ltuid, 'ltoken': ltoken}

# r = requests.post(url, cookies=cookies)
# print(r.json())