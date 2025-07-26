
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
- 通常指使用者，即試圖登入應用程式的個人
客體(object)
實體(entity)
身份(identity)
- 負責**驗證**使用者身份，並產生包含使用者資訊的「SAML 斷言 (Assertion)」。例如：企業的 Active Directory (ADFS), Okta, Azure AD
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
	- X.500
		- X.500 是一套 Directory Service standard(目錄服務標準)，他定義了一個階層式的樹狀結構，每一個物件都有一個全域中唯一的 DN(Distinguished Name)
			- DN example : C=TW, O=MyCompany, OU=IT, CN=JohnDoe
		- X.500 標準本身有包含一套存取目錄協定，稱為 DAP (Directory Access Protocol)，但由於太過笨重而被棄用
	- LDAP (Lightweight Directory Access Protocol)
		- 如其名，他是基於 X.500 標準大幅簡化了存取目錄的複雜度，所以又被稱為 X.500-Lite
	- SAML (Security Assertion Markup Language)
		- 基於XML標準，核心用於主體、IdP(Identity Provider 身份提供者)與 SP(Service Provider )服務提供者間的身份驗證，簡單的理解 IdP 會作為組織的「統一登入入口」，SP 本身不處理主體密碼，完全信任 idP 的驗證結果
		- SAML 高度依賴 XML Signature 與加密，且SAML斷言必須經過簽章以防止竄改
	- OIDC (OpenID Connect)
		- OIDC 是建立在 OAuth 2.0 協定以上的現代化身份驗證層，OAuth 2.0 負責授權 (Authorization)， OIDC 則用於身份驗證 (Authentication)
		- OIDC 採用更輕量的 JSON Web Tokens (JWT) 來傳遞訊息，核心用於 End User、 RP(Replying Party)、OP(Open ID)間的身份驗證，RP 可以對照 SAML 的 SP，OP 可以對照 SAML 的 IdP
		- 與  SAML 相比， SAML 是企業的身份驗證解決方案，而 OIDC 則是方便消費者層級的身份驗證運用，核心在於「提供身份」的角色，OP 就是通用身份的提供者


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

資訊安全管理應從高層的政策出發，經由安全模型將政策具體化，最後透過安全機制落實於系統與流程，三者層層對應、密切相連，可以確保組織資訊安全的系統性與有效性。

8.2 準備考試至少要唸到那四個安全模型？
Answer：

考試準備 Security Models 安全模型至少要唸到四個重點模型： BBCC
	- Bell-LaPadula Models 
	- Biba Models
	- Chinese Wall (Brewer-Nash)
	- Clark-Wilson Model

---
# 9. 根據上課的說法，何謂零信任(zero trust)？

9.1 根據上課的說法，何謂零信任(zero trust)？
Answer：

零信任(Zero-Trust)：可稱為 Access Control 2.0
- 與傳統以網路為中心的架構不同，Zero-Trust 以資料為中心(Data-Centric)，並劃定虛擬邊界(Virtual Perimeter)
- Zero-Trust 把 Authentication(身份驗證)＆ Authorization(檢查授權)作到更細膩(Fine-grained)、更動態(Dynamic)、更透明(Transparent)

---