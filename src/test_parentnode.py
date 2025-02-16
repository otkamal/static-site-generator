import unittest
import parentnode
import leafnode

VALID_TWO_PROPS_DICT = {"prop_1":"val_1", "prop_2":"val_2"}
VALID_ONE_PROP_DICT = {"prop_A":"val_A"}

# VALID_LEAFNODE_NO_PROPS = leafnode.LeafNode(tag = "tag", value = "value", props = None)
# VALID_LEAFNODE_NO_TAG_NO_PROPS = leafnode.LeafNode(value = "value", props = None)
# VALID_LEAFNODE_EMPTY_PROPS = leafnode.LeafNode(tag = "tag", value = "value", props = {})
# VALID_LEAFNODE_ONE_PROP = leafnode.LeafNode(tag = "tag", value = "value", props = VALID_ONE_PROP_DICT)
# VALID_LEAFNODE_TWO_PROPS = leafnode.LeafNode(tag = "tag", value = "value", props = VALID_TWO_PROPS_DICT)
# INVALID_LEAFNODE_BAD_VALUE = leafnode.LeafNode(tag = "tag", value = None, props = VALID_TWO_PROPS_DICT)
# INVALID_LEAFNODE_BAD_PROPS = leafnode.LeafNode(tag = "tag", value = "value", props = 5)
# INVALID_LEAFNODE_MISSING_ALL = leafnode.LeafNode(tag = None, value = None, props = None)

# VALID_PARENTNODE_ONE_VALID_CHILD = parentnode.ParentNode(tag = "tag", children = [VALID_LEAFNODE_EMPTY_PROPS], props = None)
# VALID_PARENTNODE_TWO_VALID_CHILDREN = parentnode.ParentNode(tag = "tag", children = [VALID_LEAFNODE_EMPTY_PROPS, VALID_LEAFNODE_ONE_PROP], props = None)
# VALID_PARENTNODE_ONE_VALID_ONE_INVALID_CHILDREN = parentnode.ParentNode(tag = "tag", children = [VALID_LEAFNODE_EMPTY_PROPS, INVALID_LEAFNODE_BAD_PROPS], props = None)
# VALID_PARENTNODE_PARENT_CHILD = parentnode.ParentNode(tag = "tag", children = [VALID_PARENTNODE_ONE_VALID_CHILD], props = None)
# VALID_PARENTNODE_NESTED_PARENTS = parentnode.ParentNode(tag = "tag", children = [VALID_PARENTNODE_PARENT_CHILD], props = VALID_TWO_PROPS_DICT)
# VALID_PARENTNODE_ONE_PARENT_ONE_CHILD_CHILDREN = parentnode.ParentNode(tag = "tag", children = [VALID_PARENTNODE_ONE_VALID_CHILD, VALID_LEAFNODE_ONE_PROP], props = None)
# INVALID_PARENTNODE_EMPTY_CHILDREN = parentnode.ParentNode(tag = "tag", children = [], props = VALID_ONE_PROP_DICT)
# INVALID_PARENTNODE_NO_CHILDREN = parentnode.ParentNode(tag = "tag", props = VALID_ONE_PROP_DICT)
# INVALID_PARENTNODE_BAD_CHILDREN = parentnode.ParentNode(tag = "tag", children = [INVALID_LEAFNODE_BAD_PROPS, INVALID_PARENTNODE_NO_CHILDREN], props = None)
# INVALID_PARENTNODE_BAD_PROPS = parentnode.ParentNode(tag = "tag", children = [VALID_LEAFNODE_NO_PROPS], props = 5)

class TestParentNode(unittest.TestCase):
    
    def test_invalid_parent_empty_children(self):
        with self.assertRaises(ValueError):
            parentnode.ParentNode(tag = "tag", children = [], props = VALID_ONE_PROP_DICT)
    
    def test_invalid_parent_no_children(self):
        with self.assertRaises(ValueError):
            parentnode.ParentNode(tag = "tag", props = VALID_ONE_PROP_DICT)

    def test_valid_parent_one_valid_child(self):
        self.assertIsInstance(
            parentnode.ParentNode(
                tag = "tag",
                children = [leafnode.LeafNode(tag = "tag", value = "value", props = {})],
                props = None
            ),
            parentnode.ParentNode
        )

    def test_valid_parent_many_valid_children(self):
        self.assertIsInstance(
            parentnode.ParentNode(
                tag = "tag",
                children = [
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {})
                ],
                props = None
            ),
            parentnode.ParentNode
        )

    def test_valid_parent_many_different_children(self):
        self.assertIsInstance(
            parentnode.ParentNode(
                tag = "tag",
                children = [
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                    parentnode.ParentNode(
                        tag = "tag",
                        children = [
                            leafnode.LeafNode(tag = "tag", value = "value", props = {})
                        ], 
                        props = None
                    ),
                    parentnode.ParentNode(
                        tag = "tag",
                        children = [
                            leafnode.LeafNode(tag = "tag", value = "value", props = {})
                        ], 
                        props = None
                    ),
                    parentnode.ParentNode(
                        tag = "tag",
                        children = [
                            leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                            leafnode.LeafNode(tag = "tag", value = "value", props = {}),
                            leafnode.LeafNode(tag = "tag", value = "value", props = {})
                        ], 
                        props = None
                    )
                ],
                props = None
            ),
            parentnode.ParentNode
        )


if __name__ == "__main__":
    unittest.main(verbosity = 2)