import csv
import plotly.figure_factory as ff 
import statistics as st
import pandas as pd
import random 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig  = ff.create_distplot([data],["reading_time"],show_hist=False)
fig.show()
dataset = []
for i in range(0,100):
    randomindex = random.randint(0,len(data))
    value = data[randomindex]
    dataset.append(value)
mean =st.mean(dataset)
std = st.stdev(dataset)
 
def random_set_of_mean(counter):
    dataset=[] 
    for _i in range(0,counter):
        randomindex=random.randint(0,len(data))
        value = data[randomindex]
    mean = st.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list 
    fig = ff.create_displot([df],["reading_time"],show_hist=False)
    fig.show()
def setup():
    mean_list = []
    for _i in range(0,100):
        setofmeans = random_set_of_mean(30)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    mean1 = st.stdev(mean_list)
    print("mean:",mean1)
setup()
