import openai

openai.api_key = ""

with open("apikey.txt", "r") as f:
    openai.api_key = f.read().strip()

def get_openai_response_stream(prompt, model="gpt-4o-mini", system_prompt=None):
    """
    調用 OpenAI API 並使用流式傳輸獲取回應，支持提示工程
    :param prompt: 用戶輸入的 prompt
    :param model: 使用的模型名稱
    :param system_prompt: 系統提示，為模型提供全局上下文（可選）
    :return: 逐步生成的回應
    """
    try:
        # 構建消息列表，包含系統提示（若有）
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        # 發送 API 請求，啟用流式傳輸
        stream = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            stream=True
        )
        
        result = ""
        for chunk in stream:
            if "choices" in chunk and chunk["choices"][0]["delta"].get("content"):
                content = chunk["choices"][0]["delta"]["content"]
                print(content, end="")  # 即時輸出
                result += content
        return result
    except Exception as e:
        return f"Error: {e}"
    

def askLLM(prompt, menu):
    pre_sysprompt =  f"""
        推薦菜單裡有的東西。
        使用繁體中文回答。

        作為點餐系統助手，你需要判斷顧客問題中出現的關鍵字是屬於適合天氣、份量、價格、口味、心情、類型中的哪個：
        (1)適合天氣: 晴天、雨天、陰天、天氣冷、天氣熱、心情差。
        (2)份量: 食量小、食量大、餓、飽。
        (3)價格: 便宜、划算、貴、價格、塊、元。
        (4)口味: 酸、甜、苦、辣。 
        (5)類型: 小吃、甜點、主食、飲料。
        找到所屬類別之後，到菜單中尋找該類別與顧客問題中的關鍵字相符的品項後，推薦給顧客，其中顧客問題中的關鍵字內若有飽這個字代表要推薦小份量，顧客問題中的關鍵字內若有餓這個字代表要推薦大份量，顧客問題中的關鍵字內若有心情差代表要挑晴天。

        範例回答:
        問題: 有什麼推薦的?
        回答: 親愛的顧客您好!我們有主食、小吃、甜點及飲料四種類型的品項可供選擇，請問您有偏好什麼嗎?
        若緊接著顧客說: 都可以、隨便、都行等類似單詞，就從菜單類型這個類別中主食、小吃、甜點、飲料這四個類型各挑一個推薦給顧客。
        問題: 甜點裡有什麼推薦的嗎?
        回答: 親愛的顧客您好!甜點的部分我們有檸檬塔，它一款以檸檬為主的甜點，酸甜可口!巧克力慕斯蛋糕:滑順濃郁的巧克力慕斯，入口即化!
        若緊接著顧客說: 都可以、隨便、都行等類似單詞，就從菜單類型類別中主食、小吃、甜點、飲料這四個類型各挑一個推薦給顧客。
        根據範例回答。

        菜單：{menu} 你的任務是根據顧客的需求，從上述菜單中推薦適合的選項，且推薦的選項名稱要完整輸出。如果顧客的需求不在菜單範圍內，請明確告訴他「我們的菜單沒有相關選項」。"""
    
    system_prompt = (pre_sysprompt)

    user_prompt = prompt

    response = get_openai_response_stream(user_prompt, system_prompt=system_prompt)
    print("\n完整回應:", response)
    return response
