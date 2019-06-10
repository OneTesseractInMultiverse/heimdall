import unittest
from dateutil.parser import *
import datetime
from heimdall.models.application import (
    Application
)


class ApplicationModelTests(unittest.TestCase):

    def setUp(self) -> None:
        self.application_state = {
            "application_id": "79a31f70-da87-41b3-b9a6-f946d394b387",
            "callback_url": "https://www.funnyurl.com/",
            "configuration": {
                "version": "2.8"
            },
            "description": "Counts the work force per department and users",
            "environment": "People work and get paid to get things done",
            "is_enabled": True,
            "last_modified": "Thu, 23 May 2019 03:30:20 GMT",
            "name": "Head Count Machine",
            "private_key": "QgVsC;0~#_^-VuOCCx>hlRzup!e5t=",
            "public_key": "o4/-*#U(neKGssZK&5^^Yl{KBZID~,"
        }

    # -------------------------------------------------------------------------
    # TEST UNIT APPLICATION ID IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_application_id_is_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        expected = '79a31f70-da87-41b3-b9a6-f946d394b387'
        actual = application.id

        # Assert
        self.assertEqual(expected, actual)

    # -------------------------------------------------------------------------
    # TEST UNIT APPLICATION CALLBACK URL IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_callback_url_is_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        expected = "https://www.funnyurl.com/"
        actual = application.callback_url

        # Assert
        self.assertEqual(expected, actual)

    # -------------------------------------------------------------------------
    # TEST UNIT PRIVATE KEY IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_private_key_is_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        expected = "QgVsC;0~#_^-VuOCCx>hlRzup!e5t="
        actual = application.private_key

        # Assert
        self.assertEqual(expected, actual)

    # -------------------------------------------------------------------------
    # TEST UNIT PUBLIC KEY IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_public_key_is_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        expected = "o4/-*#U(neKGssZK&5^^Yl{KBZID~,"
        actual = application.public_key

        # Assert
        self.assertEqual(expected, actual)

    # -------------------------------------------------------------------------
    # TEST UNIT LAST MODIFIED IS VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_last_modified_is_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        expected = parse("Thu, 23 May 2019 03:30:20 GMT")
        actual = application.last_modified

        # Assert
        self.assertEqual(expected, actual)

    # -------------------------------------------------------------------------
    # TEST UNIT LAST MODIFIED IS DATETIME VALID WHEN INITIAL STATE IS GIVEN
    # -------------------------------------------------------------------------
    def test_unit_last_modified_is_datetime_valid_when_initial_state_is_given(self):
        # Prepare
        application = Application(state=self.application_state)

        # Expected
        actual = application.last_modified

        # Assert
        self.assertIsInstance(actual, datetime.datetime)
