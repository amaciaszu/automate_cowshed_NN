import unittest
import pandas as pd

from modules.validations import is_valid_date, is_valid_timestamp_float
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from modules.crud import insert_cow, get_cow, get_sensor, insert_measurement, insert_sensor
from modules.models import Cow, Measurement, Sensor
from modules.request import insert_df_to_table

class UnitTestFunctions(unittest.TestCase):

    def test_is_valid_date_valid(self):
        self.assertTrue(is_valid_date("2024-08-23"))
        self.assertTrue(is_valid_date("2024-08-23", "%Y-%m-%d"))

    def test_is_valid_date_invalid(self):
        self.assertFalse(is_valid_date("2024-13-23"))  # Invalid month
        self.assertFalse(is_valid_date("23-08-2024", "%Y-%m-%d"))  # invalid format
        self.assertFalse(is_valid_date("2024/08/23"))  # invalid separator
        self.assertFalse(is_valid_date("2024-08-32"))  # invalid day

    def test_is_valid_date_custom_format(self):
        self.assertTrue(is_valid_date("23-08-2024", "%d-%m-%Y"))
        self.assertFalse(is_valid_date("08-23-2024", "%d-%m-%Y"))  # invalid format

    def test_is_valid_timestamp_float_valid(self):
        self.assertTrue(is_valid_timestamp_float(1692748800.0))  # 2023-08-23 00:00:00 UTC
        self.assertTrue(is_valid_timestamp_float(0.0))

    @patch('data_base.database.get_db_connection')
    @patch('modules.validations.is_valid_date')
    def test_insert_cow_success(self, mock_is_valid_date, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_is_valid_date.return_value = True

        cow = Cow(id="1", name="Bessie", birthdate="2020-01-01")
        response = insert_cow(cow)

        self.assertEqual(response, {"id": cow.id, "name": cow.name, "birthdate": cow.birthdate})

    @patch('data_base.database.get_db_connection')
    @patch('modules.validations.is_valid_date')
    def test_insert_cow_invalid_date(self, mock_is_valid_date, mock_get_db_connection):
        mock_is_valid_date.return_value = False
        cow = Cow(id="1", name="Bessie", birthdate="invalid-date")

        with self.assertRaises(HTTPException) as context:
            insert_cow(cow)

        self.assertEqual(context.exception.status_code, 500)
        self.assertEqual(context.exception.detail,
                         "Error inserting cow birthdate in the database. Birthdate must be a valid date")

    @patch('data_base.database.get_db_connection')
    def test_get_cow_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = ('1', 'Bessie', '2020-01-01')

        cow = get_cow("1")
        self.assertEqual((cow['id'], cow['name'], cow['birthdate']), ('1', 'Bessie', '2020-01-01'))

    @patch('data_base.database.get_db_connection')
    @patch('modules.validations.is_valid_timestamp_float')
    def test_insert_measurement_successs(self, mock_is_valid_timestamp_float, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        is_valid_timestamp_float.return_value = True

        measurement = Measurement(sensor_id="1", cow_id="1", timestamp=1692748800.0, value=10.5)
        response = insert_measurement(measurement)

        self.assertEqual(response, {"sensor_id": measurement.sensor_id, "cow_id": measurement.cow_id, "timestamp": measurement.timestamp, "value": measurement.value})

    @patch('data_base.database.get_db_connection')
    def test_insert_sensor_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        sensor = Sensor(id="1", unit="L")
        response = insert_sensor(sensor)

        self.assertEqual(response, {"id": sensor.id, "unit": sensor.unit})

    @patch('data_base.database.get_db_connection')
    def test_get_sensors_success(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = ('1', 'L')

        sensor = get_sensor("1")
        self.assertEqual((sensor['id'], sensor['unit']), ('1', 'L'))

    @patch('requests.post')
    def test_insert_df_to_table(self, mock_post):
        data = {
            'col1': [1, 2],
            'col2': ['a', 'b']
        }
        df = pd.DataFrame(data)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        insert_df_to_table('http://fakeurl.com', df)

        expected_calls = [
            (('http://fakeurl.com',), {'json': {'col1': 1, 'col2': 'a'}}),
            (('http://fakeurl.com',), {'json': {'col1': 2, 'col2': 'b'}})
        ]
        mock_post.assert_has_calls(expected_calls, any_order=False)

        self.assertEqual(mock_post.call_count, 2)

if __name__ == "__main__":
    unittest.main()
