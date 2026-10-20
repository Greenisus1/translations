"""catalog - every translatable string of every Pi app, in every language.

This file is the single source of truth. The Translations app turns it into
~/pi-translations/<app>.json packs; apps never translate themselves.

Structure: APPS[app] = {"strings": {KEY: english}, "es": {KEY: ...}, "fr": ..., "de": ...}
Every language table must cover exactly the same keys as "strings".
"""

LANGS = ["en", "es", "fr", "de"]
LANG_NAMES = {"en": "English", "es": "Espanol", "fr": "Francais", "de": "Deutsch"}

APPS = {}

APPS["girderdash"] = {
 "strings": {
  "TITLE": "GIRDERDASH",
  "HUD": "LEVEL {level}  LIVES {lives}  SCORE {score}  BEST {best}",
  "CONTROLS": "arrows/wasd move · space jump · p pause · q quit",
  "OUCH": " OUCH! ",
  "CLEAR": " BEACON LIT! TOWER CLEAR ",
  "CLEAR_SUB": " enter: next tower · q: quit ",
  "OVER": " TOWER WINS ",
  "OVER_SUB": " score {score} · enter: retry · q: quit ",
  "TOO_SMALL": "girderdash needs a terminal at least {w}x{h} (yours is {ww}x{hh}).",
 },
 "es": {
  "TITLE": "GIRDERDASH",
  "HUD": "NIVEL {level}  VIDAS {lives}  PUNTOS {score}  MEJOR {best}",
  "CONTROLS": "flechas/wasd mueve · espacio salta · p pausa · q salir",
  "OUCH": " ¡AY! ",
  "CLEAR": " ¡BALIZA ENCENDIDA! TORRE SUPERADA ",
  "CLEAR_SUB": " enter: siguiente torre · q: salir ",
  "OVER": " LA TORRE GANA ",
  "OVER_SUB": " puntos {score} · enter: otra vez · q: salir ",
  "TOO_SMALL": "girderdash necesita un terminal de al menos {w}x{h} (el tuyo es {ww}x{hh}).",
 },
 "fr": {
  "TITLE": "GIRDERDASH",
  "HUD": "NIVEAU {level}  VIES {lives}  SCORE {score}  RECORD {best}",
  "CONTROLS": "fleches/wasd bouger · espace sauter · p pause · q quitter",
  "OUCH": " AIE ! ",
  "CLEAR": " BALISE ALLUMEE ! TOUR REUSSIE ",
  "CLEAR_SUB": " entree : tour suivante · q : quitter ",
  "OVER": " LA TOUR GAGNE ",
  "OVER_SUB": " score {score} · entree : rejouer · q : quitter ",
  "TOO_SMALL": "girderdash demande un terminal d'au moins {w}x{h} (le tien fait {ww}x{hh}).",
 },
 "de": {
  "TITLE": "GIRDERDASH",
  "HUD": "LEVEL {level}  LEBEN {lives}  PUNKTE {score}  REKORD {best}",
  "CONTROLS": "pfeile/wasd bewegen · leertaste springen · p pause · q ende",
  "OUCH": " AUTSCH! ",
  "CLEAR": " LEUCHTFEUER AN! TURM GESCHAFFT ",
  "CLEAR_SUB": " enter: naechster turm · q: ende ",
  "OVER": " DER TURM GEWINNT ",
  "OVER_SUB": " punkte {score} · enter: nochmal · q: ende ",
  "TOO_SMALL": "girderdash braucht ein Terminal mit mindestens {w}x{h} (deins hat {ww}x{hh}).",
 },
}

APPS["translations"] = {
 "strings": {
  "TITLE": "TRANSLATIONS",
  "PICK_LANG": "Choose a language",
  "APPLY": "enter: apply to all apps · q: quit",
  "APPLIED": "Applied {lang} to {n} apps.",
  "CURRENT": "Current language: {lang}",
  "APPS_HDR": "Apps with language packs:",
  "RESET": "r: reset everything to English",
  "RESET_DONE": "Back to English everywhere.",
 },
 "es": {
  "TITLE": "TRADUCCIONES",
  "PICK_LANG": "Elige un idioma",
  "APPLY": "enter: aplicar a todas las apps · q: salir",
  "APPLIED": "{lang} aplicado a {n} apps.",
  "CURRENT": "Idioma actual: {lang}",
  "APPS_HDR": "Apps con paquetes de idioma:",
  "RESET": "r: volver todo a English",
  "RESET_DONE": "Todo vuelve a English.",
 },
 "fr": {
  "TITLE": "TRADUCTIONS",
  "PICK_LANG": "Choisis une langue",
  "APPLY": "entree : appliquer a toutes les apps · q : quitter",
  "APPLIED": "{lang} applique a {n} apps.",
  "CURRENT": "Langue actuelle : {lang}",
  "APPS_HDR": "Apps avec packs de langue :",
  "RESET": "r : tout remettre en English",
  "RESET_DONE": "Tout est revenu en English.",
 },
 "de": {
  "TITLE": "UEBERSETZUNGEN",
  "PICK_LANG": "Waehle eine Sprache",
  "APPLY": "enter: auf alle apps anwenden · q: ende",
  "APPLIED": "{lang} auf {n} Apps angewendet.",
  "CURRENT": "Aktuelle Sprache: {lang}",
  "APPS_HDR": "Apps mit Sprachpaketen:",
  "RESET": "r: alles auf English zurueck",
  "RESET_DONE": "Alles wieder auf English.",
 },
}

APPS["arcadewisp"] = {
 "strings": {
  "PAUSED": "PAUSED",
  "HELP": "A/D or arrows move | F fire (invaders) | Space pause | R retry | Q menu",
  "MENU1": "1 Paddle duel (classic, gate, sprint; solo/two players)",
  "MENU2": "2 Brick breaker - clear the colored wall",
  "MENU3": "3 Invaders - dodge and shoot the wave",
  "MENU4": "4 Drop - steer through rising platform gaps",
  "MENU_LEVEL": "+/- level for bricks/invaders: {level}",
  "MENU_FREE": "All modes included. No paid unlocks.",
  "MENU_LOCAL": "Local best scores and badges. No Game Center/network.",
  "MENU_QUIT": "Q quits. Minimum terminal 50x25.",
 },
 "es": {
  "PAUSED": "PAUSA",
  "HELP": "A/D o flechas mueven | F dispara (invaders) | Espacio pausa | R otra vez | Q menu",
  "MENU1": "1 Duelo de palas (clasico, puerta, sprint; uno o dos jugadores)",
  "MENU2": "2 Rompebloques - limpia el muro de colores",
  "MENU3": "3 Invaders - esquiva y dispara a la oleada",
  "MENU4": "4 Caida - guiate por los huecos de las plataformas",
  "MENU_LEVEL": "+/- nivel para bricks/invaders: {level}",
  "MENU_FREE": "Todos los modos incluidos. Sin pagos.",
  "MENU_LOCAL": "Mejores marcas y medallas locales. Sin red.",
  "MENU_QUIT": "Q sale. Terminal minimo 50x25.",
 },
 "fr": {
  "PAUSED": "PAUSE",
  "HELP": "A/D ou fleches pour bouger | F tir (invaders) | Espace pause | R rejouer | Q menu",
  "MENU1": "1 Duel de raquettes (classique, porte, sprint; un ou deux joueurs)",
  "MENU2": "2 Casse-briques - detruisez le mur colore",
  "MENU3": "3 Invaders - esquivez et tirez sur la vague",
  "MENU4": "4 Chute - guidez-vous entre les plateformes",
  "MENU_LEVEL": "+/- niveau pour bricks/invaders : {level}",
  "MENU_FREE": "Tous les modes inclus. Rien a payer.",
  "MENU_LOCAL": "Records et badges locaux. Pas de reseau.",
  "MENU_QUIT": "Q quitte. Terminal minimum 50x25.",
 },
 "de": {
  "PAUSED": "PAUSE",
  "HELP": "A/D oder Pfeile bewegen | F feuern (invaders) | Leertaste Pause | R neu | Q Menue",
  "MENU1": "1 Schlaeger-Duell (klassisch, Tor, Sprint; ein oder zwei Spieler)",
  "MENU2": "2 Brick Breaker - raeume die bunte Mauer ab",
  "MENU3": "3 Invaders - weiche aus und schiesse auf die Welle",
  "MENU4": "4 Drop - steuere durch die Luecken der Plattformen",
  "MENU_LEVEL": "+/- Level fuer bricks/invaders: {level}",
  "MENU_FREE": "Alle Modi inklusive. Keine Kaeufe.",
  "MENU_LOCAL": "Lokale Bestwerte und Abzeichen. Kein Netzwerk.",
  "MENU_QUIT": "Q beendet. Terminal mindestens 50x25.",
 },
}

APPS["blockboa"] = {
 "strings": {
  "HELP_GUI": "Arrow keys / WASD: turn | Space: pause | R: restart",
  "LEGEND": "▓▓ Head    ██ Snake    ▒▒ Food    ░░ Wall",
  "WON": "Board cleared! Press R.",
  "OVER": "Game over. Press R.",
  "PAUSED": "Paused",
  "PLAYING": "Playing",
  "IDLE": "Press Start or Space",
  "NEED_TTY": "Terminal mode needs an interactive TTY. Connect with an interactive SSH session; use --gui for desktop mode.",
  "BAD_TERM": "Cannot initialize the terminal. Use a supported TERM and an interactive SSH session.",
 },
 "es": {
  "HELP_GUI": "Flechas / WASD: girar | Espacio: pausa | R: reiniciar",
  "LEGEND": "▓▓ Cabeza    ██ Serpiente    ▒▒ Comida    ░░ Muro",
  "WON": "Tablero completo. Pulsa R.",
  "OVER": "Fin del juego. Pulsa R.",
  "PAUSED": "En pausa",
  "PLAYING": "Jugando",
  "IDLE": "Pulsa Start o Espacio",
  "NEED_TTY": "El modo terminal necesita una TTY interactiva. Conecta con una sesion SSH interactiva; usa --gui para el modo grafico.",
  "BAD_TERM": "No se puede iniciar el terminal. Usa un TERM valido y una sesion SSH interactiva.",
 },
 "fr": {
  "HELP_GUI": "Fleches / WASD : tourner | Espace : pause | R : recommencer",
  "LEGEND": "▓▓ Tete    ██ Serpent    ▒▒ Nourriture    ░░ Mur",
  "WON": "Plateau termine ! Appuie sur R.",
  "OVER": "Partie terminee. Appuie sur R.",
  "PAUSED": "En pause",
  "PLAYING": "En jeu",
  "IDLE": "Appuie sur Start ou Espace",
  "NEED_TTY": "Le mode terminal demande une TTY interactive. Connecte-toi en SSH interactif; utilise --gui pour le mode graphique.",
  "BAD_TERM": "Impossible d'initialiser le terminal. Utilise un TERM valide et une session SSH interactive.",
 },
 "de": {
  "HELP_GUI": "Pfeiltasten / WASD: lenken | Leertaste: Pause | R: Neustart",
  "LEGEND": "▓▓ Kopf    ██ Schlange    ▒▒ Futter    ░░ Mauer",
  "WON": "Feld geschafft! Druecke R.",
  "OVER": "Spiel vorbei. Druecke R.",
  "PAUSED": "Pausiert",
  "PLAYING": "Laeuft",
  "IDLE": "Start oder Leertaste druecken",
  "NEED_TTY": "Der Terminal-Modus braucht eine interaktive TTY. Verbinde dich mit einer interaktiven SSH-Sitzung; nutze --gui fuer den Desktop-Modus.",
  "BAD_TERM": "Terminal kann nicht gestartet werden. Nutze ein gueltiges TERM und eine interaktive SSH-Sitzung.",
 },
}

APPS["flingfort"] = {
 "strings": {
  "INTRO": "Knock out the green targets. Towers collapse when their supports break.",
  "TOO_SMALL": "Flingfort needs a terminal at least 70 columns x 22 rows.",
  "RESIZE": "Resize your terminal, or press q to quit.",
  "HUD": "FLINGFORT  |  LEVEL {n}  |  SHOTS {shots}  |  ",
  "HUD_TAG": "Original terminal physics game",
  "PAUSED": "PAUSED",
  "CONTROLS": "R: restart   N: next cleared fort   P: pause   Q: quit",
 },
 "es": {
  "INTRO": "Derriba los objetivos verdes. Las torres caen cuando se rompen sus soportes.",
  "TOO_SMALL": "Flingfort necesita un terminal de al menos 70 columnas x 22 filas.",
  "RESIZE": "Cambia el tamano del terminal, o pulsa q para salir.",
  "HUD": "FLINGFORT  |  NIVEL {n}  |  TIROS {shots}  |  ",
  "HUD_TAG": "Juego de fisica original para terminal",
  "PAUSED": "PAUSA",
  "CONTROLS": "R: reiniciar   N: siguiente fuerte   P: pausa   Q: salir",
 },
 "fr": {
  "INTRO": "Detruisez les cibles vertes. Les tours s'effondrent quand leurs supports cassent.",
  "TOO_SMALL": "Flingfort demande un terminal d'au moins 70 colonnes x 22 lignes.",
  "RESIZE": "Redimensionnez le terminal, ou tapez q pour quitter.",
  "HUD": "FLINGFORT  |  NIVEAU {n}  |  TIRS {shots}  |  ",
  "HUD_TAG": "Jeu de physique original pour terminal",
  "PAUSED": "PAUSE",
  "CONTROLS": "R : recommencer   N : fort suivant   P : pause   Q : quitter",
 },
 "de": {
  "INTRO": "Triff die gruenen Ziele. Tuerme fallen, wenn ihre Stuetzen brechen.",
  "TOO_SMALL": "Flingfort braucht ein Terminal mit mindestens 70 Spalten x 22 Zeilen.",
  "RESIZE": "Aendere die Terminal-Groesse oder druecke q zum Beenden.",
  "HUD": "FLINGFORT  |  LEVEL {n}  |  SCHUESSE {shots}  |  ",
  "HUD_TAG": "Originales Terminal-Physikspiel",
  "PAUSED": "PAUSE",
  "CONTROLS": "R: Neustart   N: naechste Festung   P: Pause   Q: Ende",
 },
}

APPS["flipspire"] = {
 "strings": {
  "GAME_OVER": "GAME OVER | Score {score}",
  "RESIZE": "Resize to 70x26. Physics paused. Q quits.",
  "HUD": "SCORE {score} | balls used {used}/3",
  "PAUSED": "PAUSED",
  "CONTROLS": "↑ launch | ← left flipper | → right flipper | Space pause | R restart | Q quit",
 },
 "es": {
  "GAME_OVER": "FIN DEL JUEGO | Puntos {score}",
  "RESIZE": "Amplia a 70x26. Fisica en pausa. Q sale.",
  "HUD": "PUNTOS {score} | bolas usadas {used}/3",
  "PAUSED": "PAUSA",
  "CONTROLS": "↑ lanzar | ← flipper izq. | → flipper der. | Espacio pausa | R reiniciar | Q salir",
 },
 "fr": {
  "GAME_OVER": "PARTIE TERMINEE | Score {score}",
  "RESIZE": "Passez a 70x26. Physique en pause. Q quitte.",
  "HUD": "SCORE {score} | balles utilisees {used}/3",
  "PAUSED": "PAUSE",
  "CONTROLS": "↑ lancer | ← flipper gauche | → flipper droit | Espace pause | R rejouer | Q quitter",
 },
 "de": {
  "GAME_OVER": "SPIEL VORBEI | Punkte {score}",
  "RESIZE": "Auf 70x26 vergroessern. Physik pausiert. Q beendet.",
  "HUD": "PUNKTE {score} | Baelle benutzt {used}/3",
  "PAUSED": "PAUSE",
  "CONTROLS": "↑ Start | ← linker Flipper | → rechter Flipper | Leertaste Pause | R Neustart | Q Ende",
 },
}

APPS["snake-arena"] = {
 "strings": {
  "GAME_OVER": "GAME OVER. R restarts",
  "RULES": "Walls wrap. Your own body is safe. Rival bodies still bite - their remains are food.",
  "CONTROLS": "Arrows/WASD turn | Space pause | R restart | Esc/q exit",
 },
 "es": {
  "GAME_OVER": "FIN DEL JUEGO. R reinicia",
  "RULES": "Los muros envuelven. Tu propio cuerpo es seguro. Los cuerpos rivales aun muerden: sus restos son comida.",
  "CONTROLS": "Flechas/WASD giran | Espacio pausa | R reinicia | Esc/q sale",
 },
 "fr": {
  "GAME_OVER": "PARTIE TERMINEE. R recommence",
  "RULES": "Les murs bouclent. Ton propre corps est sans danger. Les corps rivaux mordent encore : leurs restes sont de la nourriture.",
  "CONTROLS": "Fleches/WASD pour tourner | Espace pause | R recommence | Echap/q quitte",
 },
 "de": {
  "GAME_OVER": "SPIEL VORBEI. R startet neu",
  "RULES": "Mauern laufen um. Dein eigener Koerper ist sicher. Rivalen-Koerper beissen noch - ihre Reste sind Futter.",
  "CONTROLS": "Pfeile/WASD lenken | Leertaste Pause | R Neustart | Esc/q Ende",
 },
}

APPS["cranestack"] = {
 "strings": {
  "MISSED": "MISSED! Space to retry",
  "PERFECT_COMBO": "PERFECT x{combo}",
  "PERFECT": "PERFECT!",
  "HUD": "CRANESTACK  SCORE {score}  BEST {best}  L{level}  space drop  [] fov  f fps  p pause  q quit",
 },
 "es": {
  "MISSED": "FALLADO. Espacio para reintentar",
  "PERFECT_COMBO": "PERFECTO x{combo}",
  "PERFECT": "PERFECTO!",
  "HUD": "CRANESTACK  PUNTOS {score}  MEJOR {best}  N{level}  espacio soltar  [] fov  f fps  p pausa  q salir",
 },
 "fr": {
  "MISSED": "RATE ! Espace pour rejouer",
  "PERFECT_COMBO": "PARFAIT x{combo}",
  "PERFECT": "PARFAIT !",
  "HUD": "CRANESTACK  SCORE {score}  RECORD {best}  N{level}  espace lacher  [] fov  f fps  p pause  q quitter",
 },
 "de": {
  "MISSED": "DANEBEN! Leertaste fuer neuen Versuch",
  "PERFECT_COMBO": "PERFEKT x{combo}",
  "PERFECT": "PERFEKT!",
  "HUD": "CRANESTACK  PUNKTE {score}  REKORD {best}  L{level}  leertaste abwerfen  [] fov  f fps  p pause  q ende",
 },
}
