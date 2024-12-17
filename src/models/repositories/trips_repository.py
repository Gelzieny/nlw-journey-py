from sqlite3 import Connection

class TripsRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
    

  def create_trip(self, trips_infos: dict) -> None:
    cursor = self.__conn.cursor()
    sql = """INSERT INTO trips (id, destination, start_date, end_date, owner_name, owner_email)
         VALUES (:id, :destination, :start_date, :end_date, :owner_name, :owner_email)"""

    cursor.execute(sql, trips_infos)

    self.__conn.commit()

  def find_trips(self):
    cursor = self.__conn.cursor()
    cursor.execute(f"""SELECT * FROM TRIPS""")
    return  cursor.fetchall()

  def find_trip_by_id(self, trip_id: str) -> tuple:
    cursor = self.__conn.cursor()
    cursor.execute("""SELECT * FROM TRIPS WHERE id = ?""", (trip_id,))
    return cursor.fetchone()

  
  def update_trip_status(self, trip_id: str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute("""UPDATE TRIPS SET STATUS = 1 WHERE id = ?""", (trip_id,))
    self.__conn.commit()