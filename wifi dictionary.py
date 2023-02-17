import itertools as its
words = "1234567890abcdefghijklmnopqrstuvwxyz"
r =its.product(words,repeat=8)
dic = open("pwd.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()    