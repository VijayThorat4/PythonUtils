import wx

class Menu1(wx.Frame):
    def __init__(self, parent, MenuName, *args):
        super(Menu1).__init__()

        self.menubar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        for arg in args:
            self.fileItem = self.fileMenu.Append(wx.ID_EXIT, arg)

        self.menubar.Append(self.fileMenu, MenuName)
        parent.SetMenuBar(self.menubar)
