import unittest
from dateutil.parser import *
import datetime
from heimdall.models.identity import (
    Identity
)


class IdentityModelTests(unittest.TestCase):

    def setUp(self) -> None:
        self.identity_state = {
            "identity_id": '47422981-44bd-4d5f-8e57-dde7f411de50',
            "business_id": "3487-8732",
            "identity_data": {"user_name": "John Smith", "department":  "Accountability"},
            "created": "Thu, 23 May 2019 03:30:20 GMT",
            "last_modified": "Thu, 23 May 2019 03:30:20 GMT",
            "disabled": False,
            "type": 'user_identity'
        }

    # -------------------------------------------------------------------------
    # TEST IDENTITY ID IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_identity_id_is_valid_when_initial_state_is_given(self):
        # Prepare
        identity = Identity(state=self.identity_state)

        # Expected
        expected = '47422981-44bd-4d5f-8e57-dde7f411de50'
        actual = identity.id

        # Assert
        self.assertEqual(expected, actual)

    def test_unit_business_id_is_valid_when_initial_state_is_given(self):
        # Prepare
        identity = Identity(state=self.identity_state)

        # Expected
        expected = '3487-8732'
        actual = identity.business_id

        # Assert
        self.assertEqual(expected, actual)

    def test_unit_last_modified_is_valid_when_initial_state_is_given(self):
        # Prepare
        identity = Identity(state=self.identity_state)

        # Expected
        expected = parse('Thu, 23 May 2019 03:30:20 GMT')
        actual = identity.last_modified

        # Assert
        self.assertEqual(expected, actual)

    def test_unit_type_is_valid_when_initial_state_is_given(self):
        # Prepare
        identity = Identity(state=self.identity_state)

        # Expected
        actual = identity.last_modified

        # Assert
        self.assertIsInstance(actual, datetime.datetime)