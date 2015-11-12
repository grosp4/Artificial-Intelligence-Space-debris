__author__ = 'Pedro'
# import necessary libaries
import numpy as np
from  pyorbital.orbital import Orbital
import datetime
from filenameGenerator import generateFilename

class Dataset():

    def __init__(self):

        #satellite name
        self.satelliteName = ''

        #source directory
        self.sourceDirectory = ''

        #the number of samples to collect, which in practice means
        #how many times should the function get_position() from pyorbital
        #will be run
        self.numberOfSamples = 0

        #number of inputs of the network, in practice, number of columns of the database matrix
        self.numberOfInputs = 0

        #where the treated dataset in Numpy array will be stored
        self.dataset = None

        #diference in seconds between each point to next point of the dataset
        self.incrementSeconds = 0

    def extractDataset(self,
                       satelliteName='ISS (ZARYA)',
                       sourceDirectory=generateFilename(description = "stations",
                                                        extension = ".txt",
                                                        dateToday = False),
                       referenceDate = (2015,10,28,0,0,0),
                       numberOfSamples = 1440,
                       numberOfInputs = 4,
                       incrementSeconds = 60):

        self.satelliteName = satelliteName
        self.sourceDirectory = sourceDirectory
        self.referenceDate = referenceDate
        self.numberOfSamples = numberOfSamples
        self.numberOfInputs = numberOfInputs
        self.dataset = np.zeros(shape=[1,self.numberOfInputs])
        self.incrementSeconds = incrementSeconds
        self.min = 0
        self.max = 0
        self.min_dataset = 0
        self.max_dataset = 0

        try:
            # reading input data
            input_data = Orbital(self.satelliteName, self.sourceDirectory)

            # calculate date
            date = datetime.datetime(*self.referenceDate)

            #1440 for the number of minutes in a day
            for point_n in xrange(self.numberOfSamples):
                #each point will be collected with a specified difference of seconds
                date += datetime.timedelta(0,incrementSeconds)
                output_data = input_data.get_position(date,normalize=False)
                self.dataset = np.vstack([self.dataset, np.append(output_data[0],[point_n + referenceDate[4]])])

            self.dataset = np.delete(self.dataset,0,0)

            return 0

        except:

            return 1

    def rescale(self,column='all',factor=0.0001):
        
        #test if of wrong type
        if type(self.dataset).__module__ != np.__name__:
            return 1

        if column == 'all':
            #all columns get multiplied by a given factor
            self.dataset = self.dataset * factor
            return 0

        elif isinstance( column, int ):
            #one column gets multiplied by a given factor
            self.dataset[:, column] =  self.dataset[:, column] * factor

        else:
            return 2

    def normalize(self, normFunct = 'sigmoid', minmax = (-1,1)):

        if type(self.dataset).__module__ != np.__name__:
            return 1
        
        #default normalization function. But can be expanded to support more funcs.
        if normFunct == 'sigmoid':
            try:
                #normalization function (sigmoid)
                self.dataset = 1/(1+np.exp(-self.dataset))
                return 0

            except:
                return 2

        if normFunct == 'minmax':

            #minimum and maximum values of the normalized dataset
            self.min = minmax[0]
            self.max = minmax[1]

            try:
                #normalization function : minmax

                self.min_dataset = self.dataset.min(axis=0)
                self.max_dataset = self.dataset.max(axis=0)

                self.dataset = (self.dataset - self.min_dataset) / (self.max_dataset - self.min_dataset)

                #minmax normalization doesn't need pre-rescaled data
                # it already rescales it after standardizing
                self.dataset = self.dataset * (self.max - self.min) + self.min

                return 0

            except:
                return 3

        else:
            return 4

    def denormalize(self):

        if self.min < self.max:

            self.dataset = (self.dataset - self.min) / (self.max - self.min)

            self.dataset = self.dataset * (self.max_dataset - self.min_dataset) + self.min_dataset

            return 0

        return 1

    def saveToFile(self,filepath = generateFilename(),outputWriteMode='wb+'):

        if type(self.dataset).__module__ != np.__name__:
            return 1

        try:
            f = file(filepath,outputWriteMode)
            np.save(f,self.dataset)
            f.close()
            return 0

        except:
            return 1

    def separate(self,filepathOut = generateFilename(description="NNoutput_x_t"), filepathIn = '', columns = [0,3], outputWriteMode = 'wb+'):

        if type(columns) is not list:
            return 2

        if columns == []:
            return 3

        if filepathIn != '':
            try:
                newDataset = np.load(filepathIn)

                if type(newDataset).__module__ != np.__name__:
                    return 4

            except:
                return 5

        else:
            newDataset = self.dataset

            if type(newDataset).__module__ != np.__name__:
                return 6

        if max(columns) > newDataset.shape[1]:
            return 7

        #choose which columns should be extracted and saved
        newDataset = newDataset[:,columns]

        try:
            f = file(filepathOut,outputWriteMode)
            np.save(f,newDataset)
            f.close()
            return 0

        except:
            return 1



if __name__ =="__main__":

    def test(num=1):

        if num == 1:
            dataset = Dataset()
            treat = dataset.extractDataset()

            outputDataset = dataset.dataset
            outputSourceDirectory = dataset.sourceDirectory

            rescale = dataset.rescale()
            outputRescaled = dataset.dataset

            normalized = dataset.normalize()
            outputNormalized = dataset.dataset

            save = dataset.saveToFile()

            print "\nThis is a test to the class Dataset in module gain_dataset"

            if treat == 0:
                print "\nDataset collected from file %s" % outputSourceDirectory
                print outputDataset

            if treat == 1:
                print "\nDataset not collected. Possibly due to a problem with the input file."
                print "The directory of the .txt file with the TLE info is %s" % outputSourceDirectory

            if save == 2:
                print "\nNo data to save!"

            if rescale == 0:
                print "\nDataset rescaled!"
                print outputRescaled

            if rescale == 1:
                print "\nNo dataset to rescale!"

            if rescale == 2:
                print "\nColumn must be either 'all' or an integer!"

            if normalized == 0:
                print '\nDataset normalized!'
                print outputNormalized

            if normalized == 2:
                print '\nNo dataset to normalize!'

            if normalized == 3:
                print '\nDataset incompatible with normalization!'

            if save == 0:
                print '\nNormalized dataset saved to file: %s' % generateFilename()

            if save != 0:
                print '\nError saving normalized dataset to file!'

        if num == 2:
            dataset = Dataset()
            treat = dataset.extractDataset()
            outputDataset = dataset.dataset
            outputSourceDirectory = dataset.sourceDirectory

            normalized = dataset.normalize(normFunct='minmax')
            outputNormalized = dataset.dataset

            denormalized = dataset.denormalize()
            outputDenormalized = dataset.dataset

            print "\nThis is a test to the class Dataset in module gain_dataset"

            if treat == 0:
                print "\nDataset collected from file %s" % outputSourceDirectory
                print outputDataset

            if treat == 1:
                print "\nDataset not collected. Possibly due to a problem with the input file."
                print "The directory of the .txt file with the TLE info is %s" % outputSourceDirectory

            if normalized == 0:
                print "\nNormalized dataset (-1 to 1) with minmax: "
                print  outputNormalized

            if normalized == 1:
                print "\nError normalizing dataset."

            if normalized == 2:
                print '\nNo dataset to normalize!'

            if normalized == 3:
                print '\nDataset incompatible with normalization!'

            if denormalized == 0:
                print '\nDataset denormalized!'
                print outputDenormalized

            if denormalized == 1:
                print '\nError denormalizing dataset!'

        if num == 3:
            dataset = Dataset()
            treat = dataset.extractDataset()
            outputDataset = dataset.dataset
            outputSourceDirectory = dataset.sourceDirectory

            separate = dataset.separate()
            sepFile = generateFilename(description='NNoutput_x_t')
            sepDataset = np.load(sepFile)

            print "\nThis is a test to the class Dataset in module gain_dataset"

            if treat == 0:
                print "\nDataset collected from file %s" % outputSourceDirectory
                print outputDataset

            if treat == 1:
                print "\nDataset not collected. Possibly due to a problem with the input file."
                print "The directory of the .txt file with the TLE info is %s" % outputSourceDirectory

            if separate == 0:
                print '\nDataset separated to file : %s\n' %sepFile
                print sepDataset

            if separate != 0:
                print '\nError separating dataset!'

    test(3)