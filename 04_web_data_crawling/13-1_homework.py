from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


# url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=11035&target=after&page=2"
# page = urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
# print(soup.title)

# #한 개 페이지 가져오기
# comment_all = soup.find_all('td', class_='title')
# print(len(comment_all))
#
# comments = []
# for one in comment_all:
#     temp = list(one.children)[6].strip()
#     # print(temp)
#     # comments.append(temp)
#     comment_5.append(temp)

##1~5페이지 정보가져오기
basic_url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=11035&target=after&page='

comment_5 = []
for i in range(1,6,1):
    real_url = basic_url + str(i)
    page = urlopen(real_url)
    soup = BeautifulSoup(page, 'html.parser')
    comment_all = soup.find_all('td', class_ = 'title')
    print(len(comment_all))

    comments = []
    for one in comment_all:
        temp = list(one.children)[6].strip()
       # print(temp)
       # comments.append(temp)
        comment_5.append(temp)

print(len(comment_5),comment_5)
#
dict_dat = {"영화댓글": comment_5}
dat = pd.DataFrame(dict_dat)
dat.to_csv("황금광시대영화댓글.csv", index=False)
dat.to_excel("황금광시대영화댓글.xlsx", index=False)