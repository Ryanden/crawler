# 우리가 웹브라우저를 통해 보는 HTML 문서는 GET 요청의 결과
# requests 를 사용해 'http://comic.naver.com/index.nhn' 주소에 get 요청을 하고
# 요청 결과를 response 변수에 할당해서 status_code 속성을 출력

import requests

response = requests.get('http://comic.naver.com/index.nhn')


gaus_60 = requests.get('http://comic.naver.com/webtoon/detail.nhn?titleId=675554&no=540&weekday=mon')
print(response.status_code)

# webtoon_contet = response.text
#
# f = open('weekday.html', 'wt')
#
# f.write(webtoon_contet)
# f.close()

with open('weekday.html', 'wt') as f:
    f.write(response.text)

with open('gaus.html', 'wt') as f:
    f.write(gaus_60.text)