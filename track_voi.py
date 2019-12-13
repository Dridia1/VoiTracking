import requests
import json
import time

# Position in Gothenburg
lat = "57.700968"
lng = "11.972693"

URL = "https://api.voiapp.io/v1/vehicle/status/ready?lat=%s&lng=%s" % (lat, lng) # The URL to send a GET request to.

def sendRequest():
	r = requests.get(url = URL)

	return r.json()

	'''
	formatted_data = []
	for r in data:
		formatted_data.append([r['id'], r['location'], r['name'], r['battery']])
		
	return formatted_data
	'''


if __name__ == '__main__':
	f = open("data.cfg", "r")
	n = int(f.read().splitlines()[0])
	

	while True:
		try:
			
			fileName = 'data' + str(n + 1) + ".json"

			print('Sending request')
			r_data = sendRequest()

			with open(fileName, 'w') as outfile:
				json.dump(r_data, outfile)

			n = n + 1
			
			time.sleep(1800)
			
		except Exception as e:
			print(e)
			f = open("data.cfg", "w+")
			f.write(str(n))
			raise('Something went wrong. Saving current filenumber to cfg-file')