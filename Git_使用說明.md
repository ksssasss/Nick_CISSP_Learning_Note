# Obsidian Git 版本控制使用說明

## 概述
您的 Obsidian Vault 現在已經成功設定為 Git 儲存庫，並安裝了 obsidian-git 插件。這讓您可以追蹤筆記的版本變更，並在不同裝置間同步您的筆記。

## 已完成的設定

### ✅ Git 儲存庫初始化
- 已建立 `.git` 資料夾
- 已設定 Git 使用者資訊
- 已建立初始提交（包含 360 個檔案）

### ✅ .gitignore 檔案
已建立適合 Obsidian 的 `.gitignore` 檔案，排除：
- Obsidian 工作區設定檔案
- macOS 系統檔案（.DS_Store）
- 暫存檔案
- 音訊檔案（*.m4a, *.mp3 等）
- Python 虛擬環境

### ✅ obsidian-git 插件
- 插件已安裝並啟用
- 可在 Obsidian 設定中看到 "Git" 選項

## 在 Obsidian 中使用 Git

### 1. 透過 Obsidian 介面使用
1. 開啟 Obsidian
2. 前往 **設定** → **社群插件** → **Git**
3. 您會看到以下選項：
   - **Pull**：從遠端儲存庫拉取最新變更
   - **Push**：推送本地變更到遠端儲存庫
   - **Commit**：提交變更
   - **Show Status**：顯示 Git 狀態

### 2. 常用 Git 操作

#### 提交變更
1. 在 Obsidian 中編輯筆記
2. 前往 **設定** → **社群插件** → **Git**
3. 點擊 **Commit** 按鈕
4. 輸入提交訊息（例如：「更新 CISSP 學習筆記」）
5. 點擊 **Commit**

#### 推送到遠端儲存庫（如果有的話）
1. 點擊 **Push** 按鈕
2. 如果設定正確，變更會推送到遠端儲存庫

#### 拉取最新變更
1. 點擊 **Pull** 按鈕
2. 從遠端儲存庫拉取最新變更

### 3. 透過終端機使用 Git

您也可以使用終端機進行 Git 操作：

```bash
# 查看狀態
git status

# 加入所有變更
git add .

# 提交變更
git commit -m "更新筆記內容"

# 查看提交歷史
git log --oneline

# 查看特定檔案的變更
git diff 檔案名稱.md
```

## 建議的工作流程

### 每日工作流程
1. **開始工作前**：執行 `git pull` 拉取最新變更
2. **編輯筆記**：正常編輯您的筆記
3. **定期提交**：每完成一個主題或章節就提交一次
4. **結束工作前**：執行 `git push` 推送變更

### 提交訊息建議
- 使用繁體中文描述變更內容
- 保持訊息簡潔但具體
- 例如：
  - 「新增 CISSP D2 章節筆記」
  - 「更新威脅研究報告」
  - 「修正筆記格式」

## 進階設定（可選）

### 設定遠端儲存庫
如果您想要備份到 GitHub 或其他 Git 服務：

```bash
# 添加遠端儲存庫
git remote add origin https://github.com/您的使用者名稱/您的儲存庫名稱.git

# 推送到遠端
git push -u origin main
```

### 自動備份
您可以設定自動備份腳本：

```bash
#!/bin/bash
cd "/Users/nickweng/Documents/Obsidian Vault"
git add .
git commit -m "自動備份 $(date)"
git push
```

## 注意事項

1. **大型檔案**：Git 不適合追蹤大型檔案（如音訊、影片），這些檔案已在 `.gitignore` 中排除
2. **敏感資訊**：請確保不要提交包含敏感資訊的筆記
3. **定期備份**：建議定期推送到遠端儲存庫作為備份
4. **衝突解決**：如果多人協作，可能會有衝突需要手動解決

## 故障排除

### 常見問題
1. **插件無法使用**：確認插件已啟用
2. **Git 認證問題**：可能需要設定 SSH 金鑰或個人存取權杖
3. **大型檔案問題**：檢查 `.gitignore` 設定

### 有用的 Git 指令
```bash
# 查看 Git 設定
git config --list

# 查看分支
git branch

# 查看遠端儲存庫
git remote -v

# 重置最後一次提交
git reset --soft HEAD~1
```

## 結語
現在您的 Obsidian Vault 已經完全整合了 Git 版本控制！這讓您可以：
- 追蹤筆記的變更歷史
- 在不同裝置間同步
- 備份重要的筆記內容
- 協作編輯（如果需要的話）

開始享受版本控制帶來的便利吧！ 