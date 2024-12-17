import uuid
import pytest
from datetime import datetime, timedelta

from models.repositories.trips_repository import TripsRepository
from models.settings.db_connection_handle import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4)

@pytest.mark.skip(reason="Interação com o banco")
def test_create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_repository.create_trip({
    "id": trip_id,
    "destination": "Rio de Janeiro",
    "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
    "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
    "owner_name": "João Silva",
    "owner_email": "joao@email.com"
  })

@pytest.mark.skip(reason="Interação com o banco")
def test_find_trip_by_id():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_repository.find_trip_by_id(trip_id)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_trips():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_repository.find_trips()

@pytest.mark.skip(reason="Interação com o banco")
def test_update_trip_status():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)

  trips_repository.update_trip_status(trip_id)