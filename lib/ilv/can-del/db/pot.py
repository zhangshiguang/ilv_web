#!/usr/local/bin/python3
#-*-code:utf8-*-
"""
Sumary:
These are methods of databse
get_db get a database

"""

# 动态加载所需要的数据链接库
import importlib

########################################################################
# 获取默认数据库
# 参数名称 dbType   dbHost     dbUsr    dbPsw   dbName
# 参数作用 数据类型 数据服务器  登陆用户 登陆密码 数据库名
# SQLite值 sqlite   None       None     None    data/sqlite/ilv_db 
# MySQL值  mysql    localhost  root             ilv_db  
########################################################################
def get_db(dbType="sqlite",
           dbHost=None, 
           dbUsr=None, 
           dbPsw=None,
           dbName="data/sqlite/ilv_db"):
    db = None
    if dbType=="sqlite":
        db_lib = importlib.import_module("ilv.db.SQLite")
        db = db_lib.SQLite(dbHost=dbHost, dbUsr=dbUsr, dbPsw=dbPsw, dbName=dbName)
    elif dbType=="mysql":
        db_lib = importlib.import_module("ilv.db.MySQL")
        db = db_lib.MySQL(dbHost=dbHost, dbUsr=dbUsr, dbPsw=dbPsw, dbName=dbName)
    elif dbType=="Oracle":
        pass
    else:
        db_lib = importlib.import_module("ilv.db.SQLite")
        db = db_lib.SQLite(dbHost=dbHost, dbUsr=dbUsr, dbPsw=dbPsw, dbName=dbName)
    return db

########################################################################
# 获取SQLite数据库
########################################################################
def get_sqlite_db(dbHost=None,
                  dbUsr=None,
                  dbPsw=None,
                  dbName="data/sqlite/ilv_db"):
    return get_db(dbType="sqlite",dbHost=dbHost,dbUsr=dbUsr,dbPsw=dbPsw,dbName=dbName)

########################################################################
# 获取Mysql数据库
########################################################################
def get_mysql_db(dbHost="localhost",
                  dbUsr="root",
                  dbPsw="",
                  dbName="ilv_db"):
    return get_db(dbType="mysql",dbHost=dbHost,dbUsr=dbUsr,dbPsw=dbPsw,dbName=dbName)

