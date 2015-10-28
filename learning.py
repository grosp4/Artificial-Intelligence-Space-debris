"""/******************************************************************************/
/** \file          TBD
 *  \brief         learning prediction with given inputs
 *******************************************************************************
 *
 *
 *
 *  \brief         learning prediction with given inputs
 *
 *  \authors       grosp4, pedro
 *
 *  \date          20.10.2015
 *
 *  \remark        Last Modification
 *                  \li pedro, 20.10.2015, Created
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



input_data = numblibrary.array([[0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

      
                       
expected_output_data = numblibrary.array([[0,0,1,1]]).T



numblibrary.random.seed(1)

random_values = 2*numblibrary.random.random((3,1)) - 1

## doing the job
for iter in range(10000):
    
    # calculating 
    calculation = sigmoid(numblibrary.dot(input_data,random_values))
    
    #checking the error
    calculation_error = expected_output_data - calculation
    
    #compare error and reality
    calculation_delta = calculation_error * sigmoid(calculation,True)
    
    
    random_values += numblibrary.dot(input_data.T,calculation_delta)
    
# print results    
print("Output After Training:")
print(calculation)