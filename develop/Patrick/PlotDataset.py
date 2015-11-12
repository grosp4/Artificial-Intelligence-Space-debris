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
#  *                              - file_to_load   path including filename, file has to be numpy matrix, max. 4 columns
#  *                              => 2 dimensions -> x,y plotting
#  *                              => 3 dimensions -> x,y,z plotting
#  *                              => 4 dimensions -> x,y,z plotting in function of time  plotting
#  *
#  *                              - x_axes_name   name of the x axes
#  *                              - y_axes_name   name of the y axes
#  *                              - z_axes_name   name of the z axes
#  *                              - time_step     time steps in seconds for plotting, default = 0, meaning no time stepped plotting, recommended values 0.00001 < time_step < 0.01
#  *
#  *     returns:                 0
#  *     description:             draws plots  based on given parameters
#  *                              
#  *
#  *******************************************************************************/
def plotData( file_to_load = '', x_axes_name = 'x axes name', y_axes_name = 'y axes name', z_axes_name = 'z axes name ', time_step = 0):
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


                # if we dont have a time step for plotting, we just plot the result
                if time_step == 0:

                        plt.show()

                else:
                        plt.ion()
                        plt.show()

                        for time in range (dataset_size[0]):
                                plt.plot(data_y_axes,data_x_axes, '-ro')
                                plt.draw()
                                systemtime.sleep(time_step)


            # 3 dimensional -> x,y,z
            elif dataset_size[1] == 3:

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

                # if we dont have a time step for plotting, we just plot the result
                if time_step == 0:
                        #print 3 dimensional plot
                        plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                        plt.show()

                else:
                        plt.ion()
                        plt.show()

                        for time in range (dataset_size[0]):
                                plot3d.scatter(data_x_axes[time], data_y_axes[time], data_z_axes[time], c='r', marker='o')
                                plt.draw()
                                systemtime.sleep(time_step)


            # 4 dimensional -> x,y,z and a t axis
            elif dataset_size[1] == 4:

                data_x_axes = dataset[:,0]
                data_y_axes = dataset[:,1]
                data_z_axes = dataset[:,2]
                data_t_axes = dataset[:,3]

                #print 3 dimensional plot
                fig_3d = plt.figure()
                plot3d = fig_3d.add_subplot(111, projection='3d')
                plot3d.set_xlabel(x_axes_name)
                plot3d.set_ylabel(y_axes_name)
                plot3d.set_zlabel(z_axes_name)

                # if we dont have a time step for plotting, we just plot the result
                if time_step == 0:

                        #print 3 dimensional plot
                        print("no timestep!\n")
                        plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                        plt.show()

                else:
                        plt.ion()
                        plt.show()

                        for time in range (dataset_size[0]):
                                plot3d.scatter(data_x_axes[time], data_y_axes[time], data_z_axes[time], c='r', marker='o')
                                plt.draw()
                                systemtime.sleep(time_step)


            else:
                print("Debug: This file contains more than 4 dimensions and therefore it can not be drawn, Error in: %S \n", file_to_load)

    return 0
