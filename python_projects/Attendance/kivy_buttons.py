from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class MainApp(App):
    def build(self):
        screen = Screen()
        layout = GridLayout(cols=2, spacing=10)

        # Example buttons with different shapes
        shapes_buttons = [
            Button(text="Flat Button"),

        ]

        # Example buttons with different colors
        colors = [
            (1, 0, 0, 1),   # Red
            (0, 1, 0, 1),   # Green
            (0, 0, 1, 1),   # Blue
            (1, 1, 0, 1),   # Yellow
            (1, 0, 1, 1),   # Magenta
            (0, 1, 1, 1),   # Cyan
            (0.5, 0.5, 0.5, 1),  # Gray
            (0, 0, 0, 1),   # Black
            (0.8, 0.2, 0.5, 1)  # Custom color
        ]
        color_buttons = [
            Button(text="Button", background_color=color) for color in colors
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