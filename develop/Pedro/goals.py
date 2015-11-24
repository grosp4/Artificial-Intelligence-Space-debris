__author__ = 'Pedro'

from gain_dataset import Dataset
from filenameGenerator import generateFilename
from Pedro.neuralNetwork import NN
from Patrick import *
import numpy as np

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

        #======== Input Dataset ===============

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

        #Separate Dataset
        sepInFileX = generateFilename(description='inputDataset_x_t')
        sepInFileY = generateFilename(description='inputDataset_y_t')
        sepInFileZ = generateFilename(description='inputDataset_z_t')
        columnsX_T = [0,3]
        columnsY_T = [1,3]
        columnsZ_T = [2,3]

        separateInX = inputDataset.separate(sepInFileX,'',columnsX_T)
        separateInY = inputDataset.separate(sepInFileY,'',columnsY_T)
        separateInZ = inputDataset.separate(sepInFileZ,'',columnsZ_T)

        #Normalize Input Dataset
        normMethod = 'minmax'
        minmaxValues = (-1,1)
        normInput = inputDataset.normalize(normMethod,minmaxValues)
        normInMatrix = inputDataset.dataset

        #Save Normalized Input Values
        normInFilePath = generateFilename(description='normInputDataset')
        saveNormInput = inputDataset.saveToFile(normInFilePath)

        #Separate Normalized Output Dataset
        sepInNormFileX = generateFilename(description='inputNormDataset_x_t')
        sepInNormFileY = generateFilename(description='inputNormDataset_y_t')
        sepInNormFileZ = generateFilename(description='inputNormDataset_z_t')

        separateNormInX = inputDataset.separate(sepInNormFileX,'',columnsX_T)
        separateNormInY = inputDataset.separate(sepInNormFileY,'',columnsY_T)
        separateNormInZ = inputDataset.separate(sepInNormFileZ,'',columnsZ_T)

        #======== Output Dataset ===============

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

        #Separate Dataset
        sepOutFileX = generateFilename(description='outputDataset_x_t')
        sepOutFileY = generateFilename(description='outputDataset_y_t')
        sepOutFileZ = generateFilename(description='outputDataset_z_t')
        columnsX_T = [0,3]
        columnsY_T = [1,3]
        columnsZ_T = [2,3]

        separateOutX = outputDataset.separate(sepOutFileX,'',columnsX_T)
        separateOutY = outputDataset.separate(sepOutFileY,'',columnsY_T)
        separateOutZ = outputDataset.separate(sepOutFileZ,'',columnsZ_T)

        #Normalize Ouput Dataset
        normMethod = 'minmax'
        minmaxValues = (-1,1)
        normOutput = outputDataset.normalize(normMethod,minmaxValues)
        normOutMatrix = outputDataset.dataset

        #Save Normalized Ouput Values
        normOutFilePath = generateFilename(description='normOutputDataset')
        saveNormOutput = outputDataset.saveToFile(normOutFilePath)

        #Separate Normalized Output Dataset
        sepOutNormFileX = generateFilename(description='outputNormDataset_x_t')
        sepOutNormFileY = generateFilename(description='outputNormDataset_y_t')
        sepOutNormFileZ = generateFilename(description='outputNormDataset_z_t')

        separateNormOutX = outputDataset.separate(sepOutNormFileX,'',columnsX_T)
        separateNormOutY = outputDataset.separate(sepOutNormFileY,'',columnsY_T)
        separateNormOutZ = outputDataset.separate(sepOutNormFileZ,'',columnsZ_T)

        if extractInDataset + \
                saveInDataset + \
                separateInX + \
                separateInY + \
                separateInZ + \
                normInput + \
                saveNormInput + \
                separateNormInX + \
                separateNormInY + \
                separateNormInZ + \
                extractOutDataset + \
                saveOutDataset + \
                separateOutX + \
                separateOutY + \
                separateOutZ + \
                normOutput + \
                saveNormOutput + \
                separateNormOutX + \
                separateNormOutY + \
                separateNormOutZ == 0:

            completed = 0

        #============================== Verbose ==========================

        if verbose:

            if extractInDataset == 0:
                print "\nInput dataset extracted!"

    if version == 4:

        inputDataFilepath = generateFilename(description = "stations", extension = ".txt", dateToday = False)

        fp = open(inputDataFilepath)

        listOfSatellites = []

        for i, line in enumerate(fp):
            if i%3 == 0:
                listOfSatellites.append(line.strip())

        for satelliteName in listOfSatellites:
            print satelliteName

            #======== Input Dataset ===============

            inputDataset = Dataset()

            #Extract Input Dataset
            referenceDate = (2015,10,28,0,0,0)
            numberOfSamples = 1440
            numberOfInputs = 4
            incrementSeconds = 60

            extractInDataset = inputDataset.extractDataset(satelliteName,inputDataFilepath,referenceDate,numberOfSamples,numberOfInputs,incrementSeconds)
            extractedInMatrix = inputDataset.dataset

            #Save Input Dataset
            inputFilePath = generateFilename(description='inputDataset%s'%satelliteName)
            saveInDataset = inputDataset.saveToFile(inputFilePath)

            #Separate Dataset
            sepInFileX = generateFilename(description='inputDataset_x_t%s'%satelliteName)
            sepInFileY = generateFilename(description='inputDataset_y_t%s'%satelliteName)
            sepInFileZ = generateFilename(description='inputDataset_z_t%s'%satelliteName)
            columnsX_T = [0,3]
            columnsY_T = [1,3]
            columnsZ_T = [2,3]

            separateInX = inputDataset.separate(sepInFileX,'',columnsX_T)
            separateInY = inputDataset.separate(sepInFileY,'',columnsY_T)
            separateInZ = inputDataset.separate(sepInFileZ,'',columnsZ_T)

            #Normalize Input Dataset
            normMethod = 'minmax'
            minmaxValues = (-1,1)
            normInput = inputDataset.normalize(normMethod,minmaxValues)
            normInMatrix = inputDataset.dataset

            #Save Normalized Input Values
            normInFilePath = generateFilename(description='normInputDataset%s'%satelliteName)
            saveNormInput = inputDataset.saveToFile(normInFilePath)

            #Separate Normalized Output Dataset
            sepInNormFileX = generateFilename(description='inputNormDataset_x_t%s'%satelliteName)
            sepInNormFileY = generateFilename(description='inputNormDataset_y_t%s'%satelliteName)
            sepInNormFileZ = generateFilename(description='inputNormDataset_z_t%s'%satelliteName)

            separateNormInX = inputDataset.separate(sepInNormFileX,'',columnsX_T)
            separateNormInY = inputDataset.separate(sepInNormFileY,'',columnsY_T)
            separateNormInZ = inputDataset.separate(sepInNormFileZ,'',columnsZ_T)

            #======== Output Dataset ===============

            outputDataset = Dataset()

            #Extract Ouput Dataset
            referenceDate = (2015,10,28,0,1,0) #incremented one minute in relation to the input
            numberOfSamples = 1440
            numberOfInputs = 4
            incrementSeconds = 60

            extractOutDataset = outputDataset.extractDataset(satelliteName,inputDataFilepath,referenceDate,numberOfSamples,numberOfInputs,incrementSeconds)
            extractedOutMatrix = outputDataset.dataset

            #Save Ouput Dataset
            outputFilePath = generateFilename(description='outputDataset%s'%satelliteName)
            saveOutDataset = outputDataset.saveToFile(outputFilePath)

            #Separate Dataset
            sepOutFileX = generateFilename(description='outputDataset_x_t%s'%satelliteName)
            sepOutFileY = generateFilename(description='outputDataset_y_t%s'%satelliteName)
            sepOutFileZ = generateFilename(description='outputDataset_z_t%s'%satelliteName)
            columnsX_T = [0,3]
            columnsY_T = [1,3]
            columnsZ_T = [2,3]

            separateOutX = outputDataset.separate(sepOutFileX,'',columnsX_T)
            separateOutY = outputDataset.separate(sepOutFileY,'',columnsY_T)
            separateOutZ = outputDataset.separate(sepOutFileZ,'',columnsZ_T)

            #Normalize Ouput Dataset
            normMethod = 'minmax'
            minmaxValues = (-1,1)
            normOutput = outputDataset.normalize(normMethod,minmaxValues)
            normOutMatrix = outputDataset.dataset

            #Save Normalized Ouput Values
            normOutFilePath = generateFilename(description='normOutputDataset%s'%satelliteName)
            saveNormOutput = outputDataset.saveToFile(normOutFilePath)

            #Separate Normalized Output Dataset
            sepOutNormFileX = generateFilename(description='outputNormDataset_x_t%s'%satelliteName)
            sepOutNormFileY = generateFilename(description='outputNormDataset_y_t%s'%satelliteName)
            sepOutNormFileZ = generateFilename(description='outputNormDataset_z_t%s'%satelliteName)

            separateNormOutX = outputDataset.separate(sepOutNormFileX,'',columnsX_T)
            separateNormOutY = outputDataset.separate(sepOutNormFileY,'',columnsY_T)
            separateNormOutZ = outputDataset.separate(sepOutNormFileZ,'',columnsZ_T)

            if extractInDataset + \
                    saveInDataset + \
                    separateInX + \
                    separateInY + \
                    separateInZ + \
                    normInput + \
                    saveNormInput + \
                    separateNormInX + \
                    separateNormInY + \
                    separateNormInZ + \
                    extractOutDataset + \
                    saveOutDataset + \
                    separateOutX + \
                    separateOutY + \
                    separateOutZ + \
                    normOutput + \
                    saveNormOutput + \
                    separateNormOutX + \
                    separateNormOutY + \
                    separateNormOutZ == 0:

                completed = 0

    return completed

def teach(version = 2, verbose = False):

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

        #Load Dataset in Neural Network
        inputFilePath = generateFilename(description='normInputDataset')
        outputFilePath = generateFilename(description='normOutputDataset')
        loadData = NN1.loadData(inputFilePath,outputFilePath)

        #Teach using Pybrain
        epochs=5
        hiddenLayers=4
        teachNN = NN1.teachPyBrain(epochs=epochs,hiddenLayers=hiddenLayers,verbose=False)

        #Save Results (Save outputs for given inputs)
        saveResultsPath = generateFilename(description='resultsNN')
        saveResults = NN1.saveResults(saveResultsPath)

        #Separate Results
        sepResultsFilepathX = generateFilename(description='resultsNN_x_t')
        sepResultsFilepathY = generateFilename(description='resultsNN_y_t')
        sepResultsFilepathZ = generateFilename(description='resultsNN_z_t')
        columnsX_T = [0,3]
        columnsY_T = [1,3]
        columnsZ_T = [2,3]

        sepResultsX = Dataset().separate(sepResultsFilepathX,saveResultsPath,columnsX_T)
        sepResultsY = Dataset().separate(sepResultsFilepathY,saveResultsPath,columnsY_T)
        sepResultsZ = Dataset().separate(sepResultsFilepathZ,saveResultsPath,columnsZ_T)

        #Denormalize Results
        outputFilePath = generateFilename(description='outputDataset')
        minmaxValues = (-1.,1.)
        resultsData = Dataset()
        resultsData.dataset = NN1.results
        outputDataset = np.load(outputFilePath)
        resultsData.min_dataset = outputDataset.min(axis=0)
        resultsData.max_dataset = outputDataset.max(axis=0)
        resultsData.min = minmaxValues[0]
        resultsData.max = minmaxValues[1]
        denormResults = resultsData.denormalize()

        #Save Denormalized Results
        denormResultsPath = generateFilename(description='denormResultsNN')
        resultsData.saveToFile(denormResultsPath)

        #Separate Denormalized Results
        sepDenormResultsFilepathX = generateFilename(description='denormResultsNN_x_t')
        sepDenormResultsFilepathY = generateFilename(description='denormResultsNN_y_t')
        sepDenormResultsFilepathZ = generateFilename(description='denormResultsNN_z_t')
        columnsX_T = [0,3]
        columnsY_T = [1,3]
        columnsZ_T = [2,3]

        sepDenormResultsX = Dataset().separate(sepDenormResultsFilepathX,denormResultsPath,columnsX_T)
        sepDenormResultsY = Dataset().separate(sepDenormResultsFilepathY,denormResultsPath,columnsY_T)
        sepDenormResultsZ = Dataset().separate(sepDenormResultsFilepathZ,denormResultsPath,columnsZ_T)

        #Save Errors
        saveErrorsPath = generateFilename(description='errorsNN')
        saveErrors = NN1.saveError(saveErrorsPath)

        #Save Weights
        savedWeightsfilepath = generateFilename(description='weightsNN')
        savedWeights = NN1.getWeights()
        saveWeights = NN1.saveWeights()

        print savedWeights

        print

        for item in savedWeights:
            print item

        if loadData + \
                teachNN + \
                saveResults + \
                sepResultsX + \
                sepResultsY + \
                sepResultsZ + \
                denormResults + \
                sepDenormResultsX + \
                sepDenormResultsY + \
                sepDenormResultsZ + \
                saveErrors == 0:

            completed = 0

    if version == 3:

        inputDataFilepath = generateFilename(description = "stations", extension = ".txt", dateToday = False)

        fp = open(inputDataFilepath)

        listOfSatellites = []

        for i, line in enumerate(fp):
            if i%3 == 0:
                listOfSatellites.append(line.strip())

        for satellites in listOfSatellites:

            print satellites

            NN1 = NN()

            #Load Dataset in Neural Network
            inputFilePath = generateFilename(description='normInputDataset%s'%satellites)
            outputFilePath = generateFilename(description='normOutputDataset%s'%satellites)
            loadData = NN1.loadData(inputFilePath,outputFilePath)

            #Teach using Pybrain
            epochs=5
            hiddenLayers=4
            teachNN = NN1.teachPyBrain(epochs=epochs,hiddenLayers=hiddenLayers,verbose=False)

            #Save Results (Save outputs for given inputs)
            saveResultsPath = generateFilename(description='resultsNN%s'%satellites)
            saveResults = NN1.saveResults(saveResultsPath)

            #Separate Results
            sepResultsFilepathX = generateFilename(description='resultsNN_x_t%s'%satellites)
            sepResultsFilepathY = generateFilename(description='resultsNN_y_t%s'%satellites)
            sepResultsFilepathZ = generateFilename(description='resultsNN_z_t%s'%satellites)
            columnsX_T = [0,3]
            columnsY_T = [1,3]
            columnsZ_T = [2,3]

            sepResultsX = Dataset().separate(sepResultsFilepathX,saveResultsPath,columnsX_T)
            sepResultsY = Dataset().separate(sepResultsFilepathY,saveResultsPath,columnsY_T)
            sepResultsZ = Dataset().separate(sepResultsFilepathZ,saveResultsPath,columnsZ_T)

            #Denormalize Results
            outputFilePath = generateFilename(description='outputDataset%s'%satellites)
            minmaxValues = (-1.,1.)
            resultsData = Dataset()
            resultsData.dataset = NN1.results
            outputDataset = np.load(outputFilePath)
            resultsData.min_dataset = outputDataset.min(axis=0)
            resultsData.max_dataset = outputDataset.max(axis=0)
            resultsData.min = minmaxValues[0]
            resultsData.max = minmaxValues[1]
            denormResults = resultsData.denormalize()

            #Save Denormalized Results
            denormResultsPath = generateFilename(description='denormResultsNN%s'%satellites)
            resultsData.saveToFile(denormResultsPath)

            #Separate Denormalized Results
            sepDenormResultsFilepathX = generateFilename(description='denormResultsNN_x_t%s'%satellites)
            sepDenormResultsFilepathY = generateFilename(description='denormResultsNN_y_t%s'%satellites)
            sepDenormResultsFilepathZ = generateFilename(description='denormResultsNN_z_t%s'%satellites)
            columnsX_T = [0,3]
            columnsY_T = [1,3]
            columnsZ_T = [2,3]

            sepDenormResultsX = Dataset().separate(sepDenormResultsFilepathX,denormResultsPath,columnsX_T)
            sepDenormResultsY = Dataset().separate(sepDenormResultsFilepathY,denormResultsPath,columnsY_T)
            sepDenormResultsZ = Dataset().separate(sepDenormResultsFilepathZ,denormResultsPath,columnsZ_T)

            #Save Errors
            saveErrorsPath = generateFilename(description='errorsNN%s'%satellites)
            saveErrors = NN1.saveError(saveErrorsPath)

            #Save Weights
            savedWeightsfilepath = generateFilename(description='weightsNN%s'%satellites)
            savedWeights = NN1.getWeights()
            saveWeights = NN1.saveWeights()

            if loadData + \
                    teachNN + \
                    saveResults + \
                    sepResultsX + \
                    sepResultsY + \
                    sepResultsZ + \
                    denormResults + \
                    sepDenormResultsX + \
                    sepDenormResultsY + \
                    sepDenormResultsZ + \
                    saveErrors == 0:

                completed = 0

                pass

    if version == 4:

        listNumberHiddenLayers =[2,3,4,5]
        listNumberEpochs = [5,10,30,60]

        for hiddenLayers in listNumberHiddenLayers:
            for epochs in listNumberEpochs:
                print "layers %d , epochs %d" % (hiddenLayers,epochs)
                NN1 = NN()

                #Load Dataset in Neural Network
                inputFilePath = generateFilename(description='normInputDataset')
                outputFilePath = generateFilename(description='normOutputDataset')
                loadData = NN1.loadData(inputFilePath,outputFilePath)

                #Teach using Pybrain
                teachNN = NN1.teachPyBrain(epochs=epochs,hiddenLayers=hiddenLayers,verbose=False)

                #Save Results (Save outputs for given inputs)
                saveResultsPath = generateFilename(description='resultsNN_%d_h_%d_e_'%(hiddenLayers,epochs))
                saveResults = NN1.saveResults(saveResultsPath)

                #Separate Results
                sepResultsFilepathX = generateFilename(description='resultsNN_x_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                sepResultsFilepathY = generateFilename(description='resultsNN_y_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                sepResultsFilepathZ = generateFilename(description='resultsNN_z_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                columnsX_T = [0,3]
                columnsY_T = [1,3]
                columnsZ_T = [2,3]

                sepResultsX = Dataset().separate(sepResultsFilepathX,saveResultsPath,columnsX_T)
                sepResultsY = Dataset().separate(sepResultsFilepathY,saveResultsPath,columnsY_T)
                sepResultsZ = Dataset().separate(sepResultsFilepathZ,saveResultsPath,columnsZ_T)

                #Denormalize Results
                outputFilePath = generateFilename(description='outputDataset')
                minmaxValues = (-1.,1.)
                resultsData = Dataset()
                resultsData.dataset = NN1.results
                outputDataset = np.load(outputFilePath)
                resultsData.min_dataset = outputDataset.min(axis=0)
                resultsData.max_dataset = outputDataset.max(axis=0)
                resultsData.min = minmaxValues[0]
                resultsData.max = minmaxValues[1]
                denormResults = resultsData.denormalize()

                #Save Denormalized Results
                denormResultsPath = generateFilename(description='denormResultsNN_%d_h_%d_e_'%(hiddenLayers,epochs))
                resultsData.saveToFile(denormResultsPath)

                #Separate Denormalized Results
                sepDenormResultsFilepathX = generateFilename(description='denormResultsNN_x_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                sepDenormResultsFilepathY = generateFilename(description='denormResultsNN_y_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                sepDenormResultsFilepathZ = generateFilename(description='denormResultsNN_z_t_%d_h_%d_e_'%(hiddenLayers,epochs))
                columnsX_T = [0,3]
                columnsY_T = [1,3]
                columnsZ_T = [2,3]

                sepDenormResultsX = Dataset().separate(sepDenormResultsFilepathX,denormResultsPath,columnsX_T)
                sepDenormResultsY = Dataset().separate(sepDenormResultsFilepathY,denormResultsPath,columnsY_T)
                sepDenormResultsZ = Dataset().separate(sepDenormResultsFilepathZ,denormResultsPath,columnsZ_T)

                #Save Errors
                saveErrorsPath = generateFilename(description='errorsNN_%d_h_%d_e_'%(hiddenLayers,epochs))
                saveErrors = NN1.saveError(saveErrorsPath)

                #Save Weights
                savedWeightsfilepath = generateFilename(description='weightsNN_%d_h_%d_e_'%(hiddenLayers,epochs))
                savedWeights = NN1.getWeights()
                saveWeights = NN1.saveWeights()

    return completed

if __name__ == "__main__":

    #from goals import teach

    def test(number=1,verbose=True):
        if number == 1:
            collect = collectDataset(version=3,verbose=verbose)
            teachNN = teach(version=2,verbose=verbose)

        if number == 2:
            teachNN = teach(version=2,verbose=verbose)

        if number == 3:
            #collect = collectDataset(version=4,verbose=verbose)
            teachNN = teach(version=3,verbose=verbose)

        if number == 4:
            collect = collectDataset(version=3,verbose=verbose)
            teachNN = teach(version=4,verbose=verbose)

    test(4)