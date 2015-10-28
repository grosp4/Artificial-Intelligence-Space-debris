"""/******************************************************************************/
/** \file          TBD
 *  \brief         getting data out of the dataset
 *******************************************************************************
 *
 *
 *
 *  \brief         getting data out of the dataset
 *
 *  \authors       grosp4, pedro
 *
 *  \date          20.10.2015
 *
 *  \remark        Last Modification
 *                  \li pedro, 20.10.2015, Created
                    \li grosp4,pdro 21.10.2015 updated
 *

 *
 ******************************************************************************/
/*
 *  functions:     sigmoid
 *
 ******************************************************************************/
 """


# import necessary libaries
import numpy as numblibrary
from  pyorbital import tlefile
from  pyorbital.orbital import Orbital
from datetime import datetime

# define sigmoid function (->Wiki)
def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    
    return 1/(1+numblibrary.exp(-x))

# creating input and output data  


random_file_name = tlefile.read('ISS', r'D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\database\TLE_files\ISS_DATA.txt')
input_data = Orbital('ISS', r'D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\database\TLE_files\ISS_DATA.txt')

# calculate data
date_at_vessel = datetime.utcnow()
expected_output_data = input_data.get_position(date_at_vessel,normalize=False)

# print data
print "\nPosition of the satellite : \n X = %.6f Km \n Y = %.6f Km \n Z = %.6f Km" % (expected_output_data[0][0],expected_output_data[0][1],expected_output_data[0][2])
print "\nVelocity of the satellite : \n Vx = %.6f Km/s \n Vy = %.6f Km/s \n Vz = %.6f Km/s " % (expected_output_data[1][0],expected_output_data[1][1],expected_output_data[1][2])




"""  
input_data = numblibrary.array([[0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

      
                       
expected_output_data = numblibrary.array([[0,0,1,1]]).T
"""

# generating random guesses
#numblibrary.random.seed(1)
#
#random_values = 2*numblibrary.random.random((3,1)) - 1
#
### doing the job
#for iter in range(10000):
#    
#    # calculating 
#    calculation = sigmoid(numblibrary.dot(input_data,random_values))
#    
#    #checking the error
#    calculation_error = expected_output_data - calculation
#    
#    #compare error and reality
#    calculation_delta = calculation_error * sigmoid(calculation,True)
#    
#    
#    random_values += numblibrary.dot(input_data.T,calculation_delta)
#    
## print results    
#print("Output After Training:")
#print(calculation)


#end