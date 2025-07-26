# Access Control
Identity and Access Management(I+3A)
page.306
## What is **==Access Control==**?

存取(Access)即使用（資源），是主體使用客體的行為
而存取控制(Access Control)即 存取行為的管制

### 核心主題

1. 情境(Contexts)
2. 身分與存取管理(Identity and Access Management,IAM) --> ==I + 3A==
	- I: 身份 Identity
	- 3A: 
		1. 驗證身份, Authentication
		2. 檢查授權, Authorization
		3. 紀錄行為, Account to
3. Zero-trsut

---

need to know 原則
no more mo less 原則


---

3A, 存取管制動作:
>驗證身份, Authentication
>檢查授權, Authorization
>紀錄行為, Account to

---
## Contexts of Access Control
pag.309

情境(Contexts)
1. Logical access control
2. Network access control
3. Remote access control
4. Physical access control
5. Perimeter access control
6. Media access control

媒體不適用3A，其管制動作有3項
>1. 用搶的(先搶先行), comtipete first
>2. 用輪的(傳令), toke passitive
>3. 用問的, polling

---

## Access Control Learning Map

```tree
Access Control
- 情境
- 內涵(I+3A)
	- 1. 驗證身份
		- steps, *page.317*
			- 出示身份
			- 檢查身份
			- 檢查結果
		- MFA
		- SSO
		- Protocols
	- 2. 檢查授權
		- 授權機制
		- 安全模型
	- 3. 紀錄行為
		- 寫log,看log,追責任
- 零信任(Access Control 2.0)
	- 觀念轉變 --> 存取控制不再以網路為中心，回歸初衷
	- 控制升級 --> 3A升級版 --> 實踐必須更細膩、更動態、更透明
```

---

something you know: 一種信物的形式, 存在腦袋中的信物
something you have: 出示身份，證明身份(信物，證明身份的秘密)
something you are: 

Type 1, ,2, 3

---
single sign on --> 跨系統存取資源

---
把關, enforce

DAC, MAC, rule-base(RBAC)
presentation 都有

授權機制總共7個，都要唸

---

BBCC 模型


---
Access control 很常聯想到技術層面，其實最常被漏掉的是「行政管理」

架構, Architecture --> 人工構成的
結構, --> The main elements are not emphasized. There is a certain relationship among the various elements.

結構化資料:
table, tree, star, sql

relation 是表格
資料庫：關聯式 != 關係式

結構化儲存庫, Structured repository

帳號資料庫, Account 

AD就是微軟家的帳號資料庫
AD is exactly Microsoft’s account database.

ADS(AD service) 就是管微軟AD的程式
service = process

Domain Controler: 管AD的機器

---

![[AA69FB3B-603C-44A5-8927-3A0BC2FBCAFA.jpeg]]
token --> 令牌，起跑的權利
	核心概念
		象徵
		持有
	用接力賽跑來理解 --> 沒拿到接力棒就不能跑

Assertions, 斷言 --> SAML協定 --> XML
Claims, 宣稱 --> OIDC --> JSON
都是token內部的==基本資料==
也是目前SSO協定選用的主流


X.500 --> 呈現方式
token --> SAML, OIDC

單因子沒有誰最強，但有誰最弱 --> 生物特徵
NIST甚至有規範單因子認證的情境下不可使用生物特徵作為factor

![[E9636601-4B2B-44FB-8DA5-850154180252_1_201_a.jpeg]]

| Authentication Factors  | example       |
| ----------------------- | ------------- |
| Something you know (知道) | 密碼、個人問題、PIN碼  |
| Something you have (擁有) | 實體卡、手機、OTP 裝置 |
| Something you are (屬於)  | 指紋、臉部、虹膜等生物辨識 |
OTP有分同步／不同步，以時間來界定
TOTP (Time-based One-Time Password) --> 與時間同步
HOPT (HMAC-based One-Time Password) --> 非時間一致，無關時間的同步

---
Biometric Applications
Enrollment
	Biometric features
	Biometric template
	Model database
Verification
	One_to_One (1:1)
Identification
	One_to_Many ( 1:N)

FAR and FRR *important*
*page.328*

---

[![[2AEF4570-D085-4502-ADEA-456B034BC65E.jpeg]]](https://wentzwu.com/2019/12/08/single-sign-on-sso/)
勿忘初衷，為什麼要SSO --> 讓用戶方便
SSO的風險，容易被駭，你方便駭客也方便

## Authentication Protocols

Network
	PAP --> account & password 明文直送
	CHAP --> challenge & response 挑戰與回應, 回傳hash
	EAP-* --> EAP是提供給廠商擴充協定用，並非直接用於身份驗證
	RADUIS --> 與PPP相比，PPP擔任前台角色，RADUIS擔任後台
Operating System
	NTLM
	Kerberos 
		Roles: Client, Server, KDC(AS + TGS)
		Tickes: TGT & TGS
Application
	LDAP & X.500
	SAML & OIDC

必考：PPP, 控制電路 --> 不是身份驗證所使用，是拿來看身份驗證的「結果」用

EAP補充
	通常使用格式EAP-*，like ==EAP-TLS==, EAP-TTLS
	微軟專用 --> PEAP

---
![[8505FAA9-C824-41B9-A2A7-ECE9A71C91CB.jpeg]]
提供服務的stuff，就叫server
TGS理解 --> 售票中心
TGT理解 --> 買票、購票資格
只要跟AS做完身份驗證，AS就會提供user TGT
延伸(不重要) --> 經典的pass the ticket attack

---
## Authorization Overview

Authorization   權利, not 權限
權限 --> 講事情

CISSP的 Access Control 強調單指==授權==這動作，即授予==特權==
Privileges = Permissions + Rights 權力

Authorization Mechanisms
	DAC & MAC (Orange Book)
		C level --> DAC
		B level --> MAC, Mandatory Access Control --> 重點在於念制度
		DAC, Discretionary Access Control --> 課程中我們稱為「查表法」
			Access Control Matrix, ACM 權限表
				Access Control List, ACL
				Capability table
	RBAC & ABAC
	Risk-based Access Control
	Rule-based Access Control
	History-based Access Control
Security Models (BBCC)
	Bell-LaPadula Models
		- 禁止資料向「下」存取
	Biba Models
		- 禁止資料向「上」存取
	Chinese Wall (Brewer-Nash)
		- ==避免透過資料拼湊==的方式取得高階機密資料
		- 設定利益衝突群組，透過存取紀錄來==動態阻斷==資料取得
	Clark-Wilson Model
		- 確保資料完整性

---

![[87C43F3A-5246-4095-A98B-8ED6C3AA7B64_4_5005_c.jpeg]]

DAC, Discretionary Access Control
>Decisions
>- Owner
>- Need to know
>- Least Privilege

>Implementation
>- Custodian
>- Identity-based

>Enforcement
>- Security Kernel
>- Access Control Matrix

電腦只會照著你的制度來執行
技術實作都是為了實現管理概念
觀念：
人不可靠，靠制度
管理制度，要靠電腦輔助

DAC 缺點
	靠人，相對於MAC不可靠
	

---

## Mandatory Access Control, MAC

MAC 是 制度法

Policy
>- Confidentiality
>- Data Classification
>- Security Clearance

Model
>- Bell-LaPadula (BLP) Model
>- Information Flow Model
>- Lattice Models

Mechanism
>- Security Kernel
>- Trusted Computer Base (TCB)
>- Trusted Computer System (TCS)

---

RBAC 就是角色集群的權限
微軟用群組功能實現RBAC

ABAC

| 比較項目    | RBAC（角色型存取控制） | ABAC（屬性型存取控制）         |
| ------- | ------------- | --------------------- |
| 權限授予依據  | 預定義角色         | 多維屬性（包含角色、部門、裝置、時間等)  |
| 適用環境    | 角色明確、結構清楚的組織  | 使用者多、情境複雜或需求彈性的組織     |
| 精細化控管程度 | 較粗略，依賴角色數量增加  | 精細且動態，策略可高度自訂         |
| 管理維運難度  | 管理簡單、易於實作     | 初期設定及維護較複雜，需明確定義屬性和策略 |
| 常見缺點    | 角色爆炸（角色數量膨脹）  | 策略設計複雜、執行效能考量         |
| 常見優點    | 易於理解、管理與審查    | 靈活、可彈性因應各種情境與合規要求     |

## 應用建議


XACML --> 授權使用的協定

---

資料流、控制流 --> 工程師語言
資料不要外洩 --> 長官語言
學者的語言 --> 剛廠商理解實作用

---

### **SAML vs. OIDC：CISSP 觀點的快速比較**

| **特性**   | **SAML (Security Assertion Markup Language)** | **OIDC (OpenID Connect)**        |
| -------- | --------------------------------------------- | -------------------------------- |
| **底層技術** | XML, SOAP, XML Signature                      | JSON, REST, JWT (JSON Web Token) |
| **複雜度**  | 較為繁重，設定複雜，XML 解析耗能                            | 較為輕量，API 友好，易於實作                 |
| **主要用途** | 企業級 Web 應用程式 SSO                              | 消費級應用、行動應用、單頁應用 (SPA) 的 SSO      |
| **成熟度**  | 非常成熟，廣泛應用於政府和大型企業                             | 較新，但已成為現代應用的主流標準                 |
| **安全性**  | 依賴 XML 數位簽章和加密                                | 依賴 JWT 的簽章 (JWS) 和加密 (JWE)       |
| **裝置支援** | 對行動裝置支援較差                                     | 原生為行動和 Web 設計                    |
| **傳遞資訊** | SAML 斷言 (Assertion)                           | ID Token (JWT) 和 Access Token    |