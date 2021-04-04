import re
# abcd, book, desk
# ca?e
#care, cafe, case, cave

p = re.compile("ca.e") #.: 하나의 문자를 의미
# ^(^de) : 문자열의 시작
# $ (se$) :문자열의 끝 > 


    if m:
def print_match(m):
        print("m.group():", m.group())
        print("m.string:", m.string)
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")

        print("매칭되지 않음")
        print("매칭되지 않음")

# m = p.match("careless ")
# print_match(m)

# m = p.search("good care")
# print_match(m)

lst = p.findall("good care cafe")
print(lst)