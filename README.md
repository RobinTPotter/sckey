## Supercollider Keyboard 

using the same keys as the zx spectrum music maker, press up to 8 key combinations to send osc messages to a running supercollider.

use tmux to start jack:

```
jackd -R -d alsa -r 44100 -d hw:0
```

and supercollider:

```
export QT_QPA_PLATFORM=offscreen
sclang
```

and finally the amazing keyboard (needs root):

```
sudo /home/pi/.pyenv/versions/3.8.16/bin/python sckey.py
```



 
