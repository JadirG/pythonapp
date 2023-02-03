import uvicorn
import cx_Oracle
from fastapi import FastAPI

connection = cx_Oracle.connect("USR_STAGE_DWH", "mriReqZu6bGCt#=aAme3", "ALIAS_DB_DSTAGEDWH:1521/DSTAGEDWH_SRV")
cursor = connection.cursor()
cursor.execute("SELECT sysdate FROM dual")

# Fetch and print the result of the query
result = cursor.fetchone()

app = FastAPI()


@app.get("/")
async def root():
    return {"Uvicorn": result[0]}
    cursor.close()
    connection.close()