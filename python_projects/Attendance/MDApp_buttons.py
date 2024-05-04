from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import (
    MDRaisedButton,
    MDFlatButton,
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDIconButton,
    MDRoundFlatButton,
    MDFloatingActionButton,
    MDRoundFlatIconButton
)
from kivy.uix.gridlayout import GridLayout

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        layout = GridLayout(cols=2, spacing=10)

        # Example buttons with different shapes
        shapes_buttons = [
            MDFlatButton(text="Flat Button"),
            MDRaisedButton(text="Raised Button"),
            MDRoundFlatButton(text="Round Flat Button"),
            MDFillRoundFlatButton(text="Fill Round Flat Button"),
            MDFillRoundFlatIconButton(text="Fill Round Flat Icon", icon="android"),
            MDIconButton(icon="android"),
            MDRoundFlatIconButton(text="Round Flat Icon", icon="android"),
            MDFloatingActionButton(icon="plus")
        ]

        # Example buttons with different colors
        colors = [
            (1, 0, 0, 1),  # Red
            (0, 1, 0, 1),  # Green
            (0, 0, 1, 1),  # Blue
            (1, 1, 0, 1),  # Yellow
            (1, 0, 1, 1),  # Magenta
            (0, 1, 1, 1), # Cyan 
            (0.5, 0.5, 0.5, 1), # Gray
            (0, 0, 0, 1), # Black 
            (0.8, 0.2, 0.5, 1) # custome colur

        ]
        color_buttons = [
            MDRaisedButton(text="Button", md_bg_color=color) for color in colors
        ]

        # Adding shape buttons to the layout
        for button in shapes_buttons:
            layout.add_widget(button)

        # Adding color buttons to the layout
        for button in color_buttons:
            layout.add_widget(button)

        screen.add_widget(layout)

        return screen

MainApp().run()


# Icons 
"""
    "android"
    "apple"
    "account"
    "account-box"
    "account-circle"
    "camera"
    "calendar"
    "car"
    "cash"
    "cellphone"
    "chart-bar"
    "chat"
    "check"
    "check-circle"
    "checkbox-marked"
    "checkbox-blank-outline"
    "chevron-left"
    "chevron-right"
    "city"
    "close"

"""