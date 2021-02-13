print('Please input your word:')
word = input()
word = word.casefold()
reversed_word = word[::-1]

print(reversed_word)

if word == reversed_word:
    print('Great! It is a pallindrome.')
else:
    print('LOL! It is not a pallindrome.')
