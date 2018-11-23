string = input()
answer = ''
for ch in string:
    if ch.isupper():
        answer += ch.lower()
    elif ch.islower():
        answer += ch.upper()
    else:
        answer += ch
print(answer)