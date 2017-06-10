from abc import abstractmethod
from interfaces.private.canvas_component import CanvasComponent


class CanvasPublicInterface(CanvasComponent):
    """All methods on this interface are to be implemented in thi API implementation"""
    @abstractmethod
    def __init__(self, size):
        """
        :param dimensions: tuple of ints (x,y)
        """

    @abstractmethod
    def add_drawable(self, drawable):
        """Add a new drawable to the  Canvas
        :param drawable: An instance of class drawable
        :return: None
        """

    @abstractmethod
    def setup(self):
        """All user code needed to be run before the animation starts such as initializing variables

        This function should be implemented by the API user
        :return None:
        """

    @abstractmethod
    def update_frame(self):
        """All user code needed to be run to update the animation frame.

        This function should be implemented by the API user
        :return None:
        """

    @abstractmethod
    def display(self, fps):
        """Display the canvas and run the animation. NOTE this is a blocking function

        :param fps: frames per second (integer)
        :return: None
        """

    @abstractmethod
    def sleep(self, time):
        """wait for time specified in seconds."""



