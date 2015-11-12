__author__ = 'Pedro'

from gain_dataset import Dataset
from filenameGenerator import generateFilename
from Pedro.neuralNetwork import NN
from Patrick import *

def collectDataset(version = 3, verbose = False):

    completed = 1

    #collects dataset (input and output) with sigmoid normalization (rescaling factor of 0.0001)
    if version == 1:

        inputDataset = Dataset()
        outputDataset = Dataset()

        inputFilePath = generateFilename(description='inputDataset')
        outputFilePath = generateFilename(description='outputDataset')

        extractInDataset = inputDataset.extractDataset()
        extractedInMatrix = inputDataset.dataset

        rescaleInDataset = inputDataset.rescale()
        extractedInRescaled = inputDataset.dataset

        normalizeInDataset = inputDataset.normalize()
        extractedInNormalized = inputDataset.dataset

        saveInDataset = inputDataset.saveToFile(inputFilePath)

        extractOutDataset = outputDataset.extractDataset(referenceDate=(2015,10,28,0,1,0))
        extractedOutMatrix = outputDataset.dataset

        rescaleOutDataset = outputDataset.rescale()
        extractedOutRescaled = outputDataset.dataset

        normalizeOutDataset = outputDataset.normalize()
        extractedOutNormalized = outputDataset.dataset

        saveOutDataset = outputDataset.saveToFile(outputFilePath)

        #if all of the tasks succeeded (all the methods returned 0), the goal is completed
        if not (extractInDataset
                or rescaleInDataset
                or normalizeInDataset
                or saveInDataset
                or extractOutDataset
                or rescaleOutDataset
                or normalizeOutDataset
                or saveOutDataset):

            completed = 0

        #in verbose mode, all important variables are printed
        if verbose:

            print "Version 1 of goal: Collect Dataset"
            print
            print "Input file path: %s" % inputFilePath
            print "Output file path: %s" % outputFilePath
            print

            if not extractInDataset:
                print extractedInMatrix
                print "Input dataset successfully extracted!"
            if extractInDataset:
                print "Problem extracting input dataset!"

            if not rescaleInDataset:
                print extractedInRescaled
                print "Input dataset successfully rescaled!"
            if rescaleInDataset:
                print "Problem rescaling input dataset!"

            if not normalizeInDataset:
                print extractedInNormalized
                print "Input dataset successfully normalized!"
            if normalizeInDataset:
                print "Problem normalizing input dataset!"

            if not saveInDataset:
                print "Input dataset saved!"
            if saveInDataset:
                print "Problem saving input dataset!"

            if not extractOutDataset:
                print extractedOutMatrix
                print "Output dataset successfully extracted!"
            if extractOutDataset:
                print "Problem extracting output dataset!"

            if not rescaleOutDataset:
                print extractedOutRescaled
                print "Output dataset successfully rescaled!"
            if rescaleOutDataset:
                print "Problem rescaling output dataset!"

            if not normalizeOutDataset:
                print extractedOutNormalized
                print "Output dataset successfully normalized!"
            if normalizeOutDataset:
                print "Problem normalizing output dataset!"

            if not saveOutDataset:
                print "Output dataset saved!"
            if saveOutDataset:
                print "Problem saving output dataset!"

            if not completed:
                print "Data collection completed!"
            if completed:
                print "\n\n>>>> Data collection not completed! <<<<"

        return completed

    #collects dataset (input and output) with minmax normalization function
    if version == 2:

        inputDataset = Dataset()
        outputDataset = Dataset()

        inputFilePath = generateFilename(description='minmaxinputDataset')
        outputFilePath = generateFilename(description='minmaxoutputDataset')

        extractInDataset = inputDataset.extractDataset()
        extractedInMatrix = inputDataset.dataset

        normalizeInDataset = inputDataset.normalize(normFunct='minmax')
        extractedInNormalized = inputDataset.dataset

        saveInDataset = inputDataset.saveToFile(inputFilePath)

        extractOutDataset = outputDataset.extractDataset(referenceDate=(2015,10,28,0,1,0))
        extractedOutMatrix = outputDataset.dataset

        normalizeOutDataset = outputDataset.normalize(normFunct='minmax')
        extractedOutNormalized = outputDataset.dataset

        saveOutDataset = outputDataset.saveToFile(outputFilePath)

        #if all of the tasks succeeded (all the methods returned 0), the goal is completed
        if not (extractInDataset
                or normalizeInDataset
                or saveInDataset
                or extractOutDataset
                or normalizeOutDataset
                or saveOutDataset):

            completed = 0

        if verbose:

            print "Version 2 of goal: Collect Dataset"
            print
            print "Input file path: %s" % inputFilePath
            print "Output file path: %s" % outputFilePath
            print

            if not extractInDataset:
                print extractedInMatrix
                print "Input dataset successfully extracted!"
            if extractInDataset:
                print "Problem extracting input dataset!"

            if not normalizeInDataset:
                print extractedInNormalized
                print "Input dataset successfully normalized!"
            if normalizeInDataset:
                print "Problem normalizing input dataset!"

            if not saveInDataset:
                print "Input dataset saved!"
            if saveInDataset:
                print "Problem saving input dataset!"

            if not extractOutDataset:
                print extractedOutMatrix
                print "Output dataset successfully extracted!"
            if extractOutDataset:
                print "Problem extracting output dataset!"

            if not normalizeOutDataset:
                print extractedOutNormalized
                print "Output dataset successfully normalized!"
            if normalizeOutDataset:
                print "Problem normalizing output dataset!"

            if not saveOutDataset:
                print "Output dataset saved!"
            if saveOutDataset:
                print "\n>>> Problem saving output dataset! <<<"

            if not completed:
                print "Data collection completed!"
            if completed:
                print "\n\n>>>> Data collection not completed! <<<<"

    if version == 3:

        inputDataset = Dataset()

        #Extract Input Dataset
        satelliteName = 'ISS (ZARYA)'
        inputDataFilepath = generateFilename(description = "stations", extension = ".txt", dateToday = False)
        referenceDate = (2015,10,28,0,0,0)
        numberOfSamples = 1440
        numberOfInputs = 4
        incrementSeconds = 60

        extractInDataset = inputDataset.extractDataset(satelliteName,inputDataFilepath,referenceDate,numberOfSamples,numberOfInputs,incrementSeconds)
        extractedInMatrix = inputDataset.dataset

        #Save Input Dataset
        inputFilePath = generateFilename(description='inputDataset')
        saveInDataset = inputDataset.saveToFile(inputFilePath)

        #Normalize Input Dataset
        normMethod = 'minmax'
        minmaxValues = (-1,1)
        normInput = inputDataset.normalize(normMethod,minmaxValues)
        normInMatrix = inputDataset.dataset

        #Save Normalized Input Values
        normInFilePath = generateFilename(description='normInputDataset')
        saveNormInput = inputDataset.saveToFile(normInFilePath)

        #===============================

        outputDataset = Dataset()

        #Extract Ouput Dataset
        satelliteName = 'ISS (ZARYA)'
        inputDataFilepath = generateFilename(description = "stations", extension = ".txt", dateToday = False)
        referenceDate = (2015,10,28,0,1,0) #incremented one minute in relation to the input
        numberOfSamples = 1440
        numberOfInputs = 4
        incrementSeconds = 60

        extractOutDataset = outputDataset.extractDataset(satelliteName,inputDataFilepath,referenceDate,numberOfSamples,numberOfInputs,incrementSeconds)
        extractedOutMatrix = outputDataset.dataset

        #Save Ouput Dataset
        outputFilePath = generateFilename(description='outputDataset')
        saveOutDataset = outputDataset.saveToFile(outputFilePath)

        #Normalize Ouput Dataset
        normMethod = 'minmax'
        minmaxValues = (-1,1)
        normOutput = outputDataset.normalize(normMethod,minmaxValues)
        normOutMatrix = outputDataset.dataset

        #Save Normalized Ouput Values
        normOutFilePath = generateFilename(description='normOutputDataset')
        saveNormOutput = outputDataset.saveToFile(normOutFilePath)

        if extractInDataset + saveInDataset + normInput + saveNormInput + extractOutDataset + saveOutDataset + normOutput + saveNormOutput == 0:
            completed = 0

        #============================== Verbose ==========================

        if verbose:

            if extractInDataset == 0:
                print "\nInput dataset extracted!"

    return completed


def teach(version = 1, verbose = False):

    completed = 1

    if version == 1:
        NN1 = NN()

        inputFilePath = generateFilename(description='minmaxinputDataset')
        outputFilePath = generateFilename(description='minmaxoutputDataset')

        loadData = NN1.loadData(inputFilePath,outputFilePath)

        train = NN1.teachPyBrain(verbose=False)

        saveResults = NN1.saveResults()

        fileIn = generateFilename(description="networkResults")

        fileOut_x_t = generateFilename(description="NNoutput_x_t")
        fileOut_y_t = generateFilename(description="NNoutput_y_t")
        fileOut_z_t = generateFilename(description="NNoutput_z_t")

        dataset = Dataset()

        sepX = dataset.separate(filepathOut=fileOut_x_t,filepathIn=fileIn,columns=[0,3])
        sepY = dataset.separate(filepathOut=fileOut_y_t,filepathIn=fileIn,columns=[1,3])
        sepZ = dataset.separate(filepathOut=fileOut_z_t,filepathIn=fileIn,columns=[2,3])

        errorFilepath = generateFilename(description="networkError")

        saveErrors = NN1.saveError(errorFilepath)

        #plotData(fileOut_x_t)
        #plotData(fileOut_y_t)
        #plotData(fileOut_z_t)

        completed = 0


    if version == 2:

        NN1 = NN()
        

    return completed

if __name__ == "__main__":

    #from goals import teach

    def test(number=1,verbose=True):
        if number == 1:
            collectDataset(version=3,verbose=verbose)


    test(1)