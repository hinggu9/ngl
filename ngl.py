import requests, threading, asyncio

instagram = "" #NGL 아이디
message = "" #질문
device = ""

async def go():
    req = requests.Session()
    r = req.post(f'https://ngl.link/api/submit', headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}, data={
                'username': instagram,
                'question': message,
                'deviceId': device
            })
    print('\033[32m' + f"[ NGL ] Submit 을 Post 시도했어요!" + '\033[0m')
    print('\033[33m' + f"[ NGL value ] {r}" + '\033[0m')

for i in range(int(10)): #기본 보낼갯수
    threading.Thread(target=asyncio.run, args=(go(),)).start()
