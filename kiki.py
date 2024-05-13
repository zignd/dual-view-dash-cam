from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2

class KivyCamera(Image):
    def __init__(self, capture, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / 30)  # update at 30Hz

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert it to texture
            buf = cv2.flip(frame, 0).tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture

class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("Cannot open camera")
            exit()
        return KivyCamera(self.capture)

    def on_stop(self):
        # When everything done, release the capture
        self.capture.release()

if __name__ == '__main__':
    CamApp().run()
