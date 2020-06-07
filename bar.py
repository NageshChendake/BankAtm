import plotly.plotly as py
import plotly.graph_objs as go
from atm import *


thing = main("atm")
yAxis = makeList(thing,0)
#print(xAxis)
xAxis = makeList(thing,1)
#print(yAxis)

data = [go.Bar(
            x=xAxis,
            y=yAxis
    )]

py.iplot(data, filename='basic-bar')

