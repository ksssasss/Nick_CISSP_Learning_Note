
# 1. 何謂存取控制(access control)？存取控制要唸那三個主題？請簡述之。

1.1 何謂存取控制(access control)？
Answer：

存取(Access)即使用（資源），是主體使用客體的行為
而存取控制(Access Control)即 存取行為的管制

1.2 存取控制要唸那三個主題？請簡述之。
Answer：

1. 情境(Contexts)
	1. 邏輯存取控制 Logical access control
	2. 網路存取控制 Network access control
	3. 遠端存取控制Remote access control
	4. 實體存取控制 Physical access control
	5. 周邊存取控制 Perimeter access control
	6. 媒體存取控制 Media access control
2. 身分與存取管理(Identity and Access Management,IAM) --> ==I + 3A==
	- I: 身份 Identity
	- 3A: 
		1. 驗證身份, Authentication
		2. 檢查授權, Authorization
		3. 紀錄行為, Account to
3. Zero-Trust --> 存取控制 Access Control 2.0
	- 以資料為中心 Data-Centric
	- 虛擬邊界 Virtual Perimeter
	- 更細膩 Fine-grained
	- 更動態 Dynamic
	- 更透明 Transparent

---
# 2. 存取控制的3A是指驗證身份(authentication)、檢查授權(authorization)與記錄行為(accounting)。這三個A各自要唸那些主題？

2.1 存取控制的3A是指驗證身份(authentication)、檢查授權(authorization)與記錄行為(accounting)。這三個A各自要唸那些主題？
Answer：

驗證身份(authentication) 核心主題：
- Steps 步驟 
- Multi-Factor-Authentication, MFA 多因子驗證 
- Single-Sign-On 單一登入
- Authentication Protocols 身份驗證協議

檢查授權(authorization) 核心主題：
- Authorization Mechanisms 授權機制
	- DAC 自主型存取控制 & MAC 強制型存取控制
	- RBAC, Role-Based Access Control(角色) & ABAC, Attribute-Based Access Control(屬性)
	- ABAC Branch by ISC2:
		- Risk-based Access Control 風險
		- Rule-based Access Control 規則
		- History-based Access Control 存取紀錄
- Security Models 安全模型
	- Bell-LaPadula Models 
	- Biba Models
	- Chinese Wall (Brewer-Nash)
	- Clark-Wilson Model

- 記錄行為(accounting) 核心主題：
	- Accounting 記錄 --> 寫 LOG
	- Auditing 稽核 --> 看 LOG
	- Accountability 追責 --> 追責任



---
# 3. 請說明何謂主體(subject)、客體(object)、實體(entity)、身份(identity)、信物(authenticator)及身份驗證因子(authentication factor)

3.1 請說明何謂主體(subject)、客體(object)、實體(entity)、身份(identity)、信物(authenticator)及身份驗證因子(authentication factor)
Answer：

主體(subject)
客體(object)
實體(entity)
身份(identity)
信物(authenticator)
身份驗證因子(authentication factor)

---
# 4. 請說明何謂帳號(account)、儲存體(repository) 、資料庫(database)  、目錄(directory)及服務(service)

4.1 請說明何謂帳號(account)、儲存體(repository) 、資料庫(database)  、目錄(directory)及服務(service)
Answer：

帳號(account)
儲存體(repository) 
資料庫(database)  目錄(directory)
服務(service)

---
# 5. 請列出講義所提到的生物特徵(biometric)？為何生物特徵不適合用在單因子驗證？

5.1 請列出講義所提到的生物特徵(biometric)？
Answer：

5.2 為何生物特徵不適合用在單因子驗證？
Answer：

---
# 6. 身份驗證(authentication)的步驟為何？ 請從網路、作業系統及應用程式的角度重點說明身份驗證協議(protocols)

6.1 身份驗證(authentication)的步驟為何？
Answer：

身份驗證步驟(authentication steps)
- Identification 出示身份
- Verification 檢查身份 
- Notification 檢查結果

6.2 請從網路、作業系統及應用程式的角度重點說明身份驗證協議(protocols)
Answer：

身份驗證協議(Authentication protocols)：
1. Network 網路
	- PAP, Password Authentication Protocol
		- account & password 明文直送
	- CHAP, Challenge Handshake Authentication Protocol
		- challenge & response 挑戰與回應
		- 由Server端傳送「challenge」訊息給Client端
		- Client端接收到Challenge後會與 ID, Secret(共同密碼、沒傳輸)組合並計算雜湊值(MD5)
		- 回傳雜湊值給Server，如果與Server端運算的雜湊值一致即通過驗證
	- EAP-*
		- EAP是提供給廠商擴充協定用，並非直接用於身份驗證
	- RADUIS
		- 本身並非認證協議，是用於「包裝、傳輸認證協議」的協定
		- 與PPP相比，可以理解為PPP擔任前台角色，RADUIS擔任後台

2. Operating System 作業系統
	- NTLM
		- 採用 challenge & response 驗證機制
		- 安全性低已棄用，先今驗證改以 Kerberos 為主
	- Kerberos
		- 用於 AD 身份驗證協定，核心在於 Client, Server, KDC(Key Distribution Center, 金鑰配發中心) 之間的互動驗證機制
		- Kerberos 協定中使用到的金鑰：
			- $K_C$ (Client Secret Key)：由 Client 密碼單向雜湊 (Hash) 而成，只有 Client 和 KDC 知道
			- $K_{TGS}$ (TGS Secret Key)：只有 KDC 的 AS 和 TGS 知道的秘密金鑰
			- $K_S$ (Service Secret Key)：只有 KDC 和特定的 Service Server 知道的秘密金鑰
		- 核心流程：
			- Step 1:
				1. Client 向 KDC AS(Authentication Server) 請求 TGT(Ticket-Granting-Ticket)
				2. Client 向 KDC TGS(Ticket-Granting Server) 請求 TGT
			- Step 2:
				- Client 向 SS(Service Server) 請求服務
		- 驗證細節：
			- Step 1: AS-REQ
				- Client 向 KDC 發送明文請求身份驗證(當中包含使用 $K_C$ 加密的當前 Timestamp)
			- Step 2: AS-REP
				- Client 向 KDC 發送明文請求身份驗證(當中包含使用 $K_C$ 加密的當前 Timestamp)，KDC中的 AS(Authentication Server) 會向資料庫確認使用者存取權限，並找到對應 Client 的 $K_C$ ， 解密 Client 請求並得到相應的 Timestamp 即初步驗證成功，並回覆 AS-REP
					- A message : 使用 $K_C$ 加密，內含 Client/TGS Session Key、TGS ID、Lifetime、Timestamp
					- B message(即 TGT): 使用 $K_{TGS}$ 加密，內含 Client/TGS Session Key(和A訊息中的是同一把)、Client ID、Client IP、Lifetime、Timestamp
				- Client 取得 AS-REP 後，會利用 $K_C$ 解密 A 訊息，取得 Client/TGS Session Key
			- Step 3: TGS-REQ
				- Client 向 TGS 發送服務請求，證明自己是 TGT 合法持有者
					- C message(Authenticator): 使用 ${SK}_{C,TGS}$ (Client/TGS Session Key)來加密，內含 Client ID, Timestamp，C message 的用途是證明請求即時性，只有合法的 Client 才能從 AS-REP 解密出 ${SK}_{C,TGS}$
					- D message : 明文傳送 TGT(也就是 Step 2 的 B message) 及 Client 要存取的 Server ID
			- Step 4: TGS-REP
				- TGS 使用自己的 $K_{TGS}$ 解密 TGT ，取得內含的 ${SK}_{C,TGS}$ 
				- 再利用 ${SK}_{C,TGS}$ 解密 C message 後，驗證 TGT & C 中的 Client ID 是否一致、Timestamp 是否相應，如驗證通過 TGS 就會配發 ST(Server Ticket)
					- E message(即 ST) : 使用目標 Service 的 $K_S$ 加密，內含 ${SK}_{C,S}$ (Client/Service Session Key，新的隨機會話金鑰，用於最後 Client 與 Service 的通訊)、Client ID、Client IP、Lifetime、Timestamp
					- F message : 使用 ${SK}_{C,TGS}$ 加密，內含 ${SK}_{C,S}$ (和 E message 是同一把)
				- Client 取得 TGS-REP 後，會利用之前儲存的 ${SK}_{C,TGS}$ 解密訊息 F 來取得 ${SK}_{C,S}$ ，訊息 E 暫存
			- Step 5: AP-REQ
				- Client 拿 ST 向服務伺服器請求服務
					- 新的 Authenticator 並使用 ${SK}_{C,S}$ 加密，內含 Client ID、Timestamp
					- ST，即剛剛 TGS-REP 收到所暫存的 E message
			- Step 6: AP-REP
				- SS 收到請求後，會使用自己的 $K_S$ 解密 ST 並取得 ${SK}_{C,S}$ 
				- 利用 ${SK}_{C,S}$ 去解密 AP-REQ 的 Authenticator，並驗證其內文中的 Client ID、Timestamp 是否與 ST 中的訊息一致
				- 驗證通過後，確認 Client 身份 SS 便會開始提供服務，後續 Client & SS 間的繪話都可以使用 ${SK}_{C,S}$ 實施加密來確保會話安全

3. Application 應用程式
	- LDAP & X.500
	- SAML & OIDC

---
# 7. 上課提到那些授權機制(authorization mechanisms)，請簡述之

7.1 上課提到那些授權機制(authorization mechanisms)，請簡述之
Answer：

授權機制(authorization mechanisms)
- DAC 自主型存取控制 & MAC 強制型存取控制
- RBAC, Role-Based Access Control(角色) & ABAC, Attribute-Based Access Control(屬性)
- ABAC Branch by ISC2:
	- Risk-based Access Control 風險
	- Rule-based Access Control 規則
	- History-based Access Control 存取紀錄

---
# 8. 請說明政策(Policy)、安全模型(Security Models)舆安全機制(Mechanisms)的關係？準備考試至少要唸到那四個安全模型？

8.1 請說明政策(Policy)、安全模型(Security Models)舆安全機制(Mechanisms)的關係？
Answer：

8.2 準備考試至少要唸到那四個安全模型？
Answer：

---
# 9. 根據上課的說法，何謂零信任(zero trust)？

9.1 根據上課的說法，何謂零信任(zero trust)？
Answer：

---