import os
import re
import requests
from urllib.parse import urlparse
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_image(url, save_path):
    try:
        logging.info(f"正在下載圖片: {url}")
        
        # 設置 HackMD 的 headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Cookie': 'connect.sid=s%3A-aGb-LwpRxSnevljLgzIYSKGsyWeXSuM.YdqdzBB9rHm9Pp%2FQsO8QbWbS2fCY1IBdUrEDyw%2BaXbw; locale=en-US; _ga_NGVZMM6DR6=GS1.1.1742618972.2.1.1742618976.56.1.2072139245; indent_type=space; keymap=sublime; loginstate=true; space_units=4; userid=cbcd0028-1957-4235-b0e8-8881e6723b52; _ga=GA1.1.1099914875.1742484672; _csrf=-QHmzpDUeYj_k4xIK7wgLiMO; _ga_ZZGGWE1BMN=GS1.1.1742484671.1.1.1742486173.27.0.0; NEXT_LOCALE=zh; g_state={"i_l":0}; aws-waf-token=5370ef28-669f-4292-bc49-25dcbe3382ca:AQoAbAZsiL88AAAA:/cbTtMXJbHDDa96PqDcD0eE4XIF87VRatNiea/s3VSPySCu0S0AAG6KMswLsohuNffV5J79nv24awUM1h90aE8rOlE5zRv6Xas4ttOBwk9Akbl2dr+6bVKSKQXzl5hjWGMiw4Cels2FcNgx98si0d4D71LtoNXm4Q00tCcBg0spBSyVA44NF0aQg; _clck=p23e40%7C2%7Cfud%7C0%7C1905'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"成功下載圖片到: {save_path}")
            return True
        else:
            logging.error(f"下載失敗，狀態碼: {response.status_code}")
            logging.error(f"回應內容: {response.text[:200]}")  # 只顯示前200個字元
    except Exception as e:
        logging.error(f"下載圖片時發生錯誤: {url}")
        logging.error(f"錯誤訊息: {str(e)}")
    return False

def extract_filename(url):
    return os.path.basename(urlparse(url).path)

def process_markdown_file(file_path):
    # 創建圖片目錄
    if not os.path.exists('images'):
        os.makedirs('images')
        logging.info("創建圖片目錄: images")
    
    # 讀取 Markdown 文件
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logging.info(f"成功讀取文件: {file_path}")
    except Exception as e:
        logging.error(f"讀取文件時發生錯誤: {file_path}")
        logging.error(f"錯誤訊息: {str(e)}")
        return
    
    # 找出所有圖片連結
    pattern = r'!\[image\]\((https://hackmd\.io/_uploads/[^)]+)\)'
    matches = list(re.finditer(pattern, content))
    logging.info(f"找到 {len(matches)} 個圖片連結")
    
    # 下載圖片並更新連結
    success_count = 0
    for match in matches:
        url = match.group(1)
        filename = extract_filename(url)
        local_path = os.path.join('images', filename)
        
        if download_image(url, local_path):
            # 更新 Markdown 中的連結
            new_link = f'![image](images/{filename})'
            content = content.replace(match.group(0), new_link)
            success_count += 1
            logging.info(f"更新連結: {url} -> {new_link}")
    
    # 寫回更新後的文件
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"成功更新文件: {file_path}")
        logging.info(f"成功下載並更新了 {success_count} 個圖片")
    except Exception as e:
        logging.error(f"寫入文件時發生錯誤: {file_path}")
        logging.error(f"錯誤訊息: {str(e)}")

if __name__ == '__main__':
    # 禁用 SSL 警告
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    process_markdown_file('MY PENETRATION NOTE.md') 