
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
6. 展示層(Presentation)
7. 應用層(Application)

---
# 4. 何謂封包(Protocol Data Unit, PDU)? 何謂unicast, multicast, broadcast與anycast？

4.1 何謂封包(Protocol Data Unit, PDU)?
Answer：


4.2 何謂unicast, multicast, broadcast與anycast?
Answer：

---
# 5. 乙太網路100BASE-TX使用那一種訊號(signal)、線材(cable)以及那一種媒體存取控制(MAC)的機制？無線網路802.11be (Wi-Fi 7) 使用了那些頻帶(bands)？這二者傳輸率的理論上限值為何？

5.1 乙太網路100BASE-TX使用那一種訊號(signal)、線材(cable)以及那一種媒體存取控制(MAC)的機制？
Answer：


5.2 無線網路802.11be (Wi-Fi 7) 使用了那些頻帶(bands)？
Answer：


5.3 這二者傳輸率的理論上限值為何？
Answer：


---
# 6. 請參考講義，簡述Wi-Fi無線網路各個世代的安全機制。

6.1 請參考講義，簡述Wi-Fi無線網路各個世代的安全機制。
Answer：



---
# 7. 請簡述IPv4的定址規格及規則(保留號)。

7.1 請簡述IPv4的定址規格及規則(保留號)。
Answer：



---
# 8. IPsec可以作什麼？請簡述其重點。

8.1 IPsec可以作什麼？請簡述其重點。
Answer：



---
# 9. 何謂路由(routing)、路由表(Routing Table)與路由器(Router)?

9.1 何謂路由(routing)、路由表(Routing Table)與路由器(Router)?
Answer：



---
# 10. 請從傳輸前、中、後的角度明TCP的傳輸控制機制。

10.1 請從傳輸前、中、後的角度明TCP的傳輸控制機制。
Answer：


---
# 11. 何謂會話(session)？會話中所傳遞之訊息的呈現(presentation)須考慮那些議題？

11.1 何謂會話(session)？
Answer：


11.2 會話中所傳遞之訊息的呈現(presentation)須考慮那些議題？
Answer：


---
# 12. 請說明HTTP與TCP的關係，以及HTTPS與TLS的關係

12.1 請說明HTTP與TCP的關係，以及HTTPS與TLS的關係
Answer：


---
# 13. 請說明DNS的如何運作

13.1 請說明DNS的如何運作
Answer：


---
# 14. 請簡述modem, repeater, bridge, router, firewall及application gateway的用途

14.1 請簡述modem, repeater, bridge, router, firewall及application gateway的用途
Answer：



---
# 15. 何謂Cipher Suite？請簡述之

15.1 何謂Cipher Suite？請簡述之
Answer：