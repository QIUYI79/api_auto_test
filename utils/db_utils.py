# utils/db_utils.py
import pymysql


class DBUtils:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='test_qa',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, sql, params=None):
        """执行查询，支持传参防SQL注入"""
        if params is None:
            params = ()
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

    def execute_update(self, sql, params=None):
        """执行增删改，支持传参"""
        if params is None:
            params = ()
        self.cursor.execute(sql, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()