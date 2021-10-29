import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics 
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#population_mean = statistics.mean(data)
#std_deviation_data = statistics.stdev(data)

#for i in range(0,100):
    #random_index = random.randint(0,len(data))
    #value = data[random_index]
    #dataset.append(value)
    
#mean = statistics.mean(dataset)
#std_deviation = statistics.stdev(dataset)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data) - 1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean], y= [0,1], mode = "lines", name = "MEAN"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean Of sampling Distribution: ", mean)
setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("Standard Deviation of sample Distribution: ", std_deviation)
standard_deviation()

 


#print("Mean Of the sample: ",mean)
#print("Std_deviation of the sample: ", std_deviation)



#print("Mean Of the data: ",population_mean)
#print("Std_deviation of the Data: ", std_deviation_data)

#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.show()

