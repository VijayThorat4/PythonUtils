import wx

from Controls import Controls
from Frame import Frame
from Table import Table2 as Table
from Menu import Menu1


class App(wx.App):
    """Application Class"""
    def OnInit(self):
        """OnInit: Gets auto called on object construction"""

        self.frame = Frame()
        self.controls = Controls()

        self._x = 20
        self._y = 60
        self._panelSize = wx.Size(430,120)
        self._startPosition = wx.Point(20,20)

        self._controls = wx.Panel(self.frame, id=wx.ID_ANY,
                                  pos=wx.Point(0,0),
                                  size=(-1,-1),
                                  style=wx.SIMPLE_BORDER, name=wx.PanelNameStr)
        self.createMenuBar(self.frame)
        self.createTable(self._controls,wx.Point(20,120))

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def createMenuBar(self,parent):
        self.MyMenu = Menu1(parent, 'File', 'New', 'Save', 'Save As', 'Clear')

    def createMenuBar(self,parent):
        self.MyMenu = Menu1(parent, 'Setting', 'Change WorDir', 'Change Background')


    def OnQuit(self, event):
        self.frame.Close()

    def createTable(self,parent, position):
        self._table = Table(parent,position)

new1 = App()
