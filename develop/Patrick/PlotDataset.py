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
import numpy as numblibrary


#  ******************************************************************************/
# /*
#  *     functionname:          @ plotData
#  *     parameter:
#  *     :             @ list_of_FilesToLoad, amount of plots you want to plot into ONE plot!
#  *     :             @ list_of_x_AxesName, z axes name
#  *     :             @ list_of_y_AxesName, y axes name
#  *     :             @ list_of_z_AxesName, z axes name
#  *     :             @ plotmode, 0 = 2D mode, 1 = 3D Mode
#  *     :             @ newplot , 0 = no new plots, you will plot into the old plot
#  *
#  *     returns:               @ 0, or and error message in console
#  *     description:           @ creates 2D or 3D plots on given data
#  *
#  *
#  *******************************************************************************/
#  *
#  *
#  *******************************************************************************/
def plotData( list_of_FilesToLoad = None, list_of_x_AxesName = "x Axes", list_of_y_AxesName = "Y Axes" , list_of_z_AxesName = "Z Axes" , list_of_t_AxesName = "time axes", plotmode = 0, newPlot = 0 ):
    # initialize index

    currentListElement = 0
    # check if the list of filenames has an entry
    if list_of_FilesToLoad == None :
            print("Error in PlotDataset, no files supplied, please provide at least one [;,2] numpy matrix file! \n")
            error = 1

    # if we have entries we will plot them
    else:
            error = 0
            #if we want new plots, we close all old ones
            if newPlot == 1:
                    plt.close("all")

            figure = plt.figure()

            # print as long as we have elements in our list
            while currentListElement <len(list_of_FilesToLoad) :
                    dataset = numblibrary.load(list_of_FilesToLoad[currentListElement])

                    # check if all values in dataset are zero
                    if numblibrary.all(dataset == 0):
                            print("Error in PlotDataset, contains invalid data \n")
                            print('Pathname in PlotData path is: %S \n', list_of_FilesToLoad[currentListElement])
                            error = 1
                            break

                    # if dataset contains values, we have a valid file, if not abort
                    else:
                            #  decide wether the matrix is 1, 2, 3, 4 dimensional -> specify plot
                            dataset_size = dataset.shape
                            if debug:
                                    print (dataset_size[1], currentListElement)

                            # for multiplotting, change color
                            if currentListElement == 0:
                                    symbolInPlot = 'r*'

                            elif currentListElement == 1:
                                    symbolInPlot = 'c.'

                            elif currentListElement == 2:
                                    symbolInPlot = 'b.'

                            else:
                                    symbolInPlot = 's*'

                            # 2 dimensional -> x,y
                            if dataset_size[1] == 2:

                                    if plotmode == 0:
                                            plot2d= figure.add_subplot(111)
                                            data_x_axes = dataset[:, 0]
                                            data_y_axes = dataset[:, 1]

                                            #Draw 2 dim diagram
                                            plt.xlabel(list_of_x_AxesName)
                                            plt.ylabel(list_of_y_AxesName)

                                            plot2d.plot(data_y_axes,data_x_axes, symbolInPlot, label="Output Dataset")

                                    #refuse 3D Plot
                                    if plotmode == 1:
                                            print("This function can not plot 2D Data (x,t) in 3D \n")
                                            error = 1
                                            break

                            # 3 dimensional -> x,y,t
                            elif dataset_size[1] == 3:
                                    #generate two subplots for x to z and y to z correlation
                                    if plotmode == 0:
                                            plot2d_x= figure.add_subplot(111)
                                            plot2d_y= figure.add_subplot(121)
                                            data_x_axes = dataset[:, 0]
                                            data_y_axes = dataset[:, 1]
                                            data_z_axes = dataset[:, 2]

                                            #Draw 2 dim diagram
                                            plt.xlabel(list_of_x_AxesName)
                                            plt.ylabel(list_of_y_AxesName)

                                            plot2d_x.plot(data_z_axes, data_x_axes, symbolInPlot, label=" to TBD")
                                            plot2d_y.plot(data_z_axes, data_y_axes, symbolInPlot, label=" to TBD")

                                    #refuse 3D Plot
                                    if plotmode == 1:
                                            print("This function can not plot 2D Data (x,y,t) in 3D \n")
                                            error = 1
                                            break

                            # 3 dimensional -> x,y,z,t, plotting without time function (time is indizes of length of elements)
                            elif dataset_size[1] == 4:

                                    data_x_axes = dataset[:, 0]
                                    data_y_axes = dataset[:, 1]
                                    data_z_axes = dataset[:, 2]
                                    data_t_axes = dataset[:, 3]

                                    #generate two subplots for x to z and y to z correlation
                                    if plotmode == 0:
                                            if debug:
                                                    print "2D Mode active"

                                            plot2d_x= figure.add_subplot(311)
                                            plot2d_y= figure.add_subplot(312)
                                            plot2d_z= figure.add_subplot(313)
                                            plt.tight_layout()

                                            #Draw 2 dim diagram
                                            plot2d_x.set_ylabel(list_of_x_AxesName)
                                            plot2d_y.set_ylabel(list_of_y_AxesName)
                                            plot2d_z.set_ylabel(list_of_z_AxesName)
                                            plt.xlabel(list_of_t_AxesName)

                                            plot2d_x.plot(data_t_axes, data_x_axes, symbolInPlot, label=" to TBD")
                                            plot2d_y.plot(data_t_axes, data_y_axes, symbolInPlot, label=" to TBD")
                                            plot2d_z.plot(data_t_axes, data_z_axes, symbolInPlot, label=" to TBD")

                                    #if 3D has been requested
                                    else:
                                            if debug:
                                                    print "3D Mode active"

                                            plot3d =figure.add_subplot(111, projection='3d')
                                            plot3d.scatter(data_x_axes, data_y_axes, data_z_axes, c= 'r', marker='o')
                                            plot3d.set_ylabel(list_of_x_AxesName)
                                            plot3d.set_ylabel(list_of_y_AxesName)
                                            plot3d.set_ylabel(list_of_z_AxesName)
                    currentListElement+= 1

            if error == 0:
                    plt.show()
            plt.legend("")

    return 0

# DEBUG MAIN #
if __name__ == "__main__":

        # debug variables
        debug = 1
        version = 3

        #version 1: 2D Tests  without new plot, 2 times max, 2Dim x,t only
        if version == 1:
                newplot = 0
                plotmode = 0

                TESTlist_of_x_AxesNames = [ "Xasdf" ]
                TESTlist_of_y_AxesNames = [ "Yasdf" ]
                TESTlist_of_z_AxesNames = [ "Zasdf" ]
                TESTlist_of_t_AxesNames = [ "Tasdf" ]

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_x_t_20151112.npy",r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_y_t_20151112.npy"]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames , TESTlist_of_t_AxesNames, plotmode, newplot )

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_x_t_20151112.npy",r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_y_t_20151112.npy"]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames ,TESTlist_of_t_AxesNames, plotmode, newplot )


        #version 2: 2D Tests  new plot, 1 times max, 3 Dim x,y,z,t
        if version == 2:
                newplot = 0
                plotmode = 0

                TESTlist_of_x_AxesNames = [ "Xasdf" ]
                TESTlist_of_y_AxesNames = [ "Yasdf" ]
                TESTlist_of_z_AxesNames = [ "Zasdf" ]
                TESTlist_of_t_AxesNames = [ "Tasdf" ]

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames ,TESTlist_of_t_AxesNames, plotmode, newplot )


        #version 3: 2D Tests  without new plot, 2 times max, 3 Dim x,y,z,t
        if version == 3:
                newplot = 0
                plotmode = 0

                TESTlist_of_x_AxesNames = [ "Xasdf" ]
                TESTlist_of_y_AxesNames = [ "Yasdf" ]
                TESTlist_of_z_AxesNames = [ "Zasdf" ]
                TESTlist_of_t_AxesNames = [ "Tasdf" ]

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\denormResultsNN_20151112.npy"]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames ,TESTlist_of_t_AxesNames, plotmode, newplot )


        #version 4: 3D Tests  without new plot, 2 times max, 3 Dim x,y,z,t
        if version == 4:
                newplot = 0
                plotmode = 1

                TESTlist_of_x_AxesNames = [ "Xasdf" ]
                TESTlist_of_y_AxesNames = [ "Yasdf" ]
                TESTlist_of_z_AxesNames = [ "Zasdf" ]
                TESTlist_of_t_AxesNames = [ "Tasdf" ]

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_20151112.npy",r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\denormResultsNN_20151112.npy"]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames ,TESTlist_of_t_AxesNames, plotmode, newplot )

        #version 5: 2D Tests  without new plot, 1 time max, 3Dim x,t only
        if version == 5:
                newplot = 0
                plotmode = 1

                TESTlist_of_x_AxesNames = [ "Xasdf" ]
                TESTlist_of_y_AxesNames = [ "Yasdf" ]
                TESTlist_of_z_AxesNames = [ "Zasdf" ]
                TESTlist_of_t_AxesNames = [ "Tasdf" ]

                file_2D_for_function = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_x_t_20151112.npy",r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_y_t_20151112.npy"]
                plotData( file_2D_for_function , TESTlist_of_x_AxesNames, TESTlist_of_y_AxesNames , TESTlist_of_z_AxesNames , TESTlist_of_t_AxesNames, plotmode, newplot )

        #version 6: without parameters
        if version == 6:

                plotData()




