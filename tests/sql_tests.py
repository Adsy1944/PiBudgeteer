import sql_connection


class TestClass():

    def test_connection(self):
        '''Test connection'''
        self.mydb = sql_connection.connect()
        print(self.mydb)
        assert self.mydb is not None
