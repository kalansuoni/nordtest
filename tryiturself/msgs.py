def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


text_messages = [
    "Hello!",
    "How are you?",
    "See you later.",
    "Good luck!",
    "Have a great day!"
]

sent_messages = []


send_messages(text_messages[:], sent_messages)

print("\nOriginal list:")
print(text_messages)

print("\nSent messages:")
print(sent_messages)