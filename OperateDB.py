# データベースを操作する方法とかを記したファイル

import sqlite3
import os


class OperatingDB():
    def __init__(self, sqlite_db_path):
        self.db_path = sqlite_db_path
        self.conn = None
        self.cur = None
        self._cursor()

    def connect(self):
        """接続"""
        if self.conn is not None:
            self.close()
        self.conn = sqlite3.connect(self.db_path)

    def _cursor(self):
        """カーソル"""
        if self.conn is None:
            self.connect()
        if self.cur is None:
            self.cur = self.conn.cursor()

    def create_table(self, table_insert):
        """テーブル作成"""
        self.cur.execute(
            '''CREATE TABLE %s''' % (table_insert))

    def commit(self):
        """DBの変更を反映"""
        self.conn.commit()

    def execute(self, exec_sql):
        """
        クエリ実行
            例: c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        @param
            exec_sql,str    : 実行クエリ
        """
        if self.cur is None:
            self._cursor()
        return self.cur.execute(exec_sql)

    def execute_many(self, exec_sql):
        """
        複数クエリ実行
        @param
            exec_sql,list   : 実行クエリ(リストで複数実行)
        """
        if self.cur is None:
            self._cursor()
        for exe in exec_sql:
            self.cur.execute(exe)

    def close(self):
        """DB操作閉じる"""
        if self.conn is not None:
            self.conn.close()
        self.cur = None
        self.conn = None


if __name__ == "__main__":
    sqlite_path = 'TEST.db'  # DBパス

    delete_flag = True  # DBを初期化する場合
    if delete_flag:
        os.remove(sqlite_path)  # DB削除

    db_obj = OperatingDB(sqlite_path)  # オブジェクト作成

    if delete_flag:
        # テーブル作成
        db_obj.create_table(
            "persons(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)")

    # 実行データ
    exe = ['''INSERT INTO persons(name) values("A")''', '''INSERT INTO persons(name) values("B")''',
           '''INSERT INTO persons(name) values("C")''']
    db_obj.execute_many(exe)  # 実行

    exe_sql = "SELECT * FROM persons"
    result = db_obj.execute(exe_sql).fetchall()  # 実行して中身を返す
    print(result)

    db_obj.commit()  # コミットは要らないかも?
    db_obj.close()
