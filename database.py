# -*- coding: utf-8 -*-
import pymssql
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
DB_SERVER = config["DB_SERVER"]
DB_USERNAME = config["DB_USERNAME"]
DB_PASSWORD = config["DB_PASSWORD"]
DB_NAME = config["DB_NAME"]

# Thông tin kết nối
server = DB_SERVER  # Tên server hoặc địa chỉ IP
user = DB_USERNAME      # Tên người dùng SQL Server
password = DB_PASSWORD   # Mật khẩu
database = DB_NAME  # Tên cơ sở dữ liệu

try:
    # Kết nối đến SQL Server
    conn = pymssql.connect(server, user, password, database)
    print("Kết nối thành công đến SQL Server!")

    # Tạo cursor để thực hiện truy vấn
    cursor = conn.cursor()

    # Truy vấn dữ liệu
    cursor.execute("SELECT TOP 1 * FROM ta_inspectionmst")

    # Lấy kết quả
    for row in cursor.fetchall():
        print(row)

    # Đóng kết nối
    conn.close()

except pymssql.InterfaceError as e:
    print("Lỗi kết nối SQL Server: {}".format(e))
except pymssql.DatabaseError as e:
    print("Lỗi cơ sở dữ liệu: {}".format(e))
