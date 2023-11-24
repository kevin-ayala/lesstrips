import requests
import googlemaps

# TODO: Store keys elsewhere
api_key = 'AIzaSyDA_65RKIFqNhtpXSJNYVRT9ali79U6qgI'
gmaps = googlemaps.Client(key='AIzaSyDA_65RKIFqNhtpXSJNYVRT9ali79U6qgI')

# sending get request and saving the response as response object
r = requests.get(
    f'https://maps.googleapis.com/maps/api/geocode/json?place_id=ChIJ8wA55eoNK4cRwdm_2MFhQFE&key= {api_key}')
dr = requests.get(
    f'https://maps.googleapis.com/maps/api/distancematrix/json?origins=33.4721077%2C-112.0261424&destinations=40.659569%2C-73.933783&key=AIzaSyD4I0zmGa0P0z2OnpaC7iUpikmDBWCwhIg')

# TODO: Get distance to work with two points, then it it to distinguish the distance between three points
# calculates the distance between each point
distance = gmaps.distance_matrix((33.4721077, -112.0261424), (40.659569, -73.933783))
print(distance['rows'])

# extracting data in json format
data_origin = r.json()
data_destination = dr.json()

# extracting latitude, longitude and formatted address of the first matching location
latitude_origin = data_origin['results'][0]['geometry']['location']['lat']
longitude_origin = data_origin['results'][0]['geometry']['location']['lng']

