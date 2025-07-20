# SneakyChef Campaign Summary

## Actor Profile
- **Name:** SneakyChef
- **Type:** Advanced Persistent Threat (APT) actor from Asia. State sponsorship unconfirmed.
- **Active Since:** At least August 2023
- **Primary Motives:** Espionage and data theft. Primarily targets intellectual information and credentials.
- **Targets:** Government entities and private sectors, particularly in India and Asia.
    - **Observed/Potential Targets:** Ministry of Foreign Affairs/Embassies in Pakistan, India, Angola.

## Tactics, Techniques, and Procedures (TTPs)
- **Initial Access:** Spear-Phishing emails containing malicious attachments or links.
- **Decoy Documents:** Leverages decoy documents, some appearing to be scanned copies of official documents obtained potentially through prior compromises.
- **Execution & Persistence:** Multi-stage attack chains utilizing various techniques.
- **Core Techniques:**
    - **DLL Side-Loading:** Loading malicious DLLs using legitimate executables.
    - **Custom C2 Protocols:** Using non-standard communication methods with command-and-control servers.
    - **Use of Legitimate Tools/Components:** Abusing tools like `regsvr32` or components like ActiveX (`DynamicWrapperX.dll`).

## Observed Intrusion Chains

### Intrusion Chain 1: SugarGhost (LNK -> JS -> DLL Side-Load)
1.  **Vector:** Malicious LNK file (masquerading).
2.  **Execution:** LNK executes embedded JavaScript.
3.  **Staging:** JavaScript drops:
    - Decoy document
    - BAT loader file
    - Malicious Loader DLL (`Mocks.DLL`)
    - Encrypted SugarGhost payload (`Dplay.org`)
4.  **Loader Execution:** JavaScript executes the BAT file.
5.  **Side-Loading:** BAT file executes the loader DLL (`Mocks.DLL`).
6.  **Payload Execution:** `Mocks.DLL` decrypts `Dplay.org` and injects the SugarGhost RAT into a legitimate process (e.g., `rundll32.exe`).
7.  **C2:** Connects to C2 server.

### Intrusion Chain 2: SugarGhost (SFX -> VBS -> DLL Side-Load)
1.  **Vector:** Self-Extracting Archive (SFX) file.
2.  **Execution:** SFX archive executes VBScript upon opening.
3.  **Payload Execution:** VBScript performs DLL Side-Loading (similar mechanism to Chain 1) to load, decrypt, and inject SugarGhost RAT.
4.  **C2:** Connects to C2 server.

### Intrusion Chain 3: SugarGhost (LNK -> JS -> ActiveX -> Shellcode)
1.  **Vector:** Malicious LNK file.
2.  **Execution:** LNK executes embedded JavaScript.
3.  **Staging:** JavaScript drops:
    - Decoy document
    - Legitimate ActiveX component (`DynamicWrapperX.dll`)
    - Encrypted SugarGhost component (`LEAY2.way`)
4.  **Component Loading:** JavaScript uses `regsvr32.exe` to load `DynamicWrapperX.dll` into memory.
5.  **Shellcode Execution:**
    - JavaScript decodes an embedded Base64 encoded Shellcode.
    - The Shellcode utilizes Windows API functions exposed by `DynamicWrapperX.dll` to execute itself.
6.  **Payload Execution:** The Shellcode decrypts `LEAY2.way` and injects the SugarGhost component into a process.
7.  **C2:** Connects to C2 server.
    *Note: The use of a legitimate ActiveX component to facilitate shellcode execution is considered an interesting and less common technique.*

### Intrusion Chain 4: SpiceRAT (HTA -> BAT -> Scheduled Task)
*(Details primarily from notes)*
1.  **Vector:** Malicious HTA (HTML Application) file.
2.  **Execution:** HTA file likely drops/executes a BAT file.
3.  **Persistence:** BAT file creates a Scheduled Task for persistence.
4.  **Payload Loading:** A malicious DLL loads the encrypted SpiceRAT payload (`CGMIMP32.HLP`), decrypts it, and runs it in memory.
5.  **Payload:** SpiceRAT

## Payloads

### SugarGh0st RAT
- **Origin:** Customized Gh0st RAT variant (named by Cisco Talos).
- **Capabilities:**
    - Keylogging
    - Process and service manipulation
    - Event log deletion
    - Command execution facilitated by C2

### SpiceRAT
- **Origin:** Modular RAT (named by Cisco Talos).
- **Type:** 32-bit Windows executable.
- **Capabilities (from notes):**
    - Creates Mutex for instance control.
    - Performs system reconnaissance.
    - Sends reconnaissance data to C2.
    - Downloads and runs additional plugin binaries.
    - Plugins enable further malicious activities.

## C2 Communication
- **Protocol:** Custom protocols observed.
- **SugarGhost Pattern:** May send a specific byte sequence (`0x000011A40100`) followed by a message like `"D_OK"` (potentially indicating a successful download or check-in).

## Assertion / Attribution Clues
- **Language Artifacts:**
    - Simplified Chinese names found in the "Last modified names" field of decoy documents.
    - Simplified Chinese comments found within SFX archive scripts. 

Canvas: [[SneakyChef_Campaign_Summary.canvas|SneakyChef_Campaign_Summary]]