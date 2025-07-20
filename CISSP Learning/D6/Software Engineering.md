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

Distributed
- ==Git==
- Mercurial
Client/ Server
- CVS
- SVN
Proprietary
- Microsoft TFS
- Bitbucket


