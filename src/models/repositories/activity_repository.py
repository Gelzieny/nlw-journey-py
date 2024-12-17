from sqlite3 import Connection

class ActivityRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
  
  def register_activity(self, info_act: dict) -> None:
    cursor = self.__conn.cursor()
    sql = """INSERT INTO activities (id, trip_id, title, occurs_at)
              VALUES (:id, :trip_id, :title, :occurs_at)"""
    
    cursor.execute(sql, info_act)

    self.__conn.commit()

  def find_activity(self):
    cursor = self.__conn.cursor()
    cursor.execute(f"""SELECT * FROM activities""")
    return  cursor.fetchall()

  def find_activity_from_trip(self, trip_id: str) -> list[tuple]:
    cursor = self.__conn.cursor()
    cursor.execute("""SELECT * FROM activities WHERE trip_id = ?""", (trip_id,))
    return cursor.fetchall()