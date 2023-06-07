import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.base import EventLoop
from kivy.core.window import Keyboard
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem




class Tab1Content(BoxLayout):
    def __init__(self, **kwargs):
        super(Tab1Content, self).__init__(**kwargs)
        self.orientation = 'vertical'

        top_layout = GridLayout(cols=2, size_hint=(1, 0.6))

        top_layout.add_widget(Label(text="Waga detalu (kg)"))
        self.p_wag = TextInput(multiline=False)
        top_layout.add_widget(self.p_wag)

        top_layout.add_widget(Label(text="Maszyna"))
        self.maszyna_spinner = Spinner(text="Maszyna1", values=["Maszyna1", "Maszyna2", "Maszyna3"])
        top_layout.add_widget(self.maszyna_spinner)

        top_layout.add_widget(Label(text="Tworzywo (zł/kg)"))
        self.p_two = TextInput(multiline=False)
        top_layout.add_widget(self.p_two)

        top_layout.add_widget(Label(text="Czas cyklu (s)"))
        self.p_cyk = TextInput(multiline=False)
        top_layout.add_widget(self.p_cyk)

        top_layout.add_widget(Label(text="Liczba operatorów (szt.)"))
        self.p_ope = TextInput(multiline=False)
        top_layout.add_widget(self.p_ope)

        bottom_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        calculate_button = Button(text="Oblicz!", on_press=self.calculate_sum, size_hint=(0.5, 0.8))
        bottom_buttons_layout.add_widget(calculate_button)

        clear_button = Button(text="Wyczyść!", on_press=self.clear, size_hint=(1, 0.8))
        bottom_buttons_layout.add_widget(clear_button)

        save_button = Button(text="Zapisz!", on_press=self.save, size_hint=(1, 0.8))
        bottom_buttons_layout.add_widget(save_button)

    def clear(self, *args):
        self.p_wag.text = ""
        self.p_two.text = ""
        self.p_cyk.text = ""
        self.p_ope.text = ""
        # Wyczyszczenie pola sum_textinput
        self.ids.sum_textinput.text = ''
        # Wyczyszczenie wartości spinnera
        self.ids.maszyna_spinner_id.text = ''

    def calculate_sum(self, *args):
        try:
            waga = float(self.p_wag.text)
            maszyna = self.maszyna_spinner.text
            tworzywo = float(self.p_two.text)
            cykl = float(self.p_cyk.text)
            operator = float(self.p_ope.text)

            if maszyna == "Maszyna1":
                koszt_maszyny = 100
            elif maszyna == "Maszyna2":
                koszt_maszyny = 200
            elif maszyna == "Maszyna3":
                koszt_maszyny = 300
            else:
                koszt_maszyny = 0

            suma = round((waga * tworzywo) + (3600 / cykl) / koszt_maszyny * operator, 4)
            self.ids.sum_textinput.text = f"Koszt produkcji: {suma}"
        except ValueError:
            print("Błąd: Wprowadź poprawne wartości liczbowe")

    def save(self, *args):
        waga = self.p_wag.text
        maszyna = self.maszyna_spinner.text
        tworzywo = self.p_two.text
        cykl = self.p_cyk.text
        operator = self.p_ope.text

        print(f'Waga: {waga}, Maszyna: {maszyna}, Tworzywo: {tworzywo}, Cykl: {cykl}, Operator: {operator}')


class MyLayout(TabbedPanel):
    pass


class My7App(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    My7App().run()
