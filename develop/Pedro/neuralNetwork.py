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
        self.target = None
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

        #Data related to the pyBrain teaching
        self.ds = None
        self.net = None
        self.trainer = None
        self.trainError = None
        self.results = None

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
                        return x*(1.0-x)

                    else:
                        return 1.0/(1.0+np.exp(-x))

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

    def teachPyBrain(self,epochs=5,hiddenLayers=4,verbose=False):
        from pybrain.datasets import SupervisedDataSet
        from pybrain.supervised.trainers import BackpropTrainer
        from pybrain.tools.shortcuts import buildNetwork

        numberOfColumnsInput = self.inputDataset.shape[1]
        numberOfColumnsTarget = self.outputDataset.shape[1]

        self.ds = SupervisedDataSet(numberOfColumnsInput,numberOfColumnsTarget)

        self.ds.setField('input', self.inputDataset)
        self.ds.setField('target', self.outputDataset)

        self.net = buildNetwork(numberOfColumnsInput, hiddenLayers, numberOfColumnsTarget)
        self.trainer = BackpropTrainer(self.net, self.ds)

        if verbose:
            print self.inputDataset

        self.trainError = np.zeros((1,2))

        for epoch in xrange(epochs):

            #index of epoch should start with 1
            epoch += 1
            error = self.trainer.train()

            self.trainError = np.vstack([self.trainError, np.append(epoch,error)])

            if verbose:
                print "Error after epoch %d: %f" % (epoch, error)
                print "Output: "
                print self.net.activateOnDataset(self.ds)

        self.trainError = np.delete(self.trainError,0,0)

        self.results = self.net.activateOnDataset(self.ds)

        if verbose:

            print "Expected output: "
            print self.outputDataset

            for mod in self.net.modules:
                print "Module:", mod.name
                if mod.paramdim > 0:
                    print"--parameters:", mod.params
                for conn in self.net.connections[mod]:
                    print "-connection to", conn.outmod.name
                    if conn.paramdim > 0:
                         print "- parameters", conn.params
                if hasattr(self.net, "recurrentConns"):
                    print "Recurrent connections"
                    for conn in self.net.recurrentConns:
                        print "-", conn.inmod.name, " to", conn.outmod.name
                        if conn.paramdim > 0:
                            print "- parameters", conn.params

        return 0

    def saveResults(self,filepath = generateFilename(description='networkResults'),outputWriteMode='wb+'):

        if type(self.results).__module__ != np.__name__:
            return 2

        try:
            f = file(filepath,outputWriteMode)
            np.save(f,self.results)
            f.close()
            return 0

        except:
            return 1

    def saveError(self,filepath = generateFilename(description='networkError'),outputWriteMode='wb+'):

        if type(self.trainError).__module__ != np.__name__:
            return 2

        try:
            f = file(filepath,outputWriteMode)
            np.save(f,self.trainError)
            f.close()
            return 0

        except:
            return 1

    def getWeights(self):
        for mod in self.net.modules:
            for conn in self.net.connections[mod]:
                print conn
                #for cc in range(len(conn.params)):
                    #print conn.whichBuffers(cc), conn.params[cc]

if __name__ == "__main__":

    def test(number = 1):

        completed = 1

        if number == 1:

            NN1 = NN()

            inputFilePath = generateFilename(description='normInputDataset')
            outputFilePath = generateFilename(description='normOutputDataset')

            loadData = NN1.loadData(inputFilePath,outputFilePath)

            NN1.teachPyBrain(verbose=False)

            NN1.getWeights()


            #print str(np.mean(np.abs(NN1.l2_error)))

            completed = 0

        if number == 2:



            completed = 0

    test()