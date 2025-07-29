
# 1. 何謂網路(network)？Domain 4的口訣為何？代表什麼意義？網路工程要唸那些議題？

1.1 何謂網路(network)？
Answer：

網路(network)是一種系統
- 組成元素：由傳輸媒介(transport media) 與節點(node) 組成
- 存在目的：目的在於傳輸訊息、共享資源

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


---
# 8. IPsec可以作什麼？請簡述其重點。

8.1 IPsec可以作什麼？請簡述其重點。
Answer：

IPsec 可以提供「安全服務」，用於確保網路層資料傳輸的安全
- 強化完整性 --> AH, Authentication Header
- 完整性、機密性均強化 --> ESP, Encapsulating Security Payload

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