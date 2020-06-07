import plotly.plotly as py
import pandas as pd
from atm import *


thinglist = main("branch")
thingyList = {"name" : thinglist[0],
              "pop" : thinglist[1],
	       "lon" : thinglist[2],
                "lat" : thinglist[3]}
df = pd.DataFrame(thingyList)
df.head()

df['text'] = df['name'] + '<br> Visitors' + (df['pop']).astype(str)
limits = [(0,41),(42,82),(83,124),(125,166),(167,208)]
colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","black"]
cities = []
scale = 700
nameList = ["low","medium","moderate","high","very high"]
for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = df_sub['lon'],
        lat = df_sub['lat'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['pop']/scale,
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = nameList[i] )
    
    cities.append(city)

layout = dict(
        title = 'Captial One Branch Locations',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict( data=cities, layout=layout )
py.iplot( fig, validate=False, filename='d3-bubble-map-populations' )

