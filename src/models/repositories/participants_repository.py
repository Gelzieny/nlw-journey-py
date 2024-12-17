from sqlite3 import Connection

class ParticipantsRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
  
  def register_participants(self, info_part: dict) -> None:
    cursor = self.__conn.cursor()
    sql = """INSERT INTO participants (id, trip_id, emails_to_invite_id, name)
         VALUES (:id, :trip_id, :emails_to_invite_id, :name)"""
    
    cursor.execute(sql, info_part)

    self.__conn.commit()

  def find_participants_from_trip(self, trip_id: str) -> list[tuple]:
    cursor = self.__conn.cursor()
    cursor.execute("""select 
                        p.id,
                        p.name,
                        p.is_confirmed,
                        eti.email
                      from participants as p
                        join emails_to_invite eti 
                          on eti.id = p.emails_to_invite_id 
                      where p.trip_id  = ?""", (trip_id,))
    return cursor.fetchall()
  
  def update_participants_status(self, part_id: str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute("""update participants SET is_confirmed = 1 WHERE id = ?""", (part_id,))
    self.__conn.commit()

  def find_participants(self):
    cursor = self.__conn.cursor()
    cursor.execute(f"""select 
                          p.id,
                          p.name,
                          p.is_confirmed,
                          eti.email
                        from participants as p
                          join emails_to_invite eti 
                            on eti.id = p.emails_to_invite_id """)
    return  cursor.fetchall()
