from requests_html import HTMLSession
session = HTMLSession()

def get():
    data = []

    r = session.get("https://www.goodreads.com/user_challenges/25489329")
    progress = r.html.find(".progressText", first=True)

    my_progress = progress.text
    books_read = r.html.find(".bookCover")

    data.append(my_progress)

    for x in range(0, 5):
        data.append(books_read[x].attrs["alt"])

    return data
