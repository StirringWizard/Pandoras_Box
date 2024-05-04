from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
import csv

class ContactApp(MDApp):
    def build(self):
        self.layout = MDBoxLayout(orientation='vertical', padding=20)
        
        # Input fields
        self.name_input = MDTextField(hint_text='Name', mode="fill")
        self.phone_input = MDTextField(hint_text='Phone', mode="fill")
        self.email_input = MDTextField(hint_text='Email', mode="fill")
        
        # Add input fields to layout
        self.layout.add_widget(MDLabel(text='Name:'))
        self.layout.add_widget(self.name_input)
        self.layout.add_widget(MDLabel(text='Phone:'))
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(MDLabel(text='Email:'))
        self.layout.add_widget(self.email_input)
        
        # Button to save contact
        self.save_button = MDFlatButton(text='Save Contact', size_hint=(1, None), height=48)
        self.save_button.bind(on_release=self.save_contact)
        self.layout.add_widget(self.save_button)
        
        return self.layout
    
    def save_contact(self, instance):
        name = self.name_input.text.strip()
        phone = self.phone_input.text.strip()
        email = self.email_input.text.strip()
        
        # Check if any field is empty
        if not (name and phone and email):
            return
        
        # Write data to CSV file
        with open('contacts.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])
        
        # Clear input fields
        self.name_input.text = ''
        self.phone_input.text = ''
        self.email_input.text = ''
        
        # Notify user that contact has been saved
        self.layout.add_widget(MDLabel(text='Contact saved!'))

if __name__ == '__main__':
    ContactApp().run()
