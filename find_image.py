import os
from os import path


class ImageFetch:
    """ Utility to Fetch single image path
        and provide  it to others
    """

    def __init__(self,imagerootpath = ""):
        """ Contructor
            accepts one arg
            string: imagerootpath = path to the root dataset directory
        """
        self.rootimagedirectory = imagerootpath

    def getPerPersonFolder(self):
        """
        getter method
        :return:
        """
        num_of_dirs_in_root =  593 # len(os.listdir(self.rootimagedirectory))
        num_of_individuals = int(num_of_dirs_in_root/4)
        return num_of_individuals
    def getLeftIndexFolders(self):
        pass

    def getLeftMiddleFolders(self):
        pass

    def getRightIndexFolders(self):
        pass

    def getRightMiddleFolders(self):
        pass
