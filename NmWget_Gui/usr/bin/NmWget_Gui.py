#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# (C)Copyright 2020 Neeraj P.Praveen
# All rights reserved.
# Version 1.1.0

import wx
import wx.py
import os,sys
from subprocess import PIPE, Popen
import gettext
wget_path="/usr/bin/wget"
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):_
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)

        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(1, _("Exit"), "Exit", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, _("File"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(2, _("About NmWget"), "About NmWget", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, _("About"))
        self.SetMenuBar(self.frame_1_menubar)
        print "MenuBar is created "

        # Menu Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Argument"), style=wx.ST_NO_AUTORESIZE)
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, _("--help"))
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Load"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Termininate"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        str2="NmWget 1.1.0 \n (C)Copyright 2020 Neeraj P.Praveen \n All rights reserved \n Version 1.1.0 \n"
        str1=str2+"******************************************\n"
        self.text_ctrl_1.WriteText(str1)
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.onclick_exit, id=1)
        self.Bind(wx.EVT_MENU, self.onclick_about, id=2)
        self.Bind(wx.EVT_BUTTON, self.On_click_load, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_click_terminate, self.button_2)
        # end NmWget

    def __set_properties(self):
        
        self.SetTitle(_("NmWget"))
        self.frame_1_statusbar.SetStatusWidths([-1])
        
        frame_1_statusbar_fields = [_("NmWget 1.1.0")]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        self.text_ctrl_2.SetMinSize((160, 27))
        self.text_ctrl_2.SetFocus()
        self.button_1.SetToolTipString(_("Run NmWget with Argument"))
        self.button_2.SetToolTipString(_("Stop NmWget"))
        self.text_ctrl_1.SetMinSize((400, 250))
     

    def __do_layout(self):
        # begin NmWget: MyFrame1.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5.Add(self.label_1, 0, wx.EXPAND, 0)
        sizer_5.Add(self.text_ctrl_2, 0, wx.SHAPED, 0)
        sizer_5.Add(self.button_1, 0, 0, 0)
        sizer_5.Add(self.button_2, 0, 0, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_3.Add(self.text_ctrl_1, 0, wx.EXPAND | wx.ALIGN_RIGHT | wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        self.Centre()
        # end NmWget

    def onclick_exit(MenuEvent12, event):
	print "Exiting......"
        exit()
       

       

    def onclick_about(MenuEvent21, event): 
       msgx=wx.MessageBox('(C)Copyright 2020 Neeraj P.Praveen \n All rights resrved. \n Version 1.1.0', 'About',wx.OK)
       print "Message Box showing"
       
    def On_click_load(self, event):  
        self.text_ctrl_1.Clear()
	arguments=self.text_ctrl_2.GetValue()
	try:
         self.text_ctrl_1.WriteText(cmdline(wget_path+" "+arguments))
	except:
	 print "Error : Python.Module.Subprocess.Import_Error"


    def on_click_terminate(self, event): 
	try:
         os.system("pkill -9 wget")
	except:
	 print "Error : Python.Module.Os.System.Process_Kill_Error"


# end of class MyFrame1
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name
    try:
      os.system("clear")
    except:
      print "Error : Python.Module.Os.System.Clear_Error"
    print "Starting GUI "
    print "****************************************************\n"
    print "(C)Copyright 2020 , Neeraj P.Praveen \n All rights reserved. \n Version 1.1.0 \n"
    print "Neerajppraveen2@gmail.com"
    print "****************************************************\n"
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame1(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
