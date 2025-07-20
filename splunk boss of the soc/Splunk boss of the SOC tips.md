# Splunk Boss of the SOC tips

## 基本搜索語法與查詢結構

### 核心搜索語法

```
index=<索引名稱> sourcetype=<來源類型> <search string> | <pipe line>
```

- **索引指定**：明確指定索引可大幅提高搜索效率

```
index="botsv3" 
```

- **時間範圍設定**：使用relative time修飾符

```
earliest=-24h latest=now
```

- **布林運算符**：結合多個條件

```
"error" AND "database"
"attack" OR "breach"
```


### 關鍵字段提取與過濾

```
index="botsv3" sourcetype="windows:security" EventCode=4625 OR EventCode=4624
```


## 常用SPL命令詳解

### 基礎統計與分析命令

- **stats**：計算統計數據，尤其適合找出異常行為

```
index="botsv3" sourcetype="windows:security" | stats count by EventCode, user
```

- **table**：以表格形式呈現選定字段

```
index="botsv3" | table _time, source, user, action
```

- **top/rare**：找出最常見/最罕見的值

```
index="botsv3" | top limit=10 src_ip
index="botsv3" | rare limit=10 dest_ip
```


### 過濾與修改命令

- **where**：基於條件過濾結果

```
index="botsv3" | where count > 5 AND user!="admin"
```

- **eval**：創建或修改字段

```
| eval risk_score=case(count>10, "高", count>5, "中", true(), "低")
```

- **rex**：使用正則表達式提取字段

```
| rex field=request "(?<page>[^/]+)$"
```

- **dedup**：移除重複結果

```
| dedup user_id
```


### 高級分析命令

- **transaction**：關聯多個事件

```
| transaction user maxspan=1h
```

- **map**：執行嵌套搜索，特別適合追蹤攻擊鏈

```
| map search="search index=botsv3 user=$user$ | stats count"
```

- **join**：合併多個搜索結果

```
| join user [search index=botsv3 sourcetype=auth]
```


## BOTS比賽常見題型與解題思路

### 事件關聯分析

APT攻擊場景是BOTS中最具挑戰性的部分，需要識別完整的攻擊鏈：

```
index="botsv3" "lateral movement" OR "privilege escalation" OR "data exfiltration" 
| stats count by technique, src_ip, dest_ip
```


### 惡意網絡流量檢測

識別可疑的網絡連接和數據傳輸：

```
index="botsv3" sourcetype="firewall*" 
| stats dc(dest_port) as port_count dc(dest_ip) as ip_count by src_ip
| where port_count>500 OR ip_count>500
```


### 帳戶暴力破解檢測

識別多次登入失敗後成功的帳戶：

```
index="botsv3" (EventCode=4625 OR EventCode=4624) 
| bin span=1m _time
| stats count, dc(EventCode) as EventCodeDC, values(EventCode) as EventCode by _time, Account_Name
| where count > 3
```


### 惡意軟體/勒索軟體檢測

```
index="botsv3" sourcetype="endpoint*" 
| stats count by process_name, file_hash
| sort -count
```


## Competition tips

### Time managements

1. **快速索引資料**：使用`| stats count by sourcetype`找出所有資料來源
2. **明確時間範圍**：縮小時間範圍以提高搜索速度

### Problem-solving framework

1. **確定目標**：理解問題需要找出什麼（如惡意IP、攻擊類型等）
2. **識別數據源**：確定相關的索引和sourcetype
3. **細化搜索**：使用字段和過濾條件縮小範圍
4. **統計分析**：利用統計命令找出異常
5. **驗證結果**：交叉引用多個數據源確認發現

### Common trap warnings

- **避免過度篩選**：確保勾選"無事件取向"(No Event Sampling)選項
- **APT場景難點**：從參賽經驗來看，找到攻擊入口點最具挑戰性
- **不忽視彩蛋題目**：根據的經驗，彩蛋題目常考察參賽者對前面題目內容的記憶


# Statistical table & Dashboard tips

## 一、基礎查詢與統計

**1. 查詢所有 index 或 source**

```splunk
* | stats count by index
* | stats count by source | sort -count | head 10
```

用於初步了解有哪些資料來源。

**2. 事件數量統計**

```splunk
index=botsv1 | stats count by sourcetype
```

快速掌握各類型事件的分布。

---

## 二、常用統計指令與進階分析

**1. tstats 優化加速查詢**

```splunk
| tstats count FROM datamodel=Endpoint.Processes 
  WHERE (Processes.process_name=cmd.exe OR Processes.process_name=powershell.exe) 
  BY _time span=1h Processes.parent_process_name
```

利用加速資料模型，極速統計特定進程的啟動情況。

**2. 進程關聯分析**

```splunk
index=botsv1 sourcetype=XmlWinEventLog:Microsoft-Windows-Sysmon/Operational EventCode=1 
| stats count by host, process_path, parent_process_name 
| where count > 5
```

找出異常父子進程關係，偵測可疑行為。

---

## 三、網路與威脅偵測

**1. DNS 可疑查詢**

```splunk
index=botsv1 sourcetype=stream:dns 
| search query=*coin* OR query=*pool* 
| stats count by query, query_type 
| sort -count
```

檢查是否有挖礦或 C2 相關的 DNS 請求。

**2. 非標準埠位流量**

```splunk
index=botsv1 dest_port IN (1337,31337,4444) 
| stats count by src_ip, dest_ip, dest_port 
| eval port_type=case(dest_port=1337,"LEET", dest_port=31337,"ELITE", 1=1,"SUSPECT") 
| sort -count
```

找出橫向移動或特殊攻擊流量。

---

## 四、檔案與帳號異常行為偵測

**1. 多主機檔案異動**

```splunk
index=botsv1 (sourcetype=linux_secure OR sourcetype=WinRegistry) 
  (file_path=*/tmp/* OR file_path=*Temp*) 
| stats dc(host) as affected_hosts by file_name, file_hash 
| where affected_hosts > 1
```

偵測多主機同時異動同一檔案，常見於勒索軟體攻擊。

**2. 登入失敗異常（暴力破解）**

```splunk
index=botsv1 sourcetype=linux_secure "authentication failure" 
| timechart span=5m count 
| eventstats avg(count) as avg stdev(count) as stdev 
| eval threshold=avg+(3*stdev) 
| where count > threshold
```

用統計異常值快速偵測暴力破解行為。

---

## 五、威脅情報與行為基線

**1. 威脅情報比對**

```splunk
index=botsv1 dest_ip=* 
| lookup threat_feeds.csv ip as dest_ip 
| search threat_type=* 
| stats count by dest_ip, threat_type, dest_port
```

將內部流量與外部威脅情報進行關聯。

**2. 使用者行為異常分析**

```splunk
index=botsv1 user=* 
| bin _time span=1h 
| stats dc(eventtype) as event_types, values(sourcetype) as sources by user 
| outlier action=filter method=stdev threshold=3 field=event_types
```

建立行為基線，偵測異常帳號活動。

---

## 六、效能與儀表板最佳化

**1. 搜尋加速與時間序列圖**

```splunk
| tstats summariesonly=t prestats=t count 
  FROM datamodel=Network_Traffic 
  WHERE (dest_port=443 OR dest_port=80) 
  BY _time span=1h 
| timechart span=1h sum(count)
```

利用 summariesonly 與時間分桶，快速產生流量趨勢圖。

---

## Competition tips

- 優先熟悉 `tstats`、`stats`、`timechart`、`eventstats`、`lookup` 等指令。
- 多利用資料模型與 summariesonly 加速查詢。
- 針對不同場景（APT、勒索、橫向移動、暴力破解）預先準備常用查詢片段。
- 透過統計異常值（如 3σ）自動過濾雜訊，聚焦可疑事件。

# Yuanta training presentation

## 顯示最常見客戶作業系統平台
~~~splunk
sourcetype=access_comined | top limit=5 platform
~~~

## 建立一個顯示一段時間內最常失敗的網頁瀏覽器圖表
~~~splunk
status>=400 | timechart count by useragent limit=5 useother=f
~~~

## 機器學習ML的預測功能
~~~splunk
action=purchase | timechart count span=5m | predict count future_timespan=24
~~~
- span=5m --> 將時間範圍劃分爲5分鐘的「跨度」
- predict count future_timespan=24 預測24個跨度

## 使用 lookup 命令，延伸既有資料，生成新欄位
~~~splunk
<your search> | lookup product_codes.csv product_id as product_id
~~~
- lookup --> 可即時對應查閱表格
- ***.csv 為Splunk的查閱表格名稱

## 透過iplocation和geostats命令取得地理位置資訊
~~~splunk
<your search> | iplocation clientip | geostats count by <field>
~~~
### 延伸可加入搜尋過濾條件
~~~splunk
sourcetype=access_combined | iplocation clientip | search Country!="United States" | geostats count by City
~~~

## 利用 fields 進行欄位篩選
### 把需要的欄位抓出來，增加搜尋效能
~~~splunk
index=web sourcetype=access_* prouctName=*
| fields product_name, product_price
| eval difference = proudct_price -5
| table product_name, product_price, difference
~~~
### 去除不需要欄位
~~~splunk
index=web sourcetype=access_*
| top product_name
| fields - percent
~~~
