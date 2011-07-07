# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul  7 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import options

import gettext
_ = gettext.gettext

###########################################################################
## Class pymnui
###########################################################################

class pymnui ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _("Pymn"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txt_topic = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.txt_topic, 1, wx.ALL, 5 )
		
		self.btn_alert = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_alert, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.txt_window = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_CHARWRAP|wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer1.Add( self.txt_window, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.txt_chatbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer1.Add( self.txt_chatbox, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_alert.Bind( wx.EVT_BUTTON, self.findAlerts )
		self.txt_window.Bind( wx.EVT_TEXT, self.checkHighlight )
		self.txt_chatbox.Bind( wx.EVT_TEXT_ENTER, self.sendText )
		self.Show()

	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def findAlerts( self, event ):
		pass
	
	def checkHighlight( self, event ):
		pass
	
	def sendText( self, event ):
		output = "<%s> %s\n" % (options.nick, self.txt_chatbox.GetValue())
		self.txt_window.AppendText(output)
		self.txt_chatbox.Clear()
