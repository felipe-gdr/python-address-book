import unittest

from model.group import Group
from model.person import Person

class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = Group('Pink Floyd')

    def test_group_str(self):
        self.assertEqual('Pink Floyd', str(self.group))

    def test_add_members_to_group(self):
        david = Person('David', 'Gilmour')
        syd = Person('Syd', 'Barret')

        self.group.addPerson(david)
        self.group.addPerson(syd)

        self.assertEqual(2, len(self.group.members))

        # Verify that the People groups count got incremented
        self.assertEqual(1, len(david.groups))
        self.assertEqual(1, len(syd.groups))

        # Try to add person to a group that they are already a member of
        # and verify that the members count doesn't change
        self.group.addPerson(syd)
        self.assertEqual(2, len(self.group.members))

        # The persons' group count did not get incremented neither
        self.assertEqual(1, len(syd.groups))

if __name__ == '__main__':
    unittest.main()
