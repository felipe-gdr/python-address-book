import unittest

from model.person import Person
from model.group import Group

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('David', 'Gilmour')

    def test_person_str(self):
        self.assertEqual('Gilmour, David', str(self.person))

    def test_add_street_address(self):
        self.person.addStreetAddress('15 Charlotte Street')
        self.assertEqual(1, len(self.person.street_addresses))

    def test_add_empty_street_address(self):
        self.assertRaises(ValueError, self.person.addStreetAddress, '')

    def test_add_email_address(self):
        self.person.addEmailAddress('dgilmour@pf.uk')
        self.assertEqual(1, len(self.person.email_addresses))

    def test_add_empty_email_address(self):
        self.assertRaises(ValueError, self.person.addEmailAddress, '')

    def test_add_phone_number(self):
        self.person.addPhoneNumber('+44 7770 231 213')
        self.assertEqual(1, len(self.person.phone_numbers))

    def test_add_empty_phone_number(self):
        self.assertRaises(ValueError, self.person.addPhoneNumber, '')

    def test_add_person_to_group(self):
        groupPf = Group('Pink Floyd')
        groupSt = Group('Spinal Tap')

        self.person.addToGroup(groupPf)
        self.person.addToGroup(groupSt)

        self.assertEqual(2, len(self.person.groups))

        # Add person to a duplicated group, and verify that the
        # group count doesn't change
        groupPfDup = Group('Pink Floyd')

        self.person.addToGroup(groupPf)
        self.assertEqual(2, len(self.person.groups))

        # Verify that the Groups' members count got incremented
        self.assertEqual(1, len(groupPf.members))
        self.assertEqual(1, len(groupSt.members))

        # The duplicated Group's members did not get incremented
        self.assertEqual(0, len(groupPfDup.members))

if __name__ == '__main__':
    unittest.main()
