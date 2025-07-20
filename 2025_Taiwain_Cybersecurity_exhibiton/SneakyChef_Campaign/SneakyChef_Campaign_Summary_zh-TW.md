# SneakyChef 攻擊活動總結

## 行為者檔案 (Actor Profile)
- **名稱 (Name):** SneakyChef
- **類型 (Type):** 來自亞洲的進階持續性威脅 (Advanced Persistent Threat, APT) 行為者。國家級贊助背景未經確認。
- **活躍時間 (Active Since):** 至少自 2023 年 8 月起
- **主要動機 (Primary Motives):** 間諜活動 (Espionage) 與資料竊取 (Data Theft)。主要目標為智慧財產資訊與憑證 (credentials)。
- **目標 (Targets):** 政府實體與私營部門，特別是位於印度 (India) 與亞洲 (Asia) 的目標。
    - **已觀察/潛在目標 (Observed/Potential Targets):** 巴基斯坦 (Pakistan)、印度 (India)、安哥拉 (Angola) 的外交部/大使館。

## 戰術、技術與程序 (Tactics, Techniques, and Procedures, TTPs)
- **初始入侵 (Initial Access):** 包含惡意附件或連結的魚叉式網路釣魚 (Spear-Phishing) 郵件。
- **誘餌文件 (Decoy Documents):** 利用誘餌文件，部分文件看似是透過先前入侵行為取得的官方文件掃描檔。
- **執行與持續性 (Execution & Persistence):** 利用多種技術的多階段攻擊鏈 (Multi-stage attack chains)。
- **核心技術 (Core Techniques):**
    - **DLL 側載 (DLL Side-Loading):** 使用合法執行檔載入惡意 DLL。
    - **客製化 C2 協定 (Custom C2 Protocols):** 使用非標準的通訊方式與 C2 (command-and-control) 伺服器溝通。
    - **利用合法工具/元件 (Use of Legitimate Tools/Components):** 濫用如 `regsvr32` 等工具或如 ActiveX (`DynamicWrapperX.dll`) 等元件。

## 已觀察到的入侵鏈 (Observed Intrusion Chains)

### 入侵鏈 1: SugarGhost (LNK -> JS -> DLL Side-Load)
1.  **入侵媒介 (Vector):** 惡意 LNK 檔案 (偽裝)。
2.  **執行 (Execution):** LNK 執行內嵌的 JavaScript (JS)。
3.  **部署準備 (Staging):** JavaScript 投放：
    - 誘餌文件 (Decoy document)
    - BAT loader 檔案
    - 惡意 Loader DLL (`Mocks.DLL`)
    - 加密的 SugarGhost payload (`Dplay.org`)
4.  **載入器執行 (Loader Execution):** JavaScript 執行 BAT 檔案。
5.  **側載 (Side-Loading):** BAT 檔案執行 loader DLL (`Mocks.DLL`)。
6.  **Payload 執行 (Payload Execution):** `Mocks.DLL` 解密 `Dplay.org` 並將 SugarGhost RAT 注入 (inject) 合法處理程序 (例如 `rundll32.exe`)。
7.  **C2:** 連線至 C2 伺服器。

### 入侵鏈 2: SugarGhost (SFX -> VBS -> DLL Side-Load)
1.  **入侵媒介 (Vector):** 自解壓縮檔 (Self-Extracting Archive, SFX) 檔案。
2.  **執行 (Execution):** SFX 檔案在開啟時執行 VBScript (VBS)。
3.  **Payload 執行 (Payload Execution):** VBScript 執行 DLL Side-Loading (機制類似入侵鏈 1) 以載入、解密並注入 SugarGhost RAT。
4.  **C2:** 連線至 C2 伺服器。

### 入侵鏈 3: SugarGhost (LNK -> JS -> ActiveX -> Shellcode)
1.  **入侵媒介 (Vector):** 惡意 LNK 檔案。
2.  **執行 (Execution):** LNK 執行內嵌的 JavaScript (JS)。
3.  **部署準備 (Staging):** JavaScript 投放：
    - 誘餌文件 (Decoy document)
    - 合法的 ActiveX 元件 (`DynamicWrapperX.dll`)
    - 加密的 SugarGhost 元件 (`LEAY2.way`)
4.  **元件載入 (Component Loading):** JavaScript 使用 `regsvr32.exe` 將 `DynamicWrapperX.dll` 載入記憶體。
5.  **Shellcode 執行 (Shellcode Execution):**
    - JavaScript 解碼一個內嵌的 Base64 編碼 Shellcode。
    - 該 Shellcode 利用 `DynamicWrapperX.dll` 提供的 Windows API 函數來執行自身。
6.  **Payload 執行 (Payload Execution):** Shellcode 解密 `LEAY2.way` 並將 SugarGhost 元件注入處理程序。
7.  **C2:** 連線至 C2 伺服器。
    *註：利用合法的 ActiveX 元件來輔助 Shellcode 執行被認為是一種有趣且較不常見的技術。*

### 入侵鏈 4: SpiceRAT (HTA -> BAT -> Scheduled Task)
*(主要來自筆記的細節)*
1.  **入侵媒介 (Vector):** 惡意 HTA (HTML Application) 檔案。
2.  **執行 (Execution):** HTA 檔案可能投放/執行一個 BAT 檔案。
3.  **持續性 (Persistence):** BAT 檔案建立一個排程工作 (Scheduled Task) 以達成持續性。
4.  **Payload 載入 (Payload Loading):** 一個惡意 DLL 載入加密的 SpiceRAT payload (`CGMIMP32.HLP`)，將其解密並在記憶體中執行。
5.  **Payload:** SpiceRAT

## Payloads

### SugarGh0st RAT
- **來源 (Origin):** 客製化的 Gh0st RAT 變種 (由 Cisco Talos 命名)。
- **功能 (Capabilities):**
    - 鍵盤側錄 (Keylogging)
    - 處理程序與服務操控 (Process and service manipulation)
    - 事件日誌刪除 (Event log deletion)
    - 由 C2 輔助的指令執行 (Command execution facilitated by C2)

### SpiceRAT
- **來源 (Origin):** 模組化的 RAT (Modular RAT) (由 Cisco Talos 命名)。
- **類型 (Type):** 32 位元 Windows 執行檔。
- **功能 (Capabilities) (來自筆記):**
    - 建立 Mutex 以控制實例。
    - 執行系統偵察 (reconnaissance)。
    - 將偵察資料傳送至 C2。
    - 下載並執行額外的插件 (plugin) 二進位檔。
    - 插件可啟用進一步的惡意活動。

## C2 通訊 (C2 Communication)
- **協定 (Protocol):** 觀察到使用客製化協定。
- **SugarGhost 模式 (SugarGhost Pattern):** 可能會傳送特定的位元組序列 (`0x000011A40100`)，後接如 `"D_OK"` 的訊息 (可能表示下載成功或簽到)。

## 歸因/判斷線索 (Assertion / Attribution Clues)
- **語言跡證 (Language Artifacts):**
    - 在誘餌文件的「最後修改者名稱 (Last modified names)」欄位中發現簡體中文名稱。
    - 在 SFX 壓縮檔腳本中發現簡體中文註解。 

Canvas: [[SneakyChef_Campaign_Summary.canvas|SneakyChef_Campaign_Summary]]