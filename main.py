def cesar_cipher(text, key):
	crypted_text = ""
	
	for char in text:
		crypted_text += chr((ord(char) + key) % 1_114_112)

	return crypted_text

def cesar_uncipher(crypted_message, key):
		return cesar_cipher(crypted_message, -key)



message = "chocolat"
crypted_message = cesar_cipher(message, 531200000)
initial_message = cesar_uncipher(crypted_message, 531200000)
print(initial_message == message)