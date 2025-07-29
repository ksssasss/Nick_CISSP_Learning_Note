# Network Engineering
ISO OSI Reference Model, TCP/IP, and IEEE 802, *page.453*


網路是一種系統
- 組成元素：由傳輸媒介(transport media) 與節點(node) 組成
- 存在目的：目的在於傳輸訊息、共享資源

幾乎所有工程系統都透過 multi-layer 分層
元素與元素間的關係、各層與各層之間的關係、從各層、元素去找風險

---
# Network Overview

![[Network Engineering-image-20250726.png]]

這邊指的「架網路」，指的是 LAN

Connections
- Links 鏈結 : 直連沒有穿插 Node
- route (Path) : 中間有走過 Node
- P2P, Point-to-Point, 中間的線(傳輸媒介)就是 Link
- E2E, End-to-End, 中間的傳輸媒介就是 Route(Paht)
- P2P, E2E 重點在於表達節點與節點之間的關係
- 關係 != 連線

通訊協定
- CSMA/CD
	- 用於同軸電纜，供多個設備「共享」同一個傳輸媒介，各個節點運用邏輯鏈結(Logic Link)傳輸
		- 衍生議題：LLC, Logic Link Control (我們上課說 Virtual Link, ISO 說是 Data Link)
			- 流量控制
			- 錯誤控制
- CSMA/CA
	- 用於無線網路的協定，目的是避免碰撞

### Local Area Network (LAN)
*page.482*

MAC, Media Access Control 媒體存取控制
LLC, Logic Link Control

---
從 IP Address 的角度來看
- 1 號網路 = 0 號電腦，example: 10.225.10.0

---
類比訊號：正弦波，連續型訊號
數位訊號：間歇型訊號(1, 0)

---
數位訊號疊加 --> collision 碰撞
類比、數位訊號的轉變 --> Modem 調變

Hub, Repeater：無條件轉發、放大訊號
Hub, Repeater 的問題：Collision Domain


---
### MAC Adress
*page.479*

---
### Layering, Encapsulation, and De-encapsulation
*page.460*

留意系統分層不需要一定要照著 ISO OSI Model 的分層與不可跳級
在設計上是可以自定義的

膠囊的概念是最經典的封裝法
封裝後的結果 --> 封包

---

Repeater：讓訊號跑更遠
Bridge：提升網路效能
Router：連接不同的網域
Firewall：過濾封包（ 封包的稱法 ISO: PDU(Protocol Data Unit) , CISCO: Packet）
Application Gateway：協定轉換

Bridge 為什麼可以提升效能，Bridge 會去解讀封包、學習與記錄設備卡號及封包流向

PDU: {Header, Payload}
- Header
	- ==Source== 
	- ==Destination==
- Payload
	- Service Data Unit (SDU)

PDU 重點： 收件人是誰、寄件人是誰

---
### Types of Communication
*page.462*
可以用平衡負載的觀念去理解

---

要唸！考試大綱直接寫：
switch hub 流量的轉送方式
cut-through/ store-and-forward

---
網段其實可以用線的概念來理解
一段線： Segment

不要講切網段，講切「網路」
Bridge不會阻擋同個「網路」的廣播封包（各網段都收得到）
廣播封包的範圍 就是 網路的範圍
一個廣播域 = 一個網路

---

## Wide Area Networks (WAN)
*page.490*

TCP/IP 不管網路架設，從「連網」後開始管制

Protocol stack 通信協定組合 (better than Protocol Suite)

### Network Layer
*page.493*

CIDR 子網路遮罩表示法

Router metric
- hop
- cost

只要你的設備支援 TCP/IP，就都會有 Routing Table

---
### Routing Protocols
*page.499*
最常見外部路由 OSPF, BGP

---

### ICMP & Fingerprinting
*page.500*
「控制」
ping 是一個程式，預設發送 4 次封包(window)
發 ICMP 8 port 封包給指定 IP
收到 8 port 的設備必須回復 0 port response

echo request/ reply (8/0)

TL, time to live:
預設 64 (不一定)，如果 ping 出來的 TL = 60，代表經過 4 個 Router
這邊可以參考講義的系統預設值
所以也可以被駭客利用來偵蒐，判別主機系統類別

偷渡資料議題：hacker可以利用置換icmp內的payload來傳遞資料

---
### Transport Layer
*page.510*

TCP, UDP = flag

flag:
- SYN, Synchronization
- ACK, Acknowledgement
- FIN, Finish
- RST, Reset

傳輸前、中、後 都必須經過控制

port number 就是程式的號碼
example: 80 port --> web server 的程式號碼

windows server = linux demand

DNS port number 用了 TCP 53 port 也用了 UDP 53 port for DNS query
為什麼要用 UDP? 資料量太大，對 DNS Record 負擔太大
TCP 用於 DNS Record 資料的互相備份複製 --> Zone Transfer

DNS 儲存的資料叫做 Zone file

SIEM Log 收容為什麼走 UDP --> 也是因為量大

---
### Session Layer
*page.515*
什麼是 Session？
Session 就是一段時間 --> 一段時間的會話
" Session " is a period devoted to a particular activity.
Wuson課程定義(狹義)：登入到登出的那一段時間
登入就會有身份驗證
身份驗證就會取得 token
token 就是一種 狀態(State) 管理的機制
再看到單工、雙工議題，會話的單向還是雙向

- Token Management
- State Management 
- Interaction Management
- Protocols

---
### Application Layer
*page.517*

留意下各 Protocol 的用途是什麼，配套軟體是什麼
https標準指令
- get 查詢
- post 新增
- push 修改
- delete 刪除

DNSSEC --> 保護DNS --> 要看
TCP安全性：目前 TLS 版本至少要 1.2 (SSL以棄置)

TLS 安全參數的調整 --> Cipher suites
*page.299*

---
### IPsec
*page.502*

IPsec 可以幹嘛？ 提供「安全服務」
提供什麼安全服務？(IPsec - v3)
- 給看不給改，強化完整性 --> AH
- 不給看也不給改，完整性、機密性均強化 --> ESP

AH --> hash
ESP --> 加密，所以要有配套的金鑰協議 --> IKEv2

安全服務有試用範圍，範圍有半套、全套
*page.503*
- 半套的 Tunnel Mode
- 全套的 Transport Mode

不管你選擇 AH、ESP，均可選擇 Tunnel Mode or Transport Mode
*page.504*
