import requests
from datetime import datetime
my_lat = 50.43
my_long = 1.88


parameters = {
    "lat" : my_lat,
    "lng" : my_long 
    #"formatted" : 0
    
}
response = requests.get("https://api.sunrise-sunset.org/json" , parameters=parameters)
print(response.status_code)
data=response.json()
print(data)

#time_now = datetime.now()
#print(time_now)
