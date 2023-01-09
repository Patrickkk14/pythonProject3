import time

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import requests
import json
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import matplotlib.pyplot as mlt
import numpy as nmpi
import matplotlib.pyplot as plt
import numpy as np
import array as beta
from kivymd.uix.list import MDList,OneLineListItem
from kivymd.uix.screen import Screen
from kivy.uix.label import Label
from  kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput


















class HomeScreen(Screen):

    def press(self):
        result = requests.get("https://smartwatermeter-682d9-default-rtdb.firebaseio.com/"".json")
        data = json.loads(result.content.decode())
        print(data)
    pass



class SettingScreen(Screen):
    t = time.asctime()
    def __init__(self,**kwargs):
        super().__init__(**kwargs)





class HistoryScreen(Screen):
    def __int__(self,**kwargs):
        super(HistoryScreen, self).__int__()
        self.cols= 2
        self.add_widget(Label(text="Name:"))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)


    pass
GUI = Builder.load_file("main.kv")


class WaterMeter(App):


    Window.size = (400, 600)


    def build(self):


        return GUI


    def on_start(self):
            Clock.schedule_interval(self.update_label, 2)

    def update_label(self , *args):

        result = requests.get("https://smartwatermeter-682d9-default-rtdb.firebaseio.com/"".json")
        data = json.loads(result.content.decode())

        Lminutes = self.root.ids['home_screen'].ids['Lminutes']
        Lminutes.text = str(data['Liters per minute']) + "L"
        ml_consumption = self.root.ids['home_screen'].ids['ml_consumption']
        ml_consumption.text = str(data['Total Liquid Released']) + "ML"

        print("--------------------------------")
        t = time.asctime()
        print(t)
        print(ml_consumption.text)
        print(Lminutes.text)





    def view_graph(self):

            fig = plt.figure()
            ax = fig.add_subplot()

            x1 = []
            y1 = []
            x2 = []
            y2 = []

            count = 1
            i = 0

            while count <= 20:
                result = requests.get("https://smartwatermeter-682d9-default-rtdb.firebaseio.com/"".json")
                data = json.loads(result.content.decode())
                print(data)
                Lminutes = self.root.ids['home_screen'].ids['Lminutes']
                Lminutes.text = str(data['Liters per minute']) + " L"
                ml_consumption = self.root.ids['home_screen'].ids['ml_consumption']
                ml_consumption.text = str(data['Total Liquid Released']) + " ML"
                t = time.asctime()
                print("----------------------")

                x1.append(i)
                y1.append(ml_consumption.text)
                x2.append(i)
                y2.append(Lminutes.text)

                i += 1
                plt.title('Water Summary')
                plt.xlabel('Number of Seconds')
                plt.plot(x1, y1, label='line 1')
                plt.plot(x2, y2, label='line 2')
                plt.tight_layout()
                plt.show(block=False)
                plt.pause(1)
                time.sleep(0.1)

                count+=1
            plt.close()

    def change_screen(self, screen_name):
        print(self.root.ids)
        screen_manager = (self.root.ids['screen_manager'])
        screen_manager.current =screen_name
        screen_manager.transition










if __name__ == "__main__":
    WaterMeter().run()