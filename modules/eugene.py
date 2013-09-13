import os
import simplejson
import requests
import random
from time import sleep
import re

dotdir = os.path.expanduser('~/.phenny')
cookie_file = dotdir+'/eugene.json'

EUGENE_URL = "http://www.princetonai.com/bot/botanswer.do"

def load_cookies():
    try:
        f = open(cookie_file)
        cookies = simplejson.loads(f.read())
        f.close()
        return cookies
    except:
        return {}

def save_cookies(cookies):
    try:
        f = open(cookie_file, 'w')
        f.write(simplejson.dumps(cookies, indent=2))
        f.close()
        return True
    except:
        return False

def get_cookie(username):
    cookies = load_cookies()
    if username in cookies:
        return {"JSESSIONID": cookies.get(username)}
    else:
        return {}

def set_cookie(username, cookie):
    cookies = load_cookies()
    cookies[username] = cookie
    save_cookies(cookies)

def eugene(phenny, input):
    cookies = get_cookie(input.nick)
    payload = {"request": input[11:]}

    r = requests.get(EUGENE_URL, params=payload, cookies=cookies)

    if len(r.cookies):
        set_cookie(input.nick, r.cookies['JSESSIONID'])

    sleep(random.randrange(2,5))
    reply = re.sub('Eugene', 'SkizzyBot')
    phenny.reply(reply)

eugene.rule = r'$nickname:?'
eugene.priority = 'low'
eugene.thread = False
