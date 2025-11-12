import string

def cesar_cipher(text, key):
	crypted_text = ""
	
	for char in text:
		crypted_text += chr((ord(char) + key) % 1_114_112)

	return crypted_text

def cesar_uncipher(crypted_message, key):
		return cesar_cipher(crypted_message, -key)


def hack_cesar_cipher(crypted_message, alphabet):

	for possible_key in range(0, 1_114_112):
		possible_uncryption = cesar_uncipher(crypted_message, possible_key)
		if possible_uncryption[0] in alphabet:
			print(possible_key)
			print(possible_uncryption)
			print("_"*20)






message = "chocolat"


crypted_message = cesar_cipher(message, 531_200_000) # exo 1

initial_message = cesar_uncipher(crypted_message, 531200000) # exo 2
print(initial_message == message)

hack_cesar_cipher(crypted_message, alphabet=string.printable) # exo3


