Brightness media buttons work only on with laptops and don't work on desktop PCs. There is some official explanation but it sounds pathetic and isn't worth including here.

My initial attempt was to use AutoHotKey to tie buttons to brightness change. However, brightness buttons are special for some reason in that they work on some deeper level than AHK or something. 

Despite buttons being disfunctional Windows shows brightness slider changing when brightness buttons are pressed. It means that it retains the current brightness somewhere. My search has shown that brightness is stored in Windows registry entries for current power plan.

This program runs in a loop and listens to the change of this specific registry entry. When it changes, program sends a brightness change signal to the monitor. When the computer turns on it will set the brightness depending on time of day - 0 in the evening  and 100 in the morning.


