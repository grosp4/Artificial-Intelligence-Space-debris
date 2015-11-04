__author__ = 'Pedro'

import numpy as np
import random
from filenameGenerator import generateFilename

class NN():

    def __init__(self,dataset=None,numberOfHiddenLayers=1,numberOfOutputs = 4):
        self.dataset = dataset
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

    #Loads normalized matrix (ready to go as an input for the NN)
    def loadNormalized(self,filename = generateFilename(generateFilename(author='Pedro',description='datasetNormalized',extension='.npy',dateToday=True))):
        try:
            self.dataset = np.load(r"C:\Users\Honor\Documents\GitHub\Artificial-Intelligence-Space-debris\develop\dataset\PedrodatasetNormalized_20151104.npy")
            return 0

        except:
            print 'Error!'
            return 1

    def teach(self,steps=1440):
        if self.dataset.any() != None:

            def sigmoid(x,deriv=False):
                if(deriv==True):
                    return x*(1-x)

                else:
                    return 1/(1+np.exp(-x))

            X = self.dataset[...,[0,1,2]]
            #y = self.dataset[...,3]

            y = np.empty((1,1))

            for i in self.dataset:
                np.append(y,i[3])

            random.seed(0)

            syn0 = 2*np.random.random((3,1440)) - 1
            syn1 = 2*np.random.random((1440,1)) - 1

            for j in xrange(steps):

                #select random row from the dataset

                #compare with the next value
                l0 = X

                l1 = sigmoid(np.dot(l0,syn0))
                l2 = sigmoid(np.dot(l1,syn1))

                l2_error = y - l2

                l2_delta = l2_error*sigmoid(l2,deriv=True)

                l1_error = l2_delta.dot(syn1.T)

                l1_delta = l1_error * sigmoid(l1,deriv=True)

                syn1 += l1.T.dot(l2_delta)
                syn0 += np.dot(l0.T,l1_delta)

            self.l0 = l0
            self.l1 = l1
            self.l2 = l2
            self.l1_delta = l1_delta
            self.l2_delta = l2_delta
            self.l1_error = l1_error
            self.l2_error = l2_error
            self.syn0 = syn0
            self.syn1 = syn1

            return 0

        else:
            return 1

if __name__ == "__main__":
    NN1 = NN()
    loadData = NN1.loadNormalized()
    teaching = NN1.teach()

    print str(np.mean(np.abs(NN1.l2_error)))