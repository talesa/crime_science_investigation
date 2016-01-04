import requests

postcode_request = 'http://api.postcodes.io/postcodes/'
police_request = 'https://data.police.uk/api/'
filip_postcode = 'tw200hq'

r = requests.get(postcode_request + filip_postcode)
r = r.json()

lat, lon = r['result']['latitude'], r['result']['longitude']



for month in range(1, 13):
	r = requests.get(police_request + 'crimes-at-location?date={}&lat={}&lng={}'.format('2014-{}'.format(month), lat, lon))
	print(r.json())


