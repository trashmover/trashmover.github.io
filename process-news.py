f = open("news.txt", "r")
content = f.readlines()
for i in range(len(content)):
    cur = content[i][len(str(i)) + 1:-1]
    print("<li>" + cur + "</li>")
