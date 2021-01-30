import random
import plotly.express as px
import plotly.figure_factory as pf
import csv
import pandas

df = pandas.read_csv('data.csv')


# diceSum = []
# count = []

# for i in range(1,100):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     diceSum.append(dice1 + dice2)
#     count.append(i)

height = pf.create_distplot([df['Height(Inches)'].tolist()], ['Height'], show_hist = False)
height.show()

weight = pf.create_distplot([df['Weight(Pounds)'].tolist()], ['Weight'], show_hist = False)
weight.show()