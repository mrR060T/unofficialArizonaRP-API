from cabinet import cabinet

cookies = {
    "_csrf": "beca1db16fe73e6ee12017a0f264cc688de80c02484feba72ea47146be696d13a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22AAfQJ9v6QQluwRoPDmr83FVicVaOjd7j%22%3B%7D",
    "PHPSESSID": "obbloeaa6tfc0lbilbuk01f183", 
    "R3ACTLB": "eda1f7dd44e64778b46af1550a72762f",
    "serverID": "c01a5d4edebab15cc76460bbc64fe69bd25715bec7c0121ec8f191f888d04f9ea%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22serverID%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D"
}

user = cabinet(cookies=cookies)
info = user.skill()
print(info)