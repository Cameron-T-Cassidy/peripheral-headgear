# Bluetooth Communication between Raspberry Pis

Run listen.py before running send.py.
Otherwise, send.py will crash if run first because it needs to connect to the host in listen.py, which becomes a known host once listen.py is running.

hostMACAddress and serverMACAddress need to be the same MAC Address.
Replace the shown MAC addresses with the MAC address of the raspberry pi that will act as your server

```
python3 listen.py
```

```
python3 send.py
```