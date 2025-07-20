import os
import openai

def transcribe_audio(audio_file):
    try:
        # 開啟音訊檔案
        with open(audio_file, "rb") as audio:
            # 使用 Whisper API 轉換音訊為文字
            transcript = openai.Audio.transcribe(
                file=audio,
                model="whisper-1",
                language="zh"
            )
            return transcript.text
    except Exception as e:
        print(f"轉換過程發生錯誤：{str(e)}")
        return ""

def main():
    # 設定 OpenAI API 金鑰
    openai.api_key = "YOUR_API_KEY"  # 請替換成您的 OpenAI API 金鑰
    
    # 指定音訊檔案路徑
    audio_file = "Recording 20250416123351.m4a"
    
    # 轉換音訊為文字
    print("正在轉換音訊為文字...")
    text = transcribe_audio(audio_file)
    
    if text:
        # 建立輸出檔案名稱
        output_file = os.path.splitext(audio_file)[0] + '_transcript.txt'
        
        # 將文字寫入檔案
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"轉換完成！文字已儲存至 {output_file}")
    else:
        print("轉換失敗，請檢查錯誤訊息。")

if __name__ == "__main__":
    main() 