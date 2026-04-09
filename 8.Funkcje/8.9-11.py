#8.9
print("8.9")

messages = ['Witaj mariuszku!', 'Cześć bobi!', 'Siema eniu!', 'Witamy na bagnie!']

def show_messages(messages):
	for message in messages:
		print(message)

show_messages(messages)


#8.10
print("\n8.10")

def show_messages(messages):
	"""Wyświetla wszystkie komunikaty znajdujące się na liście"""
	print("Pokazuje wszystkie komunikaty:")
	for message in messages:
		print(message)


def send_messages(messages, sent_messages):
	print("\nWysyłam wszystkie komunikaty:")
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)


messages = ['Witaj mariuszku!', 'Cześć bobi!', 'Siema eniu!', 'Witamy na bagnie!']
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinalne listy:")
print(messages)
print(sent_messages)


#8.11
print("\n8.11")

def show_messages(messages):
	"""Wyświetla wszystkie komunikaty znajdujące się na liście"""
	print("Pokazuje wszystkie komunikaty:")
	for message in messages:
		print(message)


def send_messages(messages, sent_messages):
	print("\nWysyłam wszystkie komunikaty:")
	while messages:
		current_message = messages.pop(0)
		print(current_message)
		sent_messages.append(current_message)


messages = ['Witaj mariuszku!', 'Cześć bobi!', 'Siema eniu!', 'Witamy na bagnie!']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinalne listy:")
print(messages)
print(sent_messages)