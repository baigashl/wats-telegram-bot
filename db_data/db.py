
from config_data import TOKEN, user, password, db_name, ip
import psycopg2


try:
    connection = psycopg2.connect(
        host=ip,
        user=user,
        password=password,
        database=db_name,
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"server version: {cursor.fetchone()}")
    print(connection.cursor())
    print('first')
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users_db_tel_bot(
                id serial PRIMARY KEY,
                sku varchar(50) NOT NULL,
                product_name varchar(255) NOT NULL,
                image1 varchar(255),
                image2 varchar(255),
                image3 varchar(255),
                image4 varchar(255),
                image5 varchar(255),
                image6 varchar(255),
                image7 varchar(255),
                image8 varchar(255),
                image9 varchar(255),
                image10 varchar(255),
                image11 varchar(255),
                image12 varchar(255),
                image13 varchar(255),
                image14 varchar(255),
                image15 varchar(255)
                );
                """
        )
    print('second')

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT sku FROM users_db_tel_bot;"""
        )
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users_db_tel_bot;"""
        )
        data = cursor.fetchall()
        p = {}
        for i in data:
            p[i[1]] = []
            for n in i[2:]:
                if n != None:
                    p[i[1]].append(n)
        # print(p)

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS info_user(
                id_order bigint NOT NULL,
                user_name varchar(50) NOT NULL,
                phone varchar(50) NOT NULL,
                product varchar(255) NOT NULL,
                status varchar(50),
                sku varchar(50) NOT NULL,
                send varchar(10) NOT NULL
                );
                """
        )

except Exception as ex:
    print("Error")

finally:
    pass