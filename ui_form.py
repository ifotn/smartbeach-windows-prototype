# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
import requests
from matplotlib import image as mpimg
from requests.auth import HTTPBasicAuth
import mplcursors
################################################################################
## Form generated from reading UI file 'AppZRzvsx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

matplotlib.use('Qt5Agg')
from PySide6 import QtWidgets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from datetime import datetime, timedelta

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDoubleSpinBox, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
                               QWidget, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsWidget,
                               QVBoxLayout, QGraphicsProxyWidget)
import resources_rc


class Ui_MainWindow(object):
    def __init__(self):
        self.feature_list = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 720)
        MainWindow.setMaximumSize(QSize(2048, 1400))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
                                 "background-color: rgb(37, 48, 65);\n"
                                 "background-image: url(:/background/BeachBackground.jpg);\n"
                                 "}\n"
                                 "#Left{\n"
                                 "background-color: rgb(37, 48, 65);\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Left = QWidget(self.centralwidget)
        self.Left.setObjectName(u"Left")
        self.Left.setGeometry(QRect(10, 190, 331, 521))
        self.Left.setStyleSheet(u"#Left{\n"
                                "	background-color: qlineargradient(spread:pad, x1:0.605, y1:0.840909, x2:1, y2:1, stop:0 rgba(0, 89, 158, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "	font: 700 italic 9pt \"Segoe UI\";\n"
                                "}")
        self.label = QLabel(self.Left)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 121, 21))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.Left)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 121, 21))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.wind_speed = QDoubleSpinBox(self.Left)
        self.wind_speed.setObjectName(u"wind_speed")
        self.wind_speed.setGeometry(QRect(190, 70, 62, 22))
        self.label_3 = QLabel(self.Left)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 151, 21))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.gst = QDoubleSpinBox(self.Left)
        self.gst.setObjectName(u"gst")
        self.gst.setGeometry(QRect(190, 110, 62, 22))
        self.label_4 = QLabel(self.Left)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 151, 21))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.Left)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setGeometry(QRect(190, 150, 62, 22))
        self.label_5 = QLabel(self.Left)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 190, 151, 21))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.apd = QDoubleSpinBox(self.Left)
        self.apd.setObjectName(u"apd")
        self.apd.setGeometry(QRect(190, 190, 62, 22))
        self.apd.setMaximum(1000000)
        self.label_6 = QLabel(self.Left)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 230, 151, 21))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.mwd = QDoubleSpinBox(self.Left)
        self.mwd.setObjectName(u"mwd")
        self.mwd.setGeometry(QRect(190, 230, 62, 22))
        self.mwd.setMaximum(10000)
        self.label_7 = QLabel(self.Left)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 270, 151, 21))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pressure = QDoubleSpinBox(self.Left)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setGeometry(QRect(190, 270, 62, 22))
        self.pressure.setMaximum(100000)
        self.label_8 = QLabel(self.Left)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 310, 151, 21))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.atmp = QDoubleSpinBox(self.Left)
        self.atmp.setObjectName(u"atmp")
        self.atmp.setGeometry(QRect(190, 310, 62, 22))
        self.atmp.setMinimum(-100)
        self.label_9 = QLabel(self.Left)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 350, 151, 21))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.wtmp = QDoubleSpinBox(self.Left)
        self.wtmp.setObjectName(u"wtmp")
        self.wtmp.setGeometry(QRect(190, 350, 62, 22))
        self.label_10 = QLabel(self.Left)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 390, 151, 21))
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dewp = QDoubleSpinBox(self.Left)
        self.dewp.setObjectName(u"dewp")
        self.dewp.setGeometry(QRect(190, 390, 62, 22))
        self.pushButton = QPushButton(self.Left)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 460, 91, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(55, 202, 255);\n"
                                      "font: 700 9pt \"Segoe UI\";\n"
                                      "color:rgb(255, 255, 255)")

        self.updateButton = QPushButton(self.Left)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(240, 20, 61, 21))
        self.updateButton.setStyleSheet(u"background-color: rgb(55, 202, 255);\n"
                                      "font: 700 9pt \"Segoe UI\";\n"
                                      "color:rgb(255, 255, 255)")

        self.Right = QWidget(self.centralwidget)
        self.Right.setObjectName(u"Right")
        self.Right.setGeometry(QRect(370, 20, 661, 861))
        self.Right.setStyleSheet(u"#Right{\n"
                                 "\n"
                                 "}")
        self.Result = QTextBrowser(self.Right)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(10, 10, 471, 71))

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.predict_value)
        self.updateButton.clicked.connect(self.update_value)
        self.Result.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);font: 700 italic 10pt \"Segoe UI\";")
        self.ImageViewer = QGraphicsView(self.Right)
        self.ImageViewer.setObjectName(u"ImageViewer")
        self.ImageViewer.setGeometry(QRect(10, 90, 471, 181))
        self.ImageViewer.setAutoFillBackground(False)
        self.ImageViewer.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.ImageViewer.setLineWidth(1)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        self.ImageViewer.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.NoBrush)
        self.ImageViewer.setForegroundBrush(brush1)
        self.Warning = QGraphicsView(self.Right)
        self.Warning.setObjectName(u"Warning")
        self.Warning.setGeometry(QRect(510, 150, 111, 100))
        self.Warning.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.DayPrediction = QGraphicsView(self.Right)
        self.DayPrediction.setObjectName(u"DayPrediction")
        self.DayPrediction.setGeometry(QRect(10, 280, 611, 220))
        self.DayPrediction.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.WeeklyPrediction = QGraphicsView(self.Right)
        self.WeeklyPrediction.setObjectName(u"graphicsView")
        self.WeeklyPrediction.setGeometry(QRect(10, 500, 611, 191))
        self.WeeklyPrediction.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_11 = QLabel(self.Right)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 100, 241, 20))
        self.label_11.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_12 = QLabel(self.Right)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(500, -10, 200, 91))
        self.label_12.setStyleSheet(u"font: 700 italic 6pt \"Segoe UI\";")
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"The Beach is Expected to be as follows:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Prediction Model Accuracy: 90 %", None))
        self.Light = QtWidgets.QLabel(self.centralwidget)
        self.Light.setObjectName(u"Light")
        self.Light.setGeometry(QRect(900, 100, 50, 50))
        self.Light.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.dateTimeEdit = QDateTimeEdit(self.Left)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(110, 20, 121, 22))
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        current_datetime = datetime.now()

        # Extract and print the current date
        current_date = current_datetime.date()
        new_datetime = current_datetime + timedelta(days=10)

        self.dateTimeEdit.setMaximumDateTime(new_datetime)
        # self.dateTimeEdit.dateTimeChanged.connect(self.update_value())
        self.feature_list = self.update_value()
        icon = QIcon("Smart-Beach-Logo (1).png")
        MainWindow.setWindowTitle("SmartBeach: Predict Wave Conditions")

        # Set the icon for the application window
        MainWindow.setWindowIcon(icon)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Target Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wind Speed", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Global Surface Temperature", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DPD", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"APD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MWD", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ATMP", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"WTMP", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DEWP", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))

    # retranslateUi

    def get_inputs(self):
        date_time = self.dateTimeEdit.dateTime()
        date = date_time.toString("yyyy-MM-dd hh:mm:ss")
        datetime_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        date_time_x = datetime_obj.timestamp()
        wind_speed = self.wind_speed.value()
        gst = self.gst.value()
        dpd = self.doubleSpinBox_3.value()
        apd = self.apd.value()
        mwd = self.mwd.value()
        pressure = self.pressure.value()
        atmp = self.atmp.value()
        wtmp = self.wtmp.value()
        dewp = self.dewp.value()
        print(wind_speed, gst, dpd, apd, mwd, pressure, atmp, wtmp, dewp, date_time_x)
        return [wind_speed, gst, dpd, apd, mwd, pressure, atmp, wtmp, dewp, date_time_x]

    def predict_value(self):
        # Load the data0
        feature_inputs = self.get_inputs()
        data = pd.read_csv('All_variables_cleaned.csv')
        date_time_list = []

        for date in data['Time']:
            datetime_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            datetime_obj = datetime_obj.strptime(date, "%Y-%m-%d %H:%M:%S")
            date_time_list.append(datetime_obj.timestamp())
        data['Time Float'] = date_time_list
        features = ['WSPD', 'GST', 'DPD', 'APD', 'MWD', 'PRES', 'ATMP', 'WTMP', 'Time Float']
        X = data[features]
        y = data['Wave Category']
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Create a Random Forest classifier
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        # Train the model
        model.fit(X_train, y_train)
        current_time = self.dateTimeEdit.dateTime()
        # Replace date values with timestamps in the original list
        for i in range(len(self.feature_list)):
            self.feature_list[i] = (
                int(datetime.strptime(self.feature_list[i][0], '%Y-%m-%dT%H:%M:%SZ').timestamp()),
                *self.feature_list[i][1:])

        print(self.feature_list)
        day_prediction = []

        for hour in range(24):

            feature_inputs = [self.feature_list[hour][1], self.feature_list[hour][2], self.feature_list[hour][3],
                              self.feature_list[hour][4], self.feature_list[hour][5], self.feature_list[hour][6],
                              self.feature_list[hour][7], self.feature_list[hour][8], self.feature_list[hour][0]]
            new_value_to_predict = np.array(feature_inputs)

            # Create input values for the current hour
            x_value_to_predict = np.array([new_value_to_predict])

            # Make a prediction for the given x value
            y_pred = model.predict(x_value_to_predict)
            day_prediction.append(y_pred[0])

            # Append the predicted value to the list
        timestamps = np.arange(24)  # Assuming 24 hours, replace with your actual timestamps
        weekdays = np.arange(7)
        current_time = self.dateTimeEdit.dateTime()
        weekly_feature_list = self.feature_list
        weekly_predicted_values = []
        week_days = []

        for day in range(6):
            current_time.addDays(day)
            predicted_values = []
            time_list = []
            for hour in range(24):
                current_time = current_time.addSecs(3600)
                current_date = current_time.toString("yyyy-MM-dd hh:mm:ss")
                current_datetime_obj = datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S")
                current_date_time_x = current_datetime_obj.timestamp()

                feature_inputs = [weekly_feature_list[hour][1], weekly_feature_list[hour][2], weekly_feature_list[hour][3],
                                  weekly_feature_list[hour][4], weekly_feature_list[hour][5], weekly_feature_list[hour][6],
                                  weekly_feature_list[hour][7], weekly_feature_list[hour][8], weekly_feature_list[hour][0]]
                new_value_to_predict = np.array(feature_inputs)

                # Create input values for the current hour
                x_value_to_predict = np.array([new_value_to_predict])

                # Make a prediction for the given x value
                y_pred = model.predict(x_value_to_predict)

                # Append the predicted value to the list
                predicted_values.append(y_pred[0])
                time_list.append(current_time.date().toString("dd.MM.yyyy"))
                weekly_feature_list.remove(weekly_feature_list[hour])

            week_days.append(time_list[0])
            weekly_predicted_values.append(predicted_values)

        layout = QVBoxLayout(self.ImageViewer)
        weekly_layout = QVBoxLayout(self.ImageViewer)

        self.graphics_view = QGraphicsView(self.Right)
        layout.addWidget(self.graphics_view)

        # Create a QGraphicsScene to hold the Matplotlib plot
        self.scene = QGraphicsScene(self.Right)
        self.DayPrediction.setScene(self.scene)

        # Create a QGraphicsProxyWidget to embed the Matplotlib canvas in the scene
        self.proxy_widget = QGraphicsProxyWidget()
        self.scene.addItem(self.proxy_widget)

        # Create the Matplotlib figure and axis with a specific size
        figure_size = (7, 2.7)  # Adjust the size as needed
        self.figure, self.ax = plt.subplots(figsize=figure_size, dpi=80)
        # self.figure.set(facecolor='rgba(0, 0, 0, 0)')
        # self.ax.set(facecolor='rgba(0, 0, 0, 0)')

        self.figure.patch.set_facecolor('blue')
        self.figure.patch.set_alpha(0.0)

        self.ax.patch.set_facecolor('none')
        self.ax.patch.set_alpha(0.0)

        # Create a FigureCanvasQTAgg to embed in the QGraphicsProxyWidget
        self.canvas = FigureCanvas(self.figure)
        self.proxy_widget.setWidget(self.canvas)

        # Call a method to update the plot
        self.update_plot(day_prediction, timestamps)

        self.weekly_graphics_view = QGraphicsView(self.Right)
        weekly_layout.addWidget(self.weekly_graphics_view)

        # Create a QGraphicsScene to hold the Matplotlib plot
        self.weekly_scene = QGraphicsScene(self.Right)
        self.WeeklyPrediction.setScene(self.weekly_scene)

        # Create a QGraphicsProxyWidget to embed the Matplotlib canvas in the scene
        self.weekly_proxy_widget = QGraphicsProxyWidget()
        self.weekly_scene.addItem(self.weekly_proxy_widget)

        # Create the Matplotlib figure and axis with a specific size
        weekly_figure_size = (8, 2.7)  # Adjust the size as needed
        self.weekly_figure, self.weekly_ax = plt.subplots(figsize=weekly_figure_size, dpi=70)

        # Create a FigureCanvasQTAgg to embed in the QGraphicsProxyWidget
        self.weekly_canvas = FigureCanvas(self.weekly_figure)
        self.weekly_proxy_widget.setWidget(self.weekly_canvas)
        weekly_plot_data = []

        # Call a method to update the plot
        for week in weekly_predicted_values:
            if week.__contains__("High"):
                weekly_plot_data.append("High")
            elif week.__contains__("Medium"):
                weekly_plot_data.append("Medium")
            else:
                weekly_plot_data.append("Low")
        self.weekly_update_plot(weekly_plot_data, week_days)

        scene = QGraphicsScene()
        warn_scene = QGraphicsScene()
        light_scene = QGraphicsScene()
        if y_pred[0] == 'Low':
            result_msg = "Safe Beach: The waves are expected tobe Low and Safe to Swim"
            image_path = "low_wave.jpg"
            warning_path = "safe to swim.png"
            light_path = "greenlight.gif"
        elif y_pred[0] == 'Medium':
            result_msg = "Moderate Beach: The waves are expected tobe Medium! Be Carefully while swimming"
            image_path = "medium_wave.jpg"
            warning_path = "safe to swim.png"
            light_path = "greenlight.gif"
        else:
            result_msg = "UnSafe Beach: The waves are expected tobe High and Not Safe to Swim"
            image_path = "high_wave.jpg"
            warning_path = "not safe to swim.jpg"
            light_path = "redlight.gif"

        self.Result.setPlainText(result_msg)

        pixmap = QPixmap(image_path)
        desired_size = (450, 150)
        scaled_pixmap = pixmap.scaled(desired_size[0], desired_size[1])

        warn_pixmap = QPixmap(warning_path)
        warn_desired_size = (100, 90)
        warn_scaled_pixmap = warn_pixmap.scaled(warn_desired_size[0], warn_desired_size[1])

        # Create a QGraphicsPixmapItem and set the pixmap
        pixmap_item = scene.addPixmap(scaled_pixmap)
        warn_scene.addPixmap(warn_scaled_pixmap)

        # # Set the scene in the QGraphicsView
        self.ImageViewer.setScene(scene)

        #
        # # Show the QGraphicsView
        self.ImageViewer.show()
        self.Warning.setScene(warn_scene)
        self.Warning.show()

        movie = QMovie(light_path)
        size = QSize(50, 50)
        movie.setScaledSize(size)

        # # Create a QGraphicsPixmapItem to display the GIF
        # gif_item = QGraphicsPixmapItem()
        # light_size = (50,50)
        self.Light.setMovie(movie)

        # Add the GIF item to the scene
        # light_scene.addItem(gif_item)

        # Start the GIF animation
        movie.start()

        # Show the QGraphicsView
        self.Light.show()

    def update_plot(self, predicted_values, timestamps):
        predicted_labels = predicted_values
        timestamps = timestamps

        label_properties = {'Low': {'color': 'green', 'value': 0.5},
                            'Medium': {'color': 'yellow', 'value': 1},
                            'High': {'color': 'red', 'value': 1.5}}

        # Map the predicted labels to colors and numeric values
        colors = [label_properties[label]['color'] for label in predicted_labels]
        values = [label_properties[label]['value'] for label in predicted_labels]

        # Clear the previous plot
        self.ax.clear()

        # Create a scatter plot with colored markers
        scatter = self.ax.scatter(timestamps, values, c=colors, marker='o', s=50, alpha=0.7)

        # Load the image as a background for the entire figure
        fig = plt.gcf()
        background_img = mpimg.imread('ax_background.png')
        fig.figimage(background_img, 0, 0, origin='upper', resize=True, alpha=0.5, zorder=-1)

        # Set labels and title
        self.ax.set_xlabel('Time (hours)', fontsize=8)
        self.ax.set_ylabel('Prediction', fontsize=8)
        self.ax.set_title('Predicted Output Over Time', fontsize=10)
        self.ax.set_xticks(timestamps)
        self.ax.set_xticklabels(timestamps, fontsize=8, rotation=45,
                                ha='right')  # Rotate x-axis labels for better visibility

        # Set custom y-axis ticks and labels
        y_ticks = [label_properties[label]['value'] for label in label_properties]
        y_labels = list(label_properties.keys())
        self.ax.set_yticks(y_ticks)
        self.ax.set_yticklabels(y_labels, fontsize=8)

        # Add cursor hover effects
        cursor = mplcursors.cursor(scatter, hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(f"{predicted_labels[sel.target.index]}"))

        # Draw the plot to the FigureCanvas
        self.canvas.draw()
        self.ax.patch.set_alpha(0)
        plt.show()
        plt.close()

    def weekly_update_plot(self, predicted_values, timestamps):
        # Assuming you have the predicted labels and timestamps
        predicted_labels = predicted_values
        timestamps = timestamps

        label_properties = {'Low': {'color': 'green', 'value': 0.5},
                            'Medium': {'color': 'yellow', 'value': 1},
                            'High': {'color': 'red', 'value': 1.5}}


        # Map the predicted labels to colors and numeric values
        colors = [label_properties[label]['color'] for label in predicted_labels]
        values = [label_properties[label]['value'] for label in predicted_labels]

        # Clear the previous plot
        self.weekly_ax.clear()

        # Create a scatter plot with colored markers
        scatter = self.weekly_ax.scatter(timestamps, values, c=colors, marker='o', s=50, alpha=0.7)

        # Load the image as a background for the entire figure
        fig = plt.gcf()
        background_img = mpimg.imread('ax_background.png')
        fig.figimage(background_img, 0, 0, origin='upper', resize=True, alpha=0.5, zorder=-1)

        # Set labels and title
        self.weekly_ax.set_xlabel('Dates', fontsize=8)
        self.weekly_ax.set_ylabel('Prediction', fontsize=8)
        self.weekly_ax.set_title('Predicted Output Over 7 days', fontsize=10)
        self.weekly_ax.set_xticks(timestamps)
        self.weekly_ax.set_xticklabels(timestamps, fontsize=8, rotation=0,
                                ha='right')  # Rotate x-axis labels for better visibility

        # Set custom y-axis ticks and labels
        y_ticks = [label_properties[label]['value'] for label in label_properties]
        y_labels = list(label_properties.keys())
        self.weekly_ax.set_yticks(y_ticks)
        self.weekly_ax.set_yticklabels(y_labels, fontsize=8)

        # Add cursor hover effects
        cursor = mplcursors.cursor(scatter, hover=True)
        cursor.connect("add", lambda sel: sel.annotation.set_text(f"{predicted_labels[sel.target.index]}"))

        # Draw the plot to the FigureCanvas
        self.weekly_canvas.draw()
        self.weekly_ax.patch.set_alpha(0)
        plt.show()
        plt.close()

    def update_value(self):
        current_time = self.dateTimeEdit.dateTime()
        start_time = current_time.toString("yyyy-MM-ddTHH:mm:ssZ")
        end_time = (current_time.addDays(7)).toString("yyyy-MM-ddTHH:mm:ssZ")
        property_update = ['wind_speed_10m:ms', 'wind_gusts_10m_1h:ms', 'dew_point_2m:C', 'wind_dir_FL10:d',
                           'mean_wave_direction:d', 'msl_pressure:hPa', 't_2m:C', 'windchill:C']

        for feature in property_update:
            url = fr"https://api.meteomatics.com/{start_time}--{end_time}:PT1H/{feature}/44.1776378,-81.6348713/json"

            # Use HTTP Basic Authentication
            # response = requests.get(url, auth=HTTPBasicAuth("georgiancollege_mani_anamika","414KARc3fu"))
            response = requests.get(url, auth=HTTPBasicAuth("gc_fubar_ralph","93QBE5Egva"))
            print(response)

            if response.status_code == 200:
                # The API request was successful
                data = response.json()
                print("Response:", data)
                dates_values = data['data'][0]['coordinates'][0]['dates']
                # Storing dates and values in a single array with two columns
                if feature == 'wind_speed_10m:ms':
                    dates_given = [(entry['date']) for entry in dates_values]
                    wsd_value_pairs = [entry['value'] for entry in dates_values]
                    self.wind_speed.setValue(wsd_value_pairs[0])
                elif feature == 'wind_gusts_10m_1h:ms':
                    gst_value_pairs = [entry['value'] for entry in dates_values]
                    self.gst.setValue(gst_value_pairs[0])
                elif feature == 'dew_point_2m:C':
                    dpd_value_pairs = [entry['value'] for entry in dates_values]
                    self.doubleSpinBox_3.setValue(dpd_value_pairs[0])
                elif feature == 'wind_dir_FL10:d':
                    wd_value_pairs = [entry['value'] for entry in dates_values]
                    self.apd.setValue(wd_value_pairs[0])
                elif feature == 'mean_wave_direction:d':
                    mwd_value_pairs = [entry['value'] for entry in dates_values]
                    self.mwd.setValue(mwd_value_pairs[0])
                elif feature == 'msl_pressure:hPa':
                    pressure_value_pairs = [entry['value'] for entry in dates_values]
                    self.pressure.setValue(pressure_value_pairs[0])
                elif feature == 't_2m:C':
                    temp_value_pairs = [entry['value'] for entry in dates_values]
                    self.atmp.setValue(temp_value_pairs[0])
                elif feature == 'windchill:C':
                    wtmp_value_pairs = [entry['value'] for entry in dates_values]
                    self.wtmp.setValue(wtmp_value_pairs[0])
            else:
                print(f"Error: {response.status_code} - {response.text}")

                # Combine all arrays into one
        combined_array = list(zip(
            dates_given,
            wsd_value_pairs,
            gst_value_pairs,
            dpd_value_pairs,
            wd_value_pairs,
            mwd_value_pairs,
            pressure_value_pairs,
            temp_value_pairs,
            wtmp_value_pairs,
        ))

        self.feature_list = combined_array

        return combined_array


