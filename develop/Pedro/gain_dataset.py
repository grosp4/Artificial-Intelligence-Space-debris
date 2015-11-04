__author__ = 'Pedro'
# import necessary libaries
import numpy as np
from  pyorbital.orbital import Orbital
import datetime
from filenameGenerator import generateFilename

class Dataset():

    def __init__(self,
                 satelliteName='ISS (ZARYA)',
                 sourceDirectory=generateFilename(description="stations",extension=".txt",dateToday=False),
                 datasetMatrixFile=generateFilename(),
                 outputWriteMode='wb+',
                 numberOfSamples=1440,
                 dataset=None,
                 numberOfInputs=4
                 ):

        #satellite name
        self.satelliteName = satelliteName

        #source directory
        self.sourceDirectory = sourceDirectory

        #directory of the file where the dataset matrix will be stored
        self.datasetMatrixFile = datasetMatrixFile

        #the mode in which the system will write the file with (r+,w,wb,wb+,etc..)
        self.outputWriteMode = outputWriteMode

        #the number of samples to collect, which in practice means
        #how many times should the function get_position() from pyorbital
        #will be run
        self.numberOfSamples = numberOfSamples

        #number of inputs of the network, in practice, number of columns of the database matrix
        self.numberOfInputs = numberOfInputs

        #where the treated dataset in Numpy array will be stored
        self.dataset = np.zeros(self.numberOfInputs)

    def setSatelliteName(self,name):
        self.satelliteName = name

    def getSatelliteName(self):
        return self.satelliteName

    def setSourceDirectory(self,directory):
        self.sourceDirectory = directory

    def getSourceDirectory(self):
        return self.sourceDirectory

    def setDatasetMatrixFile(self,directory):
        self.datasetMatrixFile = directory

    def getDatasetMatrixFile(self):
        return self.datasetMatrixFile

    def setOutputWriteMode(self,mode):
        self.outputWriteMode = mode

    def getOutputWriteMode(self):
        return self.outputWriteMode

    def setNumberOfSamples(self,number):
        self.numberOfSamples = number

    def getNumberOfSamples(self):
        return self.numberOfSamples

    def setNumberOfInputs(self,number):
        self.numberOfInputs = number

    def getNumberOfInputs(self):
        return self.numberOfInputs

    def extractDataset(self):

        #generate dataset
        self.dataset = np.zeros(shape=[1,self.getNumberOfInputs()])

        try:
            # reading input data
            input_data = Orbital(self.getSatelliteName(),self.getSourceDirectory())

            # calculate data
            reference_date = datetime.datetime(2015,10,28,0,0,0)

            #1440 for the number of minutes in a day
            for step in xrange(self.getNumberOfSamples()):
                #increment the time step in 60 seconds
                reference_date += datetime.timedelta(0,60)
                output_data = input_data.get_position(reference_date,normalize=False)
                self.dataset = np.vstack([self.dataset, np.append(output_data[0],[step])])
                #dataset.append(output_data[0])

            self.dataset = np.delete(self.dataset,0,0)

            return 0

        except:

            return 1

    def saveToFile(self):

        if not (self.dataset == np.zeros(self.numberOfInputs)).all():
            try:
                f = file(self.getDatasetMatrixFile(),self.getOutputWriteMode())
                np.save(f,self.dataset)

                return 0

            except:
                return 1

        else:
            return 2

if __name__ =="__main__":

    dataset = Dataset()
    treat = dataset.extractDataset()
    save = dataset.saveToFile()

    print "\nThis is a test to the class Dataset in module gain_dataset"

    if treat == 0:
        print "\nDataset collected from file %s" % dataset.getSourceDirectory()
        print dataset.dataset

    if treat == 1:
        print "\nDataset not collected. Possibly due to a problem with the input file."
        print "The directory of the .txt file with the TLE info is %s" % dataset.getSourceDirectory()

    if save == 0:
        print "\nDataset saved to directory %s" % dataset.getDatasetMatrixFile()

    if save == 1:
        print "\nProblem saving the dataset matrix to a file."
        print "It should have been stored in : %s" % dataset.getDatasetMatrixFile()

    if save == 2:
        print "\nNo data to save!"