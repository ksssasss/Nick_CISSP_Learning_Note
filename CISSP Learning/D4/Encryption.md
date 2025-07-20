# Encryption
Symmetric and Asymmetric Cryptography, page.247

![[Pasted image 20250716102043.png]]

怎麼念？ 探討元素及其目的

雜湊、編碼 != 加密

Symmetric: 一把鑰匙
Asymmetric: 兩把鑰匙

技術面：
key pair: 兩把鑰匙，同時出廠，精心配對
兩把鑰匙的特性：互為加解密
私鑰：給自己使用的金鑰  --> 數位簽章
公鑰：給除了自己以外他人的金鑰 

用途面：
Digital Signature 數位簽章：被私鑰加密的雜湊值

數位簽章筆對：
接收者拿到我的公鑰，解密後取得簽約hash
原始合約取hash，並利用私鑰實施加密

數位簽章完成了
==身份比對==與==資料的真實性==


Symmetric & Asymmetric 互補使用

hash 好的理解： fingerprint

---

## Cipher Taxonomy
page. 250

![[Pasted image 20250716135242.png]]

凱薩加解密器
One-Time Pads

RSA --> 加密原理 --> 質因素分解
EIGnamal -->加密原理 --> 離散數學

IBM創立的演算法 -- Lucifer --> 被美國後來認證為公用的資料加密演算法 --> DES
Rijndael也是演算法的名字, 兩個比利時學者名字合併而來 --> 

為什麼 RSA金鑰肥度 相較於 AES 這麼大 --> RSA 限定質數

要了解cpu的機制，會考
32位元、64位元的差異
為什麼金鑰的長度會影響加解密的速度
就是因為cpu的位元差異，跟處理速度與暫存器處理週期習習相關

---

Confusion and Difusion
page. 256

---

ECB, Electronic Codebook Mode (only for Block Cipher)
page.266

加密  --> iv, 初始向量
hash --> salt

透過小企鵝圖片範例可以清楚了解 ECB --> iv --> CBC mode 的概念


