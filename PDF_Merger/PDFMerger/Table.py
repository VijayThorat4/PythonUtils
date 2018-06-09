
import wx

data = [( 1, 'Jessica Alba Pomona'*2, '1981'),
        ( 2, 'Sigourney Weaver New York'*2, '1949'),
        ( 3, 'Angelina Jolie los angeles'*2, '1975'),
        ( 4, 'Natalie Portman Jerusalem'*3, '1981'),
        ( 5, 'Rachel Weiss London'*2, '1971'), 
        ( 6, 'Scarlett Johansson New York'*3, '1984' ),
        ( 7, 'Sagar Pohekar'*8, '1991'),
        ( 8, 'Dango Pohekar'*8, '1991'),
        ( 9, 'Mango Pohekar'*8, '1991'),
        (10, 'Chango Pohekar'*8, '1991')]


class Table(wx.Frame):

    def __init__(self, parent, position, *args, **kw):
        wx.Frame.__init__(self,parent, pos=position)

        self.panel = wx.Panel(parent, wx.ID_ANY, pos=position,size=wx.Size(420,5500))
        self.index = 0
 
        self.list = wx.ListCtrl(self.panel, size=(-1,100), 
                                     style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        self.list.InsertColumn(0, 'Sr. No', width=140)
        self.list.InsertColumn(1, 'File', width=130)
        self.list.InsertColumn(2, 'Size', wx.LIST_FORMAT_RIGHT, 90)
 
        idx = 0
        for i in data:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1
            
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.list, 0, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.sizer)

"""
import wx
import wx.lib.mixins.listctrl

data = [('Jessica Alba', 'Pomona', '1981'), ('Sigourney Weaver', 'New York', '1949'),
  ('Angelina Jolie', 'Los Angeles', '1975'), ('Natalie Portman', 'Jerusalem', '1981'),
  ('Rachel Weiss', 'London', '1971'), ('Scarlett Johansson', 'New York', '1984')]


class AutoWidthListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):

    def __init__(self, parent, *args, **kw):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)


class Table:

    def __init__(self, panel, *args, **kw):
        self.InitUI(panel)

    def InitUI(self,panel):        

        #hbox = wx.BoxSizer(wx.HORIZONTAL)

        #panel = wx.Panel(self)

        self.list = AutoWidthListCtrl(panel)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        idx = 0

        for i in data:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1

        #hbox.Add(self.list, 1, wx.EXPAND)
        #self.SetSizer(hbox)
"""        
class Table2(wx.ListCtrl):
    
    def __init__(self, parent, position):
        self.item_list = ["A", "B", "C"]
        self.panel = wx.Panel(parent, wx.ID_ANY, pos=position,size=wx.Size(420,150),
                              style=wx.SIMPLE_BORDER)
        wx.ListCtrl.__init__(self, self.panel, -1, pos=wx.DefaultPosition, size=(420,150),
                style=wx.LC_REPORT)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._Ping)
        self.InsertColumn(0, 'No', width=40)
        self.InsertColumn(1, 'File', width=320)
        self.InsertColumn(2, 'Size', wx.LIST_FORMAT_RIGHT, 40)
 
        idx = 0
        for i in data:
            index = self.InsertItem(idx, str(i[0]))
            self.SetItem(index, 1, i[1])
            self.SetItem(index, 2, i[2])
            idx += 1
    def OnGetItemText(self, item, col):
        if col==0:
            return self.item_list[item]
    def OnGetItemImage(self, item):
        return -1
    def OnGetItemAttr(self, item):
        return None
        
    def _Ping(self, evt):
        x =  int(evt.GetItem().GetText())
        print("ping", self.GetItemText(x,1))

