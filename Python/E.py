message = input(">")
words = message.split(' ')  # Si lo imprimimos imprime en lista cada mensaje separado
emojis = {
    ":)": "😀",
    ":(": "😞",
}

output = ""
for word in words:
    output += emojis.get(word, word) + ""
print(output)
