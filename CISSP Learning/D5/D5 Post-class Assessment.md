
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
		- 採用challenge & response驗證機制
		- 安全性低已棄用，先今驗證改以Kerberos為主
	- Kerberos
		- 

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