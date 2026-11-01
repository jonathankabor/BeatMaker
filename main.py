from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from sound_kit_service import SoundKitService
from track import TrackWidget







Builder.load_file('track.kv')




class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()
    
    def on_parent(self, widget, parent):
        for i in range(0, self.sound_kit_service.get_nb_tracks()):
            self.tracks_layout.add_widget(TrackWidget())

class BeatMakerApp(App):
    pass


BeatMakerApp().run()