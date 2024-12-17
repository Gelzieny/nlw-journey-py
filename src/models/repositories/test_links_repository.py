import uuid
import pytest

from models.repositories.links_repository import LinksRepository
from  models.settings.db_connection_handle import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4)
link_id = str(uuid.uuid4)


@pytest.mark.skip(reason="Interação com o banco")
def test_register_link():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  link_repository.register_link({
    "id": link_id,
    "trip_id": trip_id,
    "link": "somelink.com",
    "title": "Instagram"
  })

@pytest.mark.skip(reason="Interação com o banco")
def test_find_links_from_trip():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  link_repository.find_links_from_trip(trip_id)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_links():
  conn = db_connection_handler.get_connection()
  link_repository = LinksRepository(conn)

  link_repository.find_links()
