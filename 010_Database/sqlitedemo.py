import sqlite3


con = sqlite3.connect("mydb.db")

# qry = "create table student(id int primary key,name varchar(20),email varchar(40),phone varchar(15))"

# qry = "insert into student values(2,'jay','jay@gmail.com','7485968574')"

# qry = "update student set phone='4567896352' where id=2"

# qry = "delete from student where id=2"
# con.execute(qry)
# con.commit()

qry = "alter table student add column gender varchar(10)"

con.execute(qry)



# qry = "select * from student"
# data = con.execute(qry).fetchall()

# for i in data:
#     for j in i:
#         print(j,end="  ")
#     print()