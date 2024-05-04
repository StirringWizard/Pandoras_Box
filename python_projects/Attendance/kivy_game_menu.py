from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class MainMenu(App):
    def build(self):
        # Main menu layout
        main_layout = FloatLayout()

        # Main menu buttons
        btn_new_game = Button(text='New Game', size_hint=(None, None), size=(200, 50), pos_hint={'x': 0, 'top': 1})
        btn_options = Button(text='Options', size_hint=(None, None), size=(200, 50), pos_hint={'x': 0, 'top': 0.9})
        btn_exit = Button(text='Exit', size_hint=(None, None), size=(200, 50), pos_hint={'x': 0, 'top': 0.8})

        # Bind button events
        btn_new_game.bind(on_release=self.start_game)
        btn_options.bind(on_release=self.open_options)
        btn_exit.bind(on_release=self.exit_app)

        # Add buttons to main menu layout
        main_layout.add_widget(btn_new_game)
        main_layout.add_widget(btn_options)
        main_layout.add_widget(btn_exit)

        return main_layout

    def start_game(self, instance):
        print("Starting new game...")

    def open_options(self, instance):
        # Options menu layout
        options_layout = FloatLayout()

        # Options menu buttons
        btn_sound = Button(text='Sound', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        btn_graphics = Button(text='Graphics', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_back = Button(text='Back', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'center_y': 0.4})

        # Bind button events
        btn_sound.bind(on_release=self.set_sound)
        btn_graphics.bind(on_release=self.set_graphics)
        btn_back.bind(on_release=self.back_to_main_menu)

        # Add buttons to options menu layout
        options_layout.add_widget(btn_sound)
        options_layout.add_widget(btn_graphics)
        options_layout.add_widget(btn_back)

        # Replace main menu with options menu
        self.root.clear_widgets()
        self.root.add_widget(options_layout)

    def exit_app(self, instance):
        print("Exiting application...")
        App.get_running_app().stop()

    def set_sound(self, instance):
        print("Setting sound options...")

    def set_graphics(self, instance):
        print("Setting graphics options...")

    def back_to_main_menu(self, instance):
        # Rebuild main menu
        self.root.clear_widgets()
        self.root.add_widget(self.build())


if __name__ == '__main__':
    MainMenu().run()