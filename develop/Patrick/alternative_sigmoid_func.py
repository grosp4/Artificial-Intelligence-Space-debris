__author__ = 'Patrick'
# /******************************************************************************/
# /** \file          alternative_sigmoid_func
#  *  \brief         TBD
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         TBD
#  *
#  *  \authors       grosp4,
#  *
#  *  \date          29.10.2015
#  *
#  *  \remark        Last Modification
#  *                  \li grosp4, 29.10.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     alternative_sigmoid_func
#  *
#  ******************************************************************************/


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as numblibrary
import os.path

#  ******************************************************************************/
# /*
#  *     functionname:          alternative_sigmoid_func
#  *     parameter:
#  *
#  *                              - x           data, format TBD!
#  *                              - derivation  false or true
#  *
#  *     returns:                 wildcard value
#  *     description:             this functions is an easier and faster version of the ideal sigmoid
#  *                              to avoid overflows
#  *
#  *******************************************************************************/
def alternative_sigmoid_func(x,derivation=False):
    if(derivation==True):
        return x*(1-x)

    return 1/(1+numblibrary.abs(x))