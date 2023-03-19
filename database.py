from influxdb_client import InfluxDBClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('INFLUX_URL')
token = os.getenv('INFLUX_TOKEN')
bucket = os.getenv('INFLUX_BUCKET')
org = os.getenv('INFLUX_ORG')

class DB():
    def __init__(self):
        self.client = InfluxDBClient(url=url, token=token, org=org)

    def query(self, query):
        return self.client.query_api().query(query, org=org)


def main():
    db = DB()
    Humidity_query = """option v = {timeRangeStart: -1h, timeRangeStop: now()}
                from(bucket: "DEV")
                |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
                |> filter(fn: (r) => r["_measurement"] == "SENSOR_DATA")
                |> filter(fn: (r) => r["DATA"] == "BME")
                |> filter(fn: (r) => r["device"] == "STAB_1")
                |> filter(fn: (r) => r["_field"] == "Humidity")
            """
    tables = db.query(Humidity_query)
    for table in tables:
        for record in table.records:
            print(f"{record.values.get('_field')} = {record.values.get('_value')} ")

if __name__ == '__main__':
    main()




