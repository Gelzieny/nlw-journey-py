import uuid
import pytest

from  models.settings.db_connection_handle import db_connection_handler
from models.repositories.participants_repository import ParticipantsRepository


db_connection_handler.connect()
trip_id = str(uuid.uuid4)
part_id = str(uuid.uuid4)

@pytest.mark.skip(reason="Interação com o banco")
def test_create_participants():
  conn = db_connection_handler.get_connection()
  part_repository = ParticipantsRepository(conn)

  part_repository.register_participants({
    "id": part_id,
    "trip_id": trip_id,
    "emails_to_invite_id": "teste@gmail.com",
    "name": "Teste R. Silva"
  })