import string

Phrase = input("Enter your phrase: ")

if Phrase.find("[") == 0 and Phrase.find("]") == len(Phrase) - 1:
    s = []
    for x in Phrase:
        if x != "," and x != " " and x != "[" and x != "]":
            s.append(x)
    print(s)

else:
    pass

letters = string.ascii_letters
digits = string.digits
count_digit = 0
B = True
for i in Phrase:
    for x in letters:
        if Phrase.find(x) != -1:
            print(str(Phrase))
            B = False
            break
    if B == False:
        break
    for x in digits:
        if i == x:
            count_digit += 1
    if count_digit == len(Phrase):
        print(int(Phrase))
    

    
