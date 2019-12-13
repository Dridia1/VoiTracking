import math

def calculate_distance(PointA, PointB):
	
	"""
		Calculate the distance between 2 latitude and longitude points
		
		@param PointA (dictionary): {"lat": "42.2323232", "lng": "11.2323232"}
		@param PointB (dictionary): {"lat": "42.3232323", "lng": "11.3232323"}

		@return d (float): The distance between the 2 points specified in meters
	"""
	
	r = 6371e3 # Earths radius in Meters
	lat1 = math.radians(float(PointA['lat']))
	lat2 = math.radians(float(PointB['lat']))
	dlat = math.radians(float(PointB['lat']) - float(PointA['lat']))
	dlng = math.radians(float(PointB['lng']) - float(PointA['lng']))
	
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dlng/2) * math.sin(dlng/2)
		
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	
	d = r * c
		
	return d


if __name__ == '__main__':
	
	a = {"lat": "57.68766403198242", "lng": "11.992720603942871"}
	b = {"lat": "57.6897087", "lng": "11.9898823"}

	print(calculateDistance(a, b))
	