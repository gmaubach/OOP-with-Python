**VHS-K Objektorientierte Programmierung mit Python 2020-08-31-04.09.2020**

* Das ausführen von Programmen (RUN) sollte im folgenden Dialog mit "Execute in a dedicated Console" durchgeführt werden. Manchmal wird das Console-Fenster im Hintergrund angezeigt. Dann muss es mit Klick auf das Console-Icon in der Taskleiste in den Vordergrund geholt werden.

* Neue Pyton-Versionen sind in der Regel nicht abwärtskompatibel.
* Python2 und Python3 sind bzgl der Zeichenkodierung inkompatibel:
	* Python2: kodiert Texte in ASCII
	* Python3: kodiert Text in UTF-8
* Möchte man in Python3 Programme ausführen, die für Python2 geschrieben sind und die Zeichenketten erwarten, muss man in Python vor die Zeichenkette "b" schreiben, um den Text als ASCII-Zeichenkette zu kennzeichnen.

* Das ctypes-Modul kann mit der Methode cdll einen in "C" geschriebene Bibliothek einbinden.
* Der Name der Bibiothek wird am Ende von ctypes.cdll.scara angegeben.

