# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LEGOKibbleBalanceBasicFrame
###########################################################################

class LEGOKibbleBalanceBasicFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 979,703 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		gbSizer1 = wx.GridBagSizer( 5, 5 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Status", wx.Point( 0,0 ), wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 50, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText4.SetForegroundColour( wx.Colour( 255, 128, 0 ) )
		
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )
		
		self.statusField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statusField.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.statusField.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.statusField.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.statusField.Enable( False )
		
		gbSizer1.Add( self.statusField, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Mass (g)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 50, 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 255, 128, 0 ) )
		
		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.massField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.massField.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		self.massField.Enable( False )
		
		gbSizer1.Add( self.massField, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.zeroButton = wx.Button( self, wx.ID_ANY, u"Zero", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zeroButton.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.zeroButton, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.measureButton = wx.Button( self, wx.ID_ANY, u"Measure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.measureButton.SetFont( wx.Font( 50, 70, 90, 90, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.measureButton, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 0 )
		gbSizer1.AddGrowableRow( 1 )
		gbSizer1.AddGrowableRow( 2 )
		gbSizer1.AddGrowableRow( 3 )
		gbSizer1.AddGrowableRow( 4 )
		gbSizer1.AddGrowableRow( 5 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.zeroButton.Bind( wx.EVT_BUTTON, self.zeroButtonOnButtonClick )
		self.measureButton.Bind( wx.EVT_BUTTON, self.measureButtonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def zeroButtonOnButtonClick( self, event ):
		event.Skip()
	
	def measureButtonOnButtonClick( self, event ):
		event.Skip()
	

