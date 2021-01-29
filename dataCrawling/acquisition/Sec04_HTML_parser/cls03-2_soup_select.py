from bs4 import BeautifulSoup

text = '''
<!--
<style>
a[href*="a.h"] {
    font-size:30
}
</style>
-->
<a href=a.html>a</a>
<a href=b.html>b</a>
<a href=c.html>c</a>
'''

soup = BeautifulSoup(text, 'html.parser')

a = soup.select_one('a[href*="a.h"]')
print(a.text)