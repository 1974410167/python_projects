import random
import time
import pymysql
from faker import Faker
from concurrent.futures import ThreadPoolExecutor
db = pymysql.connect(
    host='127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'performance_test',
    charset = 'utf8'
)



class gen_job():

    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    def g_name(self):

        name = self.fake.name()
        return repr(name)

    def g_grade(self):

        grade = random.randint(0,100)
        return grade

class gen_user():
    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    def gu_name(self):

        name = self.fake.name()
        return repr(name)
    def gu_phone(self):

        phone = self.fake.phone_number()
        return repr(phone)
    def gu_address(self):

        address = self.fake.address()
        return repr(address)
    def gu_cs_id(self):

        cs_id = random.randint(0,1000000)
        return cs_id



def insert_sql():
    t1 = time.time()

    with db.cursor() as cur:

        obj = gen_job()

        for _ in range(100):

            sql = f"insert into cs_grade(c_name,c_grade) values"
            for i in range(9):
                c_name = obj.g_name()
                c_grade = obj.g_grade()

                sql = sql + f"({c_name},{c_grade}),"

            c_name = obj.g_name()
            c_grade = obj.g_grade()

            sql = sql + f"({c_name},{c_grade})"
            cur.execute(sql)

        db.commit()
    t2 = time.time()
    print(t2-t1)

def main():
    with ThreadPoolExecutor(max_workers=10) as f:




if __name__ == '__main__':











