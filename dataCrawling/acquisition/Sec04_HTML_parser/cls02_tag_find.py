from bs4 import BeautifulSoup

text = '''
<!--
<style>
a {
    font-size:30
</style>
-->
<a href=a.html>a</a>
<a href=b.html>b</a>
<a href=c.html>c</a>
'''

soup = BeautifulSoup(text, 'html.parser') # HTML 파서

for a in soup.select('a'): # select('태그이름')
    print(a.text)