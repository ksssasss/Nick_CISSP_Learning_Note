# Software Engineering
*page.378*

## Quality Software
![[Software Engineering-image-20250720.jpeg]]

Software
	Functionality
	Quality
Quality: U PASS ME!
	Usability
	Performance
	Availability
	Scalability
	==Security==
	Maintenance
	Extensibility
	

服務可用性，like 99.999%，是來量化可用性的一個指標
uptime --> 可用度
downtime -->

---
## SDLC: Software or System

### Software Development Life Cycle
![[Software Engineering-image-20250720 1.png]]

課程中軟體開發
- 談交付不談部署
- 談維護不談營運


### System Development Life Cycle

- Initiation
- Development/ Acquisition
- Implementation/ Assessment
- Operation/ Maintenance
- Disposal

```mermaid
graph TB
    A[Initiation] --> B[Development/<br>Acquisition]
    B --> C[Implementation/<br>Assessment]
    C --> D[Operation/<br>Maintenance]
    D --> E[Disposal]
    E --> A
    
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style B fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    style C fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px
    style D fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style E fill:#ffebee,stroke:#b71c1c,stroke-width:2px
```
---
## Software Overview

Software Environment
- Development Environment 開發環境
- Testing environment 測試環境
- Staging environment 過度環境
- Production environment 正式環境
- run-time environment --> 技術角度

Software Development Tools
- version control system: like "Git"

TIPS: 
時時都安全、處處都安全

---
## Software Runtime Environment

Hypervisor 是 VM 管家 by NIST
Mobile code 是 NIST強調的風險重點

## ==Code Repository and IDE==
*page.434*
Distributed
- ==Git==
- Mercurial
Client/ Server
- CVS
- SVN
Proprietary
- Microsoft TFS
- Bitbucket

## Object-Oriented Programming
*page.437*

Class & Object
- Attributes --> Properties 屬性
- Operations --> Methods 方法

```Example:
class Car:
    def __init__(self, color, brand):
        self.color = color      # 屬性
        self.brand = brand      # 屬性

    def drive(self):            # 方法
        print(f"{self.brand} 正在行駛")
```

OOP Features
- 封裝(Encapsulation):
	- 為了避免外部隨意存取Class中的Properties & Methods而實施存取限制的動作
- 繼承(Inheritance):
	- 子類別可繼承父類別的屬性和方法
- 多型(Polymorphism):
	- 不同類別的物件可以通過相同的接口進行操作，而表現出不同的行為(即方法的具體實現)。兩種做法:Overload & Override

Principles:
- 高聚合(High cohesion):
	- 盡量是相關的Properties & Methods才放到同一個Class中
- 低耦合(Low coupling):：
	- 盡量不要用別人的程式，即便使用也要避免將程式模組互相綁得太緊，當某個模組因某些原因不可用而需要更換時，可以降低更換模組的影響

---
## Testing Phase

Code Module <-- pair with --> Unit Test
```Example
# production Code Module
def add(a, b):
    return a + b

# 對應的 Unit Test
def test_add():
    result = add(2, 3)
    assert result == 5
```

### Software Testing Techniques
*page.442*

- Unit Testing
	- 核心概念: 用程式去測試程式
	- Unit Testing first, then Coding
- Code Review --> 人來看、機器看、專家看
	- Pair Programming:
		>結對編程，給夥伴看
	- Code Scanners
		> Example: 源碼檢測軟體
	- Fagan Inspection:
		>一種結構化的同行審查過程，在開發過程中檢查和審查設計文檔、源代碼以及其他軟件相關文檔是否有缺陷，較不適合自動化
- Integration Testing
	- Regression Testing
	- Interface testing (API & UI) --> 供 Module 之間互動
	- Fuzz Testing 模糊測試
- System Testing
	- Stress Testing
	- Security Testing
- Misure Case Testing
	>誤用案例通常會踩攻擊方觀點
- User Acceptance Testing (UAT)
	>驗收測試
- Installation Testing
- Synthetic Transactions 合成(人工)交易
	>Example: 交易系統下單測試

### Types of Testing
![[Software Engineering-image-20250720 3.png]]
Positive vs Negative Testing
- Valid vs invalid inputs

### Software Development Approaches
*page.388*

## Analysis Phase
*page.397*

### Requirements Document

- User Requirements Specification (URS)
- Use Case
	- Use Case Text
	- Use Case Diagram
- User Story

User Story Example
```
As <role>
I want <goal>
So that <benefit>

Acceptance criteria:
```
