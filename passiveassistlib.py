'''
BetterFPS and Nicephore was neither made by people from Quad Cities.

Url: https://www.google.com/maps/preview/passiveassist?pb=!1m10!2m9!1m3!1d{dist}!2d{lng}!3d{lat}!2m0!3m2!1i1034!2i620!4f14!3m2!1sZBuUX_qxIsOA9QPH_b3QDA!7e81!7m{patype}!2b1!12b1!32b1!10m1!2i2&hl=en&gl=US&authuser=0

PassiveAssist library
2020 WS01
'''
import json
try:
    import httpx as httpapi
    hsession = httpapi.Client(http2=True)
    htimeout = httpapi.Timeout(read=900, write=900, pool=900, connect_timeout=900)
except Exception:
    import requests as httpapi
    hsession = httpapi.Session()
    adapter = httpapi.adapters.HTTPAdapter(
        pool_connections=128,
        pool_maxsize=128
    )
    hsession.mount("http://", adapter)
    hsession.mount("https://", adapter)
    htimeout = httpapi.Timeout(900)

PASSIVEASSIST_CURLOC = 7
PASSIVEASSIST_CURLOC_PLACENAME = 1
PASSIVEASSIST_CURLOC_WEATHER = 5
PASSIVEASSIST_CURLOC_WEATHER_ICON = 0
PASSIVEASSIST_CURLOC_WEATHER_TEMPRATURE = PASSIVEASSIST_CURLOC_PLACENAME
PASSIVEASSIST_CURLOC_WEATHER_STATUS = 3

def parseAssist(assist: list):
    asPlaceName = assist[PASSIVEASSIST_CURLOC][PASSIVEASSIST_CURLOC_PLACENAME]
    asWeather = assist[PASSIVEASSIST_CURLOC][PASSIVEASSIST_CURLOC_WEATHER]
    wout = None
    if asWeather:
        if len(asWeather) > 1:
            asWeatherIcon = asWeather[PASSIVEASSIST_CURLOC_WEATHER_ICON]
        else:
            asWeatherIcon = None
        if len(asWeather) > 2:
            asWeatherTemp = asWeather[PASSIVEASSIST_CURLOC_WEATHER_TEMPRATURE]
        else:
            asWeatherTemp = None
        if len(asWeather) > 3:    
            asWeatherStat = asWeather[PASSIVEASSIST_CURLOC_WEATHER_STATUS]
        else:
            asWeatherStat = None
        wout = {"weatherIcon":asWeatherIcon,"currentTemprature":asWeatherTemp,"status":asWeatherStat}
    return {"placeName": asPlaceName, "weather":wout}

def getAssistStr(loc: str, dist: float, patype: int=3):
    lat, lng = loc.split(",")
    return getAssist(float(lat),float(lng), dist, patype)

def getAssist(lat: float, lng: float, dist: float, patype: int=3):
    lnk = f"https://www.google.com/maps/preview/passiveassist?pb=!1m10!2m9!1m3!1d{dist}!2d{lng}!3d{lat}!2m0!3m2!1i1034!2i620!4f14!3m2!1sZBuUX_qxIsOA9QPH_b3QDA!7e81!7m{patype}!2b1!12b1!32b1!10m1!2i2&hl=en&gl=US&authuser=0"
    hrs = hsession.get(lnk, timeout=htimeout)
    hrs.raise_for_status()

    dta = json.loads(hrs.content.decode("utf-8").replace(")]}'\n",""))
    return parseAssist(dta)

def loadAssist(file: str):
    dta = json.loads(open(file, "r", encoding="utf-8").read().replace(")]}'\n",""))
    return parseAssist(dta)
    
if __name__ == "__main__":
    print(getAssist(41.55, -90.493611, 3500)) # 1
    print(getAssist(0, 0, 3500)) # 2
    print(loadAssist("nicephore.json")) # 3