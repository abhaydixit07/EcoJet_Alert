import requests
TEQUILA_API_KEY = "WTEenXcwCxVeVwQP2uJtagLLAd7bHEOG"
TEQUILA_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
HEADERS = {
            "apikey":TEQUILA_API_KEY
        }
class FlightSearch:
    def __init__(self):
        pass

    def updating_iataCodes(self, row):
        self.row = row
        
        self.city_name = row['city']
        self.parameters = {
            "term":self.city_name,
            "location_types":"city"

        }
        self.response = requests.get(url=TEQUILA_API_ENDPOINT, params=self.parameters, headers=HEADERS)
        self.iata_code = self.response.json()["locations"][0]["code"]
        self.row["iataCode"] = self.iata_code
