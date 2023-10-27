import openai
openai.api_key="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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "what is phenyl"},
        {"role": "assistant", "content": ""}
    ]
)

print(response.choices[0].message["content"])
# chat_log=[]
# while True:
#     user_message = input()
#     if user_message.lower() == "quit":
#         break
#     else:
#         chat_log.append({"role": "user", "content": user_message})
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=chat_log
#         )
#         assistant_response = response['choices'][0]['message']['content']
#         print("ChatGPT:",assistant_response.strip('\n').strip())
#         chat_log.append({"role":"assistant","content": assistant_response.strip("\n").strip()})