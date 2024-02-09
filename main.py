from fastapi import FastAPI
from billboard import ChartData

def getChart(year):
    chart = ChartData("hot-100-songs", year=year)
    return chart

app = FastAPI()

@app.get("/")
async def root():
    return {"welcome, this is a little ugly"}


@app.get("/hot-100/{year}")
def read_item(year: str):
    hot_100 = getChart(year)
    return {hot_100}
