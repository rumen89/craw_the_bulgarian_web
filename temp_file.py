from bs4 import BeautifulSoup
import requests
from collections import deque

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# res = []

# r = requests.get("http://register.start.bg/")

# html_doc = r.text
# soup = BeautifulSoup(html_doc, 'html.parser')

# queue = deque()


# for link in soup.find_all('a'):
#     # r1 = requests.get(link.get('href'))
#     # res.append(r1.headers['server'])
#     addr = link.get('href')
#     if addr is not None and addr != '#top' and 'javascript' not in addr and\
#        addr != 'rss.php':
#         if addr[0] == 'l':
#             addr = 'http://start.bg/' + addr
#         elif addr[0] == '/':
#             addr = 'http://start.bg' + addr
#         res.append(addr)

# count = 0
# for item in res:
#     count += 1
#     print(item)
# print(count)
# # for link in res:
# #     try:
# #         if 'http' in link and '.bg' in link:
# #             print('====={}====='.format(link))
# #             r1 = requests.get(link)
# #             print(r1.headers['Server'])
# #     except:
# #         print("Not a site: {}".format(link))


def bfs(item):
    count = 0
    queue = deque()
    visited = {}

    queue.append(item)
    visited[item] = 1
    count += 1

    while len(queue) > 0:
        current_link = queue.popleft()
        r = requests.get(current_link)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):
            addr = link.get('href')

            if addr is not None and addr != '#top' and 'javascript' not in addr and\
               addr != 'rss.php' and '.bg' in addr:
                if addr[0] == 'l':
                    addr = 'http://start.bg/' + addr
                elif addr[0] == '/':
                    addr = 'http://selftart.bg' + addr
                elif 'http://' not in addr and '.bg' in addr:
                    addr = 'http://' + addr
                if addr not in visited:
                    visited[addr] = 1
                    queue.append(addr)
                    count += 1
    return (count, visited)

all = bfs('http://start.bg/link.php?id=65005')

sites = all[1]
counter = all[0]

for site in sites:
    print(site)
print(counter)
