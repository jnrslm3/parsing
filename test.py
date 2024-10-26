from bs4 import BeautifulSoup

file = open ("index.html", "r", encoding="utf-8")
html = file.read()

soup = BeautifulSoup(html, "html.parser")

main_content = soup.find("div", class_="main-content")

menu = main_content.find("div", class_="menu")

words = menu.find_all("p", class_='navigator')
for word in words:
    print(word.text)

main = soup.find("div", class_="main")
post1 = main.find_all("div", class_="post")

for post in post1:
    h1= post.find ("h1")
    print(h1.text)
    p = post.find("p")
    print(p.text)

footer = soup.find("div", class_="footer")
box = footer.find_all("div", class_="box")

for boxes in box:
    p = boxes.find("p")
    for i in boxes:
        a = i.find("a")
        print(i.text)
