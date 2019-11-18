from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','Summary','Video'])

for article in soup.find_all('article'):

	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	try:
		video_src = article.find('iframe', class_='youtube-player')['src']

		video_id = video_src.split('/')[4]
		video_id = video_id.split('?')[0]

		youtube_lnk = f'https://youtube.com/watch?v={video_id}'

	except Exception as e:
		youtube_lnk = 'No video with this post'

	print(youtube_lnk)
	print()
	csv_writer.writerow([headline,summary,youtube_lnk])


# print(article.prettify())

