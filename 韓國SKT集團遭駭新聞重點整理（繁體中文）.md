<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## 韓國SKT集團遭駭新聞重點整理（繁體中文）

**事件概述**

- 2025年4月19日，韓國最大電信商SK Telecom（SKT）遭到駭客利用惡意程式攻擊，導致部分用戶的USIM（SIM卡）相關資訊外洩[^1_3][^1_5][^1_6]。
- 外洩資訊包括用戶識別號碼、裝置唯一識別碼、USIM認證金鑰等，可能被用於非法複製SIM卡、盜用身分、攔截簡訊，進一步引發SIM Swapping等二次金融詐騙[^1_2][^1_3][^1_5]。

**事件經過與應對**

- SKT於4月19日發現異常，20日通報韓國網路振興院（KISA），並於隔日向個資保護委員會通報[^1_3][^1_5][^1_6]。
- 事件曝光後，SKT自4月28日起，針對全國約2,300萬行動用戶提供免費SIM卡（含eSIM）更換服務，門市出現排隊人潮[^1_7][^1_8][^1_10]。
- SKT同時推廣「SIM保護服務」，強化異常認證攔截與24小時安全監控[^1_10]。
- 公司承諾承擔所有責任，並對外公開道歉[^1_8][^1_10]。

**影響與爭議**

- SKT尚未公布實際受害人數及外洩資料規模[^1_3][^1_7][^1_10]。
- 部分媒體與專家懷疑攻擊可能來自北韓，但官方尚未證實[^1_3][^1_5][^1_6]。
- 消費者批評SKT未能第一時間個別通知用戶，僅於官網公告訊息[^1_2]。
- 主管機關調查發現SKT部分關鍵伺服器並未被列為「主要資訊通信基礎設施」，暴露出國家資安管理的漏洞[^1_1]。
- 事件也引發外界對韓國電信業資安預算縮減的質疑，SKT去年資安預算反而減少4%[^1_2]。

**後續與國家層級應對**

- 韓國政府已下令檢查全國資料保護體系，並組成緊急對策小組[^1_6][^1_8]。
- SKT表示現有SIM卡庫存僅能應付不到5%的換卡需求，預計5月底再補充500萬張SIM卡[^1_7][^1_8]。

**專家觀點與建議**

- 專家指出，這次事件暴露出國家對關鍵基礎設施資安管理的不足，建議需強化通訊業者資安防護、提升通報與應變機制[^1_1]。
- 用戶可透過SKT官方管道查詢個資是否外洩，並建議盡快更換SIM卡及啟用SIM保護服務[^1_1][^1_10]。

---

**總結**
SKT這起駭客事件不僅造成大規模個資外洩風險，也凸顯韓國電信業與國家資安管理上的多重問題，包括通報延遲、資安預算縮減、基礎設施保護不足等。官方與企業正積極補救並檢討資安政策，但消費者信心與產業資安體系仍面臨嚴峻挑戰[^1_2][^1_3][^1_7][^1_8][^1_10]。

<div style="text-align: center">⁂</div>

[^1_1]: https://www.youtube.com/watch?v=xdc2wtH3Ypc

[^1_2]: https://netmag.tw/2025/04/26/skt-data-breach-user-notification-anger

[^1_3]: https://www.cna.com.tw/news/aopl/202504220243.aspx

[^1_4]: https://udn.com/news/story/6812/8704298

[^1_5]: https://udn.com/news/story/6811/8691303

[^1_6]: https://news.cts.com.tw/cna/international/202504/202504222463759.html

[^1_7]: https://www.cna.com.tw/news/aopl/202504280255.aspx

[^1_8]: https://news.ltn.com.tw/news/world/breakingnews/5026243

[^1_9]: https://www.youtube.com/watch?v=3cKEPqrEmd8

[^1_10]: https://hk.news.yahoo.com/南韓-sk-電訊遭黑客攻擊-將為-2300-萬用戶免費更換-sim-卡-｜yahoo-082845225.html

[^1_11]: https://www.youtube.com/watch?v=MB6BwAtbXKY


---

# 裡面有沒有提到駭客的切入點與手法

有，根據現有公開資訊，這次SKT集團遭駭事件的切入點與攻擊手法有以下重點：

- **初始入侵點**：攻擊者很可能是先取得了SKT內部VPN閘道（如 nmcvpn.sktelecom.com）或開發者入口的帳密，這些憑證可能來自先前資料外洩或釣魚攻擊（Credential Stuffing/Phishing）。VPN伺服器常見於企業資安事件的初始切入點[^2_3]。
- **惡意程式植入**：攻擊者在4月19日晚上約11點於SKT的核心網路伺服器（HSS，Home Subscriber Server，4G/5G用戶認證伺服器）植入惡意程式，該時段選在週末夜間，屬於典型避開監控的時機點[^2_1][^2_2][^2_3][^2_4]。
- **橫向移動與權限提升**：取得初步存取權限後，駭客進一步橫向移動到其他內部系統（如NAMS網路資產管理、FIMS設施管理等），並透過竊取或破解管理員帳號進行權限提升，最終取得HSS伺服器的高權限[^2_3]。
- **資料外洩與反取證**：攻擊者在HSS伺服器上收集USIM資料（IMSI/IMEI、認證金鑰等），並可能嘗試刪除系統日誌以掩蓋行蹤（反取證手法）。資料外洩規模尚未完全確認[^2_3]。
- **多重攻擊技術**：推測攻擊者可能利用了弱密碼重複、釣魚取得MFA（多因素認證）令牌、利用未移除的測試或Demo端點，以及清除系統日誌等多種技術[^2_3]。

總結來說，這次SKT遭駭事件屬於典型的高階滲透攻擊，從外部憑證取得、內部橫向移動、權限提升、核心系統資料竊取到反取證，展現出攻擊者高度規劃與執行力[^2_3][^2_1][^2_2][^2_4]。

<div style="text-align: center">⁂</div>

[^2_1]: https://www.chosun.com/english/industry-en/2025/04/22/XZBKOWB3LNGP3ISWHV4PACCX4U/

[^2_2]: https://www.koreaherald.com/article/10471148

[^2_3]: https://www.linkedin.com/pulse/sk-telecom-2025-cyberattack-incident-david-sehyeon-baek-yexsf

[^2_4]: https://www.bitdefender.com/en-gb/blog/hotforsecurity/hackers-access-sensitive-sim-card-data-at-south-koreas-largest-telecoms-company

[^2_5]: https://www.securityweek.com/korean-telco-giant-sk-telecom-hacked/

[^2_6]: https://bloomingbit.io/en/feed/news/87046

[^2_7]: https://www.reddit.com/r/entrypoint/comments/h0pusf/hey_advice_anyone_i_just_really_wanna_do_this/

[^2_8]: https://www.sciencedirect.com/science/article/abs/pii/S0167404824003614

[^2_9]: https://www.scribd.com/document/521696049/Finding-entry-points-to-SS7-Networks

[^2_10]: https://www.donga.com/en/article/all/20250424/5567590/1

[^2_11]: https://dl.acm.org/doi/10.1016/j.cose.2024.104056

[^2_12]: https://www.youtube.com/watch?v=oISHD5dH2rs

[^2_13]: https://koreajoongangdaily.joins.com/news/2025-04-28/opinion/editorials/SKTs-delayed-response-to-hacking-incident-fuels-consumer-anxiety/2294696

[^2_14]: https://www.techradar.com/pro/security/sk-telecom-reveals-cyberattack-customer-usim-data-stolen-could-be-used-in-attacks

[^2_15]: https://www.clearskysec.com/wp-content/uploads/2020/10/Operation-Quicksand.pdf

[^2_16]: https://gbhackers.com/hack-the-box-ghost-challenge-cracked-a-detailed-technical-exploit/

[^2_17]: https://koreajoongangdaily.joins.com/news/2025-04-28/business/industry/Compromised-in-the-SKT-hack-Heres-how-to-sign-up-for-a-new-SIM/2295544

[^2_18]: https://www.infosecinstitute.com/resources/penetration-testing/discovering-entry-points/

[^2_19]: https://www.blackhat.com/presentations/bh-europe-07/Langlois/Presentation/bh-eu-07-langlois-ppt-apr19.pdf

[^2_20]: http://world.kbs.co.kr/service/news_view.htm?lang=e\&Seq_Code=192681


---

# 韓國SKT集團遭駭事件技術分析與攻擊軌跡報告

## 摘要

2025年4月19日，韓國最大電信商SK Telecom（SKT）遭駭客攻擊，導致用戶USIM（SIM卡）資料外洩。本報告整合公開資訊與技術證據，詳述攻擊時間軸、入侵手法、橫向移動軌跡及防護漏洞。攻擊者利用**BPFDoor惡意軟體**滲透核心網路伺服器，並透過VPN憑證竊取、權限提升及日誌清除等手段，竊取逾2,300萬用戶的IMSI、IMEI及USIM認證金鑰[^3_1][^3_3][^3_19]。事件暴露SKT在資安預算縮減、通報延遲及關鍵基礎設施防護不足等問題[^3_4][^3_8][^3_18]。

---

## 攻擊時間軸與核心事件

### 1. 初始入侵與惡意程式植入

- **2025年4月19日 23:00**：SKT監控系統於核心網路伺服器（HSS）偵測到異常活動，確認惡意程式植入[^3_1][^3_3][^3_19]。
- **攻擊入口點**：推測駭客透過以下途徑取得初始存取權限：
    - **VPN閘道（nmcvpn.sktelecom.com）**：利用釣魚攻擊或憑證填充（Credential Stuffing）取得合法帳密[^3_19]。
    - **開發者入口（developers.sktelecom.com）**：未修補的測試端點或弱密碼導致權限外洩[^3_19]。
- **惡意程式特性**：使用**BPFDoor後門程式**，該程式利用Berkeley Packet Filter（BPF）技術在Linux核心層隱匿網路活動，繞過防火牆偵測[^3_6][^3_10][^3_11][^3_19]。


### 2. 橫向移動與權限提升

- **內部系統滲透**：攻擊者自VPN或開發入口橫向移動至**NAMS（網路資產管理系統）**與**FIMS（設施管理系統）**，竊取管理員帳號並提升權限[^3_19]。
- **HSS伺服器入侵**：取得HSS高權限後，駭客竊取USIM相關資料，包括：
    - **IMSI（國際移動用戶識別碼）**
    - **IMEI（國際移動設備識別碼）**
    - **Ki/OPc（USIM認證金鑰）**[^3_8][^3_19]。
- **反取證措施**：清除系統日誌並使用加密通道外傳資料，延緩偵測[^3_19][^3_13]。


### 3. 事件通報與應對延遲

- **4月20日 16:46**：SKT向韓國網路振興院（KISA）通報事件，距攻擊發生已逾40小時，違反24小時通報規定[^3_18][^3_19]。
- **4月22日**：向個資保護委員會（PIPC）提交報告，並公開承認資料外洩[^3_3][^3_9]。
- **爭議點**：SKT未即時以簡訊通知用戶，僅透過官網公告，引發消費者不滿與集體訴訟[^3_5][^3_12][^3_18]。

---

## 技術分析：BPFDoor惡意軟體與攻擊手法

### 1. BPFDoor運作機制

- **隱匿性設計**：
    - 透過BPF引擎在核心層過濾封包，僅回應含特定「魔術位元組」（Magic Byte）的封包，避開傳統端口監控[^3_10][^3_11][^3_15][^3_19]。
    - 植入後自刪除執行檔，並偽裝為系統程序（如`kdmtmpflush`），增加偵測難度[^3_11][^3_19]。
- **功能模組**：
    - **反向Shell**：接收攻擊者指令，建立加密通道[^3_10][^3_15]。
    - **流量重定向**：篡改iptables規則，將合法服務端口（如SSH 22/TCP）導向惡意監聽端[^3_11][^3_19]。


### 2. 攻擊者基礎設施與關聯

- **C2伺服器**：部分攻擊IP與過往中國駭客組織**Red Menshen（紅門）**及**Earth Bluecrow**活動重疊，但BPFDoor原始碼自2022年外洩後，可能遭多方利用[^3_10][^3_11][^3_19]。
- **橫向工具**：
    - **SSH暴力破解**：針對內部伺服器使用弱密碼或預設憑證[^3_19]。
    - **Windows域滲透**：利用竊取的ADFS/OAuth權限繞過多因素驗證（MFA）[^3_19]。

---

## 資安漏洞與體制缺陷

### 1. SKT內部防護不足

- **資安預算縮減**：2024年資安投資減少4%，導致漏洞修補與監控系統更新延遲[^3_4][^3_7]。
- **HSS伺服器未列關鍵設施**：遭入侵的HSS未被韓國政府列為「主要資訊通信基礎設施」，缺乏強制性防護標準[^3_4][^3_8]。


### 2. 國家層級管理疏失

- **KISA應變延遲**：
    - 現地調查於4月21日20:00啟動，較通報時間延遲28小時，且僅遠端檢查SKT總部，未深入分析分區機房[^3_18][^3_19]。
    - 被質疑修改SKT通報時間，掩蓋違反24小時通報規定之事實[^3_18][^3_20]。
- **法規執行漏洞**：韓國《電信事業法》未明確規範電信業者核心系統的資安審查頻率與標準[^3_8][^3_9]。

---

## 影響與後續衝擊

### 1. 用戶風險與補救措施

- **SIM交換攻擊（SIM Swapping）**：外洩的USIM金鑰可能用於複製SIM卡，攔截簡訊驗證碼並入侵金融帳戶[^3_4][^3_12][^3_17]。
- **SKT補救方案**：
    - 免費更換USIM芯片（含eSIM），但初期庫存僅滿足5%需求，引發門市混亂[^3_4][^3_17]。
    - 推廣「USIM保護服務」，強化異常認證攔截[^3_3][^3_8][^3_14]。


### 2. 產業與國家安全衝擊

- **關鍵基礎設施信任危機**：SKT為韓國5G網路核心供應商，此次事件暴露國家級通訊系統的鏈式風險[^3_19]。
- **地緣政治疑慮**：攻擊手法與中國APT組織高度相似，但北韓駭客亦可能利用BPFDoor進行滲透[^3_6][^3_10][^3_19]。

---

## 結論與建議

### 1. 事件教訓

- **即時通報機制**：企業應建立自動化異常偵測與法規遵從系統，避免人為延誤[^3_18][^3_19]。
- **零信任架構（Zero Trust）**：核心系統需實施嚴格身分驗證與微分割（Microsegmentation），限制橫向移動[^3_19]。


### 2. 技術強化方向

- **威脅情資共享**：整合業界IOC（如BPFDoor雜湊值）至SIEM平台，提升威脅狩獵效率[^3_6][^3_15][^3_19]。
- **供應鏈安全審查**：第三方開發者入口與VPN服務需納入定期滲透測試範圍[^3_19]。


### 3. 政策建議

- **關鍵設施定義擴充**：將電信業HSS、5G核心網元件納入國家級資安防護規範[^3_8][^3_9]。
- **跨境協作**：與國際CERT組織合作追蹤BPFDoor關聯攻擊，制訂聯合防禦策略[^3_10][^3_11][^3_19]。

---

本報告基於公開資料與技術證據重建攻擊軌跡，凸顯進階持續性威脅（APT）對關鍵基礎設施的潛在風險。SKT事件不僅為企業資安警鐘，更需引發全球電信業對隱匿性惡意軟體與地緣駭客活動的重新評估。

<div style="text-align: center">⁂</div>

[^3_1]: https://www.chosun.com/english/industry-en/2025/04/22/XZBKOWB3LNGP3ISWHV4PACCX4U/

[^3_2]: https://arxiv.org/pdf/1701.04940.pdf

[^3_3]: https://en.yna.co.kr/view/AEN20250422003851320

[^3_4]: https://koreajoongangdaily.joins.com/news/2025-04-28/opinion/editorials/SKTs-delayed-response-to-hacking-incident-fuels-consumer-anxiety/2294696

[^3_5]: http://world.kbs.co.kr/service/news_view.htm?lang=e\&Seq_Code=192681

[^3_6]: https://m.ddaily.co.kr/page/view/2025042614063180738

[^3_7]: https://newneek.co/@newneek/article/31562

[^3_8]: https://www.industrynews.co.kr/news/articleView.html?idxno=63075

[^3_9]: https://m.newsprime.co.kr/section_view.html?no=684959

[^3_10]: https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html

[^3_11]: https://www.linkedin.com/pulse/dear-telcos-around-world-please-beware-bpfdoor-malware-baek-fkubc

[^3_12]: https://koreajoongangdaily.joins.com/news/2025-04-28/business/industry/SKT-customers-eye-collective-action-as-hack-hits-bank-accounts/2295150

[^3_13]: https://www.yna.co.kr/view/AKR20250425168300017

[^3_14]: https://www.newstree.kr/newsView/ntr202504220013

[^3_15]: https://www.countercraftsec.com/blog/iocs-intel-and-additional-resources-from-the-bpfdoor-compromise/

[^3_16]: https://www.acrotech.com.tw/news_details.php?id=318

[^3_17]: https://www.channelnewsasia.com/east-asia/south-korea-sk-telecom-sim-card-replacement-data-breach-cyber-attack-5094221

[^3_18]: https://www.financialpost.co.kr/news/articleView.html?idxno=225218

[^3_19]: https://www.linkedin.com/pulse/sk-telecom-2025-cyberattack-incident-david-sehyeon-baek-yexsf

[^3_20]: https://v.daum.net/v/20250428152908721?f=p

[^3_21]: https://www.securityweek.com/korean-telco-giant-sk-telecom-hacked/

[^3_22]: https://www.bleepingcomputer.com/news/security/sk-telecom-warns-customer-usim-data-exposed-in-malware-attack/

[^3_23]: https://www.preprints.org/manuscript/202412.2516/v2/download

[^3_24]: https://www.globalbankingandfinance.com/UK-SK-TELECOM-CYBERATTACK-e87ee729-61c6-41a7-98d8-79c2030a6a46

[^3_25]: https://www.sktelecom.com/en/view/esg/information-security.do

[^3_26]: https://www.chosun.com/english/industry-en/2025/04/25/JZ3KEMCUEFHQFP23OLT37DMRWU/

[^3_27]: https://www.lightreading.com/security/skt-takes-full-responsibility-amid-usim-hacking-fallout

[^3_28]: https://istrosec.com/service/digital-forensics/

[^3_29]: https://koreajoongangdaily.joins.com/news/2025-04-28/national/socialAffairs/Personal-information-watchdog-chief-says-SKT-probe-could-take-months-a-year/2295519

[^3_30]: https://www.sktcorp.com/what-we-do/cybersecurity-services/

[^3_31]: https://www.koreatimes.co.kr/business/companies/20250422/sk-telecom-reports-hacking-incident-involving-partial-leak-of-user-usim-data

[^3_32]: https://journals.sagepub.com/doi/full/10.1177/20322844231212661

[^3_33]: https://www.ddaily.co.kr/page/view/2025042815553187651

[^3_34]: https://v.daum.net/v/20250428152908721

[^3_35]: https://www.kmib.co.kr/article/view.asp?arcid=1745308697

[^3_36]: https://zdnet.co.kr/view/?no=20250422110252

[^3_37]: http://www.boho.or.kr

[^3_38]: https://www.yna.co.kr/view/AKR20250424072400017?input=feed_microsoft

[^3_39]: https://biz.chosun.com/it-science/ict/2025/04/24/IKVMU5OBNBCYFFNFR2GQ4UAMNI/

[^3_40]: https://m.ddaily.co.kr/page/view/2025042211141523684

[^3_41]: https://m.boannews.com/html/detail.html?idx=137004

[^3_42]: https://www.bbc.com/korean/articles/ceqrd9p9wdyo

[^3_43]: https://www.hani.co.kr/arti/economy/economy_general/1194544.html

[^3_44]: https://m.boannews.com/html/detail.html?idx=137027\&kind=\&sub_kind=

[^3_45]: https://www.trendmicro.com/zh_hk/research/25/d/bpfdoor-hidden-controller.html

[^3_46]: https://attack.mitre.org/software/S1161/

[^3_47]: https://bazaar.abuse.ch/browse/tag/bpfdoor/

[^3_48]: https://rewterz.com/threat-advisory/sophisticated-bpfdoor-malware-detected-targeting-linux-systems-active-iocs

[^3_49]: https://world.kbs.co.kr/service/news_view.htm?lang=c\&Seq_Code=85646

[^3_50]: https://macquariecloudservices.com/wp-content/uploads/sites/3/2022/06/MCS-BPF-Door-Technical-Deep-Dive.pdf

[^3_51]: https://www.pwc.at/de/dienstleistungen/Cyber/2022-year-in-retrospect-report.pdf

[^3_52]: https://www.eet-china.com/mp/a400471.html

[^3_53]: https://cymulate.com/threats/bpfdoor-stealthy-linux-malware-bypasses-firewalls-for-remote-access/

[^3_54]: https://attack.mitre.org/software

[^3_55]: https://tw.news.yahoo.com/韓龍頭sk電信遇駭個資外洩-免費替客戶換sim卡引人龍-101629760.html

[^3_56]: https://malpedia.caad.fkie.fraunhofer.de/library/96d020b5-f460-4e4b-bdfe-dab76a85a706/

[^3_57]: https://wazuh.com/blog/using-wazuh-to-detect-bpfdoor-malware/

[^3_58]: https://www.bleepingcomputer.com/news/security/bpfdoor-stealthy-linux-malware-bypasses-firewalls-for-remote-access/

[^3_59]: https://blog.qualys.com/vulnerabilities-threat-research/2022/08/01/heres-a-simple-script-to-detect-the-stealthy-nation-state-bpfdoor

[^3_60]: https://bazaar.abuse.ch/sample/fd1b20ee5bd429046d3c04e9c675c41e9095bea70e0329bd32d7edd17ebaf68a/

