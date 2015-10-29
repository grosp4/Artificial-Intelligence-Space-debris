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
#  *                  \li grosp4 , 20.10.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     none
#  *
#  ******************************************************************************/

# Import classes from your brand new package
from Patrick import Mammals
from Patrick import Birds

# Create an object of Mammals class & call a method of it
myMammal = Mammals()
myMammal.printMembers()

# Create an object of Birds class & call a method of it
myBird = Birds()
myBird.printMembers()