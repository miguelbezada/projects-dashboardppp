import nasdaqdatalink
import json
import urllib.request

nasdaqdatalink.ApiConfig.api_key = 'BmL6cKD7xtaHuqf3xD7v'

def get_data():
  nasdaqdatalink.ApiConfig.api_key = 'BmL6cKD7xtaHuqf3xD7v'
  countries = ["CAN","PER","POL","URY"]
  data_list = []
    
  for country in countries:
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{country}', start_date='2021-01-31', end_date='2022-01-31')
    if country == "CAN":
      country = "Canada"
    if country == "PER":
      country = "Peru"
    if country == "POL":
      country = "Poland"
    if country == "URY":
      country = "Uruguay"  
      
    country = {
      "country":country,
      "local_price": round(data.iloc[0,0],2),
      "dollar_ex": round(data.iloc[0,1],2),
      "dollar_price": round(data.iloc[0,2],2),
      "dollar_ppp": round(data.iloc[0,3],2),
      "dollar_valuation":round(data.iloc[0,4],2),
      "dollar_adj_valuation":round(data.iloc[0,5],2)
    }
    
    data_list.append(country)
  return data_list

def get_country():
  countries = ["Canada","Peru","Poland","Uruguay"]
  data_country = []
  for country in countries:  
  
    url =f'https://restcountries.com/v3.1/name/{country}' #the web adress with the information needed
    request = urllib.request.urlopen(url) #variable request to open the URL Library
    result = json.loads(request.read())

    country = {
      'official':country,
      'cca2': result[0]['cca2'],
      'capital': result[0]['capital'],
      'geolocation': result[0]["latlng"],
      'flag': result[0]['flags']['png'],
      'maps': result[0]['maps']['googleMaps'],
      'population': format(result[0]['population'], ',d')
    }

    data_country.append(country)
  return data_country

def get_usadata():
  nasdaqdatalink.ApiConfig.api_key = 'BmL6cKD7xtaHuqf3xD7v'
  countries = ["USA"]
  data_list = []
    
  for country in countries:
    data = nasdaqdatalink.get(f'ECONOMIST/BIGMAC_{country}', start_date='2021-01-31', end_date='2022-01-31')
    if country == "USA":
      country = "United States"
      
    country = {
      "country":country,
      "local_price": round(data.iloc[0,0],2)
    }
    
    data_list.append(country)
  return data_list