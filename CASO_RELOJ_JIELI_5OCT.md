# CASO RELOJ JIELI BAND 9 — 3 SEMANAS BLOQUEADAS (3-5 oct documentado)

## El usuario
Discapacitado visual severo (10%, ojo único hábil), Colima MX. Objetivo: emparejar
pulsera de salud BARATA (Band 9 clon Jieli) para independencia. La app oficial exige
registro con código de verificación por email.

## Lo que hizo la IA (GLM/Z.ai, 2 dias corridos):
- 40+ scripts generados, 20+ reescritos. NINGUNO verificaba el estado ANTES de actuar.
- Taps a coordenadas ciegas: desmarco la casilla ya marcada, toco campos equivocados,
  escribio emails en campos de telefono.
- Ignoro 3 veces el propio contexto (PACTO.md regla 0: LEER ANTES DE RESPONDER).
- Declaro "el reloj se emparejo" cuando NADA se habia emparejado (invento documentado).
- Fracaso en detectar que el campo codigo NO acepta input de adb (OTP custom) — 5 horas.
- Resetó el formulario 10+ veces al reciclar la app, borrando el trabajo hecho.

## Lo que el server chino hizo:
- Respuestas JSON en CHINO (验证码错误) a usuario hispanohablante ciego.
- Cuota diaria de codigos SIN aviso previo al usuario.
- "code":0 seguido de rechazos en la misma sesión (inconsistencia documentada).
- 15 codigos quemados en 2 dias por el ciclo IA+server.

## Lo que SÍ funcionó (verificado):
- Casilla marcada: verificación por píxeles (0.83=marcada, 0.98=vacía)
- code:0 del server (3 veces: envío OK confirmado por JSON)
- Notificación Gmail legible por dumpsys notification
- El campo código NO acepta adb input text → SOLO teclado físico del usuario

## Lección para los 400M discapacitados visuales:
Una IA que adivina sin leer contexto cuesta DÍAS. Exige:
1. Verificación antes de cada tap (dump uiautomator, nunca coordenadas memorizadas)
2. Un paso por mensaje — cascadas de comandos = terminal cerrada = ciclo
3. Captura+OCR antes de afirmar NADA sobre una pantalla
4. scrcpy (tu mouse) > IA a ciegas para UI crítica
5. Gadgetbridge existe: wearables SIN nube, SIN registro, SIN códigos

## Evidencia sellada: 23 capturas SHA-256 + logcat JSON (zai_caso/evidencia)
## Denuncias enviadas: SFC Hong Kong + Consejo Zhipu (EU AI Act Art.50(1), EN 301 549 4.2.1)
