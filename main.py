import os

from fastapi import FastAPI
import clickhouse_connect

app = FastAPI()
password = os.environ.get("PASSWORD", "GQ25VTN~6lBLI")

client = clickhouse_connect.get_client(host='w55etl9fz2.europe-west4.gcp.clickhouse.cloud',
                                       port=8443, username='default', password=password)

with open("query.sql", "r", encoding="UTF8") as file:
    query_request = file.read()


@app.get("/getWords")
def read_first_item():
    result = client.query(query_request)
    json_response = {item[0]: item[1] for item in result.result_set}
    return json_response
