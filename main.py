from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("frontend.kv")
FILE_PATH = "/Users/micha/Downloads/files-master/files-master/App-4-Webcam-Photo-Sharer/files/image.jpg"


class FirstScreen(Screen):

    def search_image(self):
        # get user query from TextInput
        user_query = self.manager.current_screen.ids.user_query.text

        # fetch url of the query
        img_url = f'https://source.unsplash.com/random/?{user_query}'

        # update the image with the image from the url
        self.manager.current_screen.ids.img.source = img_url


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):

        return RootWidget()


MainApp().run()
