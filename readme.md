# Simple python keylogger

A script, which traces keyboard and saves received data in .txt file and posts it into a server.

Used technologies:

- pynput
- express

At first run a server:

```
cd ./server && node server.js
```

And then run a keylogger

```
cd ./keylogger && python main.py
```
![Stolen conversation from messanger](https://user-images.githubusercontent.com/45974414/191115725-8d4afccc-6175-4f57-94ba-22a2fc098262.gif)
