import re

# with open('re_weekday_item_title.html', 'rt') as f:
#     html = f.read()
# print(html)

with open('weekday.html', 'rt') as f:
    html = f.read()

# 처음시작하는 문자는 <a 문자가 0번 이상오고 *? >를 만날때까지 감
# ()그룹화 문자가 * 여러번 반복되고 </a>를 만날때까지 감
# 1.

# p = re.compile(r'<a.*?>(.*?)</a>')

# 정규표현식 패턴 (a 태그이며, class="title"이 여는 태그에 포함되어 있을 경우, 내용부분을 그룹화)
p = re.compile(r'''<a                      #    <a로 시작하며 
                   .*?class="title".*?>    #    중간에 class="title" 문자열이 존재하며가 
                                           #    >가 등장하기전까지의 임의의 문자 최소 반복, >까지
                   (.*>)                   #    임의의 문자 반복을 그룹화 (findall또는 finditer의 match object에서 사용)
                   </a>                    #    </a>가 나오기전까지''', re.VERBOSE)
result = re.findall(p, html)

print(result)
