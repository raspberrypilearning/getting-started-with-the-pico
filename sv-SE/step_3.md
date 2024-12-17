## Installera Thonny

I det här steget kommer du att installera Thonny eller se till att du har den senaste versionen. Sedan kommer du att ansluta till en Raspberry Pi Pico och köra lite enkel Python-kod med hjälp av skalet.

--- collapse ---
---

title: Thonny på Raspberry Pi

---

- Thonny är redan installerat på Raspberry Pi OS, men kan behöva uppdateras till den senaste versionen
- Öppna ett terminalfönster, antingen genom att klicka på ikonen i det övre vänstra hörnet av skärmen eller genom att trycka på Ctrl+Alt+T samtidigt
- I fönstret skriver du följande för att uppdatera ditt OS och Thonny

```bash
sudo apt update && sudo apt upgrade -y
```

--- /collapse ---

--- collapse ---

---

title: Installera Thonny på andra operativsystem

---

- På Windows, macOS och Linux kan du installera den senaste Thonny IDE eller uppdatera en befintlig version
- I en webbläsare, navigera till [thonny.org](https://thonny.org/)
- I det övre högra hörnet av webbläsarfönstret ser du nedladdningslänkar för Windows och macOS och instruktioner för Linux
- Ladda ner relevanta filer och kör dem för att installera Thonny

![Ladda ner instruktioner från thonny site](images/thonny-site.png)

--- /collapse ---

--- task ---

Öppna appen Thonny. Det borde se ut ungefär så här:

![Thonny applikation](images/thonny-editor.png)

--- /task ---

--- task ---

Du kan använda Thonny för att skriva standard Python-kod. Skriv följande i huvudfönstret och klicka sedan på knappen **Run** (du kommer att bli ombedd att spara filen).

```python3
print('Hello World!')
```

--- /task ---

Du är nu redo att gå vidare till nästa steg och ansluta din Raspberry Pi Pico.
