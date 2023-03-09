message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😃",
    ":-)": "😃",
    ":(": "😥",
    ":-(": "😥"
}

OUTPUTSTRING = ""

for word in words:
    OUTPUTSTRING += emojis.get(word, word) + " "

print(OUTPUTSTRING)
