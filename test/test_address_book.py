import unittest

from model.person import Person
from model.group import Group
from manager.address_book import AddressBook

class TestAddressBook(unittest.TestCase):
    """ Here I've focused on creating tests that matched
    the required features, as stated in the assignment description """
    def setUp(self):
        """ Creates one *address_book* with 2 groups and some people
        in them """
        self.address_book = AddressBook()

        # Groups
        self.jacksons = Group('Jacksons 5')
        self.singers = Group('Singers')

        # Michael jackson will be a member of both groups
        self.mj = Person('Michael', 'Jackson')

        # Members group #1
        self.jacksons.addPerson(self.mj)
        self.jacksons.addPerson(Person('Tito', 'Jackson'))
        self.jacksons.addPerson(Person('Another', 'Jackson'))

        # Members group #2
        self.singers.addPerson(Person('Lionel', 'Ritchie'))
        self.singers.addPerson(self.mj)

        # Add groups to the Address Book
        self.address_book.addGroup(self.jacksons)
        self.address_book.addGroup(self.singers)

        TestAddressBook.__addMockEmails(self.address_book)

    @staticmethod
    def __addMockEmails(address_book):
        """ Create mock email addresses for every person on
        the *address_book. Each person will have 1 email for
        each group of which they are a member of. The email
        address will have the following format:
        [first_name].[last_name]@[group.name].com  """
        for person in address_book.people:
            for g in person.groups:
                email = "{0}.{1}@{2}.com".format(person.first_name, person.last_name, g.name).replace(' ','').lower()

                person.email_addresses.append(email)

    def test_add_people_to_address_book(self):
        """ Feature #1: Add a person to the address book. """
        address_book = AddressBook()

        jerry = Person('Jerry', 'Garcia')
        janis = Person('Janis', 'Joplin')

        address_book.addPerson(jerry)
        address_book.addPerson(janis)

        self.assertEqual(2, len(address_book.people))

    def test_add_groups_to_address_book(self):
        """ Feature #2: Add a group to the address book. """
        address_book = AddressBook()

        grateful = Group('Grateful Dead')
        full = Group('Full Tilt')

        address_book.addGroup(grateful)
        address_book.addGroup(full)

        self.assertEqual(2, len(address_book.groups))

    def test_find_group_members(self):
        """ Feature #3: Given a group we want to easily find its members. """
        # get by group name
        self.assertEqual(3, len(self.address_book.getMembers(group_name='Jacksons 5')))
        # get by group object
        self.assertEqual(2, len(self.address_book.getMembers(group=self.singers)))

    def test_find_person_groups(self):
        """ Feature #4: Given a person we want to easily find the
        groups the person belongs to. """

        # get by person name
        self.assertEqual(1, len(self.address_book.getGroups(person_full_name='Ritchie, Lionel')))
        # get by person object
        self.assertEqual(2, len(self.address_book.getGroups(person=self.mj)))

    def test_search_person_by_name(self):
        """ Feature #5: Given a person we want to easily find the groups
        the person belongs to. """

        # search by first name
        result1 = self.address_book.findPeopleByName(first_name='Tito')
        self.assertEqual(1, len(result1))
        self.assertEqual('Jackson, Tito', str(result1[0]))

        # search by last name
        result2 = self.address_book.findPeopleByName(last_name='Jackson')
        self.assertEqual(3, len(result2))
        self.assertEqual('Jackson, Another', str(result2[0]))
        self.assertEqual('Jackson, Michael', str(result2[1]))
        self.assertEqual('Jackson, Tito', str(result2[2]))

        # search by first and last name
        result3 = self.address_book.findPeopleByName(last_name='Jackson', first_name='Tito')
        self.assertEqual(1, len(result3))
        self.assertEqual('Jackson, Tito', str(result3[0]))

    def test_search_person_by_email(self):
        """ Feature #6: Find person by email address. """

        # search by begining of email
        result1 = self.address_book.findPeopleByEmail('mich')
        self.assertEqual(1, len(result1))
        self.assertEqual('Jackson, Michael', str(result1[0]))

        # search by complete email
        result1 = self.address_book.findPeopleByEmail('lionel.ritchie@singers.com')
        self.assertEqual(1, len(result1))
        self.assertEqual('Ritchie, Lionel', str(result1[0]))

if __name__ == '__main__':
    unittest.main()
