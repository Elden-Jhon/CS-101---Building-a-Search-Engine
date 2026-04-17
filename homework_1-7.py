text = "zip that zipper till its zipped"

text2 = "if only you had a zip"

def how_zip(text):
    find_first = text.find("zip")
    if find_first != -1:
        find_second = text.find("zip", find_first + 3)
        print(find_second)
    else:
        print(-1)

how_zip(text)
how_zip(text2)