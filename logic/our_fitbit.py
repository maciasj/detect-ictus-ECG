import fitbit
import logic.gather_keys_oauth2 as Oauth2
import pandas as pd
from datetime import datetime

def get_fitbit_csv():
    CLIENT_ID = '238RX8'
    CLIENT_SECRET = 'dff37bf9cb0059dfc910129162e035ba'

    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    # year = date.year;
    # month = date.month;
    # day = date.day;

    oneDate = pd.datetime(year = 2022, month = 12, day = 16)
    oneDayData = auth2_client.intraday_time_series('activities/heart', oneDate, detail_level='1sec')
    df= pd.DataFrame(oneDayData['activities-heart-intraday']["dataset"])

    # print(df)
    # csv_file_name = CLIENT_ID + date.today.strftime("%Y%m%d%H%M%S") 

    now = datetime.now()
    # Format the date and time as a string in the desired format
    date_time_str = f"{now.year}{now.month:02d}{now.day:02d}{now.hour:02d}{now.minute:02d}{now.second:02d}"
    csv_file_name = CLIENT_ID + date_time_str + ".csv"
    df.to_csv("data/csv/"+csv_file_name)
    return csv_file_name
