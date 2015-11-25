__author__ = 'Patrick'


from Patrick import *
from Pedro import *

#  ******************************************************************************/
# /*
#  *     functionname:          plotData
#  *     parameter:
#  *
#  *
#  *
#  *     returns:
#  *     description:           this functions calls all functions to generate the plots
#  *
#  *
#  *******************************************************************************/
def plotData (debug = 0 ):


    # generate list of elements to compare calculation and training
    #right now these values are freely choosen, to check if everything works
    compareDesiredAndTrainedData_x_t= [pedro.generateFilename("","outputDataset_x_t",".npy",True), pedro.generateFilename("","denormResultsNN_x_t",".npy",True)]
    compareDesiredAndTrainedData_y_t =[pedro.generateFilename("","outputDataset_y_t",".npy",True), pedro.generateFilename("","denormResultsNN_y_t",".npy",True)]
    compareDesiredAndTrainedData_z_t =[pedro.generateFilename("","outputDataset_z_t",".npy",True), pedro.generateFilename("","denormResultsNN_z_t",".npy",True)]

    compareDesiredAndTrainedData_3D =[pedro.generateFilename("","outputDataset",".npy",True), pedro.generateFilename("","denormResultsNN",".npy",True)]


    desired_data_output_x_t =[pedro.generateFilename("","outputDataset_x_t",".npy",True)]
    x_names =["X", "t"]
    y_names =["y", "y"]
    z_names =["z", "z"]
    t_names =[0,0]


    outputFileNameY = pedro.generateFilename("","inputDataset_y_t",".npy",True)
    outputFileNameZ = pedro.generateFilename("","inputDataset_z_t",".npy",True)
    outputFileNameX = pedro.generateFilename("","inputDataset_x_t",".npy",True)
    outputFileNameX = pedro.generateFilename("","inputDataset_x_t",".npy",True)


    PlotDataset.plotData(compareDesiredAndTrainedData_x_t, x_names, y_names, z_names,t_names,0)
    x_names =["X", "t"]
    y_names =["y", "y"]
    z_names =["z", "z"]
    t_names =[0,0]
    PlotDataset.plotData(compareDesiredAndTrainedData_y_t, x_names, y_names, z_names,t_names,0)
    x_names =["X", "t"]
    y_names =["y", "z"]
    z_names =["z", "z"]
    t_names =[0,0]
    PlotDataset.plotData(compareDesiredAndTrainedData_z_t, x_names, y_names, z_names,t_names,0)
    x_names =["X", "x"]
    y_names =["y", "y"]
    z_names =["z", "z"]
    t_names =[0,0]
    PlotDataset.plotData(compareDesiredAndTrainedData_3D, x_names, y_names, z_names, t_names,0)
    x_names =["iterations"]
    y_names =["Percentage"]
    z_names =["z"]
    t_names =[0]
    test = [pedro.generateFilename("","errorsNN",".npy",True)]
    newMatrix = numblibrary.load(pedro.generateFilename("","errorsNN",".npy",True))
    newMatrix = newMatrix.T
    np.save(generateFilename(description="transposed"),newMatrix)
    PlotDataset.plotData(test, x_names, y_names, z_names, t_names,0)




if __name__ == "__main__":

    name = pedro.generateFilename("","dataset",".npy",True)
    print name
    plotData(0)