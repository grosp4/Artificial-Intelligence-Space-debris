__author__ = 'Patrick'

# /******************************************************************************/
# /** \file          Auxillary_Functions
#  *  \brief         contains all auxillary functions which are rather small
#  *******************************************************************************
#  *
#  *
#  *
#  *  \brief         TBD
#  *
#  *  \authors       grosp4,
#  *
#  *  \date          23.11.2015
#  *
#  *  \remark        Last Modification
#  *                  \li grosp4, 2 23.11.2015, Created
#  *
#  *
#  ******************************************************************************/
# /*
#  *  functions:     getAllDatasetFileNames
#  *
#  ******************************************************************************/

import os
from os import getcwd
from os import chdir

#  ******************************************************************************/
#  *  local variables
#  ******************************************************************************/
debug = 1
#  ******************************************************************************/
# /*
#  *     functionname:          @ getAllDatasetFileNames
#  *     parameter:             @ pathname, pathname from the projects parent folder you want to go for to find files
#  *     returns:               @ list_of_files, a list of files in a a specific folder
#  *     description:           @ list all files in of a specific folder, based on a relative path of the project
#  *
#  *
#  *******************************************************************************/
def getAllDatasetFileNames(pathname= '\dataset'):

        # get current directory of package
        currentDirectory = getcwd()

        # go one folder up, because we want to go into another folder
        chdir('..')

        #get parent directory
        parentDirectory = getcwd()
        chdir(currentDirectory)

        #create new path with dataset and parent directory
        datasetDirectory = parentDirectory + pathname

        list_of_files = os.listdir(datasetDirectory)

        #debug output
        if debug:
            print datasetDirectory
            print list_of_files

        return list_of_files


# to debug
if __name__ == "__main__":

    pathname = '\dataset'
    getAllDatasetFileNames(pathname)