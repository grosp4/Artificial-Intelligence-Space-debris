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

    def saveToFile(self,filename=''):

        if not (self.dataset == np.zeros(self.numberOfInputs)).all():

            if not filename == '':
                self.setDatasetMatrixFile(filename)

            try:
                f = file(self.getDatasetMatrixFile(),self.getOutputWriteMode())
                np.save(f,self.dataset)

                return 0

            except:
                return 1

        else:
            return 2

    def normalize(self,filename=''):
        if filename == '':
            if not (self.dataset == np.zeros(self.numberOfInputs)).all():
                dataset = self.dataset

            else:
                return 2

        else:
            try:
                dataset = np.load(filename)

            except:
                return 1

        try:
            #normalization function
            self.dataset = 1/(1+np.exp(-self.dataset))
            return 0

        except:
            return 3

    def rescale(self,column='all',factor=0.001):
        if not (self.dataset == np.zeros(self.numberOfInputs)).all():
            if column == 'all':
                #all columns get multiplied by a given factor
                self.dataset = self.dataset * factor
                return 0

            elif isinstance( column, int ):
                #one column gets multiplied by a given factor
                for i in self.data:
                    i[column] = i[column] * factor
            else:
                return 2
        else:
            return 1


if __name__ =="__main__":

    dataset = Dataset()
    treat = dataset.extractDataset()
    save = dataset.saveToFile()

    outputDataset1 = dataset.dataset
    outputSourceDirectory1 = dataset.getSourceDirectory()
    outputDataMatrixFile1 = dataset.getDatasetMatrixFile()

    rescale = dataset.rescale()
    outputRescaled = dataset.dataset
    save_rescaled = dataset.saveToFile(generateFilename(author='Pedro',description='datasetRescaled',extension='.npy',dateToday=True))
    outputDataMatrixFile3 = dataset.getDatasetMatrixFile()

    normalized = dataset.normalize()
    save_normalized = dataset.saveToFile(generateFilename(author='Pedro',description='datasetNormalized',extension='.npy',dateToday=True))
    outputDataset2 = dataset.dataset
    outputDataMatrixFile2 = dataset.getDatasetMatrixFile()

    print "\nThis is a test to the class Dataset in module gain_dataset"

    if treat == 0:
        print "\nDataset collected from file %s" % outputDataset1
        print outputDataset1

    if treat == 1:
        print "\nDataset not collected. Possibly due to a problem with the input file."
        print "The directory of the .txt file with the TLE info is %s" % outputSourceDirectory1

    if save == 0:
        print "\nDataset saved to directory %s" % outputDataMatrixFile1

    if save == 1:
        print "\nProblem saving the dataset matrix to a file."
        print "It should have been stored in : %s" % outputDataMatrixFile1

    if save == 2:
        print "\nNo data to save!"

    if rescale == 0:
        print "\nDataset rescaled!"
        print outputRescaled

    if rescale == 1:
        print "\nNo dataset to rescale!"

    if rescale == 2:
        print "\nColumn must be either 'all' or an integer!"

    if save_rescaled == 0:
        print "\nRescaled data saved to file %s" % dataset.getDatasetMatrixFile()

    if save_rescaled != 0:
        print "\nError saving rescaled dataset!"

    if normalized == 0:
        print '\nDataset normalized!'
        print outputDataset2

    if normalized == 1:
        print '\nProblem opening file!'

    if normalized == 2:
        print '\nNo dataset to normalize!'

    if normalized == 3:
        print '\nDataset incompatible with normalization!'

    if save_normalized == 0:
        print '\nNormalized dataset saved to file: %s' % outputDataMatrixFile2

    if save_normalized != 0:
        print '\nError saving normalized file!'

