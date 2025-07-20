
# 1. 密碼學研究(cryptology)口訣為何？請簡述之。傳統密碼學跟當代密碼學最大的差別為何？

1.1 密碼學研究(cryptology)口訣為何？請簡述之。
Answer：
- 一大研究：密碼學研究 Cryptology
- 二大學問：
	- 密碼學 Cryptography
	- 破密學 Cryptanalysis
- 三大重點(破密學(攻擊))：
	- 情境
	- 弱點
	- 攻擊技巧
- 四大技術(密碼學(防禦))： 
	- 加密 Encryption
	- 雜湊 HASH
	- 數位簽章 DS, Digital Signature
	- 訊息驗證代碼 MAC, Message Authentication Code

1.2 傳統密碼學跟當代密碼學最大的差別為何？
Answer：
- 傳統密碼學：使用較簡單的加密方式，如凱薩加解密器，且將密文、演算法、金鑰均視為「秘密」
- 當代密碼學：使用具複雜度的演算法，如AES、RSA、SHA等，僅將「金鑰」視為秘密

---
# 2. 加密(encryption)技術要怎麼唸？請簡述加密的重點觀念

2.1 加密(encryption)技術要怎麼唸？請簡述加密的重點觀念
Answer：
探討元素及其目的
- 明文 Plain text
- 演算法 Cipher 
- 金鑰 Key
- 密文 Cipher text

重點觀念
- 雜湊、編碼 != 加密
- 對稱式：一把鑰匙
- 非對稱式：兩把鑰匙
- 數位簽章：被私鑰加密的雜湊值，完成身份比對與資料的真實性

---
# 3. 請說明【非對稱式加密】所採用之金鑰對(key pair)的技術特性及用途，並【比較】對稱及非對稱式加密技術的差異

3.1 請說明【非對稱式加密】所採用之金鑰對(key pair)的技術特性及用途
Answer：
金鑰對 key pair 特性：
- 兩把鑰匙同時出廠，精心配對
- 兩把鑰匙互為加解密
- 私鑰：給自己使用的金鑰，用於數位簽章
- 公鑰：給除了自己以外他人的金鑰

3.2 請【比較】對稱及非對稱式加密技術的差異
Answer：
1. 金鑰特性
	- 對稱式：一把鑰匙
	- 非對稱式：兩把鑰匙
2. 運算速度
	- 對稱式：效率高速度快
	- 非對稱式：超級無敵慢
3. 資料大小
	- 對稱式：沒限制
	- 非對稱式：運用於512位元以下(運算效率很差)
4. 應用情景
	- 對稱式：需要資料加密的情境廣泛利用
	- 非對稱式：金鑰交換＆數位簽章
5. 數學原理
	- 對稱式：布林值計算
	- 非對稱式：質因數分解、離散對數和橢圓曲線

---
# 4. 請列出上課提到的加解密器(cipher)、雜湊(hash)、訊息驗證代碼(MAC)及數位簽章的標準或演算法(共8個)

4.1 請列出上課提到的加解密器(cipher)、雜湊(hash)、訊息驗證代碼(MAC)及數位簽章的標準或演算法(共8個)
Answer：

- 加解密器(cipher)
	1. DES (Data Encryption Standard)
	2. AES (Advanced Encryption Standard)
- 雜湊(hash)
	1. MD5
	2. SHA-2, SHA-3
- 訊息驗證代碼(MAC)
	1. HMAC
	2. CBC-MAC
- 數位簽章(DS)
	1. DSA (Digital Signature Algorithm) 
	2. RSA DSA (Rivest-Shamir-Adleman) 
	3. EC DSA (Elliptic Curve Digital Signature Algorithm) 

---
# 5. 金鑰管理怎麼唸？金鑰生成及銷毁階段要注意那些議題？

5.1 金鑰管理怎麼唸？
Answer：

了解金鑰的生命週期：
- 生成 generation
- 儲存 Storage
- 分發 Exchange & Distribution
- 使用 Usage
- 輪替 Rotation
- 銷毀 Destruction

5.2 金鑰生成及銷毁階段要注意那些議題？
Answer：

金鑰生成
- 專業的金鑰要由專業的金鑰產生器產製
- 金鑰長度要夠長、空間要夠大
- 金鑰pattern必須具備足夠的隨機性
金鑰銷毀
- 刪除所有痕跡，使其無法透過實體＆電子方式恢復
- Crypto-erase：加一層保險，使用Data Sanitization使加密資料更難以被恢復，分為三個等級：
	- Clear
	- Purge
	- Destroy

---
# 6. 何謂憑證(certificate)？上課提到那些憑證的基本欄位？一個有效的憑證必須滿足那三個條件？請說明X.500及X.509這二個標準的用途

6.1 何謂憑證(certificate)？
Answer：
==有寫名字==的==公鑰==，就是憑證

6.2 上課提到那些憑證的基本欄位？
Answer：
- 名字
- 公鑰
- 簽發者訊息
- 效期
- 證書序列
- 數位簽章

6.3 一個有效的憑證必須滿足那三個條件？
Answer：

- 憑證來源是否可信，能不能用
- 憑證的有效性，有沒有過期
- 憑證名字有無相符，不能被吊銷

6.4 請說明X.500及X.509這二個標準的用途
Answer：

- X.500 目錄服務標準：由ISO及ITU-T訂定的網路標準，主要用於「電子目錄服務」，可以理解成一個結構化、分層式的全球資訊電話簿，用於儲存並查詢個人、組織、資源等各種資訊
- X.509 為 X.500 標準的一部分，X.509 專門定義了數位憑證的格式與結構，如CN, O, S ,C等欄位值

---
# 7. 請比較編碼(encoding)、加密(encryption)及雜湊(hash)三者的差異

7.1 請比較編碼(encoding)、加密(encryption)及雜湊(hash)三者的差異
Answer：
首先核心觀念，雜湊、編碼 != 加密
- 編碼(encoding)目的：確保資料能被不同系統正確讀取與處理，目的在於資料格式的轉換
- 加密(encryption)目的：保護資料的機密性，防止未授權讀取（擁有金鑰才能解密）
- 雜湊(hash)目的：驗證資料的完整性，確保資料有無被修改，可以理解成fingerprint

---
# 8. 請比較Nonce、鹽巴(salt)與初始向量(initialization vector)三者的差異

8.1 請比較Nonce、鹽巴(salt)與初始向量(initialization vector)三者的差異
Answer：

- Nonce：只用於一次性驗證的隨機性數值，經典案例如 OAuth
- 鹽巴(salt)：使用於「HASH」演算法，透過加入隨機的鹽值再進行雜湊，避免彩虹表＆預計算攻擊
- 初始向量(initialization vector)：使用於「加密」演算法，透過固定長度的隨機值，加入加密的過程來增加隨機性，主要的運用模板有 CBC, OFB, CFB, &CTR

---
# 9. 講義提到的使用者密碼儲存形式有那四種？

9.1 講義提到的使用者密碼儲存形式有那四種？
Answer：

Password at rest:
1. Raw Passwords
2. Encrypted Passwords
3. Hashed Passwords
4. Salted Passwords

---