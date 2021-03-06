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
import Patrick
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
#  *                            @ dataSetPattern, beinning of a filename so you can select specific files
#  *     returns:               @ list_of_files, a list of files in a a specific folder
#  *     description:           @ list all files in of a specific folder, based on a relative path of the project
#  *
#  *
#  *******************************************************************************/
def getAllDatasetFileNames(pathname= '\dataset', dataSetPattern ="all"):

        # get current directory of package
        currentDirectory = getcwd()

        # go one folder up, because we want to go into another folder
        chdir('..')

        #get parent directory
        parentDirectory = getcwd()
        chdir(currentDirectory)

        list_of_files = []
        #create new path with dataset and parent directory
        datasetDirectory = parentDirectory + pathname

        if dataSetPattern == "all":

                list_of_files = os.listdir(datasetDirectory)
                #debug output
                if debug:
                    print "Debug Auxillary_Functions.getAllDatasetFileNames: all"


        if dataSetPattern == "errors":
                #debug output
                if debug:
                    print r"Debug Auxillary_Functions.getAllDatasetFileNames: errors"

                # pattern you looking for
                pattern = "errorsNN_"
                a_list_filter = ['npy']

                for r,d,f in os.walk(datasetDirectory):
                    for file in f:
                        if file[-3:] in a_list_filter and pattern in file:
                            list_of_files.append(file)

        #debug output
        if debug:
            print "Debug Auxillary_Functions.getAllDatasetFileNames: " , list_of_files

        return list_of_files

#  ******************************************************************************/
# /*
#  *     functionname:          @ getDatasetPath
#  *     parameter:             @ pathname, a pathname in the project you want to get to
#  *     returns:               @ the path to pathname you gave
#  *     description:           @ the total path of your system to dataset folder, e.g you enter "/folder1"  result is c:/programm/myprogram/folder1
#  *
#  *
#  *******************************************************************************/
def getDatasetPath(pathname):

        # get current directory of package
        currentDirectory = getcwd()

        # go one folder up, because we want to go into another folder
        chdir('..')

        #get parent directory
        parentDirectory = getcwd()
        chdir(currentDirectory)

        #create new path with dataset and parent directory
        datasetDirectory = parentDirectory + pathname

        #debug output
        if debug:
            print "Debug Auxillary_Functions.getDatasetPath: ", datasetDirectory


        return datasetDirectory




# to debug
if __name__ == "__main__":

    version = 1

    if version == 1:
        pathname = '\dataset'
        getAllDatasetFileNames(pathname, "all")

    if version == 2:
         pathname = '\dataset'
         getAllDatasetFileNames(pathname, "errors")

    getDatasetPath(pathname)