#!/usr/bin/env python3
# VEMOS Fase 1 - Samsung como sensor perimetral. Movimiento -> foto + voz.
import cv2, time, subprocess, os, threading, urllib.request
from pathlib import Path
OUT = Path.home()/"vigila"; OUT.mkdir(exist_ok=True)
W,H = 320,240
def voz(t):
    subprocess.run(["espeak-ng","-v","es-419","-s","110","-p","30","-a","200",t],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
if not cap.isOpened(): voz("camara no disponible"); raise SystemExit(1)
voz("vigilancia activada")
bg=None; cd=0
s=int(os.environ.get("SEG","0")); fin=time.time()+s if s>0 else float("inf")
while time.time()<fin:
    ok,img=cap.read()
    if not ok: time.sleep(1); continue
    g=cv2.cvtColor(cv2.resize(img,(W,H)),cv2.COLOR_BGR2GRAY)
    g=cv2.GaussianBlur(g,(21,21),0)
    if bg is None: bg=g.astype("float"); continue
    cv2.accumulateWeighted(g,bg,0.03)
    diff=cv2.absdiff(g,cv2.convertScaleAbs(bg))
    _,th=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    if cv2.countNonZero(th)>(W*H)*0.08 and time.time()-cd>15:
        cd=time.time()
        f=str(OUT/time.strftime("mov_%Y%m%d_%H%M%S.jpg"))
        cv2.imwrite(f,img); voz("movimiento detectado"); threading.Thread(target=lambda: urllib.request.urlopen(urllib.request.Request("https://ntfy.sh/vemos-casa-7qk2",data=b"movimiento frente a la casa"),timeout=10)).start()
    time.sleep(0.5)
cap.release()
