import subprocess
import os
from transformers import pipeline
import soundfile as sf
from tqdm import tqdm
import numpy as np
import time

def convert_m4a_to_wav(m4a_path):
    wav_path = m4a_path.replace('.m4a', '.wav')
    command = ['ffmpeg', '-i', m4a_path, '-acodec', 'pcm_s16le', '-ar', '16000', wav_path]
    subprocess.run(command, check=True)
    return wav_path

def transcribe_audio(audio_path):
    # 檢查是否為 M4A 文件
    if audio_path.endswith('.m4a'):
        print("正在轉換音頻格式...")
        wav_path = convert_m4a_to_wav(audio_path)
        try:
            print("正在載入模型...")
            # 載入更大的 Whisper 模型
            pipe = pipeline("automatic-speech-recognition", 
                          model="openai/whisper-large-v3",
                          return_timestamps=True)
            
            print("正在讀取音頻文件...")
            # 讀取音頻文件
            audio_data, sample_rate = sf.read(wav_path)
            
            # 計算音頻總長度（秒）
            total_duration = len(audio_data) / sample_rate
            print(f"音頻總長度：{total_duration:.2f}秒")
            
            print("開始轉錄...")
            start_time = time.time()
            
            # 轉錄音頻，使用 generate_kwargs 來指定語言
            result = pipe(audio_data, generate_kwargs={"language": "zh"})
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"轉錄完成！耗時：{elapsed_time:.2f}秒")
            
            # 生成輸出文件名
            output_file = audio_path.replace('.m4a', '_transcript.txt')
            
            print("正在保存結果...")
            # 將結果保存到文件
            with open(output_file, 'w', encoding='utf-8') as f:
                # 直接寫入轉錄文本
                if isinstance(result, dict) and "text" in result:
                    f.write(result["text"])
                else:
                    print("警告：轉錄結果格式不正確")
                    print("原始結果：", result)
            
            print(f"結果已保存到：{output_file}")
            
        finally:
            # 清理臨時 WAV 文件
            if os.path.exists(wav_path):
                os.remove(wav_path)
    else:
        print("請提供 M4A 格式的音頻文件")

if __name__ == "__main__":
    audio_file = "Recording 20250416123351.m4a"
    try:
        transcribe_audio(audio_file)
    except Exception as e:
        print(f"發生錯誤：{str(e)}") 