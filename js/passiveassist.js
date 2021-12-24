var PASSIVEASSIST_CURLOC = 7
var PASSIVEASSIST_CURLOC_PLACENAME = 1
var PASSIVEASSIST_CURLOC_WEATHER = 5
var PASSIVEASSIST_CURLOC_WEATHER_ICON = 0
var PASSIVEASSIST_CURLOC_WEATHER_TEMPRATURE = PASSIVEASSIST_CURLOC_PLACENAME
var PASSIVEASSIST_CURLOC_WEATHER_STATUS = 3

function parseAssist(assist) {
    asPlaceName = assist[PASSIVEASSIST_CURLOC][PASSIVEASSIST_CURLOC_PLACENAME]
    asWeather = assist[PASSIVEASSIST_CURLOC][PASSIVEASSIST_CURLOC_WEATHER]
    wout = null
    if (asWeather != null) {
        if (asWeather.length > 1) {
            asWeatherIcon = asWeather[PASSIVEASSIST_CURLOC_WEATHER_ICON]
        } else {
            asWeatherIcon = null
        }
        if (asWeather.length > 2) {
            asWeatherTemp = asWeather[PASSIVEASSIST_CURLOC_WEATHER_TEMPRATURE]
        } else {
            asWeatherTemp = null
        }
        if (asWeather.length > 3) { 
            asWeatherStat = asWeather[PASSIVEASSIST_CURLOC_WEATHER_STATUS]
        } else {
            asWeatherStat = null
        }
        wout = {"weatherIcon":asWeatherIcon,"currentTemprature":asWeatherTemp,"status":asWeatherStat}
    }
    return {"placeName": asPlaceName, "weather":wout}
}

function getAssistStr(loc, dist, patype=3, cors=false) {
    locarr = loc.split(",")
    return getAssist(parseFloat(locarr[0]), parseFloat(locarr[1]), dist, patype, cors)
}

function getAssistAsync(lat, lng, dist, patype=3, cors=false, callback) {
    var xhr = new XMLHttpRequest()
    lnk = "https://www.google.com/maps/preview/passiveassist?pb=!1m10!2m9!1m3!1d"+dist.toString()+"!2d"+lng+"!3d"+lat+"!2m0!3m2!1i1034!2i620!4f14!3m2!1sZBuUX_qxIsOA9QPH_b3QDA!7e81!7m"+patype+"!2b1!12b1!32b1!10m1!2i2!99s"+Math.floor(Math.random()*100000000)+"&hl=en&gl=US&authuser=0"
    if (!cors) {
        lnk = "https://api.allorigins.win/raw?url=" + encodeURIComponent(lnk)
    }
    xhr.open("GET", lnk)
    xhr.onreadystatechange = function() {
        if (this.readyState == 4) {
            callback(parseAssist(JSON.parse(xhr.responseText.replace(")]}'", ""))))
        }
    }
    xhr.send()
}

function getAssist(lat, lng, dist, patype=3, cors=false) {
    xhr = new XMLHttpRequest()
    lnk = "https://www.google.com/maps/preview/passiveassist?pb=!1m10!2m9!1m3!1d"+dist.toString()+"!2d"+lng+"!3d"+lat+"!2m0!3m2!1i1034!2i620!4f14!3m2!1sZBuUX_qxIsOA9QPH_b3QDA!7e81!7m"+patype+"!2b1!12b1!32b1!10m1!2i2!99s"+Math.floor(Math.random()*100000000)+"&hl=en&gl=US&authuser=0"
    if (!cors) {
        lnk = "https://api.allorigins.win/raw?url=" + encodeURIComponent(lnk)
    }
    xhr.open("GET", lnk, false)
    xhr.send()

    return parseAssist(JSON.parse(xhr.responseText.replace(")]}'", "")))
}