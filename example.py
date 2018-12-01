from cabinet import cabinet

cookies = {
    "_csrf": "xxx",
    "PHPSESSID": "xxx", 
    "R3ACTLB": "xxx",
    "serverID": "xxxx"
}

user = cabinet(cookies=cookies)
info = user.skill()
print(info)