import urllib.request, json, subprocess, time
print("receptor arriba", flush=True)
def voz(t): subprocess.run(["termux-tts-speak",t],timeout=25)
ult=0
while True:
    try:
        r=urllib.request.urlopen("https://ntfy.sh/vemos-casa-7qk2/json?poll=1&since=15m",timeout=15)
        for l in r:
            m=json.loads(l)
            if m.get("event")=="message" and m.get("time",0)>ult:
                ult=m.get("time",0)
                voz("Aviso: "+m.get("message","movimiento")); print("dicho:",m.get("message"),flush=True)
    except Exception as e: print("retry:",e,flush=True)
    time.sleep(15)
