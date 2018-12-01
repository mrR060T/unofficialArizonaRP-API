
# -*- coding: utf-8 -*-

import requests
import time
import json
import os
try:
    from lxml import html
except:
    print("pip intall lxml or pip3 intall lxml")
    quit()
import urllib3
urllib3.disable_warnings()

class cabinet():

    def __init__(self, cookies):
        self.cookies = cookies

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://arizona-rp.com/',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'TE': 'Trailers',
        }

        self.htmlContent = html.fromstring(requests.get('https://arizona-rp.com/profile', headers=headers, cookies=cookies, verify=False).content)
        



    def fightStyle(self):
        try:
            profile_page = self.htmlContent

            Boxing = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[5]/div[1]/p[3]/span/text()')[0]
            Kungfu = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[5]/div[2]/p[3]/span/text()')[0]
            Kneehead = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[5]/div[3]/p[3]/span/text()')[0]
            GrabKick = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[5]/div[4]/p[3]/span/text()')[0]
            Elbow = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[5]/div[5]/p[3]/span/text()')[0]

            return{
                'boxing': Boxing,
                'kungfu': Kungfu,
                'kneehead': Kneehead,
                'grabKick': GrabKick,
                'elbow': Elbow
            }
        except:
            return 'Ошибка получения данных'


    def skill(self):
        try:
            profile_page = self.htmlContent
            m4 = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[3]/text()')[0].replace('%', '')
            ak = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[3]/text()')[0].replace('%', '')
            colt = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[3]/text()')[0].replace('%', '')
            usp = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[3]/text()')[0].replace('%', '')
            deagle = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[5]/div[3]/text()')[0].replace('%', '')
            shotgun = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[6]/div[3]/text()')[0].replace('%', '')
            mp5 = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[7]/div[3]/text()')[0].replace('%', '')
            sniper = profile_page.xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/div[8]/div[3]/text()')[0].replace('%', '')
       
            return {'m4': m4,
                    'ak': ak,
                    'colt': colt,
                    'usp': usp,
                    'deagle': deagle,
                    'shotgun': shotgun,
                    'mp5': mp5,
                    'sniper': sniper
                    }
        except:
            return 'Ошибка получения данных'
            

    def userInfo(self):
        try:        
            profile_page = self.htmlContent
            username = profile_page.xpath('//p[@class="b-title username"]/text()')[0]
            server = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[1]/p[2]/text()')[0]
            email = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[3]/p[2]/text()')[0]
            vip = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[4]/p[2]/text()')[0]
            player_id = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[2]/p[2]/text()')[0]
            level = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[5]/p[2]/text()')[0]
            twoauth = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[6]/p[2]/span/text()')[0]
            cash = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[7]/p[2]/text()')[0].replace('$', '')
            accumulations = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[8]/p[2]/text()')[0].replace('$', '')
            az = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[9]/p[2]/text()')[0]
            deposit = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[10]/p[2]/text()')[0].replace('$', '')
            status = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[11]/p[2]/text()')[0]
            job = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[12]/p[2]/text()')[0]
            organisation = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[13]/p[2]/text()')[0]
            rank = profile_page.xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[14]/p[2]/text()')[0]

            return {
                    'username': username,
                    'server': server,
                    'player_id': player_id,
                    'email': email,
                    'vip': vip,
                    'level': level,
                    '2auth': twoauth,
                    'cash': cash,
                    'accumulations': accumulations,
                    'az': az,
                    'deposit': deposit, 
                    'status': status,
                    'job': job,
                    'organisation': organisation,
                    'rank': rank
                    }
        except:
            return 'Ошибка получения данных'