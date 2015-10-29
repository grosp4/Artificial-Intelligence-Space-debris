__author__ = 'Patrick'

__author__ = 'Patrick'
"""
/******************************************************************************/
/** \file          birds
 *  \brief         example class so far
 *******************************************************************************
 *
 *
 *
 *  \brief         example class so far
 *
 *  \authors       grosp4,
 *
 *  \date          29.10.2015
 *
 *  \remark        Last Modification
 *                  \li grosp4, 20.10.2015, Created
 *
 *
 ******************************************************************************/
/*
 *  functions:     none
 *
 ******************************************************************************/
 """


class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']


    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
           print('\t%s ' % member)