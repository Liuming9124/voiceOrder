import openai
import base64

with open("apikey.txt", "r") as f:
    openai.api_key = f.read().strip()

def transcribe_audio_from_base64(base64_audio, language="zh", prompt=None, response_format="text"):
    """
    Transcribes an audio file from a Base64 string using OpenAI Whisper.

    Args:
        base64_audio (str): Base64-encoded audio file content.
        language (str): The language of the audio (e.g., "zh" for Chinese).
        prompt (str, optional): Contextual prompt to guide transcription.
        response_format (str): Format of the response ("text", "json", or "verbose_json").

    Returns:
        str or dict: The transcription in the specified format.
    """
    try:
        # 將 Base64 解碼為音訊檔案
        audio_data = base64.b64decode(base64_audio)
        with open("temp_audio.m4a", "wb") as temp_file:
            temp_file.write(audio_data)
        
        # 使用 OpenAI Whisper 進行轉錄
        with open("temp_audio.m4a", "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file,
                response_format=response_format,
                language=language,
                prompt=prompt,
            )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    with open("audio.txt", "r") as f:
        base64_audio = f.read().strip()

    # 設定語言為中文
    language = "zh"
    prompt = "請將以下音訊轉錄為中文文本。"
    response_format = "text"

    # 轉錄音訊
    response = transcribe_audio_from_base64(base64_audio, language, prompt, response_format)

    # 輸出轉錄結果
    print("轉錄結果：")
    print(response)
