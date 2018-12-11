from turtle import *

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3

message = input("Please enter a message: ")
newMessage = ''

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage+=newCharacter
  else:
    newMessage+=character
  
print(newMessage)