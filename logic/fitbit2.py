import requests
import json
import csv

# Set the base URL for the Fitbit API
base_url = "https://api.fitbit.com"

# Set the client ID and client secret for your Fitbit app
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Set the authorization URL and the token URL
auth_url = f"{base_url}/oauth2/authorize"
token_url = f"{base_url}/oauth2/token"

# Set the redirect URI for your app
redirect_uri = "http://localhost:8000/callback"

# Set the scope for the data you want to access
scope = "activity heartrate profile"

# Set the state parameter to prevent cross-site request forgery (CSRF) attacks
state = "random_string"

# Set the authorization URL with the client ID, redirect URI, scope, and state
auth_url = f"{auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"

# Redirect the user to the authorization URL
# (Note: You will need to implement the redirect yourself)

# After the user grants your app access to their data, they will be redirected to the redirect URI
# with an authorization code in the query string

# Extract the authorization code from the query string
auth_code = "YOUR_AUTHORIZATION_CODE"

# Set the payload for the token request with the client ID, client secret, authorization code, and redirect URI
payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": auth_code,
    "grant_type": "authorization_code",
    "redirect_uri": redirect_uri
}

# Make a POST request to the token URL with the payload
response = requests.post(token_url, data=payload)
data = response.json()

# Check the status code of the response
# if response.status_code == 200:
#     # The request was successful, so parse the JSON data
#     data = response.json()
#     # Extract the access token from the data
#     access_token = data["access_token"]
#     # Do something with the access token (e.g. print it to the console)
#     print(access_token)
# else:
#     # The request was not successful, so print the status code and error message
#     print(f"Error: {response.status_code} {response.reason}")


# Set the filename for the CSV file
filename = "heart_rate_data.csv"

# Open the CSV file in write mode
with open(filename, "w", newline="") as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the header row to the CSV file
    writer.writerow(["timestamp", "heart_rate"])

    # Iterate through the data returned by the Fitbit API
    for datapoint in data["activities-heart"]:
        # Extract the timestamp and heart rate from the datapoint
        timestamp = datapoint["dateTime"]
        heart_rate = datapoint["value"]["heartRate"]
        # Write the data to the CSV file
        writer.writerow([timestamp, heart_rate])

