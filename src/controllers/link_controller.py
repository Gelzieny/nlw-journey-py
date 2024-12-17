import uuid

class LinkController:
  def __init__(self, link_repository=None) -> None:
    self.__link_repository = link_repository

  def create(self, body, trip_id) -> dict:
    try:
      link_id = str(uuid.uuid4())
      self.__link_repository.register_link({
        "id": link_id,
        "trip_id": trip_id,
        "link": body['url'],
        "title": body["title"]
      })

      return{
        "body": {"linkId": link_id},
        "status_code": 201
      }
    
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }
  
  def find_link_by_id(self, trip_id: str) -> dict:
    try:
      link = self.__link_repository.find_links_from_trip(trip_id)

      if isinstance(link, tuple):
        link = [link]

      if not link: raise Exception("No Trip Found")

      link_list = []

      for i in link:
        link_data = {
          "id": i[0],  # ID do link
          "url": i[2],  # URL (email, no caso)
          "title": i[3]  # Título
        }
        link_list.append(link_data)

      return{
        "body": {
          "link":link_list
        },
        "status_code": 200
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }