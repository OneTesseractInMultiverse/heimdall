import unittest
from heimdall.models.model_base import ModelBase


class ModelBaseTests(unittest.TestCase):

    def setUp(self) -> None:
        self.test_state = {
            "state_id": "79a31f70-da87-41b3-b9a6-f946d394b387",
            "test_property": 1234,
            "test_property_2": "this is a test property"
        }

    def test_unit_as_dict_using_valid_dictionary_is_same_dictionary_as_constructor_param(self):
        # Prepare
        model = ModelBase(state=self.test_state)

        # Act
        expected = {
            "state_id": "79a31f70-da87-41b3-b9a6-f946d394b387",
            "test_property": 1234,
            "test_property_2": "this is a test property"
        }
        actual = model.as_dict()

        # Assert
        self.assertDictEqual(expected, actual)

    def test_unit_update_when_field_updated_uncommitted_changes_is_true(self):
        # Prepare
        model = ModelBase(state=self.test_state)

        # Act
        model.update({
            "test_property_2": "this is an updated property"
        })
        actual = model.has_uncommitted_changes

        # Assert
        self.assertTrue(actual)
