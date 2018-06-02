"""
Main module
"""
import tkinter as tk
from tkinter import Label
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

class PDFMerger:
    def __init__(self,win):
        """ Constructor """
        self.win = win
        #   -   Title : PDFMerger
        win.title("PDFMerger")

        #   -   Add Controls
        #   -   MenuBar
        self.createMenuBar()

        #   -   Controls Frame
        self.createControls()

        #   -   Files Lister
        #self.createFilesLister()

    def createMenuBar(self):
        self.menuBar = Menu(self.win)
        self.win.config(menu = self.menuBar)

        #   -   Configure contents in File Menu
        self.fileMenu = Menu(self.menuBar)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit",command=self._quit)

        #   -   File Menu
        self.menuBar.add_cascade(label="File",menu=self.fileMenu)

        #   -   Configure contents in Help Menu
        self.helpMenu = Menu(self.menuBar,tearoff=0)
        self.helpMenu.add_command(label="About")

        #   -   Help Menu
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)

    def _quit(self):
        self.win.quit()
        self.win.destroy()

    def createControls(self):
        """ Controls """
        #   -   Controls Frame : ctrFrame
        self.ctrFrame = ttk.LabelFrame(self.win, text=" Controls :")
        self.ctrFrame.grid(column=0, row=0, padx=20, pady=10)

        self._padx = 5
        self._pady = 5
        #   -   Btn : Add
        self.addButton = ttk.Button(self.ctrFrame,text="Add",command = self._add)
        self.addButton.grid(column=0,row=0,sticky='W', padx = self._padx, pady = self._pady)

    	#   -   Btn : Up
        self.upButton = ttk.Button(self.ctrFrame,text="Up",command = self._up)
        self.upButton.grid(column=1,row=0,sticky='W', padx = self._padx, pady = self._pady)

    	#   -   Btn : Down
        self.downButton = ttk.Button(self.ctrFrame,text="Down",command = self._down)
        self.downButton.grid(column=2,row=0,sticky='W', padx = self._padx, pady = self._pady)

    	#   -   Btn : Remove
        self.removeButton = ttk.Button(self.ctrFrame,text="Remove",command = self._remove)
        self.removeButton.grid(column=3,row=0,sticky='W', padx = self._padx, pady = self._pady)

    def _add(self):
        print("add")

    def _up(self):
        print("up")

    def _down(self):
        print("down")

    def _remove(self):
        print("remove")


def main():
    win = tk.Tk()
    PDFMerger(win)
    win.mainloop()

if __name__ == "__main__":
    main()
