AlarmBot for Termux(command line interface)

A simple voice-enabled alarm clock system built with Python, designed for use on Android (via Termux).

It allows you to:
 -Set multiple alarms with labels
 -Use voice (TTS) to read your alarm when it triggers
 -Save all alarms in a JSON file
 -Repeatedly trigger alarms until stopped manually
 -Run offline and store user preferences


Features
-ersistent alarm storage (alarms.json)
-Add, remove, and view alarms easily
-Real-time alarm trigger using system time
-Voice output (via termux-tts-speak)
-Audio playback (alarm.mp3)
-Volume control before playing alarm
-Friendly text interface
-Input validation and error handling

Requirements
-Python 3
-Termux on Android
-termux-api package installed:
     pkg install termux-api
-Place an alarm.mp3 file in the same folder as the script or you can add yours
and put it in the script.

🛠️ Setup
1. Clone or copy the Python script to your Termux environment.
2. Make sure alarm.mp3 is in the same folder.
3. Run the script:
python alarmbot.py

Usage
🏁 First Run:
You'll be asked to enter your name (only letters, 3–8 characters).
This name is saved in alarms.json.
Menu Options:
1 : add alarm
2 : remove alarm
3 : view alarm
4 : watch_alarm
5 : exit

📌 Notes
Only works in Termux with termux-tts-speak and termux-media-player.
Make sure the script is run from the directory containing alarm.mp3.
Works best when Termux runs in foreground while watching alarms.

Author
          Akerele Abdul Sobur
                Python | Automation | Termux
                   Built to stay organized and on time


