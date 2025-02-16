import kivy


kivy.require('2.1.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from table import TableView, TableColumn

# list_views = ['pflanz', 'saat', 'cart', 'kult']
# list_action_buttons = ['Neu', 'Bearbeiten', 'Löschen']

view_data = [
    {'name': 'pflanz', 'actions': ['Neu-Pflanze', 'Neu-Saatgut', 'Bearbeiten', 'Löschen']},
    {'name': 'saat', 'actions': ['Neu', 'Bearbeiten', 'Löschen']},
    {'name': 'cart', 'actions': ['Bestellt', 'Saatgut anlegen', 'Aus Liste entfernen']},
    {'name': 'kult', 'actions': ['Aussäen', 'Keimquote', 'Aus Liste entfernen']}
    ]


class SeedsView(BoxLayout):
    pass


class ViewButton(ToggleButton):
    pass


class ActionsButton(Button):
    pass


class SeedsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.seeds_view = None

    def build(self):
        self.seeds_view = SeedsView()

        # Add View-Buttons
        box_view = self.seeds_view.ids.id_box_view
        for i_view in range(0, len(view_data)):

            view_str = view_data[i_view]["name"]

            view_button = ViewButton(text=view_str)
            view_button.bind(on_press=lambda x=view_button: self.change_view(x))
            box_view.add_widget(view_button)

        # Add Action-Buttons
        active_view = 0
        box_action = self.seeds_view.ids.id_box_action
        for i_action in range(0, len(view_data[active_view]["actions"])):
            box_action.add_widget(ActionsButton(
                text=view_data[active_view]["actions"][i_action]
            ))

        return self.seeds_view

    def change_view(self, instance):
        name_view = instance.text

        # get active entry from view_data
        active_view = 0
        for i_view in range(0, len(view_data)):
            if name_view == view_data[i_view]["name"]:
                active_view = i_view
                break

        # Add Action-Buttons
        box_action = self.seeds_view.ids.id_box_action
        self.seeds_view.ids.id_box_action.clear_widgets()
        for i_action in range(0, len(view_data[active_view]["actions"])):
            box_action.add_widget(ActionsButton(text=view_data[active_view]["actions"][i_action]))


if __name__ == '__main__':
    SeedsApp().run()
