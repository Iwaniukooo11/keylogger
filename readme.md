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
cd ../keylogger && python main.py
```
