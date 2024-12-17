import uuid

class PartController:
  def __init__(self, part_repository=None, email_repository=None) -> None:
    self.__part_repository = part_repository
    self.__email_repository = email_repository

  def create(self, body, trip_id) -> dict:
    try:
      part_id = str(uuid.uuid4())
      email_id = str(uuid.uuid4())

      emails_infos = {
        "email": body['email'],
        "id": email_id,
        "trip_id": trip_id
      }

      part_infos = {
        "id": part_id,
        "trip_id": trip_id,
        "emails_to_invite_id": email_id,
        "name": body['name']
      }
      self.__email_repository.registry_email(emails_infos)
      self.__part_repository.register_participants(part_infos)

      return{
        "body": {"PartId": part_id},
        "status_code": 201
      }
    
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }

  def find_part_by_id(self, trip_id) -> dict:  
    try:
      part = self.__part_repository.find_participants_from_trip(trip_id)

      if isinstance(part, tuple):
        part = [part]
      
      if not part: raise Exception("No Trip Found")

      part_list = []

      for i in part:
        part_data = {
          "id": i[0],  
          "name": i[1], 
          "is_confirmed": i[2], 
          "email": "" if i[3] == None else i[3],  
        }
        part_list.append(part_data)

      return{
        "body": {
          "participants": part_list
        },
        "status_code": 200
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }
  
  def part_confirm(self, participantpId) -> dict:  
    try:
      self.__part_repository.update_participants_status(participantpId)
      return{
        "body": None,
        "status_code": 204
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }