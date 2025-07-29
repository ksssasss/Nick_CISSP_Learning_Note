
# 1. 何謂工程(engineering)？工程要唸那些議題？ 作好一個工程案至少要具備那二項最基本能力？何謂專案(project)？工程與專案有何關係？

1.1 何謂工程(engineering)？
Answer：

工程的本質：做東西

1.2 工程要唸那些議題？
Answer：

掌握核心觀念：時時都安全、處處都安全

Introduction
- 方法 Approches
- 安全模型 Security Models
- 密碼學研究 Cryptology
特定主題
- 數據中心Data Center
- 網路 Network
- 軟體（開發）Software

1.3  作好一個工程案至少要具備那二項最基本能力？
Answer：

1. 本職學能硬功夫
2. 專案管理軟實力

1.4 何謂專案(project)？
Answer：

有開始、有結束、有產出，產出必須在範圍內、時間內及成本內，並兼顧品質的一件事

1.5 工程與專案有何關係？
Answer：

所有「工程」都是透過「專案」的形式來執行

---
# 2. 何謂系統(system)、資訊系統(information system) 與管理系統(management system)？

2.1 何謂系統(system)、資訊系統(information system) 與管理系統(management system)？
Answer：

系統(system) 是指為了達成特定目的而一起協同運作的一群元素的統稱
- 系統 = {元素, 目的}

資訊系統(information system) 是指將資料(data)進行處理，並轉換為有用的資訊(information)的系統

管理系統(management system)
- 元素：管理(management)是達成目標的一套有系統的方法
- 所以管理系統就是一套用於管理制度的系統



---
# 3. 何謂有品質的好軟體(quality software)？請列出上課所介紹的軟體開發生命週期(SDLC)的【階段】及【每個階段的重點】。

3.1 何謂有品質的好軟體(quality software)？請列出上課所介紹的軟體開發生命週期(SDLC)的【階段】及【每個階段的重點】。
Answer：

有品質的好軟體(quality software)，必須具備：
1. 功能性 (Functionality): 軟體的功能必須能正常運作且可供使用
2. 品質(Quality): Tips. U PASS ME
	- 易用性(Usability)
	- 效能(Performance)
	- 可用性(Availability)
	- 規模性(Scalability)
	- 安全性(Security)
	- 可維護性(Maintenance)
	- 可擴充性(Extensibility)

軟體開發生命週期(SDLC) 階段：
1. 規劃(Planning)
	- 專案管理計畫書(Project Management Plan)
	- 開發方法(Development Approaches)
	- 整合產品開發團隊(Integrated Product Team)
2. 分析需求(Analysis) 
	- 需求管理(Requirement Management): Need & Requirement
	- 使用者需求規格書(URS, User Requirements Specification)
	- 使用案例(Use Case) & 使用者故事(User Story)
	- 內驗外確(V&V, Verification & Validation)
3. 設計(Design)
	- 架構設計(Architecture Design)
	- 細部設計(Detail Design)
	- 設計審查(Design Review)
4. 開發(Development)
	- 開發環境(Software Environment)
	- 開發工具(Software Development Tools)
	- 開發語言(Programming Languages)
5. 測試(Testing) 
	- 定義(Definition)
	- 分類(Taxonomy)
	- 技術(Techniques)
	- 覆蓋率(Coverage)
6. 交付(Delivery)
	- 軟體打包(Software Packages)
	- 發佈管道(Distribution Channels)
	- 持續交付(Continuous Delivery)
7. 維護(Maintenance)
	- 職責分離(Separation of Duty)
	- 漏洞管理(Vulnerability Management)
	- 惡意軟體(Malicious Software/Malware)

---
# 4. 請簡述軟體開發演進的三個代別以及每個代別的經典開發方法。

4.1 請簡述軟體開發演進的三個代別以及每個代別的經典開發方法。
Answer：

1. 預測式(Predictive Approaches)：靠經驗看到未來，但難以因應變化
	- 瀑布式(Waterfall)
	- 計畫驅動式(Plan-driven)
2. 迭代式/反復式(Iterative Approaches)：降低風險
	 - 螺旋(Spiral Model)
	 - 快速應用程式開發(Rapid Application Development, RAD)
	 - 雛形(Prototyping)
3. 敏捷式(Agile Approaches)：強調交付價值與風險管理
	- Scrum：一種產品開發方法，所以不談專案不會出現專案經理
	- Kanban：視覺化管理計畫
	- 極限編程(XP, Extreme Programming)：企業級的軟體開發框架，是軟體開發最佳實踐


---
# 5. 何謂需求(requirements)？上課介紹了那三種需求表達工具？

5.1 何謂需求(requirements)？
Answer：

需求(requirements)：將客戶的需要(Needs)文件化並進行管理後即為「需求」

5.2 上課介紹了那三種需求表達工具？
Answer：

1. Use case text：文字描述
2. Use case Diagram：圖像表示
3. User Story：特定句型描述(Role, Goal, Benefit, Criteria)

---
# 6. 何謂設計(design)、正式設計(formal design) 與架構(architecture) ？請簡述微軟威脅塑模(threat modeling)的重點。

6.1 何謂設計(design)、正式設計(formal design) 與架構(architecture) ？請簡述微軟威脅塑模(threat modeling)的重點。
Answer：

設計(design)：
- 依需求分析後產出的「書面」解決方案

正式設計(formal design) ：
- 通常是基於數學模型，具備結構化與嚴謹性的設計方案

架構(architecture) ：
- 主要元素及其關係

微軟威脅塑模(threat modeling)：
1. 畫出應用架構圖(Diagram Application Architecture) 
2. 識別威脅(Identify Threats)
	 - OWASP
	 - STRIDE
	 - DREAD
3. 識別、排序與實施控制(Identify,Prioritize & Implement Controls)
	- 風險處置
4. 記錄與確認(Document & Validate)
	- 確認安全控制措施的有效性(V&V
不論是識別出可能風險、及風險處置後的殘餘風險，都要列在風險登記表


---
# 7. 上課強調版本庫(code repository)至少應該要放那二樣東西?  請簡述git的四個基本操作。

7.1 上課強調版本庫(code repository)至少應該要放那二樣東西?  請簡述git的四個基本操作。
Answer：

版本庫(code repository)
1. 程式模組(Code Model)
2. 單元測試(Unit Test)

git 基本操作
- commit: 提交程式到在地 repo
- checkout: 讀取/讀取 至指定的 Commit 版本
- push: 將 地端 repo 上傳至 Remote/Server repo
- pull: 將 Remote/Server repo 下載至 地端 repo

---
# 8. 何謂程式(program)、程序稿(script)、行程(process)與行動代碼(mobile code)？講義介紹了那些常見的程式運行(runtime)環境？

8.1 何謂程式(program)、程序稿(script)、行程(process)與行動代碼(mobile code)？
Answer：

程式(program)：
- 尚未被呼叫執行的程式碼
程序稿(script)：
- 直譯式：不須經過編譯就可以直接執行的程式碼 (like: .bat, .sh)
行程(process)：
- 被呼叫且載入到記憶體執行的程式(program)
行動代碼(mobile code)：
- 從遠端系統下載到本地端，且能直接執行的軟體或程式碼 (like: javaScript, Acitve X)

8.2 講義介紹了那些常見的程式運行(runtime)環境？
Answer：

1. 瀏覽器(Browser)
2. .NET Framework
3. JVM, Java Runtime Environment
4. Container

---
# 9. 何謂測試(testing)? 測試有那些類型(types)及技巧(techniques)？

9.1 何謂測試(testing)?
Answer：

測試(testing)：比對程式處理完資料後產出的結果是否與預期相同

9.2 測試有那些類型(types)及技巧(techniques)？
Answer：

類型(types)：
1. "箱"測試(The "Box" Testing)
	- 白箱(White-box)(Crystal-box)
	- 黑箱(Black-box)
	- 灰箱(Grey-box)
2. 主動 vs. 被動測試(Active vs. Passive Testing)：以測試者＆被測者是否直接互動來觀測
3. 靜態 vs. 動態測試(Static vs. Dynamic Testing)：以程式(Program)是否被執行來觀測
4. 正向 vs. 負向測試(Positive vs. Negative Testing)：透過輸入有效&無效值來觀測
5. 手動 vs. 自動測試(Manual vs. Automated Testing)：以測試時是否需要人工介入來觀測

技巧(techniques)：
1. 單元測試(Unit Testing)
2. 代碼審查(Code Review)
3. 整合測試(Integration Testing)
4. 系統測試(System Testing)
5. 誤用/濫用案例測試(Misuse/Abuse Case Testing)
6. 使用者驗收測試(UAT, User Acceptance Testing)
7. 安裝測試(Installation Testing)
8. 綜合/合成交易(Synthetic Transactions)

---
# 10.請簡述交付(delivery)與部署(deployment)的差別。

10.1 請簡述交付(delivery)與部署(deployment)的差別。
Answer：

交付(delivery)與部署(deployment)的核心差異在於是否讓系統＆使用者完成部署與上線這個動作
交付(delivery)重點在打包(Software Packages)、透過何種管道進行發佈(Distribution Channels)與持續交付(Continuous Delivery)，不需要確保系統＆使用者安裝與上線