
# Main topic: WISE Model in a seven-day course.

1. Architecture: 單、複數點元素整合
2. Wuson advised taking the CISM exam after the CISSP. This exam is highly repetitive with the CISSP in 90%.
3. Then you can go to study cia atfer CISM & CISSP
4. ORP & OSG are better studied after Wuson's course.
5. Daily Scrum in 15 minutes every day.

```tree
CISSP Common Body of Knowledge (CBK)
- Domain 1: Security and Risk Management
- Domain 2: Asset Security
- Domain 3: Security Architecture and Engineering
- Domain 4: Communication and Network Security
- Domain 5: Identity and Access Management (IAM)
- Domain 6: Security Assessment and Testing
- Domain 7: Security Operations
- Domain 8: Software Development Security
```
＊ 這邊 IAM 是與 Access controls 一樣的概念 
＊ 雖然CISSP有8個Domain，但本質上就是「管理」與「工程」
```tree
Domain 1: Security and Risk Management
- Management
	- Domain 2
	- Domain 5
	- Domain 6
	- Domain 7
- Engineering
	- Domain 3
	- Domain 4
	- Domain 8
```

Tips:
Domain 1 = CIA + GRC(Governance + Risk Management + Compliance)
Domain 2 = 盤點、分類、保護
Domain 5 = Concept (情境)、Control (控制)、Zero trust (零信任)
Domain 6 = Examination(查察) , Interviewing(訪談) , Testing(測試)
Domain 7 = 日常作業、持續改善
Domain 3 = 時時都安全、處處都安全
Domain 4 = 處處都安全
Domain 8 = 時時都安全、處處都安全
## Starter (起手式) #starter

```tree
Definition
CyberSecurity Definition: Information Security is a discipline of protecting assets from threats through security controls to: 
T3 --> achieve confidentiality, integrity, and availability (CIA),
T2 --> support business, and
T1 --> create value and fulfill organizational mission and vision

- To create value and fulfill organiztion mission and vision
	- Strategy Management
	- Risk Management
	- Problem-solving
- To support Business
	- Intregrating security into processes
	- Continueous delivery of products and services
- To achieve confidentiality, intergrity, and availabiliy (CIA)
	- Inventory, Classification and Protection
```

![[Pasted image 20250705142335.png]]
![[Pasted image 20250705162232.png]]

依據美國原始的CIA條文(in FISMA)
Integrity in CIA is Ambiguous
不只有 CIA，在Integrity中尚有 Authenticity(真實性), Nonrepudiation(不可否認性)
所以在2008年時美國國防部有調整
```tree
Information Assurance (IA) in DoD
- Confidentiality
- Integrity
- Availability
- Authenticity
- Non-repudiation
```
2014年起美國資訊安全定義為 --> CyberSecurity


CIA是資安目標、也是法定目標、也是美國Fisma定義的目標
C：確保資料不外洩（偷竊、使用者洩漏）
I：確保資料不被串改，資料來源、身份需為真、收發雙方必用認定
A：資料的可用信

1. 安全的定義，即是保護：
	ex: 資訊安全，保護安全、網路安全，保護網路
2. information security != information systeams security
	You need to know " What is CISSP?”, what is this certified’s meaning?
3. 名詞定義
	1. Business --> 業務
	2. Process --> 流程
4. ==安全 --> 安全控制措施(具體的概念)==
5. Risk (風險) --> 影響目標達成的不定性因素 (*by ISO 31000*)
6. Assets (資產) --> 任何有價值且值得保護的事務，均可稱為「Assets」
7. Value (價值) --> 任何重要的、有意義的、有用處的事務，均可稱為「Value」
8. Controls (控制) --> 處置風險的手段
9. Objectives (目標) --> 未來狀態的具題描述
10. 資訊安全最重要的資產 --> 「資訊」
11. What is "System"?  You can understand it using the concept of a forest.
	 系統是一個總成 --> 元素 + 目的

 ```tree
 System
 - Elements (the individulas)
 - Purpose (the whole)
 Architecture
 - Primary elements
 - Relationships
 Layering
 - Separation of concerns
 - Dependency management
```

![[Pasted image 20250705165901.png]]
```tree
安全通用概念
	- 1. 資訊安全(定義)
	- 2. Starter (起手式)
	- 3. Mind Map (心智圖)
	- 4. 考試大綱
```

![[Pasted image 20250705113415.png]]
CISSP - Security as Protection
2. What? __Asset__
3. Why? Risk
4. How? Controls
5. Objectives

CIA is the **target** of security management

## 心智圖
![[Pasted image 20250705133706.png]]

Security Controls - Taxonomy

HIPAA Safeguards
```tree
Administrative
- Management
Technical
- Logical
Physical
```

Types of Security Control (ISC2)
```tree
Before
- Directive (Behavior)
- Deterrent (Motive)
- Preventive (Threshold) 
During
- Detective
- Corrective
After
- Recovery
Others
- Compensating
```

ISO 27001:2013 Annex A
- Access control

Nist Control Families 
- Access control

What is framework?  框架？ --> 懶人包 (實務面)
- NIST RMF


## Security Assessment


What is "Compliance"?  不合規？ --> "不符合事項"
Compliance --> 談要求
effective --> 談目標

```tree
Security Assessment Overview
- Purposed
	- Security Controls
	- Compliance (Requirements)
	- Effectiveness (Objectives)
- Methods
	- Examination (Eyes)
	- Interviewing (Mouth)
	- Testing (Hands)
- Results
	- Report (Good and Bad)
	- Corrective actions
	- Upgrade actions
```

安全稽核 = 安全評鑒?? Nah!

牛之於動物、稽核之於評鑒
稽核是具有一定條件下的評鑑(獨立單位)
```tree
Audit as Independent Assessment
- Audit
	- Internal
		- Business Unit (Self-Assessment)
		- Audit Department (1st Party Audit)
	- External
		- Customers (2nd Party Audit)
		- Certification Bodies (3rd Party Audit)
```
＊留意外部稽核的第二方角色 (2nd Party Audit)

1. 安全評鑑(security assessment)
A security assessment is the testing and/or evaluation of the management, operational, and technical security controls to determine the extent to which the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting the security requirements for an information system or organization.
＊安全稽核 = 安全評鑒?? Nah!
牛之於動物、稽核之於評鑒
稽核是具有一定條件下的評鑑(獨立單位)

2. 符合性(compliance)
用以評估是否達到相關的==要求==事項的指標

3. 有效性(effectiveness)
用以評估是否達成==目標==且可量化效益的的指標

4. 改善：有所調整，使更趨良善的過程
## Security Operations

What is Operations? 維運？--> 我們稱為"**營運**" 
留意「監控」，是兩個概念：「監」、「控」--> Monitor & Control
任何被核定的「事務」，都可稱為「Baseline」
What is Scope?  You can understand it using the concept of a list.

![[Pasted image 20250705170628.png]]

Engineering (工程) --> 工程是一種涉及開發解決方案的一組流程的方法，該解決方案可以是系統、軟件或任何可交付成果，從利益相關者的需求轉換而來，並在解決方案的整個生命週期中提供支持
```tree
Engineering
- Systems Engineering
	- 是一種跨學科的方法和手段，強調各個組成元素與協同運作，以達成特定目標。  

	- 
```


## 考試大綱


---
## Wuson feedback

```
• 系統即總成，為了達成特定【目的】而一起協週運作的【元素】總成我們即可視其為一個系統。電腦系統、作業系統、網路系統、資訊系統、管理系統、武器系統、生態系統等都是系統；它們都是由不同的元素組成，而且它們的存在都是為了達成特定的目的。
• 架構(architecture)是指一個系統(system)的【主要組成元素】以及它們之間的【關係】；簡單說，架構呈現的就是【主要元素及其關係】。
• 資訊系統也是一種系統，所以要把資訊系統的【組成元素】及【存在目的】定義清楚。資訊系統的【目的】是將資料(data)轉為資訊(information)的系統。
資訊系統的組成【元素】包含資料、電腦系統、作業系統、(應用)軟體、網路、資料中心、人員及業務流程等。

資訊(information)：經過處理、轉換，變得對人有意義的資料(data)。
• 我們的課程用【孔雀】來比喻資訊系統，用孔雀的【八根毛】比喻資訊系統的八個組成元素。資訊系統只是資產的一部份，還有其它領域的資產，例如：OT的工控系統、產業的供應鍊、國家的關鍵基礎設施、全球的智慧家庭、車聯網及物聯網等。
• 管理系統(management system)即管理制度。資訊系統輔助管理制度，也就是用技術來輔助制度的運行。先建立管理制度，再導入資訊系統來輔助才能達到最好的效能與取得差異化的競爭優勢。
```

```
• 系統即總成，為了達成特定【目的】而一起協週運作的【元素】總成我們即可視其為一個系統。電腦系統、作業系統、網路系統、資訊系統、管理系統、武器系統、生態系統等都是系統；它們都是由不同的元素組成，而且它們的存在都是為了達成特定的目的。
• 架構(architecture)是指一個系統(system)的【主要組成元素】以及它們之間的【關係】；簡單說，架構呈現的就是【主要元素及其關係】。
• 資訊系統也是一種系統，所以要把資訊系統的【組成元素】及【存在目的】定義清楚。資訊系統的【目的】是將資料(data)轉為資訊(information)的系統。
資訊系統的組成【元素】包含資料、電腦系統、作業系統、(應用)軟體、網路、資料中心、人員及業務流程等。

資訊(information)：經過處理、轉換，變得對人有意義的資料(data)。
• 我們的課程用【孔雀】來比喻資訊系統，用孔雀的【八根毛】比喻資訊系統的八個組成元素。資訊系統只是資產的一部份，還有其它領域的資產，例如：OT的工控系統、產業的供應鍊、國家的關鍵基礎設施、全球的智慧家庭、車聯網及物聯網等。
• 管理系統(management system)即管理制度。資訊系統輔助管理制度，也就是用技術來輔助制度的運行。先建立管理制度，再導入資訊系統來輔助才能達到最好的效能與取得差異化的競爭優勢。
```

```
控制(control): 處置風險的具體手段 => 控制措施作了不一定有效, 所以才要透過安全評鑑來確保安全控制措施的有效性及符合性.
```

```
這段英文的定義是NIST的版本. 我們課程的定義會更完整.
以下補充:
• 安全評鑑(security assessment)：透過【查驗、訪談、測試】等方法，來確保【安全控制措施】的【符合性及有效性】，並且產出【報告】以作為【改善】依據的過程。測試只是安全評鑑採用的【方法】之一。
• 【符合性】係指滿足特定要求；【有效性】則是指達成特定目標。
• 改善的【改】是指採取矯正行動(corrective actions)，把不符合事項改好；【善】則是採取升級行動(upgrade actions)，把原本就作得不錯的項目作得更好，也就是精益求精的概念。我們的課程把採取矯正行動及升級行動，合稱【改善】。
• 由【獨立單位】來進行的安全評鑑，才能稱為【稽核】。受稽單位自己實施安全評鑑或受稽單位間彼此進行評鑑一般稱為【自評】與【互評】。所謂的獨立單位就是指受稽單位無法影響稽核者及干預稽核的單位。
• 獨立單位可分為【第一方】（組織內部的稽核部門）、【第二方】（客戶行使合約中所保留的稽核權）、及【第三方】（如SGS, BSI, TUV, TCIC等ISO的驗證機構與主管機關）。不過在台灣，很多人都把主管機關的稽核視為第二方稽核；這個觀點與ISO 19011: 2018 - Guidelines for auditing management systems不符。
```

```
以下補充:
• 業務(business)：與交付產品及服務有關的所有活動/流程。
業務(business) = 流程(processes) + 產品及服務(products & services)。
• 營運(operations)：泛指維持組織、業務、部門或資訊系統運作的【日常作業】。
安全營運(security operations)是指組織為了確保資訊安全所進行的相關活動與日常作業。
• 營運只談operations; 維運不只談operations, 還談maintenance。
• 維運(maintenance and operations)：通常是指【資訊系統】的維護與運作，是比較技術面的用語。
```

```
• 持續改善(continuous improvement)的持續是指沒有截止日且很頻繁的去作一件事；改、善則是指採取【矯正行動】將沒作好的改正，以及採取【升級行動】將原本就作得不錯的事情作得更好、精益求精。

持續改善強調改善不是只有改善一次，而是要每天改善、常常（定期或不定期）改善、一直改善，也就是【將改善的觀念融入日常作業或日常營運】之中。
• 變更管理：持續改善也不能亂改善，如有動到基準(baseline)就必須先提變更申請，核準後才能實施。
```

```
• 基準(baseline)：任何被核定(approved)的東西都可稱為baseline。我們的課程談baseline是從變更管理的角度去看的，也就是涉及基準的變更都必須先提變更申請，核準後才能實施。
• 在專案管理領域，常見的基準有範圍(scope)、時程(schedule)、成本(cost)、績效評估(performance measurement baseline)等基準。
在IT領域有組態(configuration)基準。
在資安領域則有控制基準(control baseline)；控制基準在我們的【資通安全責任等級分級辦法】則稱為【防護基準】。
• 範圍(scope)即清單(list)；可以1,2,3,4,5…，以條列方式列出的東西就是清單。清單是實務上最常用來定義範圍的工具。
• 控制基準(control baseline)是被核定的一組控制措施，通常在國家或組織制定的標準(standards)中會指定【必須實施】的控制基準；另外，在控制框架(frameworks, 懶人包)中也會提供控制基準給組織作為參考，組織可以控制框架為基礎，根據自己的需求去調整/發展出最適的控制措施清單，以達到法律或標準等的要求。
```

```
• 工程的本質：作東西。

工程的定義：運用專業知識把一個系統（解決方案）從無到有作出來，讓它上線、使用它、維運它，一直到它除役的整個生命周期，都必須考慮利害關係人的需求，幫他們抓住未來的機會、避免潛在的威脅，以及解決眼前問題的一門學問。
• 工程的本質：作東西。所以：
系統工程: 發展系統
網路工程: 架網路
軟體工程: 寫軟體
機房工程: 蓋機房
• 專案的本質：一件事。

專案的定義：【有開始、有結束、有產出】，且產出必須在【範圍內、時間內、成本內】，並兼顧【品質】的一件事。
• 工程與專案的關係：所有的工程都是專案，簡稱工程案。
因此，作好一個工程除了必須具備本職學能硬功夫外，還必須具備專案管理軟實力。
```

![[Pasted image 20250712100153.png]]
```
• 品質(quality)：一個東西的品質就是除了功能以外的所有特質。有品質的系統必須以功能正常為前提，才能討論品質。我們課程的品質指標叫作: U PASS ME!
```

```
• 工程要唸什麼東西？
1. 工程概論：工程方法、安全模型、密碼學研究。
2. 工程專題：軟體工程、網路工程、機房工程。
```

```
• Domain 1: Security and Risk Management: CIA+GRC
• Domain 2: Asset Security: 盤點、分類、保護
• Domain 3: Security Architecture and Engineering: 時時都安全、處處都安全
• Domain 4: Communication and Network Security: 處處都安全
• Domain 5: Identity and Access Management (IAM): 情境、內涵(I+3A)、零信任
• Domain 6: Security Assessment and Testing: 目的、方法(查驗、訪談、測試)、結果
• Domain 7: Security Operations: 日常作業、持續改善
• Domain 8: Software Development: 時時都安全、處處都安全
```

```
• 投訴資格：因為ISC2會員（必須證照持有者，如CISSP）的不當作為而蒙受其害的受害者。
• 投訴者：投訴者或投訴人必須符合投訴資格。常見的投訴者有：社會大眾（所有人）、雇主或單位首長，以及ISC2會員。
• 投訴方式：須檢附宣誓書，並以書面方式投訴。投訴內容必須明確指出投訴對象違反那一條ISC2的道德專則。
• 道德守則：所有投訴者都可以引用第一條及第二條；只有雇主或單位首長(principal)可以引用；第四條只有ISC2會員可以引用。
```

---
組織：一群人的組成即可稱為組織
