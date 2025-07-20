# SneakyChef
	Asian actor
	2023 active since
	goals: Espionage and data theft
	Victim: Government entities and private sectors in India and Asia (e.g., Pakistan, India, Angola)
	TTPs: Spear-Phishing campaign, DLL Side-Loading, custom C2 commucation protocal

## Campaign
	SneakyChef has been operating since at least August 2023

technology
	Decoy documents
	SugarGhost infection
		1. (LNK -> JS variant)
		Loader DLL - Mocks.DLL
		connect to RunDLL32.exe (injected process inferred)
		Encrypted payload: Dplay.org
		
		2. (SFX -> VBS variant)
		SFXR, VBS script
		Similar DLL Side-Loading mechanism as 1.
		
		3. (LNK -> JS -> ActiveX variant)
		LNK -> JavaScript
		Drops legitimate DynamicWrapperX.dll (ActiveX) and encrypted payload (LEAY2.way)
		JS uses regsvr32 to load DynamicWrapperX.dll
		JS decodes Base64 Shellcode
		Shellcode uses DynamicWrapperX's API to execute
		Shellcode decrypts and runs LEAY2.way (encrypted SugarGhost component)
		
		4. (SpiceRAT delivery - HTA variant, from notes)
		use spice-rat as the payload
		delivery by HTA file
		and use bat file to schedule tasks

Intermediate - Final Phase (SpiceRAT - inferred from notes)
	Malicious DLL loads the encrypted SpiceRAT(CGMIMP32.HLP), decrypts and runs in memory

## Payload
### SugarGh0st
	SugarGh0st is a custiomized Gh0st RAT variant
Keyloggin
Processes and services manipulation
Deletes event logs
Facilitates commands

### SpiceRAT (Details from notes)
	SpiceRAT a 32-bit windows executable
	Creates Mutex and prefroms reconnaissance
	Sends the recon data to the C2
	Process and runs the plugin binary
	Plugins enables further attacks

## C2 communication pattern
### SugarGh0st
	0x000011A40100
	followed with a message "D_OK", likely a secussful download

## Assertion
Last modifie names field of decoy documents has simplified chinese nams
comments in the SFX script i simplified Chinese
![[Recording 20250416160053.m4a]]
