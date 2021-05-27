from font import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
import Weather, Covid_Stats
import News,time
import numpy as np
from datetime import datetime
from PyQt5.QtGui import QBrush, QColor, QPalette
from PyQt5.QtWidgets import QApplication, qApp
from qroundprogressbar import QRoundProgressBar
import csv
from PyQt5 import QtCore, QtGui, QtWidgets, QtChart
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtCore import QPointF, QDate, QDateTime, QTime
from PyQt5.QtGui import QPainter, QPen, QFont, QBrush, QColor
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 1000)
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        #MainWindow.resize(1000, 800)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    color : rgb(85, 87, 83);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"background-color: rgb(46, 52, 54);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.centralwidget)


        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 30, 2000, 800))
        self.stackedWidget.setObjectName("stackedWidget")


        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.FaceWidget = QtWidgets.QWidget(self.page_1)
        self.FaceWidget.setGeometry(QtCore.QRect(210, -10, 1600, 400))
        self.FaceWidget.setObjectName("FaceWidget")

        self.Newslabel = QtWidgets.QLabel(self.page_1)
        self.Newslabel.setGeometry(QtCore.QRect(10, 10, 1690, 700))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Newslabel.setFont(font)
        self.Newslabel.setStyleSheet("QLabel{\n"
                                     "    color: rgb(243, 243, 243);\n"
                                     "}")
        self.Newslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Newslabel.setWordWrap(False)
        self.Newslabel.setObjectName("Newslabel")

        #######################################--------------page 2--------------------------#####################################################

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        self.PandemLoadingPage = QtWidgets.QFrame(self.page_2)
        self.PandemLoadingPage.setGeometry(-20,-20,1800,1500)
        self.PandemLoadingPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
      #  self.PandemLoadingPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PandemLoadingPage.setObjectName("PandemLoadingPage")
        self.CovidHeading = QtWidgets.QLabel(self.PandemLoadingPage)
        self.CovidHeading.setGeometry(QtCore.QRect(70, 70, 678, 150))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(48)
        self.CovidHeading.setFont(font)
        self.CovidHeading.setStyleSheet("QLabel{\n"
                                        "color:rgb(255, 255, 255);\n"
                                        "}")
        #self.CovidHeading.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.CovidHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.CovidHeading.setObjectName("CovidHeading")

        self.chartWidget = QtWidgets.QWidget(self.PandemLoadingPage)
        self.chartWidget.setGeometry(QtCore.QRect(900, 100, 801, 671))
        self.chartWidget.setStyleSheet("")
        self.chartWidget.setObjectName("chartWidget")

        self.widget = QtWidgets.QWidget(self.PandemLoadingPage)
        self.widget.setGeometry(QtCore.QRect(150, 460, 581, 118))
        self.widget.setObjectName("widget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        #self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        #self.verticalLayout_4.setSpacing(50)
      #  self.horizontalLayout_2.setSpacing(40)


        self.ActiveCases = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)

        self.ActiveCases.setFont(font)
        self.ActiveCases.setStyleSheet("color:rgb(255, 255, 255)")
        self.ActiveCases.setAlignment(QtCore.Qt.AlignCenter)
        self.ActiveCases.setObjectName("ActiveCases")
        self.verticalLayout_4.addWidget(self.ActiveCases)

        self.activeNum = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(40)

        self.activeNum.setFont(font)
        self.activeNum.setStyleSheet("color: rgb(255, 255, 0);")
        self.activeNum.setAlignment(QtCore.Qt.AlignCenter)
        self.activeNum.setObjectName("activeNum")
        self.verticalLayout_4.addWidget(self.activeNum)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.RecoveredCases = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.RecoveredCases.setFont(font)
        self.RecoveredCases.setStyleSheet("color: rgb(255, 255, 255);")
        self.RecoveredCases.setAlignment(QtCore.Qt.AlignCenter)
        self.RecoveredCases.setObjectName("RecoveredCases")
        self.verticalLayout_5.addWidget(self.RecoveredCases)

        self.recoveredNum = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(40)
        self.recoveredNum.setFont(font)
        self.recoveredNum.setStyleSheet("color:rgb(0, 255, 0)")
        self.recoveredNum.setAlignment(QtCore.Qt.AlignCenter)
        self.recoveredNum.setObjectName("recoveredNum")
        self.verticalLayout_5.addWidget(self.recoveredNum)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.widget1 = QtWidgets.QWidget(self.PandemLoadingPage)
        self.widget1.setGeometry(QtCore.QRect(118, 230, 581, 118))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ConfirmedCases = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.ConfirmedCases.setFont(font)
        self.ConfirmedCases.setStyleSheet("color: rgb(255, 255, 255);")
        self.ConfirmedCases.setAlignment(QtCore.Qt.AlignCenter)
        self.ConfirmedCases.setWordWrap(True)
        self.ConfirmedCases.setObjectName("ConfirmedCases")
        self.verticalLayout_2.addWidget(self.ConfirmedCases)



        self.confirmedcasesNum = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(40)
        self.confirmedcasesNum.setFont(font)
        self.confirmedcasesNum.setStyleSheet("color:rgb(85, 255, 255)")
        self.confirmedcasesNum.setAlignment(QtCore.Qt.AlignCenter)
        self.confirmedcasesNum.setObjectName("confirmedcasesNum")
        self.verticalLayout_2.addWidget(self.confirmedcasesNum)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.DeathCases = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.DeathCases.setFont(font)
        self.DeathCases.setStyleSheet("color: rgb(255, 255, 255);")
        self.DeathCases.setAlignment(QtCore.Qt.AlignCenter)
        self.DeathCases.setObjectName("DeathCases")
        self.verticalLayout_3.addWidget(self.DeathCases)
        self.deathNum = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(40)
        self.deathNum.setFont(font)
        self.deathNum.setStyleSheet("color: rgb(255, 0, 0);")
        self.deathNum.setAlignment(QtCore.Qt.AlignCenter)
        self.deathNum.setObjectName("deathNum")
        self.verticalLayout_3.addWidget(self.deathNum)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        series = QLineSeries()
        with open("pakistan.csv", 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                dates = int(row['serial'])
                confirmed = int(row['confirmed'])
                series.append(dates, confirmed)

        chart = QChart()
        chart.addSeries(series)
        #chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setBackgroundBrush(QBrush(QColor("transparent")))
        pen = QPen(QColor(95, 255, 255))
        pen.setWidth(5)
        series.setPen(pen)

       # chart.setTitle("Pakistan", color = "white", size = "30pt" )
        chart.legend().setVisible(False)
        axisY = QtChart.QValueAxis()
        axisX = QtChart.QValueAxis()
        axisBrush = QBrush(QColor('#ffffff'))
        axisX.setLabelsBrush(axisBrush)
        axisY.setLabelsBrush(axisBrush)
        Lfont = QFont("Sans Serif")
        Lfont.setPixelSize(16)
        axisX.setLabelsFont(Lfont)
        axisY.setLabelsFont(Lfont)

        chart.legend().setAlignment(Qt.AlignBottom)

        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        font = QFont('Open Sans')
        font.setPixelSize(40)
        font.setBold(True)
        chart.setTitleFont(font)
        chart.setTitleBrush(QBrush(Qt.white))
        chart.setTitle('Pakistan')

        plotAreaGraident = QtGui.QLinearGradient()
        plotAreaGraident.setStart(QtCore.QPoint(0, 1))
        plotAreaGraident.setFinalStop(QtCore.QPoint(1, 0))
        plotAreaGraident.setColorAt(0.0, QColor(200,20,200))
        plotAreaGraident.setColorAt(1.0, QColor(20, 0, 20))
        plotAreaGraident.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        chart.setPlotAreaBackgroundBrush(plotAreaGraident)
        chart.setPlotAreaBackgroundVisible(True)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)


        self.chartWidget.setContentsMargins(0, 0, 0, 0)
        lay = QtWidgets.QHBoxLayout(self.chartWidget)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(chartview)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)


  #      self.progress = QRoundProgressBar(self.horizontalLayout_2)
   #     self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
    #    self.progress.setGeometry(QtCore.QRect(1000, 150, 801, 671))

        # style accordingly via palette
     #   palette = QPalette()
      #  brush = QBrush(QColor(0, 0, 255))
       # brush.setStyle(Qt.SolidPattern)
        #palette.setBrush(QPalette.Active, QPalette.Highlight, brush)

        #self.progress.setPalette(palette)
       # progress.show()
        #self.progress.setValue(20)

##################################------------------------page 1 --------------------------------############################33
        self.Weather = QtWidgets.QLabel(self.page_1)
        self.Weather.setAlignment(QtCore.Qt.AlignCenter)
        self.Weather.setWordWrap(False)
        self.Weather.setObjectName("Weather")
        self.Weather.setStyleSheet("color: white")
        self.Weather.setGeometry(QtCore.QRect(410, 50,1168,50))
        self.Weather.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(50)
        #font.setItalic(True)

        self.statusWeather = QtWidgets.QLabel(self.page_1)
        self.statusWeather.setAlignment(QtCore.Qt.AlignCenter)
        self.statusWeather.setWordWrap(False)
        self.statusWeather.setObjectName("WindSpeed")
        self.statusWeather.setStyleSheet("color: white")
        self.statusWeather.setGeometry(QtCore.QRect(410, 100, 1150, 50))
        self.statusWeather.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        font.setItalic(True)

        self.locationIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap7 = QtGui.QPixmap("location.png")
        self.pixmap7.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.locationIcon.setGeometry(QtCore.QRect(791, 180, 1100, 70))
        self.locationIcon.setPixmap(self.pixmap7)

        self.RainIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap5 = QtGui.QPixmap("rain.png")
        self.pixmap5.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.RainIcon.setGeometry(QtCore.QRect(1205, 130, 120, 130))
        self.RainIcon.setPixmap(self.pixmap5)

        self.Rain = QtWidgets.QLabel(self.page_1)
        self.Rain.setAlignment(QtCore.Qt.AlignCenter)
        self.Rain.setWordWrap(False)
        self.Rain.setObjectName("Rain")
        self.Rain.setStyleSheet("color: white")
        self.Rain.setGeometry(QtCore.QRect(1165, 100, 150, 65))
        self.Rain.setFont(font)

        self.SunsetIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap6 = QtGui.QPixmap("sunset.png")
        self.pixmap6.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.SunsetIcon.setGeometry(QtCore.QRect(1335, 130, 120, 130))
        self.SunsetIcon.setPixmap(self.pixmap6)

        self.Sunset = QtWidgets.QLabel(self.page_1)
        self.Sunset.setAlignment(QtCore.Qt.AlignCenter)
        self.Sunset.setWordWrap(False)
        self.Sunset.setObjectName("Sunset")
        self.Sunset.setStyleSheet("color: white")
        self.Sunset.setGeometry(QtCore.QRect(1290, 100, 150, 65))
        self.Sunset.setFont(font)


        self.Fog = QtWidgets.QLabel(self.page_1)
        self.Fog.setAlignment(QtCore.Qt.AlignCenter)
        self.Fog.setWordWrap(False)
        self.Fog.setObjectName("Fog")
        self.Fog.setStyleSheet("color: white")
        self.Fog.setGeometry(QtCore.QRect(320, 900, 1150, 50))
        self.Fog.setFont(font)

        self.HumidityIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap4 = QtGui.QPixmap("humidity.png")
        self.pixmap4.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.HumidityIcon.setGeometry(QtCore.QRect(1082, 130, 120, 130))
        self.HumidityIcon.setPixmap(self.pixmap4)

        self.Humidity = QtWidgets.QLabel(self.page_1)
        self.Humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.Humidity.setWordWrap(False)
        self.Humidity.setObjectName("Humidity")
        self.Humidity.setStyleSheet("color: white")
        self.Humidity.setGeometry(QtCore.QRect(1040, 100, 150, 65))
        self.Humidity.setFont(font)


        self.weather = QtWidgets.QLabel(self.page_1)
        self.movie = QtGui.QMovie("weather1.gif")
        self.weather.setGeometry(QtCore.QRect(680, -20, 400, 390))
        self.weather.setMinimumSize(QtCore.QSize(230,220))
        self.weather.setMaximumSize(QtCore.QSize(230,220))
        self.movie.setScaledSize(QtCore.QSize().scaled(230,220,QtCore.Qt.KeepAspectRatio))
        self.weather.setMovie(self.movie)
        self.movie.start()

        self.WindIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap2 = QtGui.QPixmap("wind.png")
        self.pixmap2.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.WindIcon.setGeometry(QtCore.QRect(435, 130, 120, 130))
        self.WindIcon.setPixmap(self.pixmap2)


        self.WindSpeed = QtWidgets.QLabel(self.page_1)
        self.WindSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.WindSpeed.setWordWrap(False)
        self.WindSpeed.setObjectName("WindSpeed")
        self.WindSpeed.setStyleSheet("color: white")
        self.WindSpeed.setGeometry(QtCore.QRect(395, 100, 140, 65))
        self.WindSpeed.setFont(font)


        self.PressureIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap3 = QtGui.QPixmap("pressure.png")
        self.pixmap3.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.PressureIcon.setGeometry(QtCore.QRect(576, 130, 120, 130))
        self.PressureIcon.setPixmap(self.pixmap3)

        self.Pressure = QtWidgets.QLabel(self.page_1)
        self.Pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure.setWordWrap(False)
        self.Pressure.setObjectName("Pressure")
        self.Pressure.setStyleSheet("color: white")
        self.Pressure.setGeometry(QtCore.QRect(540, 100, 150, 65))
        self.Pressure.setFont(font)


        self.SunriseIcon = QtWidgets.QLabel(self.page_1)
        self.pixmap1 = QtGui.QPixmap("sunrise.png")
        self.pixmap1.scaled(32, 32, QtCore.Qt.KeepAspectRatio,
                            QtCore.Qt.SmoothTransformation)

        self.SunriseIcon.setGeometry(QtCore.QRect(275, 130, 120, 123))
        self.SunriseIcon.setPixmap(self.pixmap1)

        self.Sunrise = QtWidgets.QLabel(self.page_1)
        self.Sunrise.setAlignment(QtCore.Qt.AlignCenter)
        self.Sunrise.setWordWrap(False)
        self.Sunrise.setObjectName("Sunrise")
        self.Sunrise.setStyleSheet("color: white")
        self.Sunrise.setGeometry(QtCore.QRect(225, 100, 170, 65))
        self.Sunrise.setFont(font)

        self.location = QtWidgets.QLabel(self.page_1)
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setWordWrap(False)
        self.location.setObjectName("WindSpeed")
        self.location.setStyleSheet("color: white")
        self.location.setGeometry(QtCore.QRect(815, 190, 150, 50))
        self.location.setFont(font)

        self.stackedWidget.addWidget(self.page_1)

        self.stackedWidget.addWidget(self.page_2)

########################################################################3 page 3 ##############################################################################
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalSlider = QtWidgets.QSlider(self.page_3)
        self.verticalSlider.setGeometry(QtCore.QRect(20, 150, 16, 181))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.child = QtWidgets.QLabel(self.page_3)
        self.child.setText("check")
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        self.anim = QtCore.QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QtCore.QPoint(400, 400))


        #if self.stackedWidget.currentIndex() == 2:
        self.anim.setDuration(3300)
        self.anim.start()

        self.NewsFrame1 = QtWidgets.QFrame(self.page_3)
        self.NewsFrame1.setGeometry(100,100,100,100)
        self.NewsFrame1.setFrameShape(QtWidgets.QFrame.Box)


        self.stackedWidget.addWidget(self.page_3)



        #########################-------------------page 4------------------------####################################33

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalSlider = QtWidgets.QSlider(self.page_4)
        self.verticalSlider.setGeometry(QtCore.QRect(20, 150, 16, 181))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

        self.TodaysWeather = QtWidgets.QLabel(self.page_4)
        self.TodaysWeather.setGeometry(QtCore.QRect(300, 50, 300, 150))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.TodaysWeather.setFont(font)
        self.TodaysWeather.setStyleSheet("QLabel{\n"
                                     "    color: rgb(243, 243, 243); background-color:rgb(221,85,81); border-radius:15px;\n"
                                     "}")
        #self.TodaysWeather.setStyleSheet("background-color:red;border-radius:15px;")
        #self.TodaysWeather.resize(100, 100)
        #self.TodaysWeather.setAutoFillBackground
        self.TodaysWeather.setAlignment(QtCore.Qt.AlignCenter)
        self.TodaysWeather.setWordWrap(False)
        self.TodaysWeather.setObjectName("TodaysWeather")

        self.stackedWidget.addWidget(self.page_4)

#################################3-------------------------default pages ----------#################################33

        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(65, 10, 193, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet("QLabel{\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setWordWrap(False)
        self.Time.setObjectName("Time")

        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(1530, 10, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setStyleSheet("QLabel{\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.Date.setAlignment(QtCore.Qt.AlignCenter)
        self.Date.setWordWrap(False)
        self.Date.setObjectName("Date")

        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setObjectName("Next")
        self.next_button.resize(self.next_button.minimumSizeHint())
        self.next_button.setShortcut("a")
        self.next_button.setFlat(True)
        self.next_button.setStyleSheet("color : rgba(0, 0, 0, 0)")
        self.next_button.clicked.connect(self.next_page)


        self.prev_button = QtWidgets.QPushButton(self.centralwidget)
        self.prev_button.setObjectName("Previous")
        self.prev_button.resize(self.prev_button.minimumSizeHint())
        self.prev_button.setShortcut("b")
        self.prev_button.setFlat(True)
        self.prev_button.setStyleSheet("color : rgba(0, 0, 0, 0)")
        self.prev_button.clicked.connect(self.prev_page)

        self.Authentication = QtWidgets.QLabel(self.centralwidget)
        self.Authentication.setGeometry(QtCore.QRect(830, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Authentication.setFont(font)
        self.Authentication.setStyleSheet("QLabel{\n"
"    color: rgb(243, 243, 243);\n"
"}")
        self.Authentication.setAlignment(QtCore.Qt.AlignCenter)
        self.Authentication.setWordWrap(False)
        self.Authentication.setObjectName("Authentication")



        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def next_page(self):
        new_index = self.stackedWidget.currentIndex()+1
       # if self.stackedWidget.currentIndex() == 2:
        #        self.anim.start()
        if new_index < len(self.stackedWidget):
            self.stackedWidget.setCurrentIndex(new_index)

    def prev_page(self):
        new_index = self.stackedWidget.currentIndex()-1
        if new_index >= 0:
            self.stackedWidget.setCurrentIndex(new_index)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Time.setText(_translate("MainWindow", " "))
        self.Date.setText(_translate("MainWindow", " "))
        self.Authentication.setText(_translate("MainWindow", "Hello Nawal"))


        self.CovidHeading.setText(_translate("MainWindow", "COVID-19 Dashboard"))
#        self.countryName.setText(_translate("MainWindow", str(pakistan_cases['country'])))
        self.ActiveCases.setText(_translate("MainWindow", "ACTIVE"))
        #self.activeNum.setText(_translate("MainWindow", str(pakistan_cases['active'])))
        self.RecoveredCases.setText(_translate("MainWindow", "RECOVERED"))
        #self.recoveredNum.setText(_translate("SMainWindow", str(pakistan_cases['recovered'])))
        self.ConfirmedCases.setText(_translate("MainWindow", "CONFIRMED CASES"))
        #self.confirmedcasesNum.setText(_translate("MainWindow", str(pakistan_cases['confirmed'])))
        self.DeathCases.setText(_translate("MainWindow", "DEATHS"))
        #self.deathNum.setText(_translate("MainWindow", str(pakistan_cases['deaths'])))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #def __init__(self, parent=None):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        #self.articles = News.
        #self.updateNews(self,self.articles)


        timerTime = QtCore.QTimer(self)
        timerTime.timeout.connect(self.updateDate)
        timerTime.start(1000)

        self.pyowm = Weather.PyownThread(self)
        self.pyowm.tempSignal.connect(self.updateTemp)
        self.pyowm.statusSignal.connect(self.updateStatus)
        self.pyowm.PressureSignal.connect(self.updatePressure)
        self.pyowm.SunriseSignal.connect(self.updateSunrise)
        self.pyowm.SunsetSignal.connect(self.updateSunset)
        self.pyowm.wind_speedSignal.connect(self.updateWind_speed)
        self.pyowm.HumidSignal.connect(self.updateHumidity)
        self.pyowm.rainSignal.connect(self.updateRain)
        self.pyowm.locationSignal.connect(self.updateLocation)
        self.pyowm.start()

        self.Covid = Covid_Stats.CovidThread(self)
        self.Covid.CovidSignal.connect(self.updateCovidChart)
        self.Covid.start()


        self.News = News.NewsApiThread(self)
        self.News.NewsSignal.connect(self.updateNews)
        self.News.start()

    def updateCovidChart(self,Stats):
            self.activeNum.setText(str(Stats['active']))
            self.recoveredNum.setText(str(Stats['recovered']))
            self.confirmedcasesNum.setText(str(Stats['confirmed']))
            self.deathNum.setText(str(Stats['deaths']))


    def updateDate(self):
        date = QtCore.QDateTime.currentDateTime()
        self.Date.setText(date.toString("ddd MMMM d yyyy"))
        self.Time.setText(date.toString("hh:mm:ss ap"))

    def updateLocation(self, location):
        self.location.setText(str(location['city'] + ", " + location['country_code']))

    def updateTemp(self, temp):
        self.Weather.setText(str(temp['temp']) + " \u00B0C ")

    def updateHumidity(self,humidity):
        self.Humidity.setText(str(humidity) + "%" )

    def updateRain(self,rain):
       # self.Rain.setText(str(rain['3h']) + "%" )
        self.Rain.setText(str(rain) + " cm")



    def updateSunrise(self, sunrise):
        check = (datetime.fromtimestamp(sunrise).strftime('%I:%M %p'))
        self.Sunrise.setText(str(check))

    def updateSunset(self, sunset):
        check = (datetime.fromtimestamp(sunset).strftime('%I:%M %p'))
        self.Sunset.setText(str(check))

    def updatePressure(self, pressure):
        self.Pressure.setText(str(pressure['press']) + " hPa")

    def updateStatus(self, status):
       # self.WindSpeed.setText("Currently: " + str(wind['speed']))
       self.statusWeather.setText(str(status))

    def updateWind_speed(self, wind):
        self.WindSpeed.setText(str(wind['speed']) + " m/s")
       #self.statusWeather.setText(str(status))

    def updateNews(self, articles):
        self.article = articles
        self.last_element = self.article[-1]
        self.articles_iterator = iter(articles)
        self.timer = QtCore.QTimer(timeout=self.on_timeout, interval=5000)

        self.timer.start()
        self.on_timeout()

    def unfade(self):
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(1)
        self.Newslabel.setGraphicsEffect(self.opacity_effect)
        self.timer1 = QtCore.QTimer(timeout = self.fade,interval=4000)
        self.timer1.start()


    def fade(self):
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        self.Newslabel.setGraphicsEffect(self.opacity_effect)
        self.timer2 = QtCore.QTimer(timeout=self.unfade, interval=1000)
        self.timer2.start()

    @QtCore.pyqtSlot()
    def on_timeout(self):
        try:
            value = next(self.articles_iterator)
            self.Newslabel.setText(value)
            self.fade()


        except StopIteration:
            self.articles_iterator = iter(self.article)
            self.on_timeout()
         #   self.timer.stop()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()


    sys.exit(app.exec_())