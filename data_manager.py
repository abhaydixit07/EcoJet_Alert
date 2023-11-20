import requests
SHEET_ENDPOINT_USERS = "https://api.sheety.co/485e0f70731795ba625ac5433b2ad5cd/flightdeals/users"
SHEET_ENDPOINT_GET = "https://api.sheety.co/485e0f70731795ba625ac5433b2ad5cd/flightdeals/prices"
SHEET_ENDPOINT_PUT = "https://api.sheety.co/485e0f70731795ba625ac5433b2ad5cd/flightdeals/prices"
class DataManager:
    
    def __init__(self):
        pass

    def get_data_from_sheet(self):
        self.reponse = requests.get(url=SHEET_ENDPOINT_GET)    
        self.result_data = self.reponse.json()["prices"]
        return self.result_data
    
    def update_data_in_sheet(self, row):
        self.row=row
        self.object_id=row['id']
        self.changes = {
            'iataCode':self.row['iataCode']
        }
        update_endpoint = f"{SHEET_ENDPOINT_PUT}/{self.object_id}"
        self.parameters = {
            "price":self.changes
        }
        self.response = requests.put(url=update_endpoint,json=self.parameters)

    def users_data(self):
        self.reponse = requests.get(url=SHEET_ENDPOINT_USERS)    
        self.result_data = self.reponse.json()["users"]
        return self.result_data

        
    