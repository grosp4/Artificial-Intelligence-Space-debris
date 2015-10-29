__author__ = 'Patrick'


# /******************************************************************************/
# /** \file          birds
#  *  \brief         example class so far
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         example class so far
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
#  *  functions:      __init__
#  *                  printMembers
#  ******************************************************************************/



class Birds:


    #  ******************************************************************************/
    # /*
    #  *     functionname: __init__
    #  *     parameter:
    #  *                              - wildcard        description
    #  *
    #  *     returns:                 TBD
    #  *     description:             TBD
    #  *
    #  *******************************************************************************/
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']


    #  ******************************************************************************/
    # /*
    #  *     functionname: printMembers
    #  *     parameter:
    #  *                              - wildcard        description
    #  *
    #  *     returns:                 TBD
    #  *     description:             TBD
    #  *
    #  *******************************************************************************/
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)