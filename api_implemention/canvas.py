from interfaces.private.canvas import CanvasPrivateInterface
from api_implemention.event_handler import EventManager
import time

class Canvas(CanvasPrivateInterface):

    def __init__(self, size):
        self._size = size
        self._drawables = []
        self._event_manager = None # The concrete canvas will deal with this TODO make a nice import system
        self.backend_initialize()

    def add_drawable(self, drawable):
        self._drawables.append(drawable)

    def display(self, fps):
        self.setup()
        for drawable in self._drawables:
            drawable.backend_tick()
        time_between_frames = 1/fps
        while 1:
            start = time.time()
            self.update_frame()
            self.blit_canvas()
            for drawable in self._drawables:
                drawable.backend_tick()
            self.backend_tick()
            elapsed_time = time.time() - start
            self.sleep(max(time_between_frames - elapsed_time, 0))

    def add_drawable_event_handler(self,drawable, event_type, function):
        if function is None:
            self._event_manager.remove_drawable_event_handler(drawable, event_type)
        else:
            self._event_manager.add_drawable_event_handler(drawable, event_type, function)




