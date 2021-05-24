from bokeh.plotting import figure, output_file, show
import pandas as pd
import json

def run():
    f = open('covid-cases-sf-arg.json',)
    
    data_covid_sf = json.load(f)

    output_file('covid-graphic.html')
    fig = figure(x_axis_type='datetime')

    x_vals = []
    y_vals = []

    i = len(data_covid_sf)
    for data_element in data_covid_sf:
        x_vals.append(pd.to_datetime(data_element['date']))
        y_vals.append(data_element['deaths'])
        i -= 1
    
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)

    pass

if __name__=='__main__':
    run()