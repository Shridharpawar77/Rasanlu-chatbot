from actions_1 import get_response

while True:
	request = input('you: ')
	response = get_response(request)
	print('Bot: ', response)
