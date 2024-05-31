import google.generativeai as genai

GOOGLE_API_KEY=""

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

history = [
    {
        "role": "user",
        "parts": [
            {"text": "내 이름은 준용이야 기억해줘"}
        ]
    },
    
    {
        "role": "user",
        "parts": [
            {"text": "A의 이름은 우현이야 기억해줘"}
        ]
    },
    #데이터 추가 가능
]

chat = model.start_chat(history=history)

while True:
    message_text = input("입력: ")

    if message_text == "exit":
        break

    message = {
        "role": "user",
        "parts": [
            {"text": message_text}
        ]
    }

    response = chat.send_message(message)
    print("응답:")
    for part in response.parts:
        if hasattr(part, "text"):
            print(part.text)