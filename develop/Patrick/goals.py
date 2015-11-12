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
    compareDesiredAndTrainedData_x_t=[pedro.generateFilename("","outputDataset_x_t",".npy",True), pedro.generateFilename("","outputDataset_y_t",".npy",True), pedro.generateFilename("","inputDataset",".npy",True)]
    compareDesiredAndTrainedData_y_t =[pedro.generateFilename("","outputDataset_y_t",".npy",True), pedro.generateFilename("","outputDataset_x_t",".npy",True)]
    compareDesiredAndTrainedData_z_t =[pedro.generateFilename("","outputDataset_z_t",".npy",True), pedro.generateFilename("","outputDataset_x_t",".npy",True)]

    compareDesiredAndTrainedData_3D =[pedro.generateFilename("","outputDataset",".npy",True), pedro.generateFilename("","inputDataset",".npy",True)]


    desired_data_output_x_t =[pedro.generateFilename("","outputDataset_x_t",".npy",True)]
    x_names =["X", "X","X"]
    y_names =["y", "y","X"]
    z_names =["z", "z","X"]
    t_names =[0,0,0]


    outputFileNameY = pedro.generateFilename("","inputDataset_y_t",".npy",True)
    outputFileNameZ = pedro.generateFilename("","inputDataset_z_t",".npy",True)
    outputFileNameX = pedro.generateFilename("","inputDataset_x_t",".npy",True)
    outputFileNameX = pedro.generateFilename("","inputDataset_x_t",".npy",True)


    list_of_elements = [r"D:\private stuff\Wroclaw University of Technology\Materials\advanced_topics_in_artificial_intelligence\Exercise\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\inputDataset_x_t_20151112.npy"]
    PlotDataset.plotData(compareDesiredAndTrainedData_x_t,x_names,y_names, z_names,t_names)
    #PlotDataset.plotData(compareDesiredAndTrainedData_3D, x_names, y_names, z_names, t_names)





if __name__ == "__main__":

    name = pedro.generateFilename("","dataset",".npy",True)
    print name
    plotData(0)