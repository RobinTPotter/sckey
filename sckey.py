import keyboard
from pythonosc.udp_client import SimpleUDPClient
import time

POLY = 8
nodes = [{"key": None, "node": 1000+_ , "on": False} for _ in range(POLY)]

notes = {
             "s":277 ,    "d":311,              "g":369,  "h":415,  "j":466  ,
	"z": 261, "x": 293, "c": 329, "v": 349,  "b": 392, "n": 440, "m":493, ",": 523,
}

c = SimpleUDPClient("192.168.1.71", 57110)

def on(e):
    global nodes
    global c
    print(e.name)
    if e.name=="esc":
        for n in nodes:
            c.send_message("n_free", [n["node"]])
        return

    check = [n for n in nodes if n["key"]==e.scan_code]
    if check: return
    next = [n for n in nodes if not n["key"]==e.scan_code and n["on"]==False]
    if len(next)>0: next = next[0]
    else: return
    if not e.name in notes: return
    c.send_message("s_new", ["hello_saw", next["node"]])
    c.send_message("n_set", [next["node"], "freq", notes[e.name]])
    c.send_message("n_set", [next["node"], "gate", 1])
    next["on"] = True
    next["key"] = e.scan_code
    print(f"down {next}")

def off(e):
    global nodes
    global c
    #print(f"<<{e.scan_code}>>")
    next = [n for n in nodes if n["on"] and n["key"]==e.scan_code][0]
    print(f"release {next}")
    c.send_message("n_set", [next["node"], "gate", 0])
    c.send_message("n_free", [next["node"]])
    next["on"] = False
    next["key"] = None

keyboard.on_press(on, suppress=True)
keyboard.on_release(off)

while True:
    time.sleep(1)
    print("tick")
