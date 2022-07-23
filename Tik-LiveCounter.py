from time import sleep
from requests import get
#Tiktok Live Counter non-stop
print("""

████████╗██╗██╗  ██╗     ██╗      ██████╗
╚══██╔══╝██║██║ ██╔╝     ██║     ██╔════╝
   ██║   ██║█████╔╝█████╗██║     ██║     
   ██║   ██║██╔═██╗╚════╝██║     ██║     
   ██║   ██║██║  ██╗     ███████╗╚██████╗
   ╚═╝   ╚═╝╚═╝  ╚═╝     ╚══════╝ ╚═════╝
                
          By @TweakPY - @vv1ck
""")
user=input('[?] Enter The user : ')#aa10935
try:
    head={'Host': 'tiktok.livecounts.io','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': f'https://tokcounter.com/?user={user}','X-Midas': 'bbfb14e47e2eabd33a0fc3df75371d8952f96c312d98f949d24a6606413ed3ff','X-Aurora': '4975747737387','X-Mayhem': 'none','Origin': 'https://tokcounter.com','Cache-Control': 'max-age=0','Te': 'trailers'}
    r1=get(f'https://tiktok.livecounts.io/search/{user}',headers=head)
    print('[-] searching for user ....')
    if r1.text.find(f"{user}")!=0:
        sleep(0.8)
        print('[+] Found ... !')
        s=input('[?] This is the user ['+str(r1.json()['userData']).split("'id':")[1].split(',')[0].split("'")[1]+'] [y/n] ? : ')
        if s=='y':
            userid=str(r1.json()['userData']).split("'userId':")[1].split(',')[0].split("'")[1]
            while True:
                r2=get(f'https://tiktok.livecounts.io/stats/{userid}',headers=head)
                sleep(0.2)
                print(f"""\n[+] Followers : {r2.json()['followerCount']}\n[+] Likes : {str(r2.text).split('bottomOdos')[1].split(':[')[1].split(',')[0]}\n[+] Following : {str(r2.text).split('bottomOdos')[1].split(':[')[1].split(',')[1].split(']}')[0]}""")
        else:
            print("[!] Fatel Error can't Find The user !!");print('[-] You must do that manually .. ');print("[!] Just search for the username and copy the userId")
            sleep(1)
            print(r1.text);print('-'*40)
            userid=input("[?] Enter The user id : ")
            try:
                r2=get(f'https://tiktok.livecounts.io/stats/{userid}',headers=head)
                while True:
                    r2=get(f'https://tiktok.livecounts.io/stats/{userid}',headers=head)
                    sleep(0.2)
                    print(f"""\n[+] Followers : {r2.json()['followerCount']}\n[+] Likes : {str(r2.text).split('bottomOdos')[1].split(':[')[1].split(',')[0]}\n[+] Following : {str(r2.text).split('bottomOdos')[1].split(':[')[1].split(',')[1].split(']}')[0]}""")
            except:exit("[!] Fatel Error !")
    else:print('[!] Sorry user not Found !')
except KeyboardInterrupt:exit()
except:exit("[!] Fatel Error !")