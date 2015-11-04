__author__ = 'Pedro'

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
import Pedro
import Patrick
#********************************************************************************/



#* ******************************************************************************/
# global variables
#  ******************************************************************************/
debug = True
#********************************************************************************/


#********************************************************************************/
# main starts here
#********************************************************************************/

def main():

    errors = 0

    #goal 1: collect and prepare the dataset to be processed
    datasetCollected = 1
    if Pedro.collectDataset() != 0:
        datasetCollected = 0
        errors += 1

    #goal 2: plot the dataset
    datasetPlotted = 1
    if Patrick.plotData(False) != 0:
        datasetPlotted = 0
        errors += 1

    datasetTought = 1
    if Pedro.teach() != 0:
        datasetTought = 0
        errors += 1

    # prints for status of goals
    if datasetCollected:
        print "\nDataset collected!"

    if not datasetCollected:
        print "\nDataset NOT collected!"

    if datasetPlotted:
        print "\nDataset plotted!"

    if not datasetPlotted:
        print "\nDataset NOT plotted!"

    if datasetTought:
        print "\nDataset Tought!"

    if not datasetTought:
        print "\nDataset NOT Tought!"

    if not errors:
        print "\nEveryting works fine!"
        return 0

    if errors:
        print "\n%d errors were found!" % errors

    return 1

if __name__ == "__main__":
    main()