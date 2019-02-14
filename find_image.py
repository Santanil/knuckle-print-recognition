import os
from os import path


class ImageFetch:
    """ Utility to Fetch single image path
        and provide  it to others
    """

    def __init__(self, imagerootpath=""):
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
        num_of_dirs_in_root = len(os.listdir(self.rootimagedirectory))
        num_of_individuals = int(num_of_dirs_in_root / 4)  # 4 because the dateset contains 4 finger knuckle samples
        return num_of_individuals

    def getLeftIndexFolders(self):
        list_of_leftindexfolder_for_i_person = []
        num_of_individuals = self.getPerPersonFolder()
        for personindex in range(1, num_of_individuals + 1):
            list_of_leftindexfolder_for_i_person.append("{:003d}_left index".format(personindex))
        return list_of_leftindexfolder_for_i_person

    def getLeftMiddleFolders(self):
        list_of_leftmiddlefolder_for_i_person = []
        num_of_individuals = self.getPerPersonFolder()
        for personindex in range(1, num_of_individuals + 1):
            list_of_leftmiddlefolder_for_i_person.append("{:003d}_left middle".format(personindex))
        return list_of_leftmiddlefolder_for_i_person

    def getRightIndexFolders(self):
        list_of_rightindexfolder_for_i_person = []
        num_of_individuals = self.getPerPersonFolder()
        for personindex in range(1, num_of_individuals + 1):
            list_of_rightindexfolder_for_i_person.append("{:003d}_right index".format(personindex))
        return list_of_rightindexfolder_for_i_person

    def getRightMiddleFolders(self):
        list_of_rightmiddlefolder_for_i_person = []
        num_of_individuals = self.getPerPersonFolder()
        for personindex in range(1, num_of_individuals + 1):
            list_of_rightmiddlefolder_for_i_person.append("{:003d}_right middle".format(personindex))
        return list_of_rightmiddlefolder_for_i_person

    def getimageperpersonimagelist(self):
        """[[Person1],[Person2],...,[PersonN]]"""
        listofimagedir_acc_person_ascending = []
        leftindexlist = self.getLeftIndexFolders()
        leftmiddlelist = self.getLeftMiddleFolders()
        rightindexlist = self.getRightIndexFolders()
        rightmiddlelist = self.getRightMiddleFolders()
        for i in range(0, self.getPerPersonFolder()):
            leftindexfolder = leftindexlist[i]
            leftmiddlefolder = leftmiddlelist[i]
            rightindexfolder = rightindexlist[i]
            rightmiddlefolder = rightmiddlelist[i]
            listofimagedir_acc_person_ascending.append([leftindexfolder, leftmiddlefolder,
                                                        rightindexfolder, rightmiddlefolder])
        return listofimagedir_acc_person_ascending
