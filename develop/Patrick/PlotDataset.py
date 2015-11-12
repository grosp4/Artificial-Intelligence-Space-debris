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
#  *                              - list_of_FilesToLoad   list of paths including filename, file has to be numpy matrix, max. 4 columns
#  *                              => 2 dimensions -> x,y plotting
#  *                              => 3 dimensions -> x,y,z plotting
#  *                              => 4 dimensions -> x,y,z plotting in function of time  plotting
#  *                                has to be the same length as all other parameters
#  *
#  *                              - list_of_x_AxesNames     list of names of the x axes, has to be the same length as all other parameters
#  *                              - list_of_y_AxesNames     list of names of the y axes, has to be the same length as all other parameters
#  *                              - list_of_z_AxesNames     list of names of the z axes, has to be the same length as all other parameters
#  *                              - list_of_timeStepValues  list of time steps in seconds for plotting, default = 0, meaning no time stepped plotting, recommended values 0.00001 < time_step < 0.01
#  *                                                        has to be the same length as all other parameters
#  *     returns:                 0
#  *     description:             by passing an array / list of data you can create several drawings in one plot.
#  *                              Keep in mind: indexes have to be equal for the same "draw" of a plot.
#  *
#  *
#  *******************************************************************************/
def plotData( list_of_FilesToLoad , list_of_x_AxesNames, list_of_y_AxesNames , list_of_z_AxesNames , list_of_TimeStepValues ):
    plt.close("all")


    # check if the list filenames is bigger than zero and if all list have the same length
    if len(list_of_FilesToLoad) == 0        or( len(list_of_FilesToLoad)!= len(list_of_x_AxesNames)
                                            and len(list_of_FilesToLoad)!= len(list_of_y_AxesNames)
                                            and len(list_of_FilesToLoad)!= len(list_of_z_AxesNames)
                                            and len(list_of_FilesToLoad)!= len(list_of_TimeStepValues)
                                            ):

            print("Error in PlotDataset, no filename(s) specified or given parameters have different list length, please check your parameters\n")

    else:

            #create figures and subplots
            fig_2d = plt.figure()
            plot2d= fig_2d.add_subplot(111)

            #prepare for 3D plot
            fig_3d = plt.figure()
            plot3d = fig_3d.add_subplot(111, projection='3d')

            # initialize index
            currentListElement = 0

            # print as long as we have elements in our list
            while currentListElement <len(list_of_FilesToLoad) :

                    dataset = numblibrary.load(list_of_FilesToLoad[currentListElement])


                    # check if all values in dataset are zero
                    if  numblibrary.all(dataset == 0):
                            print("Error in PlotDataset, contains invalid data \n")
                            print('Pathname in PlotData path is: %S \n', list_of_FilesToLoad[currentListElement])

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
                                    plt.xlabel(list_of_x_AxesNames[currentListElement])
                                    plt.ylabel(list_of_y_AxesNames[currentListElement])


                                    # if we dont have a time step for plotting, we just plot the result
                                    if list_of_TimeStepValues[currentListElement] == 0:
                                             if currentListElement == 0:
                                                        plot2d.plot(data_y_axes,data_x_axes, 'r*')
                                             elif currentListElement == 1:
                                                        plot2d.plot(data_y_axes,data_x_axes, 'gs')
                                             elif currentListElement == 2:
                                                        plot2d.plot(data_y_axes,data_x_axes, 'b.')
                                             elif currentListElement <= 3:
                                                        plot2d.plot(data_y_axes,data_x_axes, 'm.')


                                    else:
                                            plt.ion()
                                            plt.show()

                                            for time in range (dataset_size[0]):
                                                    plt.plot(data_y_axes,data_x_axes, '-ro')
                                                    plt.draw()
                                                    systemtime.sleep(list_of_TimeStepValues[currentListElement])

                                    plt.close(fig_3d)
                            # 3 dimensional -> x,y,z
                            elif dataset_size[1] == 3:

                                    data_x_axes = dataset[:,0]
                                    data_y_axes = dataset[:,1]
                                    data_z_axes = dataset[:,2]

                                    #print 3 dimensional plot
                                    fig_3d = plt.figure()
                                    plot3d = fig_3d.add_subplot(111, projection='3d')
                                    plot3d.set_xlabel(list_of_x_AxesNames[currentListElement])
                                    plot3d.set_ylabel(list_of_y_AxesNames[currentListElement])
                                    plot3d.set_zlabel(list_of_z_AxesNames[currentListElement])

                                    # if we dont have a time step for plotting, we just plot the result
                                    if list_of_TimeStepValues[currentListElement] == 0:
                                            #print 3 dimensional plot

                                            if currentListElement == 0:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                                            elif currentListElement == 1:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='g', marker='*')
                                            elif currentListElement == 2:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='m', marker='x')
                                            elif currentListElement <= 3:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='b', marker='.')

                                    else:
                                            plt.ion()
                                            plt.show()

                                            for time in range (dataset_size[0]):
                                                    plot3d.scatter(data_x_axes[time], data_y_axes[time], data_z_axes[time], c='r', marker='o')
                                                    plt.draw()
                                                    systemtime.sleep(list_of_TimeStepValues[currentListElement])

                                    plt.close(fig_2d)
                            # 4 dimensional -> x,y,z and a t axis
                            elif dataset_size[1] == 4:

                                    data_x_axes = dataset[:,0]
                                    data_y_axes = dataset[:,1]
                                    data_z_axes = dataset[:,2]
                                    data_t_axes = dataset[:,3]

                                    #print 3 dimensional plot
                                    plot3d.set_xlabel(list_of_x_AxesNames[currentListElement])
                                    plot3d.set_ylabel(list_of_y_AxesNames[currentListElement])
                                    plot3d.set_zlabel(list_of_z_AxesNames[currentListElement])

                                    # if we dont have a time step for plotting, we just plot the result
                                    if list_of_TimeStepValues[currentListElement] == 0:

                                            #print 3 dimensional plot
                                            print("no timestep!\n")
                                            if currentListElement == 0:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='r', marker='o')
                                            elif currentListElement == 1:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='g', marker='*')
                                            elif currentListElement == 2:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='m', marker='x')
                                            elif currentListElement <= 3:
                                                         plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c='b', marker='.')

                                    else:
                                            plt.ion()
                                            plt.show()

                                            for time in range (dataset_size[0]):
                                                    plot3d.scatter(data_x_axes[time], data_y_axes[time], data_z_axes[time], c='r', marker='o')
                                                    plt.draw()
                                                    systemtime.sleep(list_of_TimeStepValues[currentListElement])
                                    plt.close(fig_2d)


                            else:
                                print("Debug: This file contains more than 4 dimensions and therefore it can not be drawn, Error in: %S \n", file_to_load)
                    #increase loop counter
                    currentListElement+= 1
            # if time was zero, we print all graphics in one plot

    if list_of_TimeStepValues[currentListElement-1] == 0:
            plt.show()


    return 0


if __name__ == "__main__":

        TESTlist_of_FilesToLoad = [ [1,2,3,4] ,[1,2,3,4], [1,2,3,4], [1,2,3,4] ]
        fil_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",
                            r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",
                            r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",
                            r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy"
                            ]
        TESTlist_of_x_AxesNames = [ "Xasdf" ,"Xasdf", "Xasdf", "Xasdf" ]
        TESTlist_of_y_AxesNames = [ "Yasdf" ,"Yasdf", "Yasdf", "Yasdf" ]
        TESTlist_of_z_AxesNames = [ "Zasdf" ,"Zasdf", "Zasdf", "Zasdf" ]
        TESTlist_of_TimeStepValues = [0 , 0, 0, 0]

        dataset_1 = numblibrary.load(fil_for_function[0])
        dataset_2 = numblibrary.load(fil_for_function[1])
        dataset_3 = numblibrary.load(fil_for_function[2])
        dataset_4 = numblibrary.load(fil_for_function[3])

        plotData( fil_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames , TESTlist_of_TimeStepValues )