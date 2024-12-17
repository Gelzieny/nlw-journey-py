from sqlite3 import Connection

class LinksRepository:
  def __init__(self, conn: Connection) -> None:
    self.__conn = conn
  
  def register_link(self, info_link: dict) -> None:
    cursor = self.__conn.cursor()
    sql = """INSERT INTO links (id, trip_id, link, title)
             VALUES (:id, :trip_id, :link, :title)"""
    
    cursor.execute(sql, info_link)

    self.__conn.commit()

  def find_links(self):
    cursor = self.__conn.cursor()
    cursor.execute(f"""SELECT * FROM links""")
    return  cursor.fetchall()

  def find_links_from_trip(self, trip_id: str) -> tuple:
    cursor = self.__conn.cursor()
    cursor.execute("""SELECT * FROM links WHERE trip_id = ?""", (trip_id,))
    return cursor.fetchone()