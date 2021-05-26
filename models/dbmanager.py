import psycopg2


class Database:
    def __init__(self, MainGame):
            """connect remote database"""
            self.conn = psycopg2.connect(
            host="ec2-54-152-185-191.compute-1.amazonaws.com",
            database="d92mgnjut4mfd1",
            user="bpfvqodctmlkfk",
            port="5432",
            password="2e2c399974dd83b5ac8664d0fbe7e0f6c2aad1e335b3d5e2948579fd5e5e0fca")
            self.c = self.conn.cursor()
            self.MainGame = MainGame

    def createtable(self):
        """check if table exist, if not create table"""
        self.c.execute("select * from information_schema.tables where table_name=%s", ('scores',))
        if bool(self.c.rowcount) == False:
            self.c.execute("CREATE TABLE scores (id varchar, name varchar,level integer,score integer)")

    def updatescore(self):
        """check user exist, if exist, update score and level"""
        usercheck = """select * from scores where name = %s"""
        self.c.execute(usercheck, (self.MainGame.username,))
        if bool(self.c.rowcount) != False:
            checkhistory = "select score from scores where name = %s"
            username = [f'{self.MainGame.username}']
            self.c.execute(checkhistory,username)
            oldrecord = self.c.fetchone()
            if self.MainGame.score > oldrecord[0]:
                updatescore = "UPDATE scores SET level = %s, score = %s where name = %s"
                selfscore =[f'{self.MainGame.level}', f'{self.MainGame.score}', f'{self.MainGame.username}']
                self.c.execute(updatescore, selfscore)
                self.conn.commit()
        elif bool(self.c.rowcount) == False:
            self.newrecord()
        
    def newrecord(self):
        """ create new record if user not exist """
        sql = "INSERT INTO scores (id, name, level, score) VALUES (%s, %s, %s, %s)"
        val = [f'{self.MainGame.id}', f'{self.MainGame.username}', f'{self.MainGame.level}', f'{self.MainGame.score}']
        self.c.execute(sql, val)
        self.conn.commit()

    def savescore(self):
        self.createtable()
        self.updatescore()
        self.c.close()
        self.conn.close()
