# PDF-KI-Extraktion (lokal)

Python-Skript, das Text aus einem PDF-Arztbrief liest und mit einem
lokalen Sprachmodell (Ollama, Llama 3.2) strukturierte Daten als JSON
extrahiert: Name, Geburtsdatum, Dokumentdatum, Diagnosen, Absender.

- Läuft komplett lokal: keine Daten verlassen den Rechner (Datenschutz)
- Getestet nur mit erfundenen Testdaten
- Bekannte Grenzen: uneinheitliche Datumsformate, mögliche Halluzinationen
  -> Ergebnisse müssen geprüft werden

Start: python extrakt.py test.pdf
