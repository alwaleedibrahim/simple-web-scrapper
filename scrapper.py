#https://docs.python-guide.org/scenarios/scrape/
#https://stackoverflow.com/questions/44391671/python3-unicodeencodeerror-charmap-codec-cant-encode-characters-in-position

from lxml import html
import requests
f = open("out.html", 'w', encoding='utf-8')
for i in range(1, 498):
	source = requests.get("http://www.arkabeh.com/lines.php?lineid=" + str(i) + "&do=search").content
	source = source.decode('utf-8')
	source = html.fromstring(source)
	mytext = source.xpath('//div[@class="arkab-layout-cell layout-item-4"]/div//text()')
	f.write(str(mytext))

f.close()