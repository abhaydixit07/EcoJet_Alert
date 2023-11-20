import requests
ORIGIN_CITY = 'LON'
TEQUILA_API_KEY = "WTEenXcwCxVeVwQP2uJtagLLAd7bHEOG"
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HEADERS = {
        "apikey":TEQUILA_API_KEY
        }
flight_cost = {}
class FlightData:
    def __init__(self):
        pass
    def check_flight(self,row,from_time, to_time):
        self.row = row
        self.parameters = {
            "fly_from":ORIGIN_CITY,
            "fly_to": self.row["iataCode"],
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        
        self.response = requests.get(url=SEARCH_ENDPOINT, headers=HEADERS, params=self.parameters)
        try:
            self.data = self.response.json()["data"][0]
            self.price_data = self.data['price']
            
            flight_cost[self.row['city']] = {"iataCode":self.row['iataCode'],
                                             "origin_city": self.data["route"][0]["cityFrom"],
                                             "origin_airport":self.data["route"][0]["flyFrom"],
                                             "destination_city":self.data["route"][0]["cityTo"],
                                             "destination_airport":self.data["route"][0]["flyTo"],
                                             "price":self.price_data,
                                             "stop_over":0,
                                             "from_date":self.data["route"][0]["local_departure"].split("T")[0],
                                             "to_date":self.data["route"][1]["local_departure"].split("T")[0]
                                             }

        except IndexError:
            
            try:
                self.parameters["max_stopovers"] = 1
                self.response = requests.get(url=SEARCH_ENDPOINT, headers=HEADERS, params=self.parameters)
    
                self.data = self.response.json()["data"][0]
                
                self.price_data = self.data['price']
            
                flight_cost[self.row['city']] = {"iataCode":self.row['iataCode'],
                                             "origin_city": self.data["route"][0]["cityFrom"],
                                             "origin_airport":self.data["route"][0]["flyFrom"],
                                             "destination_city":self.data["route"][1]["cityTo"],
                                             "destination_airport":self.data["route"][1]["flyTo"],
                                             "price":self.price_data,
                                             "from_date":self.data["route"][0]["local_departure"].split("T")[0],
                                             "to_date":self.data["route"][2]["local_departure"].split("T")[0],
                                             "stop_over":1,
                                             "via_city":self.data["route"][0]["cityTo"]

                                             }
            except IndexError:
                flight_cost[self.row['city']] = None
                
            