import uuid
import pytest

from models.repositories.email_repository import EmailsRepository
from models.settings.db_connection_handle import db_connection_handler


db_connection_handler.connect()
trip_id = str(uuid.uuid4)
email_id = str(uuid.uuid4)

@pytest.mark.skip(reason="Interação com o banco")
def test_registry_email():
  conn = db_connection_handler.get_connection()
  email_repository = EmailsRepository(conn)

  email_repository.registry_email({
    "id": email_id,
    "trip_id": trip_id,
    "email": "teste@email.com"
  })

@pytest.mark.skip(reason="Interação com o banco")
def test_find_emails():
  conn = db_connection_handler.get_connection()
  email_repository = EmailsRepository(conn)

  email_repository.find_emails()

@pytest.mark.skip(reason="Interação com o banco")
def test_find_email_from_trip():
  conn = db_connection_handler.get_connection()
  email_repository = EmailsRepository(conn)

  email_repository.find_email_from_trip(trip_id)

@pytest.mark.skip(reason="Interação com o banco")
def test_update_email_from_id():
  conn = db_connection_handler.get_connection()
  email_repository = EmailsRepository(conn)

  email_repository.update_email(email_id, "data.gmail.com")