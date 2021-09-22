__author__ = "Sibusiso Mgidi"
__credits__ = ["Nozipho Mtsweni"]
__version__ = "1.0.0"
__maintainer__ = "Sibusiso Mgidi"
__email__ = "mgiditercy@gmail.com"
__status__ = "Maintanance"



class DemographicData(object):
    """
    This is a blueprint for getting users demographic data
    """

    def __init__(self, fisrtname, lastname, course, dateofbirth, yos):
        self.firstname = fisrtname
        self.lastname = lastname
        self.course = course
        self.dateofbirth = dateofbirth
        self.yos = yos

    def get_demographic_date(self):
        """
        This function returns users first and last name
        :return
        -- firstname: users firstname
        -- lastname: users lastname
        """

        return "Hello, {} {}".format(self.firstname, self.lastname)

    


users_object1 = DemographicData("Sibusiso", "Mgidi", "Computer Science", "1996/01/02", "5th")
sibusiso = users_object1.get_demographic_date()
print(sibusiso)


