from flask import Flask, jsonify, render_template
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)

@app.route('/')
def show_home():
  return render_template('index.html')

@app.route('/simple_plot')
def show_simple_plot():
  bar = create_plot()
  return render_template('plots.html', plot=bar)

def create_plot():
  data = [
    go.Bar(
      x = ['Hugo','Paco','Luis'],
      y = [15, 5, 19]
    )
  ]
  
  graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
