
# 1. 何謂網路(network)？Domain 4的口訣為何？代表什麼意義？網路工程要唸那些議題？

1.1 何謂網路(network)？
Answer：

網路(network)是一種系統
- 組成元素：由傳輸媒介(transport media) 與節點(node) 組成
- 存在目的：目的在於傳輸訊息、共享資源

```Wuson
老師補充:
- 為達到【資源共享】與【互傳訊息】的目的，透過傳輸媒介(Media)將兩個以上節點(Node)連接起來所形成的【結構(拓樸)】稱之為網路。
- 處處都安全是風險識別原則—從網路的架構（主要元素及其關係）來識別風險。
```

1.2 Domain 4的口訣為何？
Answer：

 處處都安全

1.3  代表什麼意義？
Answer：

代表在網路的架構面，各個主要元素都要做好安全控制，達到縱深防禦，做到處處都安全

1.4 網路工程要唸那些議題？
Answer：

核心主題：
- OSI Model
- IEEE 802
- TCP/IP
- 滲透測試

---
# 2. 何謂鏈結(link)與路徑(route)？何謂點對點(P2P)與端到端(E2E)？

2.1 何謂鏈結(link)與路徑(route)？
Answer：

在基礎網路拓撲(Network Topology)中，節點連接方式：
鏈結(link)：兩個 Node 直連沒有穿插 Node
路徑(route)：起點＆終點 Node 中間有走過 Node

2.2 何謂點對點(P2P)與端到端(E2E)？
Answer：

點對點(P2P)：Link 的延伸，兩個 Node 直連，而中間的傳輸媒介就是 Link
端到端(E2E)：Route 的延伸，兩個 Node 間接相連，中間的傳輸媒介即是 Route

```Wuson:
Link跟Route的觀念不夠清楚, 以下補充:
• Link跟Route是表達二個節點之間的【連接線】，簡稱連線；P2P與E2E是表達二個節點之間的相對【關係】。【連線】跟【關係】是不同概念，不能混為一談。
• 鏈結(link)：連接二個相鄰節點（無中間節點）的連線(connection)。
• 路徑(route)：連接二個不相鄰節點（有中間節點）的連線(connection)。路徑也可以說是由多個鍵結(link)所組成的連線。route也稱作path。
• 點對點(P2P)：指二個節點的關係是相鄰或直接相連（無中間節點）。
• 端到端(E2E)：指二個節點的關係是不相鄰或間接相連（有中間節點）。
```

---
# 3.  我們的課程把ISO OSI的七層模型再簡化為那二件事？ 請簡述ISO OSI【各層的重點】。

3.1 我們的課程把ISO OSI的七層模型再簡化為那二件事？ 請簡述ISO OSI【各層的重點】。
Answer：

課程中把ISO OSI的七層模型再簡化描述成「架網路」(LAN)、「用網路」(WAN)

ISO OSI(Open System Interconnection Model)
1. 實體層(Physical)：
	- 傳輸媒介(Media)
	- 訊號類別(Signal)
	- 傳輸模式(Transmission)
2. 資料鏈結層(Data Link)：共用傳輸媒介的使用規則
	- 媒體存取控制(MAC, Media Access Control)
	- 邏輯鏈結控制(LLC, Logical Link Control)
3. 網路層(Network)：who am I, where am I, & where i go
	- 定址(Addressing)
	- 路由交換方式(Routing)
	- 控制(Controlling)
4. 傳輸層(Transport)：傳輸模式(how to go)
	- 傳輸控制協定(TCP, Transmission Control Protocol/ 連接導向式通訊(Connection-oriented)
	- 使用者資料包協定(UDP, User Datagram Protocol) /無連接式通訊(Connectionless)
5. 會議層(Session)：「Session」是指一段專門用於特定活動的時間(登入到登出的那一段時間)
	- Token Management(身分驗證(Authentication)&檢查授權(Authorization))
	- State Management(token 即是一種狀態管理機制)
		- 用戶本地儲存(Client-Side Storage)
		- 伺服器端儲存(Server-Side Storage)
	- Interaction Management：會話方向
		- 單工(Simplex)
		- 半雙工(Half-Duplex)
		- 全雙工(Full-Duplex)
	- Protocols
		- PAP, Password Authentication Protocol
		- SIP, Session Initiation Protocol
		- RPC, Remote Procedure Call
		- NetBIOS, Network Basic Input/Output System
6. 展示層(Presentation)：訊息如何呈現
	- 編碼(Encoding)
	- 壓縮(Compression)
	- 加密(Encryption)
7. 應用層(Application)：Protocol 的用途與配套

```Wuson
應用層：用途、訊息及指令
```

---
# 4. 何謂封包(Protocol Data Unit, PDU)? 何謂unicast, multicast, broadcast與anycast？

4.1 何謂封包(Protocol Data Unit, PDU)?
Answer：

協定資料單元(PDU)：即封包，由 表頭(Header), 載荷(Payload) 組成
PDU: {Header, Payload}
- Header
	- ==Source== 
	- ==Destination==
- Payload
	- Service Data Unit (SDU)

4.2 何謂unicast, multicast, broadcast與anycast?
Answer：

單播(Unicast)：
- One-to-One 的通訊，請封包發送給指定的接收節點
群播(Multicast)：
- One-to-All 的通訊，位於同一個群組的節點都會收到封包(Subnet IP address)
廣播(Broadcast)：
- One-to-Many 的通訊，發送封包給位於同個網路的節點，網路內的所有節點
任播(Anycast)：
- One-to-One of Many, 封包會發送至最近或最好(路由)的節點 



---
# 5. 乙太網路100BASE-TX使用那一種訊號(signal)、線材(cable)以及那一種媒體存取控制(MAC)的機制？無線網路802.11be (Wi-Fi 7) 使用了那些頻帶(bands)？這二者傳輸率的理論上限值為何？

5.1 乙太網路100BASE-TX使用那一種訊號(signal)、線材(cable)以及那一種媒體存取控制(MAC)的機制？
Answer：

乙太網路100BASE-TX：
- 訊號(signal)：數位訊號(Digital)
- 線材(cable)：雙絞線(Twisted pair)
- 媒體存取控制(MAC)：CSMA/CD

5.2 無線網路802.11be (Wi-Fi 7) 使用了那些頻帶(bands)？
Answer：

- 2.4GHz
- 5GHz
- 6GHz


5.3 這二者傳輸率的理論上限值為何？
Answer：

乙太網路100BASE-TX：100Mbps
無線網路802.11be (Wi-Fi 7)：46Gbps

---
# 6. 請參考講義，簡述Wi-Fi無線網路各個世代的安全機制。

6.1 請參考講義，簡述Wi-Fi無線網路各個世代的安全機制。
Answer：

1. 無線加密協定(WEP, Wireless Encryption Protocol)
	- 無身份驗證機制
	- 加密採用 RC4 演算法，現已遭破解棄用
2. Wi-Fi存取保護(WPA, Wi-Fi Protected Access)
	- 具身份驗證機制
	- 分為個人(PSK, Pre-Shared Key)與企業版(802.1X standard)
3. WPA2, Wi-Fi Protected Access 2
	- 為 WPA 的正式版(WPA 是臨時推出)，採用正式版的 802.11i
	- 加密演算法升級為 AES-128 bits
4. WPA3, Wi-Fi Protected Access 3
	- 最新的無線安全控制機制
	- 個人版升級為對等實體同步驗證(SAE, Simultaneous Authentication of Equals)


![[D7 Post-class Assessment-image-20250731 1.png]]
```Wuson
• 上課沒有提到, 不過這張投影片要留意一下喔!
• 安全不是只有機密性，至少要從CIA去思考。Wi-Fi的安全機制至少要提到身份驗證、加密及完整性控制等。
• 第零代 WEP 無身份驗證，加解密器透過RC4，完整性控制為CRC32，已被破解
• 第一代 WPA 開始有身分驗證，個人版透過PSK驗證身份，企業版則802.1X，加解密器透過RC4(TKIP)，完整性控制為MIC
• 第二代 WPA2 個人版透過PSK驗證身份，企業版則802.1X，加解密器透過AES(Counter Mode)，完整性控制為CRC-MAC
• 第三代 WPA3 個人版透過SAE驗證身份，企業版則802.1X，加解密器透過AES(Galois/Counter Mode)，完整性控制為G-MAC，同時第三代解決了WPA2萬年金鑰的問題
• 不管是WPA, WPA2, WPA3, 身份驗證都支援二個版本: 個人版(personal profile)及企業版(enterprise profile). 個人版採用PSK, 企業版採用802.1X(只能用EAP系列的協議)
```

---
# 7. 請簡述IPv4的定址規格及規則(保留號)。

7.1 請簡述IPv4的定址規格及規則(保留號)。
Answer：

IPv4 定址規格：
- IPv4 位址由32個位元組成，並以 8 個位元為 1 單位分成 4 組，由 "." 來分隔的 10 進位數字

IPv4 保留號：
- RFC 1918 Addresses：私有 IP 地址，被設計用於本地網路(LAN)
	- CIDR: 10.0.0.0/8
	- CIDR: 172.16.0.0/12
	- CIDR: 192.168.0.0/16
- Loopback Address：迴路位址，用於網路或系統測試的特殊 IP 位址
	- IP: 127.0.0.1

![[D7 Post-class Assessment-image-20250731 2.png]]
```Wuson
• Class A,B,C,D的時代已過去了，現在都是強調classless。
• IPv4的IP Address用32個bit來表示一個節點的位址，包含Network ID及Host ID.
• IP Address必須搭配Subnet mask（另外32個bit）用來標示Network ID佔幾個bit。
• 為方便閱讀，IP Address及Subnet mask可以用十進位分節(dotted decimal notation)或CIDR的方式來表示。
• Host ID的位元全為0的號碼保留給網路號碼專用。 例如：196號網路的完整表示法為：196號網路的0號電腦。

Host ID的位元若全為1也是保留號，用來代表這個網路的所有電腦，稱為廣播位址(broadcast address)。

例如：在192.1168.1.0/24這個網路，Host ID佔8個bit，當這8個bit全為1時，產生的IP位址為192.168.1.255/24，它代表這個網路的所有電腦，也就是192.168.1.1~192.168.1.254這254台電腦。
```

---
# 8. IPsec可以作什麼？請簡述其重點。

8.1 IPsec可以作什麼？請簡述其重點。
Answer：

IPsec 可以提供「安全服務」，用於確保網路層資料傳輸的安全
- 強化完整性 --> AH, Authentication Header
- 完整性、機密性均強化 --> ESP, Encapsulating Security Payload

```Wuson
• IPsec顧名思義可以提供安全服務，以補IP的不足。因此，學習IPsec必須了解IPsec提供什麼安全服務（AH及ESP）、安全服務的適用範圍（Transport全套及Tunnel半套），以及安全服務如何建立（IKE與SA）。
• 安全服務不管是AH或ESP都可以作全套(transport mode)或半套(tunnel model)。不同的安全服務在不同的模式下運作，其封包有不同的封裝方式。
• IKE可進行交互驗證及交換密碼學相關的演算法及參數(統稱為SA, Security Association)，以啟動後續的安全服務(AH或ESP)。
```

---
# 9. 何謂路由(routing)、路由表(Routing Table)與路由器(Router)?

9.1 何謂路由(routing)、路由表(Routing Table)與路由器(Router)?
Answer：

路由(routing)
- 決定傳輸路徑怎麼走，是資料傳輸路徑(Path)選擇的決策
路由表(Routing Table)
- 通常是一個表格(資料庫)，用於存放各個路由(routing)的路徑決策
路由器(Router)
- 用於連接不同的網路，負責路由決策並轉送封包的設備

---
# 10. 請從傳輸前、中、後的角度說明TCP的傳輸控制機制。

10.1 請從傳輸前、中、後的角度說明TCP的傳輸控制機制。
Answer：

傳輸前、中、後 都必須經過控制(Three-way Handshaking)
1. 傳輸前
	- A --> ${SYN}_A$ --> B
	- A <-- ${ACK}_B$ + ${SYN}_B$ <-- B
	- A --> ${ACK}_A$ --> B
	- B 確認無誤後建立連結
2. 傳輸中
	- 透過賦予回復封包請求編號，來確認封包是否有丟失情形，like ${ACK_1}$ ${ACK}_2$ ...
 3. 傳輸後
	 - 透過傳輸 ${FIN}$ 請求結束連線

---
# 11. 何謂會話(session)？會話中所傳遞之訊息的呈現(presentation)須考慮那些議題？

11.1 何謂會話(session)？
Answer：

會話(Session)：一個使用者從登入到登出的期間

11.2 會話中所傳遞之訊息的呈現(presentation)須考慮那些議題？
Answer：

考慮訊息如何呈現
- 編碼(Encoding)
	- 美國標準資訊交換碼(ASCII)
	- 萬國碼(Unicode)
	- BASE64 編碼
- 壓縮(Compression
	- Content-Encoding: gzip
	- Content-Encoding: compress
- 加密(Encryption)
	- HTTPS
	- AES

---
# 12. 請說明HTTP與TCP的關係，以及HTTPS與TLS的關係

12.1 請說明HTTP與TCP的關係，以及HTTPS與TLS的關係
Answer：

HTTP 與 TCP 的關係
- HTTP 是應用層協議、TCP 是傳輸層協議
- 無論是 HTTP 的請求＆回應，都必須靠 TCP 傳輸資料

HTTPS與TLS的關係
- HTTPS = { HTTP + TLS}，即 HTTP over TLS，利用 TLS 加密 HTTP 封包後再利用 TCP 傳輸資料

```Wuson
以下補充:
• HTTP規範Browser與Web Server之間的訊息(如指令、狀態及標頭等)；TCP則是負責傳輸HTTP訊息的傳輸服務。Browser使用HTTP與Web Server通訊時，通常會連線到Web Server的TCP 80 Port，過程沒有加密及身份驗證等安全服務 。
• HTTPS則是要求HTTP訊息必須採安全傳輸，因此Browser使用HTTPS與Web Server通訊時，通常會連線到Web Server的TCP 443 Port，過程可以採用SSL(已過時)或TLS來提供加密及身份驗證等安全服務。
```

---
# 13. 請說明DNS的如何運作

13.1 請說明DNS的如何運作
Answer：

網域名稱系統(DNS, Domain Name System)：
- 是一套將易讀的網域名稱(Domain)轉換為機器/設備可識別 IP 位址的一套系統
- 運作流程：
	1. End User 輸入網址後，設備會向本地 DNS Server 請求該 Domain 對應 IP Address
	2. 本地 DNS Server 會檢查有無此 Domain IP Record 快取，有的話便直接回傳 End User
	3. 若快取沒有紀錄，DNS Server 會依架構逐項查詢
		1. 根名稱伺服器（Root Name Server）: like: .com, .tw
		2. 頂級網域名稱伺服器（TLD Name Server）: like example.com
		3. 權威名稱伺服器（Authoritative Name Server）：最終對應 IP 地址 Record
	4. 查詢到正確 IP 後，該 IP 資訊回逐層記錄並回傳給最初的 DNS Server，最終至 End User

```Wuson

只提到DNS Query, 漏了Zone Transfer.

• DNS是一個request/response的client/server架構的網路應用。DNS不是只有client對server的DNS Query (UDP 53)，也有server對server的Zone Transfer (TCP 53)。
• DNS Server負責管理記錄網路資源的資料庫。資料庫中常見的資源記錄(RR, Resource Record)型態包含A, PTR, CNAM, TXT, NS, MX, SRV等。資料庫常使用簡單的文字檔來儲存這些資源記錄，因此這個DNS的資料庫檔案常被稱為zone file.
• DNS為了備援及負載平衡的考量會建置一部以上的DNS Server。Zone Transfer是指將Zone File由一台DNS Server複製到另一台DNS Server。Zone Transfer通常透過TCP 53來進行。
• DNS Client (或DNS Resolver)可透過UDP 53向DNS Server提供查詢(DNS Query)。 然而，傳統的DNS Server如果須要回覆DNS Query的資料量超過512 bytes, 通常會通知DNS Client改用TCP 53來作DNS Query。(RFC 1035)

```

---
# 14. 請簡述modem, repeater, bridge, router, firewall及application gateway的用途

14.1 請簡述modem, repeater, bridge, router, firewall及application gateway的用途
Answer：

modem：
- 用於類比、數位訊號的轉化
repeater：
- 透過無條件轉換、放大，讓訊號跑更遠
bridge：
- 提升網路效能
router：
- 用於連接不同的網域
firewall：
- 過濾封包
application gateway：
- 用於協定轉換

---
# 15. 何謂Cipher Suite？請簡述之

15.1 何謂Cipher Suite？請簡述之
Answer：

密碼套件 (Cipher suite) 用來表示在**TLS/SSL**協定中使用的演算法(Cipher)組合
格式：
```
TLS_<Key_Exchange>_<Signature>_WITH_<Bulk_Encryption>_<Message_Authentication>_<Elliptic_Curve>
```
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
```

```Wuson

以下補充:
• 密碼套件(Cipher Suite)是TLS安全傳輸過程中所使用的密碼學(四大技術)演算法及相關參數的統稱。TLS 1.3跟以前的TLS版本比較起來，安全要求提高很多，主要是不再接受降級使用過時的演算法(RC4, 3DES, Hash-based MAC, CBC mode ciphers)，以及只接受支持PFS的金鑰交換方式(即不支持static key pair，如RSA,¸DH, ECDH等)。
在金鑰交換方面，TLS 1.3的PFS是強制性的要求，傳統的RSA及DH (Diffie-Hellman)/ECDH都不再被接受。而具體的說，TLS 1.3只接受暫時性的金鑰(ephemeral key, 如DHE或ECDHE)，也就是每個session都要生成不同的金鑰對，這樣私鑰外洩才能將損失控制在一個session。相對於RSA是長期使用的金鑰對(long-term key)，目前大約可使用一年；這會導致私鑰外洩的影響範圍是這一年的全部session，所以不具備PFS的優質金鑰交換特性。
• 由於TLS 1.3只接受支援PFS特性的金鑰交換方式，因此支援ephemeral key的DH家族(DHE, ECDHE)即成為TLS 1.3主要的金鑰交換方式。由於DH家族的演算法特性大大的減少了Handshake的複雜度，可以到0往覆時間(0-RTT, Zero Round-Trip Time)，因此TLS的連線速度可以大大的提升。以下是RFC 8446所接受的演算法：
o Elliptic Curve Diffie-Hellman Ephemeral (ECDHE)
o Finite Field Diffie-Hellman Ephemeral (FFDHE)

```
![[D7 Post-class Assessment-image-20250731 3.png]]
https://www.a10networks.com/glossary/key-differences-between-tls-1-2-and-tls-1-3/