# Key Management
page. 272

## Key Management Overview
page. 273

Key Management Life Cycle

專業的金鑰 --> 要由專業的金鑰產生器產製(Key Generator)
condition: 
>金鑰長度要夠長、空間要夠大
>金耀 patern 必須隨機

random string --> Key Derivation Function, KDF --> Key

查驗金鑰產生器金鑰變數 --> 送驗
US FIS 140

Perfect Forward Secrecy, PFS
page.279

DH, Diffie-Hellman (key agreement)
>RSA目前僅用在數位簽章，
>網頁金鑰等使用RSA都具有低風險係數
>目前主流是使用DH

RSA 未來金鑰憑證會更短
--> 48 天

---
Data Sanitization and Data Remanence
page.158

Level low: 
>Clear

Level medium: 
>Purge:
>- Crypto Erase 最常運用在雲端環境
>- Degaussing( 消磁)，不一定所有的磁碟硬碟都能被消磁完全

Level High:
>Destroy

---
Public Key Infrastructure
page.181

PKI --> 可以做到憑證管理(certificate)

什麼是憑證( certificate )？
==有寫名字==的==公鑰==，就是憑證

金鑰欄位值, X509
> CN
> O
> L
> ST
> C

明正發行者
> CN
> O
> C

公鑰 --> 名字 --> 效期

什麼樣的狀況會主動註銷公鑰 --> 私鑰外洩

憑證有哪幾個基本欄位
公鑰
名字
效期
證書序列
數位簽章

能不能用
不能過期
不能被吊銷
憑證不能出問題

可以利用openssl產製憑證申請檔(CSR)



