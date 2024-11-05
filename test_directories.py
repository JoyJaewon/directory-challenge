import unittest
from directories import DirectoryTree  

class TestDirectoryTree(unittest.TestCase):
    def setUp(self):
        self.directory_tree = DirectoryTree()

    def test_create(self):
        self.directory_tree.create('fruits')
        node, _ = self.directory_tree.find_node('fruits')
        self.assertIsNotNone(node)
        self.assertEqual(node.name, 'fruits')

    def test_move(self):
        self.directory_tree.create('fruits')
        self.directory_tree.create('vegetables')
        self.directory_tree.create('fruits/apples')
        self.directory_tree.move('fruits/apples', 'vegetables')
        node, _ = self.directory_tree.find_node('vegetables/apples')
        self.assertIsNotNone(node)
        self.assertEqual(node.name, 'apples')

    def test_delete(self):
        self.directory_tree.create('fruits')
        self.directory_tree.create('fruits/apples')
        self.directory_tree.delete('fruits/apples')
        node, _ = self.directory_tree.find_node('fruits/apples')
        self.assertIsNone(node)

    def test_list(self):
        self.directory_tree.create('fruits')
        self.directory_tree.create('fruits/apples')
        self.directory_tree.create('fruits/apples/fuji')
        self.directory_tree.create('vegetables')

    def test_invalid_move(self):
        self.directory_tree.create('fruits')
        self.directory_tree.create('fruits/apples')
        self.directory_tree.create('vegetables')
        self.directory_tree.move('fruits/apples', 'fruits/apples')

if __name__ == '__main__':
    unittest.main()
