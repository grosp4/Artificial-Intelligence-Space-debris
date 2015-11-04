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
#  *  functions:     plotDataset
#  *
#  ******************************************************************************/


import matplotlib.pyplot as plt
import Pedro as pedro
from mpl_toolkits.mplot3d import Axes3D
import numpy as numblibrary


#  ******************************************************************************/
# /*
#  *     functionname:          plotDataset
#  *     parameter:
#  *
#  *
#  *                              - normalization   True = normalized data, false = not normalized
#  *
#  *     returns:                 wildcard value
#  *     description:             draws plots  based on given parameters
#  *                              3 plots, y,x,z f(t) and 3d plot (f(t)
#  *
#  *******************************************************************************/
def plotData(normalization =False):
    plt.close("all")

    # if __debug__ is true we generate random values
    if __debug__ ==1:

        data_x = 1000*numblibrary.random.random((10,1)) - 1
        data_y = 2000*numblibrary.random.random((10,1)) - 1
        data_z = 3000*numblibrary.random.random((10,1)) - 1
        data_t = [1,2,3,4,5,6,7,8,9,10]

    # if __debug__ is false, we will use given data (dataset later)
    else:

        # change path due to its dataset
        if normalization:
            file_to_load = pedro.generateFilename("Pedro","datasetNormalized",".npy",True);

        else:
            file_to_load = pedro.generateFilename("Pedro","dataset",".npy",True);


        dataset = numblibrary.load(file_to_load)
        data_x = dataset[:,0]
        data_y = dataset[:,1]
        data_z = dataset[:,2]
        data_t = dataset[:,3]

        points = dataset[:,2:4]

    #Print 3 plots in its own figure, each in function of time
    figure_x = plt.figure()
    plt.plot (data_t,data_x, '-ro')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in x (unit:tbd)')

    figure_y = plt.figure()
    plt.plot( data_t,data_y, '-bs')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in y (unit:tbd)')

    figure_z = plt.figure()
    plt.plot( data_t,data_z, '-g^')
    plt.xlabel('time in tbd')
    plt.ylabel('attitude in z (unit:tbd)')

    #print 3d Plot for better visibiality
    fig_3d = plt.figure()
    plot3d = fig_3d.add_subplot(111, projection='3d')
    plot3d.scatter(data_x, data_y, data_z, c='r', marker='o')
    plot3d.set_xlabel('X axes')
    plot3d.set_ylabel('Y axes')
    plot3d.set_zlabel('Z axes')
    plt.show()
    # return __debug__ value as testvalue
    return 0