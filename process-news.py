f = open("news.txt", "r")
content = f.readlines()
clean_content = []

for cur in content:
	if cur != '\n':
		clean_content.append(cur.strip())


for i in range(len(clean_content)):
    cur = clean_content[i][len(str(i+1)) + 1:][2:]
    print("<li>" + cur + "</li>")


from googletrans import Translator
translator = Translator()

for i in range(len(clean_content)):
    cur = clean_content[i][len(str(i)) + 1:][2:]
    cur = translator.translate(cur)
    print("<li>" + cur.text + "</li>")
