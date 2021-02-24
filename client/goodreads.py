from requests_html import HTMLSession
session = HTMLSession()

r = session.get("https://www.goodreads.com/user_challenges/19364921")
progress = r.html.find(".progressText", first=True)

print("Goodreads")
print(progress.text)

books_read_recent = r.html.find(".bookCover")

print("Recently Read")

for x in range(0, 3):
        print(books_read_recent[x].attrs["alt"])
