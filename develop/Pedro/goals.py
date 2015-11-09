__author__ = 'Pedro'

from gain_dataset import Dataset
from filenameGenerator import generateFilename

def collectDataset(verbose = False):

    completed = 1

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
        print "Input file path: %s" % inputFilePath
        print "Output file path: %s" % outputFilePath

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
        if rescaleOutDataset:
            print "Problem saving output dataset!"

        if not completed:
            print "Data collection completed!"
        if completed:
            print "Data collection not completed!"

    return completed

def teach():

    completed = 1

    return completed

if __name__ == "__main__":
    collect = collectDataset(True)
    teach = teach()

    if collect == 0 and teach == 0:
        print "Dataset collected and tought to NN!"