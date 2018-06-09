import wx

class Frame(wx.Frame):
    """Frame class that displays an image. """
    _x = 520
    _y = 480

    def __init__(self, parent=None, Id=-1, pos=wx.DefaultPosition,
                 title="PDF Merger"):
        """Create a Frame instance and display image."""
        wx.Frame.__init__(self, parent, Id, title, pos, size=(Frame._x,
                                                              Frame._y))