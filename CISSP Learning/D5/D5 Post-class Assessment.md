
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

```Wuson

以下補充:
• 存取控制是指【主體使用客體的行為必須受到3A的管制】。

因為存取控制有不同情境，【安全核心】只適用邏輯存取控制(電腦系統), 因此我們很早就不強調由安全核心來進行3A管制，這個是我們課程很早期的說法。參考教練筆記還是要重心放在我們最近的上課內容喔!
• 存取控制要唸情境(context)、內涵(I+3A)及零信任(Zero Trust)這三個主題。

情境：Logical Access Control, Network Access Control, Remote Access Control, Physical Access Control, Perimeter Access Control, Media Access Control.

內涵：I+3A 。內涵是指實際的控制動作，主要是3A (Authentication, Authorization, Accounting)。要驗證身份(Authentication)必須先有身份(Identity)，所以口訣變成I+3A。

零信任：以資料為中心，畫定虛擬邊界，形成獨立的安全區域，進行更細膩(細顆粒)、更動態、更透明的存取控制。

```

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

主體(subject)：
- 可以理解為主動方
客體(object)：
- 可以理解為被動方（被使用資源的一方）
實體(entity)：
- 指實際存在且可以唯一識別的個體，通常具有多個屬性與身份
身份(identity)：
- 是用來唯一識別(uniquely identity)一個實體(entity)的屬性(attribute)
信物(authenticator)：
- 是指用來證明身份的物品，like: Password
身份驗證因子(authentication factor)：
- 因子即是組成元素
- 身份驗證因子 即 身份驗證過程所需要的組成元素，like password, 信物

---
# 4. 請說明何謂帳號(account)、儲存體(repository) 、資料庫(database)  、目錄(directory)及服務(service)

4.1 請說明何謂帳號(account)、儲存體(repository) 、資料庫(database)  、目錄(directory)及服務(service)
Answer：

帳號(account)：
- 是為了方便管理實體的技術手段
儲存體(repository) 
- 是一個通用資料的儲存空間容器
資料庫(database)  
- 是一個具備結構化性質的資料儲存空間容器
目錄(directory)
- 即是存放帳戶資料的資料庫
服務(service)：
- 即程式，提供特定功能的應用程式或處理程序，like管理目錄的程式就叫目錄服務

```Wuson

• 服務(service): 服務即程式，但必須是有API的程式。亦即透過API來提供功能給其它程式使用的程式。
• 英文的Account其實應該要翻譯成【帳戶】，但我們實務上常把Account說成是帳號。嚴格來說，【帳號】的英文應該是Account Number，它只能算是【帳戶】的一個欄位而已。例如：【銀行帳號】及【銀行帳戶】；銀行帳號只是銀行帳戶的一個欄位，而銀行帳戶有名字、帳號、餘額等欄位。因此，如果我們口中的【帳號】是指Account Number，那把帳號解釋成身份就沒有問題。但如果帳號是指Account (帳戶)，那我們就不能說是帳號是身份，此時的帳號就成為【代表實體的技術手段】了。

```

---
# 5. 請列出講義所提到的生物特徵(biometric)？為何生物特徵不適合用在單因子驗證？

5.1 請列出講義所提到的生物特徵(biometric)？
Answer：

實體 Physiological
- 指紋
- 手指靜脈
- 掌紋
- 虹膜
- 視網膜
- 臉部特徵
動態 Behavioral
- 聲音特徵 Voice Dynamics
- 簽名特徵 Signature Dynamics
- 鍵盤習慣特徵 Keystroke Dynamics
生物 Biological
- DNA
- Blood Glucose

5.2 為何生物特徵不適合用在單因子驗證？
Answer：

生物特徵無法變更，一旦遭到竊取就能直接使用，甚至在 NIST (SP 800-63B) 中直接禁止生物特徵在單因子驗證情境下使用

```Wuson

• 秘密性及恆定性。除了視網膜以外的生物特徵多半秘密性不足，而且不易改變。

```

---
# 6. 身份驗證(authentication)的步驟為何？ 請從網路、作業系統及應用程式的角度重點說明身份驗證協議(protocols)

6.1 身份驗證(authentication)的步驟為何？
Answer：

身份驗證步驟(authentication steps)
- Identification 出示身份
- Verification 檢查身份 
- Notification 檢查結果

```Wuson

• 身份驗證(authentication)的步驟：出示身份、檢查身份、通知結果。

```

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

8.1 請說明政策(Policy)、安全模型(Security Models)與安全機制(Mechanisms)的關係？
Answer：

- 政策(policy)是經營高層管理意圖的展現
- 安全模型(Security)即是將政策轉化回具體框架的解決方案
- 安全機制(Mechanisms)是實踐安全模型的具體技術＆程序或是工具

8.2 準備考試至少要唸到那四個安全模型？
Answer：

考試準備 Security Models 安全模型至少要唸到四個重點模型： BBCC
	- Bell-LaPadula Models 
	- Biba Models
	- Chinese Wall (Brewer-Nash)
	- Clark-Wilson Model

```Wuson

以下補充:
• 政策(Policy)、安全模型(Security Models)舆安全機制(Mechanisms)代表產官學界的合作。政策代表政府機構的制度(用英文寫)、安全模型代表學者對政策的研究成果及學術理論(用數學表達)，而安全機制代表產業依安全模型實作的解決方案(用電腦語言實作)。
• 管理制度(management system)要有資訊系統(information system)來輔助，以提升效能。資訊系統的設計最好也有學術理論的基礎；用數學表現的模型稱為正式模型(formal model)，用數學表現的設計則稱為正式設計(formal design)。
• 美國國防部的保密制度須要有可信賴的電腦系統(TCS, trusted computer system)來輔助；美國國防部發布可信賴電腦系統的評估準則(TCSEC)作為檢測電腦系統的標準，以作為採購的依據。TCSEC是依據BLP等安全模型所發展。

```

---
# 9. 根據上課的說法，何謂零信任(zero trust)？

9.1 根據上課的說法，何謂零信任(zero trust)？
Answer：

零信任(Zero-Trust)：可稱為 Access Control 2.0
- 與傳統以網路為中心的架構不同，Zero-Trust 以資料為中心(Data-Centric)，並劃定虛擬邊界(Virtual Perimeter)
- Zero-Trust 把 Authentication(身份驗證)＆ Authorization(檢查授權)作到更細膩(Fine-grained)、更動態(Dynamic)、更透明(Transparent)

```Wuson

以下補充:
• 零信任(zero trust)是Access Control 2.0, 也就是以資料為中心，畫定虛擬邊界，形成獨立的安全區域(Security Domain)，進行更細膩、更動態、更透明的存取控制。

那什麼是Access Control 1.0呢? Access Control 1.0的主要內涵是強調【主體(Subject)使用客體(Object)的行為必須受到3A的管制】。這邊的3A是指驗證身份(Authentication)、檢查授權(Authorization)與記錄行為(Accounting)。
• 零信任的主要的重點不是【把3A升級再優化】，也就是把3A作到【更細膩(細顆粒)、更動態、更透明】而已，因為這只是【次要】的重點。零信任最主要、最重要的重點或改變，在於放棄以網路位置為中心的繼承式信任(inherent trust)，改成在【以資料為中心，畫定虛擬邊界】所形成的安全區域(security domain)，進行【更細膩(細顆粒)、更動態、更透明】的存取控制。這種強調以零為基礎(zero-based)、經過層層驗證所累積而來的信任才是零信任的核心精神！
• 簡單的說，【從零開始累積信任】是Zero Trust的【目的】，而【更細膩(細顆粒)、更動態、更透明的存取控制】則是Zero Trust達成從零開始累積信任這個目的的【手段】。有人（含CISSP考試大綱）說Zero Trust是Trust but verify！我覺得這真的是直指核心，是Zero Trust的最佳註解！。
• 資安作到最後只剩下信心(confidence)與信任(trust)。針對人員、流程、產品與服務，以及組織，不斷的Verify and Validate (V&V, 內驗、外確)，才能建立信心與累積信任！擁有自信、口碑及公正的背書，才能消除疑慮、提升信心，達到保證(assurance)的效果！

```

---