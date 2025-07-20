
# 1. 密碼學研究(cryptology)口訣為何？請簡述之。傳統密碼學跟當代密碼學最大的差別為何？

1.1 密碼學研究(cryptology)口訣為何？請簡述之。
Answer：
- 一大研究：Cryptology 密碼學研究
- 二大學問：密碼學、破密學
- 三大重點(破密學(攻擊))： 情境、弱點、攻擊技巧
- 四大技術(密碼學(防禦))： 加密、雜湊、DS、MAC

1.2 傳統密碼學跟當代密碼學最大的差別為何？
Answer：
根據筆記，主要差別在於：
- 傳統密碼學：使用較簡單的加密方式，如凱薩加解密器
- 當代密碼學：使用複雜的演算法，如AES、RSA、SHA等，且考慮量子電腦威脅，NIST建議選用新的演算法

---
# 2. 加密(encryption)技術要怎麼唸？請簡述加密的重點觀念

2.1 加密(encryption)技術要怎麼唸？請簡述加密的重點觀念
Answer：
根據筆記，加密技術的重點觀念：
- 探討元素及其目的
- 雜湊、編碼 != 加密
- 對稱式：一把鑰匙
- 非對稱式：兩把鑰匙
- 數位簽章：被私鑰加密的雜湊值，完成身份比對與資料的真實性

---
# 3. 請說明【非對稱式加密】所採用之金鑰對(key pair)的技術特性及用途，並【比較】對稱及非對稱式加密技術的差異

3.1 請說明【非對稱式加密】所採用之金鑰對(key pair)的技術特性及用途
Answer：
根據筆記，金鑰對的特性：
- 兩把鑰匙同時出廠，精心配對
- 兩把鑰匙互為加解密
- 私鑰：給自己使用的金鑰，用於數位簽章
- 公鑰：給除了自己以外他人的金鑰

3.2 請【比較】對稱及非對稱式加密技術的差異
Answer：
根據筆記：
- 對稱式：一把鑰匙
- 非對稱式：兩把鑰匙
- 兩者互補使用

---
# 4. 請列出上課提到的加解密器(cipher)、雜湊(hash)、訊息驗證代碼(MAC)及數位簽章的標準或演算法(共8個)

4.1 請列出上課提到的加解密器(cipher)、雜湊(hash)、訊息驗證代碼(MAC)及數位簽章的標準或演算法(共8個)
Answer：
根據筆記：
1. AES (Advanced Encryption Standard) - 加密
2. SHA-2 (SHA256) - 雜湊
3. SHA-3 - 雜湊
4. HMAC - MAC
5. CBC-MAC - MAC
6. DSA (Digital Signature Algorithm) - 數位簽章
7. RSA (Rivest-Shamir-Adleman) - 數位簽章
8. ECDSA (Elliptic Curve Digital Signature Algorithm) - 數位簽章

---
# 5. 金鑰管理怎麼唸？金鑰生成及銷毁階段要注意那些議題？

5.1 金鑰管理怎麼唸？金鑰生成及銷毁階段要注意那些議題？
Answer：
根據筆記，金鑰管理重點：
- 專業的金鑰要由專業的金鑰產生器產製
- 金鑰長度要夠長、空間要夠大
- 金鑰pattern必須隨機
- 銷毁階段：使用Data Sanitization，分為Clear、Purge、Destroy三個等級

---
# 6. 何謂憑證(certificate)？上課提到那些憑證的基本欄位？一個有效的憑證必須滿足那三個條件？請說明X.500及X.509這二個標準的用途

6.1 何謂憑證(certificate)？上課提到那些憑證的基本欄位？
Answer：
根據筆記，憑證是有寫名字的公鑰，基本欄位包括：
- 公鑰
- 名字
- 效期
- 證書序列
- 數位簽章

6.2 一個有效的憑證必須滿足那三個條件？
Answer：
根據筆記，三個條件：
- 不能過期
- 不能被吊銷
- 憑證不能出問題

6.3 請說明X.500及X.509這二個標準的用途
Answer：
根據筆記，X.509是憑證標準，包含欄位值如CN、O、L、ST、C等

---
# 7. 請比較編碼(encoding)、加密(encryption)及雜湊(hash)三者的差異

7.1 請比較編碼(encoding)、加密(encryption)及雜湊(hash)三者的差異
Answer：
根據筆記，雜湊、編碼 != 加密，雜湊可以理解為fingerprint

---
# 8. 請比較Nonce、鹽巴(salt)與初始向量(initialization vector)三者的差異

8.1 請比較Nonce、鹽巴(salt)與初始向量(initialization vector)三者的差異
Answer：
根據筆記，加密使用iv（初始向量），hash使用salt（鹽巴）

---
# 9. 講義提到的使用者密碼儲存形式有那四種？

9.1 講義提到的使用者密碼儲存形式有那四種？
Answer：
根據筆記，密碼儲存形式：
1. Raw Passwords
2. Encrypted Passwords
3. Hashed Passwords
4. Salted Passwords

---