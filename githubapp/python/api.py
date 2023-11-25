
import mysql.connector

# 连接MySQL数据库
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="weather_db"
)

# 创建天气表
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE weather (city VARCHAR(255), temperature INT, humidity INT)")

# 插入天气数据
sql = "INSERT INTO weather (city, temperature, humidity) VALUES (%s, %s, %s)"
val = ("Beijing", 25, 60)
mycursor.execute(sql, val)

# 提交更改
mydb.commit()

# 打印插入的数据
print(mycursor.rowcount, "record inserted.")

# 关闭数据库连接
mydb.close()
