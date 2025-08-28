import datetime
import re

def datetime_to_sqldate(date_raw):
  desired_format = '%Y-%m-%d'
  return date_raw.strftime(desired_format)

def get_date(date_short=None):
  if date_short:
    date_str = f'{date_short[0:2]}-{date_short[2:4]}-{date_short[4:6]}'
  else:
    now = datetime.datetime.now()
    date_str = datetime_to_sqldate(now)

  return date_str

def get_date_from_url(url):
  print('Getting date from url')
  try:
    date_short = re.search('[0-9]{6}', url).group(0)
  except:
    date_short = None

  if date_short:
    date_str = f'20{date_short[0:2]}-{date_short[2:4]}-{date_short[4:6]}'
  else:
    now = datetime.datetime.now()
    date_str = datetime_to_sqldate(now)

  return date_str
