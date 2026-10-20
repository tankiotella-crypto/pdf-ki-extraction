import json, sys
from pypdf import PdfReader
import ollama

# 1. Text aus dem PDF lesen
datei = sys.argv[1] if len(sys.argv) > 1 else "test.pdf"
text = "\n".join(seite.extract_text() or "" for seite in PdfReader(datei).pages)
print("--- Gelesener Text ---")
print(text[:500], "\n")

# 2. Lokales Sprachmodell nach strukturierten Feldern fragen (Daten bleiben auf dem Rechner)
prompt = f"""Du bist ein Assistent für medizinische Dokumente.
Extrahiere aus dem folgenden Dokument genau diese Felder als JSON:
name, geburtsdatum, dokumentdatum, diagnosen (Liste), absender.
Fehlt ein Feld, setze null. Erfinde nichts. Antworte nur mit JSON.

Dokument:
{text[:6000]}"""

antwort = ollama.chat(
    model="llama3.2",
    messages=[{"role": "user", "content": prompt}],
    format="json",
    options={"temperature": 0},
)

# 3. Ergebnis ausgeben
ergebnis = json.loads(antwort["message"]["content"])
print("--- Extrahierte Daten (JSON) ---")
print(json.dumps(ergebnis, indent=2, ensure_ascii=False))
