__author__ = 'Patrick'
# import necessary libaries
import numpy as np
from  pyorbital import tlefile
from  pyorbital.orbital import Orbital
import datetime

#generate dataset
dataset = np.zeros(shape=[1,4])


# reading input data
input_data = Orbital('ISS (ZARYA)', r'C:\Users\Honor\Desktop\Project AI\stations.txt')

# calculate data
date_at_vessel = datetime.datetime(2015,10,28,0,0,0)

#1440 for the number of minutes in a day
for step in xrange(1440):
    #increment the time step in 60 seconds
    date_at_vessel += datetime.timedelta(0,60)
    output_data = input_data.get_position(date_at_vessel,normalize=False)
    dataset = np.vstack([dataset, np.append(output_data[0],[step])])
    #dataset.append(output_data[0])

dataset = np.delete(dataset,0,0)

with file(r'C:\Users\Honor\Desktop\Project AI\dataset_20151029.npy', 'wb+') as outfile:
    np.save(outfile,dataset)