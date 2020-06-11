from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from scraping.models import website_list
import requests


class Command(BaseCommand):
    help = "collect websites"
    # define logic of command
    def handle(self, *args, **options):
        url = "https://websites.co.in/sitemap"
        response = requests.get(url=url)
        print(response)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content.decode('UTF-8'), 'html.parser')
            # print(soup)
            table_body = soup.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                col = row.find_all('a')
                col = ["https:" + x.get('href') for x in col]
                cols = [x.text.strip() for x in cols]
                cols.extend(col)
                # print(cols)
                url = cols[3]
                city = cols[2]
                category = cols[1]
                title = cols[0]
                try:
                    # save in db
                    website_list.objects.create(
                        url=url,
                        title=title,
                        category=category,
                        city=city
                    )
                    print('%s added' % (title,))
                except:
                    print('%s already exists' % (title,))
       
        self.stdout.write( 'website list entries done in db' )