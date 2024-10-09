matches = {"(": ")",
           "[": "]",
           "{": "}",
           "<": ">"}

opened = []

s = input()

ans = True

for character_index in range(len(s)):
    if s[character_index] in matches.keys():
        opened.append(s[character_index])
    elif len(opened) != 0 and s[character_index] == matches[opened[-1]]:
        opened.pop()
    else:
        ans = (False, character_index + 1)
        break

if len(opened) != 0 and ans == True:
    ans = (False, len(s))

if ans == True:
    print(ans)
else:
    print(ans[0], ans[1])