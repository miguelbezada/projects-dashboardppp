# import pygal library
import pygal_maps_world.maps
import pygal
from ppp import get_data, get_country

data_bigmac = get_data()
data_countries = get_country()

def graph_localprice():
  # create a world map
  worldmap = pygal_maps_world.maps.World()
  
  # set the title of the map
  #worldmap.title = 'Under(+)/Over(-) valuation against the dollar '
  
  # adding the countries
  for i in range(len(data_bigmac)):
    worldmap.add(data_countries[i]['official'], {data_countries[i]['cca2'].lower(): data_bigmac[i]['local_price']})
  
  # save into the file
  return worldmap.render_data_uri()



def graph_ppp():
  countries = []
  dollar_ex = []
  dollar_ppp = []
  
  # create a Line chart
  ppp_chart = pygal.Line(fill=True,legend_at_bottom=True)
  
  # adding the data
  for i in range(len(data_bigmac)):
    countries.append(data_countries[i]['official'])
    dollar_ex.append(data_bigmac[i]['dollar_ex'])
    dollar_ppp.append(data_bigmac[i]['dollar_ppp'])
    
  ppp_chart.x_labels = countries
  ppp_chart.add('Dollar exchange', dollar_ex)
  ppp_chart.add('Dollar PPP', dollar_ppp)
  
  # render
  return ppp_chart.render_data_uri()

def graph_valuation():
  countries = []
  dollar_val = []
  dollar_adj_val = []
  
  # create a bar chart
  bar_chart = pygal.Bar(legend_at_bottom=True)
  
  # adding the data
  for i in range(len(data_bigmac)):
    countries.append(data_countries[i]['official'])
    dollar_val.append(data_bigmac[i]['dollar_valuation'])
    dollar_adj_val.append(data_bigmac[i]['dollar_adj_valuation'])
    
  bar_chart.x_labels = countries
  bar_chart.add('Dollar Valuation', dollar_val)
  bar_chart.add('Dollar Adjusted Valuation', dollar_adj_val)
  
  # render
  return bar_chart.render_data_uri()