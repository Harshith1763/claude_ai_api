import anthropic
import os


client = anthropic.Anthropic(
    api_key=os.environ.get('API_KEYS')
)


ask = input("ask me anything :-  ")
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=500,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": ask}
    ]
)

print(message.content)
