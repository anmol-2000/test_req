"""Model file for Application to handle Login, Create, Listing and Summary Logic"""
from utils import get_logger, get_db_connection
from auth import verify_hash, get_token


class ItemModel():
    def __init__(self):
        self.app_log = get_logger("item")
        self.conn = get_db_connection()

    async def create_item(self, item, userid):
        try:
            self.app_log.info("Adding new items to db")
            cursor = self.conn.cursor()
            cursor.execute("Insert into item_book (item_name, item_price, userid) values (?, ?, ?)", (item.item_name, item.item_price,userid))
            self.conn.commit()
            cursor.close()
            return {"Status": "Item Added Successfully"}
        except Exception as err:
            self.app_log.error(f"Error while creating item: {err}")
            return {"error": "Error while creating item"}

    async def get_item(self,userid):
        try:
            self.app_log.info("Getting Items from the db")
            cursor = self.conn.cursor()
            cursor.execute("Select item_name, item_price from item_book where userid = ?", (userid,))
            columns = [desc[0] for desc in cursor.description]
            items = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.close()
            return items
        except Exception as err:
            self.app_log.error(f"Error while getting item: {err}")
            return {"error": "Error while getting item"}

    async def get_summray(self, userid):
        try:
            self.app_log.info("Getting Items from the db")
            cursor = self.conn.cursor()
            cursor.execute("Select sum(item_price) from item_book where userid = ?",(userid,))
            item_total = cursor.fetchone()
            cursor.close()
            if item_total:
                return {'item_total': item_total[0]}
            else:
                return {'item_total': 0}
        except Exception as err:
            self.app_log.error(f"Error while getting item summary: {err}")
            return {"error":"Error while getting item"}

    async def auth(self,login):
        try:
            self.app_log.info("Authenticating user")
            cursor = self.conn.cursor()
            cursor.execute("Select * from user where userid = ?", (login.userid,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                if not await verify_hash(login.password, user[1]):
                    return {"error": "Invalid Credentials"}
                token = await get_token(login.userid)
                return {"token": token}
            else:
                return {"error": "Invalid Credentials"}
        except Exception as err:
            self.app_log.error(f"Error while authenticating user: {err}")
            return {"error":"Error while authenticating user"}




