def text_dictionary(filename):
    from collections import Counter
    import re
    c = Counter()
    text = open(filename, "r")
    for line in text:
        line = re.findall(r'\w+', line.casefold())
        for word in line:
            c[word] += 1
    d = (dict(c))
    f= open("new_text_dictionary2.txt","w+")
    for key in sorted(d.keys()):
        f.write(f"{key} {d[key]} times\n")
    text.close()
    f.close()

#text_dictionary('C:\Users\Ivanka\PycharmProjects\homework\homework_1')


