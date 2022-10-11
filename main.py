from flask import Flask, render_template
from ppp import get_data, get_country, get_usadata
from graphs import graph_localprice, graph_valuation, graph_ppp

app = Flask('app')

@app.route('/')
def hello_world():
  data = get_data()
  country = get_country()
  datausa = get_usadata()
  graph_lp = graph_localprice()
  graph_val = graph_valuation()
  graph_pp = graph_ppp()
  #print(type(data))
  return render_template("index.html",data=data, country = country, datausa = datausa, graph_val=graph_val, graph_lp = graph_lp, graph_ppp=graph_pp)

app.run(host='0.0.0.0', port=8080)
