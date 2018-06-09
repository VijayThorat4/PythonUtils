import wx

from PDFMerger.Controls import Controls
from PDFMerger.Frame import Frame
from PDFMerger.Table import Table2 as Table


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
        self.createControls(self._controls)
        self.createTable(self._controls,wx.Point(20,120))

        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def createMenuBar(self,parent):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        parent.SetMenuBar(menubar)
        parent.Bind(wx.EVT_MENU, self.OnQuit, fileItem)
        
    def OnQuit(self, event):
        self.frame.Close()
        
    def createControls(self,parent):
        """add more controls"""

        #   -   Add Button
        self._addBtn = wx.Button(self._controls, id=wx.ID_ANY,
                           label="Add", pos=wx.Point(self._x, self._y + 20),
                           size=wx.DefaultSize, style=0,
                           validator=wx.DefaultValidator,
                           name=wx.ButtonNameStr)
        self._addBtn.Bind(wx.EVT_BUTTON, self.controls._onAdd)
        
        #   -   Up Button
        self._upBtn = wx.Button(self._controls, id=wx.ID_ANY,
                           label="Up", pos=wx.Point(self._x + 100, self._y + 20),
                           size=wx.DefaultSize, style=0,
                           validator=wx.DefaultValidator,
                           name=wx.ButtonNameStr)
        self._upBtn.Bind(wx.EVT_BUTTON, self.controls._onUp)
        
        #   -   Down Button
        self._downBtn = wx.Button(self._controls, id=wx.ID_ANY,
                           label="Down", pos=wx.Point(self._x + 2*100, self._y + 20),
                           size=wx.DefaultSize, style=0,
                           validator=wx.DefaultValidator,
                           name=wx.ButtonNameStr)
        self._downBtn.Bind(wx.EVT_BUTTON, self.controls._onDown)
        
        #   -   Remove Button
        self._removeBtn = wx.Button(self._controls, id=wx.ID_ANY,
                           label="Remove", pos=wx.Point(self._x + 3*100, self._y + 20),
                           size=wx.DefaultSize, style=0,
                           validator=wx.DefaultValidator,
                           name=wx.ButtonNameStr)

        self._removeBtn.Bind(wx.EVT_BUTTON, self.controls._onRemove)
        return self._panelSize
        
    def createTable(self,parent, position):
        self._table = Table(parent,position)
        