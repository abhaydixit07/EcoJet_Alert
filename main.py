#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData, flight_cost
from notification_manager import send_email
from pprint import pprint
ORIGIN_CITY_CODE = "LON"
ORIGIN_CITY = "London"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

sheet_class = DataManager()
sheet=sheet_class.get_data_from_sheet()
print(sheet)
for row in sheet:
    if row['iataCode']=="":

        FlightSearch().updating_iataCodes(row=row)
        sheet_class.update_data_in_sheet(row=row)
for row in sheet:
    FlightData().check_flight(row,from_time=tomorrow,to_time=six_month_from_today)
msg = ""
for row in sheet:
    
    city = flight_cost[row['city']]
    if city==None:
        print(f"No flights available for {row['city']}")
        continue
    
    print(row['city'], f"£{city['price']}")
    if (int(row['lowestPrice']) > int(city['price'])):
        if city['stop_over']==0:
            msg = msg + f"Only 💵£{city['price']} to fly from ✈️{city['origin_city']}-{city['origin_airport']} to 🌍{city['destination_city']}-{city['destination_airport']} from {city['from_date']} to {city['to_date']}.\n"
        else:
            msg = msg + f"Only £{city['price']} to fly from {city['origin_city']}-{city['origin_airport']} to {city['destination_city']}-{city['destination_airport']} from {city['from_date']} to {city['to_date']}.\nFlight has 1 stopover, via {city['via_city']} city."

if  msg!='':
    # NotificationManager().send_sms(msg=msg)
    for user in sheet_class.users_data():
        mesg = ''
        mesg = f"Hi🙋‍♂️ {user['firstName']} {user['lastName']}!\nLow Price Alert! \n" + msg
        
        send_email(to_addrs=user['email'], mesg=mesg)
    
            