import os


class ImageFetch:
    """ Utility to Fetch single image path
        and provide  it to others
    """

    def __init__(self, imagerootpath=""):
        """ Contructor
            accepts one arg
            string: imagerootpath = path to the root dataset directory
            :type imagerootpath: str
        """
        self.rootimagedirectory = imagerootpath

    def totalnumberofindividuals(self):
        num_of_dirs_in_root = len(os.listdir(self.rootimagedirectory))
		num_of_individuals = 10
        
        # 4 because the dateset contains 4 finger knuckle samples
        # int(num_of_dirs_in_root / 4) + 1 # +1 so that if a for a person has 3 finger samples that wont be excluded

        return num_of_individuals

    def getLeftIndexFolders(self):
        list_of_leftindexfolder_for_i_person = []
        num_of_individuals = self.totalnumberofindividuals()
        for personindex in range(0, (num_of_individuals + 1)):
            list_of_leftindexfolder_for_i_person.append("{:003d}_left index".format(personindex+1))
        return list_of_leftindexfolder_for_i_person

    def getLeftMiddleFolders(self):
        list_of_leftmiddlefolder_for_i_person = []
        num_of_individuals = self.totalnumberofindividuals()
        for personindex in range(0, num_of_individuals + 1):
            list_of_leftmiddlefolder_for_i_person.append("{:003d}_left middle".format(personindex+1))
        return list_of_leftmiddlefolder_for_i_person

    def getRightIndexFolders(self):
        list_of_rightindexfolder_for_i_person = []
        num_of_individuals = self.totalnumberofindividuals()
        for personindex in range(0, num_of_individuals + 1):
            list_of_rightindexfolder_for_i_person.append("{:003d}_right index".format(personindex+1))
        return list_of_rightindexfolder_for_i_person

    def getRightMiddleFolders(self):
        list_of_rightmiddlefolder_for_i_person = []
        num_of_individuals = self.totalnumberofindividuals()
        for personindex in range(0, num_of_individuals + 1):
            list_of_rightmiddlefolder_for_i_person.append("{:003d}_right middle".format(personindex+1))
        return list_of_rightmiddlefolder_for_i_person

    def getimageperpersonimagelist(self):
        """[[Person1],[Person2],...,[PersonN]]"""
        listofimagedir_acc_person_ascending = []
        leftindexlist = self.getLeftIndexFolders()
        leftmiddlelist = self.getLeftMiddleFolders()
        rightindexlist = self.getRightIndexFolders()
        rightmiddlelist = self.getRightMiddleFolders()
        for i in range(0, self.totalnumberofindividuals()+1):
            leftindexfolder = self.rootimagedirectory + leftindexlist[i]
            leftmiddlefolder = self.rootimagedirectory + leftmiddlelist[i]
            rightindexfolder = self.rootimagedirectory + rightindexlist[i]
            rightmiddlefolder = self.rootimagedirectory + rightmiddlelist[i]
            listofimagedir_acc_person_ascending.append([leftindexfolder, leftmiddlefolder,
                                                        rightindexfolder, rightmiddlefolder])
        return listofimagedir_acc_person_ascending
