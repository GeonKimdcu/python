from bs4 import BeautifulSoup

text = '''
<!--
<style>
div > a {
    font-size:30
}
</style>
-->
<a href=a.html>a</a>
<div>
    <a href=b.html>b</a>
</div>
<div>
    <a href=c.html>c</a>
</div>
'''

soup = BeautifulSoup(text, 'html.parser')

for a in soup.select('div > a'):
    print(a.text)