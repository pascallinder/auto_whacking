# Auto Whacking
Auto whacking tool for Farmer Against Potatoes Idle. It offers an auto calibration, so no setup needed. It adapts to your monitor accordingly.
There several auto whackers like:
- [FAPI-whack-a-potatoe](https://github.com/Nick-Gabe/FAPI-whack-a-potatoe)
- [Whack-A-Potato AutoHotKey Script](https://github.com/Nick-Gabe/FAPI-whack-a-potatoe)
- [Whack-A-Potato Python Script (No-Setup)](https://steamcommunity.com/sharedfiles/filedetails/?id=3007440876)

While most of them work, they are either rather slow or do only work for one resolution. Additionally most of them lack the support of features that would make the experience much more enjoyable.

Credits go to [Triplesito](https://steamcommunity.com/id/TripleCreeper3) who created [Whack-A-Potato Python Script (No-Setup)](https://steamcommunity.com/sharedfiles/filedetails/?id=3007440876) which this project is based of.
## Setup
Install Python 3 from [here](https://www.python.org/downloads/)

During the installation process make sure to select "Add python 3.x to PATH", when finished restart the computer and verify the installation by opening the "cmd" (by typing it in the windows search bar), typing "python" in the command line and pressing enter, if you can see three ">>>", the installation has been successful.

Next you can execute the setup.sh by clicking on it.

Finally go to the settings of Farmer Against Potatoes Idle and deactivate Fullscreen.

That's it. You are good to go.

## Features
- Auto calibration for most monitors: If the monitor / the window gets really small, this code struggles since there are rounding errors. (It's recommended to run it in windowed fullscreen mode)
- Auto whacking 380 - 430 clicks per game. It also makes use of the combo savers. When a combo saver is available it will click on the bad potato intentionally to skip the waiting time.
- Pausable idle and play once functionality via hotkey (play once - F9 and idle - F10)
- Calibration can be shown to the user via hotkey (F8)
- Termination of the programm in case something goes wrong is also available via hotkey (F7)
- It recognises whether the whack page is open or not and will only start click when that is the case


## Limitations
- For multi monitor setup: The tool only works on the main monitor (so far) - work in progress
- Only works in windows so far. If someone is interested in coding the lines for ios or linux, feel free to do so. The code is already prepared to integrate this easily.
- The window has to run in the foreground, otherwise the triggers will not work
- During the auto whacking, the mouse / cursor is occupied and can not be used - work in progress

## Ideas + Upcoming Features
- Virtual clicks (no mouse movement) - so the user will be able to use the mouse for something else
- Multi monitor support
- Statistics as logs that show distribution of potatoes and the amount of clicks
- GUI with buttons and showing log entries
- Auto upgrading whack upgrates

## FAQ
- 

Please submit unanswered questions, issues or bugs here on github.