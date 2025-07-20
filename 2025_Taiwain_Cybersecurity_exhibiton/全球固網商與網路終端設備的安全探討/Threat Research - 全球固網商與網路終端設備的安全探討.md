by TXOne Research

# What is a Residential Gateway?
Bridges premises to Internet
Define-
	Modem modulates to/from Ethernet
Residential Gateway performs modem + computing

# Why is RG importaint and worth studying into?
Gateway devices are lucrative target foe adversaries

# How many Residential Gateways(RGs) on Earth?
Could be at least 153 million

# Inspiration of research / Brief Conclusion
Focused on ISP's infrastructure & RG
Both are no very safe
Demonstration
	How to study your RG - From board to ISP and many RGs

## Modern Infrastructure - Everything needs telecommunication

<<-- IP Protocal -->
	<<-- IPoE/ PPPoE -->>
Internet Exchange -- BRAS -- DSLAM / OLT --GPON-- RG

problem:
	ISP Premise: Remote management
	
Testing Methodology
	Focus on RG
Reading firmware/configuration files from board
	Multiple methods
		test clips
		In-circuit extraction
		Github --> ://<string>

Actual Study, Case 1
	Broadcom Gen 3
		Secure Boot & Root-of-trust
		FDE
	802.1x to authenticate with ISP
	Difficult to desolder/scrape traces
		BGA56
		Tight Clearance

Case 1 procrastinate on soldering
	Found discussion of Case 1 in China
	Found firmware distribution page
	Site offline
		AWS S3 -- Wayback Machine
		Retrieved another model's firmware by same vendor
	
	Needs a primitive to dump firmware & code exec
		LAN management looks safe
		....

Case 1, /bin/start_debug
	Connected --> protocal
	AAAAAAA --> protocal closed

PCE as root on device
Keys in root-of-trust, yet:
	Extracted FDE keys
	Extracted 802.1x keys
		Able to connect unauthorized equipment to fixed network --> Rouge RG/ONU

PON Transport Security($12, ITU-TG.984.3) Rouge RG/ONU - Upstream
PON Transport Security($12, ITU-TG.984.3) Rouge RG/ONU - Downstream

you can test GPON Layer and found vulnerability at there

Common problem with RG software
	Lack of hardening is common

Case 2 - cross-referencing iptables & services
	Certain IP ranges can reach management via WAN
	Only blocks ICMP Request

	how to get inside everyone's RG?
		make lan become WAN
	
	From the "provider" to your premise
		DVR -- a lot of "RCE" vulnerability(busybox)

Share bug from SDK
	Github
	SoC Vendor SDK: Un-stealthy Stealth Mode
	SoC Vendor SDK: Command Injection in CMS CLI

Summary
	Presented actual cases-
	
	Scenario 1. Proxies
	Scenario 2. Telecommunication infrastructure Takeover
	
	Mitigate?
		how to detect compromise of RGs?
			adversaries could update RG with rootkits
			No trustZone/Secure Boot to validate running firmware
		Integrity Check Canary
		
		Solution - End - users
			Employ a gateway/firewall behind RG
			Block private address range on incoming firewall
			configuration RG as "modern mode"(disable routing)
			
		For OEMs
			Detect abnormal network behavior in control plane
			Mandate baselines & standards
				Hardware-backed secure boot, proper use of trustzone
				FIPS 140-2, ISO/IEC 62443 4-2 Level >=2(**this is difficulst,cost problem**)
				EN 303 645
			apply secure coding 
		
		For SoC vendor
			OEMs may utilize SDK with volition
				employ secure coding practices
				employ defensive programming & ensure program robustness
			
![[全球固網商與網路終端設備的安全探討.m4a]]
