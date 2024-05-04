from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.utils import asynckivy

class MainApp(MDApp):
    def build(self):
        self.screen = Screen() 

        self.button = MDRectangleFlatButton(
            text="Show Table",
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            on_release=self.show_table
        )
        self.screen.add_widget(self.button)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        return self.screen

    def show_table(self, instance):
        table = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            check=True,
            column_data=[
                ("First Name", 100),
                ("Last Name", 100),
                ("Email Address", 200),
                ("Phone Number", 150)
            ],
            row_data=[
                ("John", "Doe", "john@example.com", "123-456-7890"),
                ("Jane", "Smith", "jane@example.com", "987-654-3210")
            ]
        )
        self.screen.clear_widgets()  # Clear existing widgets
        self.screen.add_widget(table)

MainApp().run()
