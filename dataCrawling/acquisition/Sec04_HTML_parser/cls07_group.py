from bs4 import BeautifulSoup

text = '''
<!--
<style>
div {
    font-size:30
}
</style>
-->
<a href=a.html>a</a> <b>date1</b>
<div>
    <a href=b.html>b</a> <b>date2</b>
</div>
<div>
    <a href=c.html>c</a> <b>date3</b>
</div>
'''

soup = BeautifulSoup(text, 'html.parser')

for div in soup.select('div'):
    print(div.a.text, div.b.text)