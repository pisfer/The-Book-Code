import re

file = open("data\in.bc", "rb")
out_file = open("data\output.bc", "w")
ss = file.readline().decode("utf-8")
costa = file.tell()
t = re.match(r'<intype="bc" wat="(?P<text>[\w\d]+)">', ss)

page = "12"
row = 0
place = 0
chek = False
output = ""
data = []  # data of past objects
if t:
    big_word = list(t.group("text"))
    for code in big_word:
        print(code, "----")
        for line in file.readlines():
            row += 1
            for word in list(line.decode().translate({ord("\r"): None, ord("\n"): None})):
                place += 1
                aword = word + page + "." + str(row) + "." + str(place) + ";"
                # print(word, code, word == code, aword if word == code else "None")
                if word == code and aword not in data:
                    data.append(aword)
                    chek = True
                    break
            place = 0
            if chek:
                chek = False
                break
        file.seek(costa)
        row = 0

file.seek(costa)
print(data)
for u in data: output += u[1::] + " "
out_file.write('<intype="bc" code="' + output + '">')
out_file.write("\n")
for l in file.readlines():
    out_file.write(l.decode().translate({ord("\r"): None}))
out_file.close()
file.close()
