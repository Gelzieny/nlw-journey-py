from sqlite3 import Connection

class EmailsRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
    

  def registry_email(self, emails_infos: dict) -> None:
    cursor = self.__conn.cursor()
    sql = """INSERT INTO emails_to_invite (id, trip_id, email)
         VALUES (:id, :trip_id, :email)"""
    
    cursor.execute(sql, emails_infos)
    self.__conn.commit()

  def find_emails(self):
    cursor = self.__conn.cursor()
    cursor.execute(f"""SELECT * FROM emails_to_invite""")
    return  cursor.fetchall()

  def find_email_from_trip(self, trip_id: str) -> list[tuple]:
    cursor = self.__conn.cursor()
    cursor.execute("""SELECT * FROM emails_to_invite WHERE id = ?""", (trip_id,))
    return cursor.fetchall()
  
  def update_email(self, email_id: str, email_user: str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute("""UPDATE emails_to_invite SET EMAIL = ? WHERE id = ?""", (email_user, email_id,))
    self.__conn.commit()