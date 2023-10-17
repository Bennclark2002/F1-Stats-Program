import requests
import xml.etree.ElementTree as ET

url = "http://ergast.com/api/f1/drivers"
params = {"param_name": "123"}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("XML Response:")
    print(response.text)  # Print the XML response for analysis

    root = ET.fromstring(response.text)
    driver = root.find(".//Driver")  # Find the first driver element, adjust this according to your XML structure
    
    if driver is not None:
        Firstname = driver.find("GivenName").text
        Lastname = driver.find("FamilyName").text
        DOB = driver.find("DateOfBirth").text
        Nationality = driver.find("Nationality").text

        print(f"{Firstname} {Lastname} was born on {DOB} in the country of {Nationality}")
    else:
        print("Driver data not found in the XML response.")

else:
    print(f"Error: {response.status_code}")
