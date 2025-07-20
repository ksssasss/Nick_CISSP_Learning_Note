# 韓國SKT集團遭駭事件技術分析與攻擊軌跡報告

## 摘要

2025年4月19日，韓國最大電信商SK Telecom（SKT）遭駭客攻擊，導致用戶USIM（SIM卡）資料外洩。本報告整合公開資訊與技術證據，詳述攻擊時間軸、入侵手法、橫向移動軌跡及防護漏洞。攻擊者利用**BPFDoor惡意軟體**滲透核心網路伺服器，並透過VPN憑證竊取、權限提升及日誌清除等手段，竊取逾2,300萬用戶的IMSI、IMEI及USIM認證金鑰。事件暴露SKT在資安預算縮減、通報延遲及關鍵基礎設施防護不足等問題。

---

## 攻擊時間軸與核心事件

### 1. 初始入侵與惡意程式植入

- **2025年4月19日 23:00**：SKT監控系統於核心網路伺服器（HSS）偵測到異常活動，確認惡意程式植入。
- **攻擊入口點**：推測駭客透過以下途徑取得初始存取權限：
    - **VPN閘道（nmcvpn.sktelecom.com）**：利用釣魚攻擊或憑證填充（Credential Stuffing）取得合法帳密。
    - **開發者入口（developers.sktelecom.com）**：未修補的測試端點或弱密碼導致權限外洩。
- **惡意程式特性**：使用**BPFDoor後門程式**，該程式利用Berkeley Packet Filter（BPF）技術在Linux核心層隱匿網路活動，繞過防火牆偵測。


### 2. 橫向移動與權限提升

- **內部系統滲透**：攻擊者自VPN或開發入口橫向移動至**NAMS（網路資產管理系統）**與**FIMS（設施管理系統）**，竊取管理員帳號並提升權限。
- **HSS伺服器入侵**：取得HSS高權限後，駭客竊取USIM相關資料，包括：
    - **IMSI（國際移動用戶識別碼）**
    - **IMEI（國際移動設備識別碼）**
    - **Ki/OPc（USIM認證金鑰）**。
- **反取證措施**：清除系統日誌並使用加密通道外傳資料，延緩偵測。


### 3. 事件通報與應對延遲

- **4月20日 16:46**：SKT向韓國網路振興院（KISA）通報事件，距攻擊發生已逾40小時，違反24小時通報規定。
- **4月22日**：向個資保護委員會（PIPC）提交報告，並公開承認資料外洩。
- **爭議點**：SKT未即時以簡訊通知用戶，僅透過官網公告，引發消費者不滿與集體訴訟。

---

## 技術分析：BPFDoor惡意軟體與攻擊手法

### 1. BPFDoor運作機制

- **隱匿性設計**：
    - 透過BPF引擎在核心層過濾封包，僅回應含特定「魔術位元組」（Magic Byte）的封包，避開傳統端口監控。
    - 植入後自刪除執行檔，並偽裝為系統程序（如`kdmtmpflush`），增加偵測難度。
- **功能模組**：
    - **反向Shell**：接收攻擊者指令，建立加密通道。
    - **流量重定向**：篡改iptables規則，將合法服務端口（如SSH 22/TCP）導向惡意監聽端。


### 2. 攻擊者基礎設施與關聯

- **C2伺服器**：部分攻擊IP與過往中國駭客組織**Red Menshen（紅門）**及**Earth Bluecrow**活動重疊，但BPFDoor原始碼自2022年外洩後，可能遭多方利用。
- **橫向工具**：
    - **SSH暴力破解**：針對內部伺服器使用弱密碼或預設憑證。
    - **Windows域滲透**：利用竊取的ADFS/OAuth權限繞過多因素驗證（MFA）。

---

## 資安漏洞與體制缺陷

### 1. SKT內部防護不足

- **資安預算縮減**：2024年資安投資減少4%，導致漏洞修補與監控系統更新延遲。
- **HSS伺服器未列關鍵設施**：遭入侵的HSS未被韓國政府列為「主要資訊通信基礎設施」，缺乏強制性防護標準。


### 2. 國家層級管理疏失

- **KISA應變延遲**：
    - 現地調查於4月21日20:00啟動，較通報時間延遲28小時，且僅遠端檢查SKT總部，未深入分析分區機房。
    - 被質疑修改SKT通報時間，掩蓋違反24小時通報規定之事實。
- **法規執行漏洞**：韓國《電信事業法》未明確規範電信業者核心系統的資安審查頻率與標準。

---

## 影響與後續衝擊

### 1. 用戶風險與補救措施

- **SIM交換攻擊（SIM Swapping）**：外洩的USIM金鑰可能用於複製SIM卡，攔截簡訊驗證碼並入侵金融帳戶。
- **SKT補救方案**：
    - 免費更換USIM芯片（含eSIM），但初期庫存僅滿足5%需求，引發門市混亂。
    - 推廣「USIM保護服務」，強化異常認證攔截。


### 2. 產業與國家安全衝擊

- **關鍵基礎設施信任危機**：SKT為韓國5G網路核心供應商，此次事件暴露國家級通訊系統的鏈式風險。
- **地緣政治疑慮**：攻擊手法與中國APT組織高度相似，但北韓駭客亦可能利用BPFDoor進行滲透。

---

## 結論與建議

### 1. 事件教訓

- **即時通報機制**：企業應建立自動化異常偵測與法規遵從系統，避免人為延誤。
- **零信任架構（Zero Trust）**：核心系統需實施嚴格身分驗證與微分割（Microsegmentation），限制橫向移動。


### 2. 技術強化方向

- **威脅情資共享**：整合業界IOC（如BPFDoor雜湊值）至SIEM平台，提升威脅狩獵效率。
- **供應鏈安全審查**：第三方開發者入口與VPN服務需納入定期滲透測試範圍。


### 3. 政策建議

- **關鍵設施定義擴充**：將電信業HSS、5G核心網元件納入國家級資安防護規範。
- **跨境協作**：與國際CERT組織合作追蹤BPFDoor關聯攻擊，制訂聯合防禦策略。

---

本報告基於公開資料與技術證據重建攻擊軌跡，凸顯進階持續性威脅（APT）對關鍵基礎設施的潛在風險。SKT事件不僅為企業資安警鐘，更需引發全球電信業對隱匿性惡意軟體與地緣駭客活動的重新評估。

<div style="text-align: center">⁂</div>

: https://www.chosun.com/english/industry-en/2025/04/22/XZBKOWB3LNGP3ISWHV4PACCX4U/

: https://arxiv.org/pdf/1701.04940.pdf

: https://en.yna.co.kr/view/AEN20250422003851320

: https://koreajoongangdaily.joins.com/news/2025-04-28/opinion/editorials/SKTs-delayed-response-to-hacking-incident-fuels-consumer-anxiety/2294696

: http://world.kbs.co.kr/service/news_view.htm?lang=e\&Seq_Code=192681

: https://m.ddaily.co.kr/page/view/2025042614063180738

: https://newneek.co/@newneek/article/31562

: https://www.industrynews.co.kr/news/articleView.html?idxno=63075

: https://m.newsprime.co.kr/section_view.html?no=684959

: https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html

: https://www.linkedin.com/pulse/dear-telcos-around-world-please-beware-bpfdoor-malware-baek-fkubc

: https://koreajoongangdaily.joins.com/news/2025-04-28/business/industry/SKT-customers-eye-collective-action-as-hack-hits-bank-accounts/2295150

: https://www.yna.co.kr/view/AKR20250425168300017

: https://www.newstree.kr/newsView/ntr202504220013

: https://www.countercraftsec.com/blog/iocs-intel-and-additional-resources-from-the-bpfdoor-compromise/

: https://www.acrotech.com.tw/news_details.php?id=318

: https://www.channelnewsasia.com/east-asia/south-korea-sk-telecom-sim-card-replacement-data-breach-cyber-attack-5094221

: https://www.financialpost.co.kr/news/articleView.html?idxno=225218

: https://www.linkedin.com/pulse/sk-telecom-2025-cyberattack-incident-david-sehyeon-baek-yexsf

: https://v.daum.net/v/20250428152908721?f=p

: https://www.securityweek.com/korean-telco-giant-sk-telecom-hacked/

: https://www.bleepingcomputer.com/news/security/sk-telecom-warns-customer-usim-data-exposed-in-malware-attack/

: https://www.preprints.org/manuscript/202412.2516/v2/download

: https://www.globalbankingandfinance.com/UK-SK-TELECOM-CYBERATTACK-e87ee729-61c6-41a7-98d8-79c2030a6a46

: https://www.sktelecom.com/en/view/esg/information-security.do

: https://www.chosun.com/english/industry-en/2025/04/25/JZ3KEMCUEFHQFP23OLT37DMRWU/

: https://www.lightreading.com/security/skt-takes-full-responsibility-amid-usim-hacking-fallout

: https://istrosec.com/service/digital-forensics/

: https://koreajoongangdaily.joins.com/news/2025-04-28/national/socialAffairs/Personal-information-watchdog-chief-says-SKT-probe-could-take-months-a-year/2295519

: https://www.sktcorp.com/what-we-do/cybersecurity-services/

: https://www.koreatimes.co.kr/business/companies/20250422/sk-telecom-reports-hacking-incident-involving-partial-leak-of-user-usim-data

: https://journals.sagepub.com/doi/full/10.1177/20322844231212661

: https://www.ddaily.co.kr/page/view/2025042815553187651

: https://v.daum.net/v/20250428152908721

: https://www.kmib.co.kr/article/view.asp?arcid=1745308697

: https://zdnet.co.kr/view/?no=20250422110252

: http://www.boho.or.kr

: https://www.yna.co.kr/view/AKR20250424072400017?input=feed_microsoft

: https://biz.chosun.com/it-science/ict/2025/04/24/IKVMU5OBNBCYFFNFR2GQ4UAMNI/

: https://m.ddaily.co.kr/page/view/2025042211141523684

: https://m.boannews.com/html/detail.html?idx=137004

: https://www.bbc.com/korean/articles/ceqrd9p9wdyo

: https://www.hani.co.kr/arti/economy/economy_general/1194544.html

: https://m.boannews.com/html/detail.html?idx=137027\&kind=\&sub_kind=

: https://www.trendmicro.com/zh_hk/research/25/d/bpfdoor-hidden-controller.html

: https://attack.mitre.org/software/S1161/

: https://bazaar.abuse.ch/browse/tag/bpfdoor/

: https://rewterz.com/threat-advisory/sophisticated-bpfdoor-malware-detected-targeting-linux-systems-active-iocs

: https://world.kbs.co.kr/service/news_view.htm?lang=c\&Seq_Code=85646

: https://macquariecloudservices.com/wp-content/uploads/sites/3/2022/06/MCS-BPF-Door-Technical-Deep-Dive.pdf

: https://www.pwc.at/de/dienstleistungen/Cyber/2022-year-in-retrospect-report.pdf

: https://www.eet-china.com/mp/a400471.html

: https://cymulate.com/threats/bpfdoor-stealthy-linux-malware-bypasses-firewalls-for-remote-access/

: https://attack.mitre.org/software

: https://tw.news.yahoo.com/韓龍頭sk電信遇駭個資外洩-免費替客戶換sim卡引人龍-101629760.html

: https://malpedia.caad.fkie.fraunhofer.de/library/96d020b5-f460-4e4b-bdfe-dab76a85a706/

: https://wazuh.com/blog/using-wazuh-to-detect-bpfdoor-malware/

: https://www.bleepingcomputer.com/news/security/bpfdoor-stealthy-linux-malware-bypasses-firewalls-for-remote-access/

: https://blog.qualys.com/vulnerabilities-threat-research/2022/08/01/heres-a-simple-script-to-detect-the-stealthy-nation-state-bpfdoor

: https://bazaar.abuse.ch/sample/fd1b20ee5bd429046d3c04e9c675c41e9095bea70e0329bd32d7edd17ebaf68a/

