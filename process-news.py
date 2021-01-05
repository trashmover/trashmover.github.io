# get date
from datetime import date
today = date.today().strftime("%Y%m%d")
today_dash = date.today().strftime("%Y-%m-%d")

# copy prev day
import os
os.system("cp index.html %s.html" %today)
os.system("mv %s.html ./archives/" %today)

# add history
archives = open('./archives/archives.html').readlines()
newline = "\t<li><a href=\"./%s.html\">%s</a></li>\n" %(today, today_dash)
archives.insert(21, newline)

file = open('./archives/archives.html', "w")
for line in archives:
    file.write(line)

file.close()

# write new day
f = open("news.txt", "r")
content = f.readlines()
clean_content = []

for cur in content:
    if cur != '\n':
        clean_content.append(cur.strip())


template = open("template.html").readlines()
index = open('index.html', 'w')

for line in template[:26]:
    index.write(line)

for i in range(len(clean_content)):
    cur = clean_content[i][len(str(i+1)) + 1:][0:]
    index.write("<li>" + cur + "</li>\n")

for line in template[26:]:
    index.write(line)

index.close()

'''
from googletrans import Translator
translator = Translator()

for i in range(len(clean_content)):
    cur = clean_content[i][len(str(i+1)) + 1:][0:]
    cur = translator.translate(cur)
    print("<li>" + cur.text + "</li>")
'''
