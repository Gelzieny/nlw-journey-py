import uuid
from src.drivers.email_sender import send_email

class TripController:
  def __init__(self, trip_repository=None, email_repository=None) -> None:
    self.__trip_repository = trip_repository
    self.__email_repository = email_repository

  def create(self, body) -> dict:
    try:
      emails = body.get("emails_to_invite")
      trip_id = str(uuid.uuid4())

      trip_infos = {**body, "id": trip_id}

      self.__trip_repository.create_trip(trip_infos)

      if emails:
        for email in emails:
          self.__email_repository.registry_email({
            "id": str(uuid.uuid4()),
            "trip_id": trip_id,
            "email": email
          })

      send_email(
        [body["owner_email"]],
        f"http://localhost:3000/trips/{trip_id}/confirm"
      )
      
      return{
        "body": {"id": trip_id},
        "status_code": 201
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }
  
  def find_trip_details(self) -> dict:
    try:
      trip = self.__trip_repository.find_trips()
      if not trip: raise Exception("No Trip Found")

      trip_list = [] 

      for i in trip:
        trip_data = {
          "id": i[0],
          "destination": i[1],
          "start_date": i[2],
          "end_date": i[3],
          "owner_name": i[4],
          "owner_email": i[5],
          "status": "" if i[6] is None else i[6],
        }
        trip_list.append(trip_data)

      return{
        "body": {
          "trip": trip_list
        },
        "status_code": 200
      }
    
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      } 

  def find_trip_by_id(self, trip_id: str) -> dict:
    try:
      trip = self.__trip_repository.find_trip_by_id(trip_id)

      if not trip: raise Exception("No Trip Found")

      return{
        "body": {
          "trip":{
            "id": trip[0],
            "destination": trip[1],
            "start_date": trip[2],
            "end_date": trip[3],
            "owner_name": trip[4],
            "owner_email": trip[5],
            "status": "" if trip[6] == None else trip[6],
          }
        },
        "status_code": 200
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }
    
  def trip_confirm(self, trip_id) -> dict:  
    try:
      self.__trip_repository.update_trip_status(trip_id)
      return{
        "body": None,
        "status_code": 204
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }