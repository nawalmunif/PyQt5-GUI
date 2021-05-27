from PANDEM import *
import pyowm


class PyownThread(QtCore.QThread):
    tempSignal = QtCore.pyqtSignal(dict)
    statusSignal = QtCore.pyqtSignal(str)
    wind_speedSignal = QtCore.pyqtSignal(dict)
    rainSignal = QtCore.pyqtSignal(int)
    PressureSignal = QtCore.pyqtSignal(dict)
    SunriseSignal = QtCore.pyqtSignal(int)
    SunsetSignal = QtCore.pyqtSignal(int)
    FogSignal = QtCore.pyqtSignal(dict)
    HumidSignal = QtCore.pyqtSignal(int)
    locationSignal = QtCore.pyqtSignal(dict)


    def __init__(self, parent=None):
        super(PyownThread, self).__init__(parent=parent)
        self.owm = pyowm.OWM('1589dbcc0e9608e5b70f0ede23e757c8')



    def run(self):
        while True:
            import requests
            location = requests.get(
                'https://api.ipdata.co?api-key=33196adc6072ff80c82d9b869269e3c1de3cc651a58f630332b33ea3').json()



            observation = self.owm.weather_at_place(location['city'])
            #observation2 = self.owm.
            self.locationSignal.emit(location)

            w = observation.get_weather()
            ctemp = w.get_temperature('celsius')
            self.tempSignal.emit(ctemp)

            status = w.get_status()
            self.statusSignal.emit(status)

            WindSpeed = w.get_wind()
            self.wind_speedSignal.emit(WindSpeed)

           # Rain = w.get_rain()
          #  rain = w.get_precipitation()
            #mgr = self.owm.weather_manager()
            #three_h_forecaster = mgr.forecast_at_place('Karachi,pk', '3h')
            #tomorrow = pyowm.timeutils.timestamps.tomorrow()  # datetime object for tomorrow
            #rain = three_h_forecaster.will_be_rainy_at(tomorrow)
            #self.rainSignal.emit(rain)

            rain_length= len(w.get_rain())
            if rain_length > 0:
                rainfall = w.get_rain()['3h']
            else:
                rainfall = 0
            self.rainSignal.emit(rainfall)


            Pressure = w.get_pressure()
            self.PressureSignal.emit(Pressure)

            Sunrise = w.get_sunrise_time()
            self.SunriseSignal.emit(Sunrise)

            Sunset = w.get_sunset_time()
            self.SunsetSignal.emit(Sunset)

          #  Fog = w.get_fog()
           # self.FogSignal.emit(Fog)

            Humidity = w.get_humidity()
            self.HumidSignal.emit(Humidity)

            QtCore.QThread.sleep(30*60)





