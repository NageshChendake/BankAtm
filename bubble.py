import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *

import numpy as np
import pandas as pd

file = open("accounts.txt","r")
giantString = file.read()
file.close()
giantDict = eval(giantString)

giantList = giantDict["results"]
print(len(giantList))

print("Creating 3d")

def makeBigList(dictionaryList):
	nameResult = []
	typeResult = []
	rewardsResult = []
	balanceResult = []
	for thing in dictionaryList:
		nameResult.append(thing["nickname"])
		typeResult.append(thing["type"])
		rewardsResult.append(thing["rewards"])
		balanceResult.append(thing["balance"])
	return (nameResult, typeResult, rewardsResult, balanceResult)

thingy = makeBigList(giantList)
nameList = thingy[0]
typeList = thingy[1]
rewardList = thingy[2]
balanceList = thingy[3]

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

newList = []
for element in rewardList:
	if element < 1000:
		newList.append(element//100)
	else:
		newList.append(423)
newX = pd.Series(rewardList)
newY = pd.Series(balanceList)
newZ = pd.Series(typeList)
newName = pd.Series(nameList)
trace1 = Scatter3d(
    x=newX,
    y=newY,
    z=newZ,
    text=newName,
    mode='markers',
    marker=dict(
        sizemode='diameter',
        sizeref=750,
	size=df['gdpPercap'][750:1500],
	color = df['lifeExp'][750:1500],
        colorscale = 'Viridis',
        colorbar = dict(title = 'Rewards Amount'),
        line=dict(color='rgb(140, 140, 170)')
    )
)

data=[trace1]
layout=dict(height=1000, width=1000, title='Account Information Web')
fig=dict(data=data, layout=layout)
py.iplot(fig, filename='3DBubble')
