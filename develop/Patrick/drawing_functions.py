__author__ = 'Patrick'

# /******************************************************************************/
# /** \file          drawing_functions
#  *  \brief         TBD
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         TBD
#  *
#  *  \authors       grosp4,
#  *
#  *  \date          29.10.2015
#  *
#  *  \remark        Last Modification
#  *                  \li grosp4, 29.10.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     plot_data
#  *
#  ******************************************************************************/


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as numblibrary



#  ******************************************************************************/
# /*
#  *     functionname: plot_data
#  *     parameter:
#  *
#  *                              - data            data, format TBD!
#  *
#  *     returns:                 wildcard value
#  *     description:             draws plots  based on given parameters
#  *                              3 plots, y,x,z f(t) and 3d plot (f(t)
#  *
#  *******************************************************************************/
def plot_data(data):
    plt.close("all")

    # if __debug__ is true we generate random values
    if __debug__ ==1:

        random_value_x= 1000*numblibrary.random.random((10,1)) - 1
        random_value_y= 2000*numblibrary.random.random((10,1)) - 1
        random_value_z= 3000*numblibrary.random.random((10,1)) - 1
        random_time= [1,2,3,4,5,6,7,8,9,10]

        x_value_learnt = random_value_x
        y_value_learnt = random_value_y
        z_value_learnt = random_value_z

    # if __debug__ is false, we will use given data (dataset later)
    else:
        # right now we use prepared data
        random_value_x= [1,2,3,4,5,6,7,8,9,10]
        random_value_y= [1,2,3,4,5,6,7,8,9,10]
        random_value_z= [1,2,3,4,5,6,7,8,9,10]
        random_time= [1,2,3,4,5,6,7,8,9,10]

        x_value_learnt = random_value_x
        y_value_learnt = random_value_y
        z_value_learnt = random_value_z


    #Print 3 plots in its own figure, each in function of time
    figure_x = plt.figure()
    plt.plot (random_time,random_value_x, '-ro')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in x (unit:tbd)')

    figure_y = plt.figure()
    plt.plot( random_time,random_value_y, '-bs')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in y (unit:tbd)')

    figure_z = plt.figure()
    plt.plot( random_time,random_value_z, '-g^')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in z (unit:tbd)')

    #print 3d Plot for better visibiality
    fig_3d = plt.figure()
    ax = fig_3d.add_subplot(111, projection='3d')
    ax.scatter(random_value_x, random_value_y, random_value_z, c='r', marker='o')
    ax.set_xlabel('X axes')
    ax.set_ylabel('Y axes')
    ax.set_zlabel('Z axes')
    plt.show()
    # return wildcard value as testvalue
    return __debug__