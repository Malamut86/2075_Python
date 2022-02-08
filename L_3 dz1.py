phone_words = input('число: ')
numbered_words = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
output = ""

for ch in phone_words:
    output += numbered_words.get(ch, "!") + " "
phone_words = numbered_words
print(output)

