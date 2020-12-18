import requests
import bs4

url = 'https://www.orami.co.id/shopping/category/aktivitas-bayi-bepergian?page=1'
# url = 'https://www.orami.co.id/shopping/product/tops-bridge-road-map-boy-girl-playmat-240x140x1-4cm'
resp = requests.get(url)
soup = bs4.BeautifulSoup(resp.text,'html.parser')
print(soup)
# asd = soup.find_all('p')
# for a in asd:
#     print(a)
# ====================================
# asd = soup.find('meta', attrs={'property': 'og:image'})['content']
# print(asd)
# ====================================
# print(asd)
# i=1
# for a in asd:
#     print(a)
    # if i==12:
    #     print(a)
    #     b= str(a)
    # i+=1
# print(b)
# c=b.find('meta')
# print(c)
# asd = asd[0]
# dsa = asd.find('img')['src']
# print(asd)
