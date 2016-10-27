import re

class AddressBook:
    """ An Address Book

    Attributes:
        people: a list of people added to the Address Book
        groups: a list of groups added to the Address Book
     """

    def __init__(self):
        """ Creates an empty Address Book """
        self.people = []
        self.groups = []

    def addPerson(self, person):
        """ Add a *person* to the Address Book. If the person is
        a member of any group, those groups will be added to the
        Address Book as well """
        self.people.append(person)

        for g in person.groups:
            # Add new groups to the groups list
            if not g in self.groups:
                self.groups.append(g)

    def addGroup(self, group):
        """ Add a *group* to the Address Book. If the group has
        any members, those members will be added to the
        Address Book as well """
        self.groups.append(group)

        for p in group.members:
            # Add new people to the people list
            if not p in self.people:
                self.people.append(p)

    def getMembers(self, group=None, group_name=None):
        """ Returns a list containing the members of a certain
        group """
        if (group == None and group_name == None):
            raise Exception('Either group or group_name is required')

        # if group_name was passed, get the group object with that name
        if group == None:
            group = [x for x in self.groups if x.name == group_name][0]

        if group == None:
            raise Exception('Group {0} not found'.format(group_name))

        return group.members

    def getGroups(self, person=None, person_full_name=None):
        """ Returns a list containing the groups a person is a
         member of"""
        if (person == None and person_full_name == None):
            raise Exception('Either person or person_full_name is required')

        # if person_full_name was passed, get the person object with that name
        if person == None:
            person = [x for x in self.people if str(x) == person_full_name][0]

        if person == None:
            raise Exception('Person {0} not found'.format(person_full_name))

        return person.groups

    @staticmethod
    def __personMatch(person, first_name, last_name):
        """ Utility function used to check if a person matches a pair
        of first and/or last names """
        if first_name != '' and last_name != '':
            # Both arguments are present, compare full name
            return str(person) == '{0}, {1}'.format(last_name, first_name)
        elif last_name != '':
            # Just last name is present
            return person.last_name == last_name
        else:
            # Just first name is present
            return person.first_name == first_name

    def findPeopleByName(self, first_name='', last_name=''):
        """ Finds people by first and/or last names. This function will
        return a list of matches ordered by last and first names """
        if (first_name == '' and last_name == ''):
            raise Exception('Either first or last name is required')

        result = [x for x in self.people if AddressBook.__personMatch(x, first_name, last_name)]

        result.sort(key=lambda x: str(x))

        return result

    @staticmethod
    def __emailMatch(person, email_search):
        """ Utility function used to check if a person's email list
        contain at least one email address that matches the email search
        parameter """
        pattern = re.compile("^{0}.*".format(email_search))

        for email in person.email_addresses:
            if pattern.match(email):
                return True

        return False

    def findPeopleByEmail(self, email_search):
        """ Finds people by email address. This function will
        return a list of matches ordered by last and first names """
        if (email_search == None):
            raise Exception('Search parameter is required')

        result = [x for x in self.people if AddressBook.__emailMatch(x, email_search)]

        result.sort(key=lambda x: str(x))

        return result
