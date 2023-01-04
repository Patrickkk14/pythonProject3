from kivy.app import App
from kivy.lang import Builder
import requests
import json
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeScreen(Screen):

    def press(self):
        result = requests.get("https://smartwatermeter-682d9-default-rtdb.firebaseio.com/"".json")
        data = json.loads(result.content.decode())
        print(data)


    pass

    class HistoryScreen(Screen):


     pass

    def histry(self, root):
        root.current = "history"
        root.transition.direction = "left"

GUI = Builder.load_file("homescreen.kv")

class MainApp(App):
    Window.size = (400, 600)

    def build(self):
        return GUI

    def on_start(self):
        Clock.schedule_interval(self.update_label, 2)

    def update_label(self, *args):
        result = requests.get("https://smartwatermeter-682d9-default-rtdb.firebaseio.com/"".json")
        data = json.loads(result.content.decode())
        Lminutes = self.root.ids['home_screen'].ids['Lminutes']
        Lminutes.text = str(data['Liters per minute']) + "L"
        ml_consumption = self.root.ids['home_screen'].ids['ml_consumption']
        ml_consumption.text = str(data['Total Liquid Released']) + "ML"

        start = 0
        ml = []
        con = []
        ml.append(ml_consumption.text)
        con.append(Lminutes.text)
        counter = 0
        print("Total Liquid Consumption by ML - ", ml[counter])
        print("Liquid Released Liters Per Minute - ", con[counter])
        print(" ")
        ml[counter] = start + 1
        con[counter] = start + 1






if __name__ == "__main__":
    MainApp().run()