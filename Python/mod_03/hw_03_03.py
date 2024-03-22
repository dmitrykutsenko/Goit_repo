base_rate = 40
price_per_km = 10
total_trip = 0

def calculate_trip_price(distance_km):
    global trips
    trips = 0 
    trips = total_trip + 1
    total = float(base_rate) + float(distance_km)*float(price_per_km) 

calculate_trip_price(2)

total_trip = trips
