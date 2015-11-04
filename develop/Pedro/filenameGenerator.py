__author__ = 'Pedro'

def generateFilename(author ="",description ="dataset",extension=".npy",dateToday=True):
    from os import getcwd
    from os import chdir
    from datetime import datetime

    currentDirectory = getcwd()

    #deactivated for bugfixing reasons, develop folder was missing on windows pcs
    #chdir('..')
    parentDirectory = getcwd()
    chdir(currentDirectory)

    datasetDirectory = parentDirectory + '\dataset\%s%s' % (author,description)

    if dateToday == True:
        #uses the date of the day in which the file was created
        dateOfToday = str(datetime.today())[:10].replace("-", "")
        datasetDirectory += '_' + dateOfToday

    datasetDirectory += extension

    return datasetDirectory

if __name__ =="__main__":

    #This is an example of what and how the function returns
    print "\n\nThis is a test to the module filenameGenerator."
    print "\n\nThe function generateFilename() with default arguments returns: \n %s" % generateFilename()
    print "\n\nThe same function with arguments: "
    print "author = 'Pedro'"
    print "description = 'something'"
    print "extension = '.npy'"
    print "dateToday = False"
    print "returns this path: %s" % generateFilename(author ="Pedro",description ="something",extension=".txt",dateToday=False)