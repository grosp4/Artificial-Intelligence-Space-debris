__author__ = 'Patrick'

# /******************************************************************************/
# /** \file          main
#  *  \brief         this is the main module
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         in this module everything will be started
#  *
#  *  \authors       grosp4,
#  *
#  *  \date          29.10.2015
#  *
#  *  \remark        Last Modification
#  *                  \li grosp4 , 29.10.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     none, as no main function is needed
#  *
#  ******************************************************************************/



#********************************************************************************/
# Import module and classes from your package here
#********************************************************************************/
from Patrick import Mammals
from Patrick import Birds
from Patrick import drawing_functions
from Pedro import sample_file
#********************************************************************************/



#* ******************************************************************************/
# global variables
#  ******************************************************************************/
debug = True
#********************************************************************************/


#********************************************************************************/
# main starts here
#********************************************************************************/


# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()

# print and plot test data as test program
sample_data = 0

# call functions of pedro and patricks packages
sample_file.sample()
testvalue = drawing_functions.plot_data(sample_data)

# last print to verifiy success
print testvalue