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
import time as systemtime

#  ******************************************************************************/
# /*
#  *     functionname:          plotDataset
#  *     parameter:
#  *
#  *
#  *                              - file_to_load   path including filename
#  *                              - x_axes_name   name of the x axes,
#  *                              - y_axes_name   name of the y axes,
#  *                              - z_axes_name   name of the z axes
#  *                              - t_axes_name   only used for animations! name of the t axes
#  *
#  *     returns:                 0
#  *     description:             draws plots  based on given parameters
#  *                              3 plots, y,x,z f(t) and 3d plot (f(t)
#  *
#  *******************************************************************************/
def plotData( file_to_load = '', x_axes_name = 'x axes name', y_axes_name = 'y axes name', z_axes_name = 'z axes name ', t_axes_name = 't for animations'):
    plt.close("all")

    # check if no filename has been specified, if not abort
    if file_to_load == '':
            print("Error in PlotDataset, no filename specified \n")
            print('Pathname in PlotData path is: %s \n', file_to_load)

    else:
            dataset = numblibrary.load(file_to_load)


            # check if all values in dataset are zero
            if  numblibrary.all(dataset == 0):
                    print("Error in PlotDataset,can not open file \n")
                    print('Pathname in PlotData path is: %S \n', file_to_load)

            # if dataset contains values, we have a valid file, if not abort
            else:
                    #  decide wether the matrix is 1, 2, 3, 4 dimensional -> specify plot
                    dataset_size = dataset.shape

                    print (dataset_size)
                    # 2 dimensional -> x,y
                    if dataset_size[1] == 2:

                        data_x_axes = dataset[:,0]
                        data_y_axes = dataset[:,1]

                        #Draw 2 dim diagram
                        figure_x = plt.figure()
                        plt.plot(data_y_axes,data_x_axes, '-ro')
                        plt.xlabel(x_axes_name)
                        plt.ylabel(y_axes_name)
                        plt._show


                    # 3 dimensional -> x,y,z
                    if dataset_size[1] == 3:

                        data_x_axes = dataset[:,0]
                        data_y_axes = dataset[:,1]
                        data_z_axes = dataset[:,2]

                        #print 3 dimensional plot
                        fig_3d = plt.figure()
                        plot3d = fig_3d.add_subplot(111, projection='3d')
                        plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                        plot3d.set_xlabel(x_axes_name)
                        plot3d.set_ylabel(y_axes_name)
                        plot3d.set_zlabel(z_axes_name)
                        plt.show


                    # 4 dimensional -> x,y,z and a t axis
                    if dataset_size[1] == 4:

                        data_x_axes = dataset[:,0]
                        data_y_axes = dataset[:,1]
                        data_z_axes = dataset[:,2]
                        data_t_axes = dataset[:,3]

                        fig_3d = plt.figure()
                        plot3d = fig_3d.add_subplot(111, projection='3d')
                        plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                        plot3d.set_xlabel(x_axes_name)
                        plot3d.set_ylabel(y_axes_name)
                        plot3d.set_zlabel(z_axes_name)

                        plt.show()



                    else:
                        print("Debug: This file contains more than 4 dimensions and therefore it can not be drawn, Error in: %S \n", file_to_load)


            if __debug__:
                    print('Debug: PlotData path: %S \n', file_to_load)
                    print("\n Debug: ")
                    print(dataset)

    return 0
