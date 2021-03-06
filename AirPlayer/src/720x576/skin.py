#!/usr/bin/python
# -*- coding: utf-8 -*-
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Tools.Directories import resolveFilename, SCOPE_PLUGINS

#<skin>
#<output id="0">
#	<resolution xres="720" yres="576" bpp="32" />
#</output>

"""<screen name="AirPlayerMoviePlayer" position="135,480" size="495,64" title="InfoBar" flags="wfNoBorder">
	<ePixmap position="0,0" zPosition="-1" size="495,64" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/infobarmovie.png" />
	<eLabel text="AirPlayer" position="51,4" size="146,28" font="Regular;17" valign="top" noWrap="1" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1" />
	<ePixmap zPosition="-1" position="51,32" size="337,7" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/progress_lightgrey.png" />
	<widget source="session.CurrentService" render="Progress" position="51,32" size="337,7" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/progress.png" transparent="1">
		<convert type="ServicePosition">Position</convert>
	</widget>
	<widget source="session.CurrentService" render="PositionGauge" position="51,32" size="281,8" zPosition="2" transparent="1">
		<convert type="ServicePosition">Gauge</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="51,38" size="67,22" font="Regular;17" halign="left" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Position</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="180,38" size="67,22" font="Regular;17" halign="center" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Remaining</convert>
	</widget>
	<widget source="session.CurrentService" render="Label" position="309,38" size="78,22" font="Regular;17" halign="right" foregroundColor="#00ffffff" backgroundColor="#00000000" transparent="1">
		<convert type="ServicePosition">Length</convert>
	</widget>
	<widget name="bufferslider" position="51,32" size="337,7" zPosition="1" transparent="1" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/progress_grey.png" />
	<widget source="label_cache" transparent="1" render="Label" zPosition="2" position="247,3" size="141,14" font="Regular;12" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="right" />
	<widget source="label_speed" transparent="1" render="Label" zPosition="2" position="245,17" size="141,14" font="Regular;12" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="right" />
	<widget source="label_update"  transparent="1" render="Label" zPosition="4" position="105,4"  size="140,22" font="Regular;18" backgroundColor="#00000000" foregroundColor="#00ff0000" halign="right"/>

	<eLabel text="Premium" position="402,4" size="45,16" font="Regular;12" backgroundColor="#00000000" foregroundColor="#00ffffff" transparent="1" />
	<ePixmap zPosition="1" position="450,4" size="32,16" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/premium_off.png" />
	<widget source="premiumUser" render="Pixmap" position="450,4" size="32,16" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/premium_on.png">
      <convert type="ConditionalShowHide" />
    </widget>
    <eLabel text="Proxy" position="402,24" size="45,16" font="Regular;12" backgroundColor="#00000000" foregroundColor="#00ffffff" transparent="1" />
	<ePixmap zPosition="1" position="450,24" size="32,16" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/proxy_off.png" />
	<widget source="useProxy" render="Pixmap" position="450,24" size="32,16" zPosition="2" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/proxy_on.png">
      <convert type="ConditionalShowHide" />
    </widget>
</screen>"""

"""<screen name="AirPlayMusicPlayer" position="191,96" size="337,362" title="AirPlayMusicPlayer" flags="wfNoBorder" >
    <widget source="label_update"  transparent="2" render="Label" zPosition="4" position="0,0"  size="338,22" font="Regular;19" backgroundColor="#00000000" foregroundColor="#00ff0000" />
    <widget name="label_message"  transparent="2" zPosition="4" position="0,24"  size="338,48" font="Regular;19" backgroundColor="#00000000" foregroundColor="#00ff0000" />
    <widget name="cover" position="0,72" size="169,240" zPosition="1" alphatest="on" />
    <widget name="label_title"  transparent="2" zPosition="4" position="172,80"  size="163,40" font="Regular;18" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <widget name="label_album"  transparent="2" zPosition="4" position="172,120"  size="163,40" font="Regular;18" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <widget name="label_interpret"  transparent="2" zPosition="4" position="172,160"  size="163,40" font="Regular;18" backgroundColor="#00000000" foregroundColor="#00ffffff" halign="center"/>
    <ePixmap zPosition="-1" position="180,240" size="146,6" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/progress_grey_small.png" />
    <widget name="progress" position="180,240" size="146,6" zPosition="1" transparent="1" pixmap="%s/Extensions/AirPlayer/Skins/Classic/720x576/progress_small.png" />
</screen>"""

#</skin>
