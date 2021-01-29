from bs4 import BeautifulSoup

text = '''
<!--
<style>
a[id=id1] {
    font-size:30
}
-->
</style>
<a href=a.html id=id1>a</a>
<a href=b.html>b</a>
<a href=c.html>c</a>
'''

soup = BeautifulSoup(text, 'html.parser')

#a = soup.select('a[id=id1]')
#print(a[0].text)
a = soup.select_one('a#id1')
print(a.text)
