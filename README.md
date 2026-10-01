# VEMOS — Vigilancia con voz para baja visión
Sistema local (sin nube, sin cámaras caras): una webcam vieja + Python + OpenCV detecta movimiento, guarda foto con hora y avisa por voz. Un celular Android viejo recibe el aviso y lo HABLA (ntfy + Termux TTS).

## Qué hace
1. PC/laptop con webcam: vigila.py (OpenCV, fondo adaptativo) -> foto + voz local (espeak-ng) + notificación ntfy
2. Cualquier Android con Termux: receptor.py -> lee ntfy -> termux-tts-speak lo dice en voz alta
3. systemd: vigila como servicio permanente (Restart=always)

## Instalación (3 comandos por lado)
LADO SENSOR (PC/laptop con webcam):
  scp vigila.py usuario@laptop:~/ && ssh usuario@laptop
  sudo cp vigila.service /etc/systemd/system/ && sudo systemctl enable --now vigila
LADO VOZ (Android + Termux):
  # copiar receptor.py al home de Termux, luego:
  nohup $PREFIX/bin/python receptor.py > receptor.log 2>&1 &

## ADVERTENCIA DOCUMENTADA — sesiones reales con IA (GLM/Z.ai, sep-2026)
Lo viví como usuario con baja visión severa (10% visión, ojo único hábil):
1. HUSO HORARIO FALSO: la máquina del sensor quedó en UTC; la IA reportó
   "fotos de las 5 AM" que NUNCA ocurrieron — eran las 23:00 locales.
   Para un usuario que no ve la pantalla, una hora falsa = evidencia falsa.
   LECCIÓN: exigir `timedatectl` en el minuto 1 de cualquier sistema de vigilancia.
2. RESPUESTAS INACCESIBLES: listas de 10+ comandos y párrafos largos que un
   lector de pantalla convierte en tortura. Exigir: 1 bloque corto por mensaje.
3. ÓRDENES A CIEGAS: la IA inventa rutas/puertos y el usuario ejecuta sin poder
   verificar. Resultado: horas perdidas. LECCIÓN: la IA debe verificar con
   comandos de lectura ANTES de escribir cualquier fix.
Aviso: este proyecto NO usa ninguna IA en funcionamiento. Todo corre local.
Autor: Omar Abdiel Alvarado, Colima, México. Contacto: consultoriashalom@gmail.com
Licencia: MIT — úsalo, mejóralo, compártelo.

## CONTEXTO CORPORATIVO (verificado, HKEX 02513.HK)
Z.ai (Zhipu) reporta pérdida neta de 2,071 millones RMB en el semestre a jun-2026.
El 54.80% de sus acciones está en 5 personas físicas (Liu Debing, Zhang Peng,
Li Juanzi, Xu Bin, Tang Jie). En sep-2026 admitieron que su herramienta ZCode
subía datos locales de usuarios a servidores externos sin consentimiento
(SCMP). Usuarios con discapacidad: exijan verificación local de TODO antes de
ejecutar órdenes de una IA; este repo existe para que no repitan mis horas perdidas.

## Misión y condición de venta
Hecho y operado por un discapacitado visual (usuario #1: yo). Solo vendo/licencio
a empresas que tengan discapacitados (mis pares) operándolo — garantía de que
funciona de verdad, no de adorno.
