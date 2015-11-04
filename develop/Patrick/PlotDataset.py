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
#  *                              - dataset_typ_to_print   2= raw , 1 = rescaled, 0 = normalized datad
#  *
#  *     returns:                 0
#  *     description:             draws plots  based on given parameters
#  *                              3 plots, y,x,z f(t) and 3d plot (f(t)
#  *
#  *******************************************************************************/
def plotData(dataset_typ_to_print=2):
    plt.close("all")

    if dataset_typ_to_print == 2:
        file_to_load = pedro.generateFilename("Pedro","dataset",".npy",True)

    if dataset_typ_to_print == 1:
        file_to_load = pedro.generateFilename("Pedro","databaseRescaled",".npy",True)

    else:
        file_to_load = pedro.generateFilename("Pedro","datasetNormalized",".npy",True)

    dataset = numblibrary.load(file_to_load)
    if dataset.any:
        data_x = dataset[:,0]
        data_y = dataset[:,1]
        data_z = dataset[:,2]
        data_t = dataset[:,3]
        if __debug__:
            print('Debug: PlotData path: %S \n', file_to_load)
            print("\n Debug: ")
            print(dataset )

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
    else:
        return 1