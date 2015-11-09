__author__ = 'Pedro'

import numpy as np
import random
from filenameGenerator import generateFilename
from Pedro import *
import sys

class NN():

    def __init__(self,dataset=None,numberOfHiddenLayers=1,numberOfOutputs = 4):

        #Data that comes as input to the system
        self.inputDataset = None

        #Data that the system should output (used to train the NN)
        self.outputDataset = None

        #Data that the system outputs
        self.outputDataset = None
        self.numberOfOutputs = numberOfOutputs
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.l0 = None
        self.l1 = None
        self.l2 = None
        self.l1_delta = None
        self.l2_delta = None
        self.l1_error = None
        self.l2_error = None
        self.syn0 = None
        self.syn1 = None

    #Loads data matrices (inputs/outputs to the NN)
    def loadData(self,
                 inFilename = '',
                 outFilename = ''):
        try:
            self.inputDataset = np.load(inFilename)

        except:
            print 'Error loading input data! Path: %s' % inFilename
            return 1

        try:
            self.outputDataset = np.load(outFilename)
            return 0

        except:
            print 'Error loading output data! Path: %s' % outFilename
            return 2

    def teach(self, epocs=1500):
        if type(self.inputDataset).__module__ == np.__name__:
            if type(self.outputDataset).__module__ == np.__name__:

                def sigmoid(x,deriv=False):

                    if(deriv==True):
                        return x*(1-x)

                    else:
                        return 1/(1+np.exp(-x))

                X = self.inputDataset
                y = self.outputDataset.T

                random.seed(0)

                syn0 = 2*np.random.random((4,1440))- 1
                #syn0 = 2*np.random.random((self.inputDataset.shape))- 1
                #syn0 = syn0.T
                #syn1 = 2*np.random.random((1440,4)) - 1


                for epoc in xrange(epocs):
                    #compare with the next value

                    l0 = X
                    l1 = sigmoid(np.dot(l0,syn0))
                    #l2 = sigmoid(np.dot(l1,syn1))

                    #print l2

                    #l2_error = y - l2

                    l1_error = y - l1

                    #l2_delta = l2_error*sigmoid(l2,deriv=True)

                    #l1_error = l2_delta.dot(syn1.T)

                    l1_delta = l1_error * sigmoid(l1,deriv=True)

                    #syn1 += l1.T.dot(l2_delta)
                    syn0 += np.dot(l0.T,l1_delta)

                self.l0 = l0
                self.l1 = l1
                #self.l2 = l2

                self.l1_delta = l1_delta
                #self.l2_delta = l2_delta

                self.l1_error = l1_error
                #self.l2_error = l2_error

                self.syn0 = syn0
                #self.syn1 = syn1

                return 0

        return 1

    def teachPyBrain(self,epochs=5,hiddenLayers=3,verbose=False):
        from pybrain.datasets import SupervisedDataSet
        from pybrain.supervised.trainers import BackpropTrainer
        from pybrain.tools.shortcuts import buildNetwork

        inputData = self.inputDataset
        outputData = self.outputDataset

        numberOfColumnsInput = inputData.shape[1]
        numberOfColumnsTarget = outputData.shape[1]

        ds = SupervisedDataSet(numberOfColumnsInput,numberOfColumnsTarget)

        ds.setField('input', inputData)
        ds.setField('target', outputData)

        net = buildNetwork(numberOfColumnsInput, hiddenLayers, numberOfColumnsTarget)
        trainer = BackpropTrainer(net, ds)

        print net['target']

        for epoch in xrange(epochs):
            trainError = trainer.train()
            if verbose:
                print "Error: %f" % trainError

        if verbose:

            print "Target: "
            print net['target']

            for mod in net.modules:
                print "Module:", mod.name
                if mod.paramdim > 0:
                    print"--parameters:", mod.params
                for conn in net.connections[mod]:
                    print "-connection to", conn.outmod.name
                    if conn.paramdim > 0:
                         print "- parameters", conn.params
                if hasattr(net, "recurrentConns"):
                    print "Recurrent connections"
                    for conn in net.recurrentConns:
                        print "-", conn.inmod.name, " to", conn.outmod.name
                        if conn.paramdim > 0:
                            print "- parameters", conn.params

if __name__ == "__main__":

    NN1 = NN()

    inputFilePath = generateFilename(description='inputDataset')
    outputFilePath = generateFilename(description='outputDataset')

    loadData = NN1.loadData(inputFilePath,outputFilePath)

    #print "Input dataset: "
    #print NN1.inputDataset

    #print "Output dataset: "
    #print NN1.outputDataset

    #teaching = NN1.teach()

    NN1.teachPyBrain(verbose=True)

    #print str(np.mean(np.abs(NN1.l2_error)))