import scrapy
import os
import requests
# from PIL import Image
from apod.utils.functions import get_date_from_url

class ApodSpider(scrapy.Spider):
  name = "apod"

  def start_requests(self):
    urls = [
      "https://apod.nasa.gov/apod/astropix.html", # Standard link for current daily picture
      "https://apod.nasa.gov/apod/ap241001.html", # Dated link for a specific date (YYMMDD)
      "https://apod.nasa.gov/apod/ap250825.html"
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    url = response.url
    apod_day = get_date_from_url(url)
    self.log(f"\n- Astronomy Picture Of the Day: {apod_day} -\n")
    apod_obj = {}

    apod_obj['url'] = url
    apod_obj['title'] = response.xpath('//body/center[2]/b/text()').get().strip()
    
    try:
      media_suffix = response.xpath('//body/center[1]/p[2]/a/@href').get()
      media_type = 'video' if not media_suffix else 'image'

      if media_suffix:
        apod_obj['media'] = 'https://apod.nasa.gov/apod/' + media_suffix
      else:
        apod_obj['media'] = 'unavailable'
    except:
      media_type = 'video'
            
    apod_obj['media_type'] = media_type
    apod_obj['date'] = apod_day
    apod_obj['credits'] = response.xpath('//body/center[2]/a/@href').getall()

    # Download image
    if media_type == 'image':
      self.log(f'Attempting to download image from {apod_obj['media']}')
      try:
        img_response = requests.get(apod_obj['media'])

        if img_response.status_code == 200:
          relative_dir = 'downloads'
          os.makedirs(relative_dir, exist_ok=True)
          file_path = os.path.join(relative_dir, f'{apod_day}.jpg')

          with open(file_path, 'wb') as f:
            f.write(img_response.content)
            f.close()
          self.log('Image downloaded successfully')
      except Exception as e:
        self.log('\nUnable to download image')
        self.log(f'Error: {e}')
    else:
      self.log(f'Media type {media_type} will not be downloaded')


    yield apod_obj
