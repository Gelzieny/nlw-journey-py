import uuid

class ActivityController:
  def __init__(self, activity_repository=None) -> None:
    self.__activity_repository = activity_repository

  def create(self, body, trip_id) -> dict:
    try:
      act_id = str(uuid.uuid4())

      self.__activity_repository.register_activity({
        "id": act_id,
        "trip_id": trip_id,
        "title": body['title'],
        "occurs_at": body['occurs_at']
      })

      return{
        "body": {"ActivityId": act_id},
        "status_code": 201
      }
    
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }
  
  def find_from_trip(self, trip_id) -> dict:  
    try:
      act = self.__activity_repository.find_activity_from_trip(trip_id)

      if not act: raise Exception("No Trip Found")

      act_list = [] 

      for i in act:
        act_data = {
          "id": i[0],
          "title": i[2],
          "occurs_at": i[3]
        }
        act_list.append(act_data)

      return{
        "body": {
          "activity": act_list
        },
        "status_code": 200
      }
    except Exception as exception:
      return{
        "body": {"error": "Bad Request", "message": str(exception)},
        "status_code": 400
      }