## Thonny telepítése

Ebben a lépésben telepítheted a Thonnyt, vagy ha már telepítve van akkor győződj meg róla, hogy a legújabb verzióval rendelkezel. Ezután csatlakoztasd a Raspberry Pi Pico-t a számítógéphez és futtass le néhány egyszerű Python kódot a Shell segítségével.

## --- collapse ---

cím: Thonny a Raspberry Pi-n

---

- A Thonny már telepítve van a Raspberry Pi OS programcsomagban, de előfordulhat, hogy frissíteni kell a legújabb verzióra
- A képernyő bal felső sarkában lévő ikonra kattintva vagy a Ctrl+Alt+T billentyűk egyidejű lenyomásával nyisd meg a terminál ablakot
- Az OS és a Thonny frissítéséhez gépeld be a következőket az ablakba

```bash
sudo apt update && sudo apt upgrade -y
```

\--- /collapse ---

\--- collapse ---

---

cím: Thonny telepítése más operációs rendszerekre

---

- Windows, macOS és Linux rendszerekre telepítheted a legújabb Thonny IDE-t, vagy frissítheted a meglévő verziót
- Egy webböngészőben nyisd meg a [thonny.org](https://thonny.org/) webhelyet
- A telepítéshez a böngészőablak jobb felső sarkában Windows és macOS rendszerhez letöltési hivatkozások, Linuxhoz pedig utasítások találhatók
- Töltsd le a megfelelő fájlokat, és futtasd őket a Thonny telepítéséhez

![Töltsd le az utasításokat a thonny webhelyről](images/thonny-site.png)

\--- /collapse ---

\--- task ---

Nyisd meg a Thonnyt az alkalmazásindítóból. Valami hasonlót kellene látnod:

![Thonny alkalmazás](images/thonny-editor.png)

\--- /task ---

\--- task ---

A Thonny segítségével szabványos Python kódokat írhatsz. Gépeld be a következőket a főablakba, majd kattints a **Run / Futtatás** gombra (a rendszer kérini fogja, hogy mentsd el a fájlt).

```python3
print('Hello World!')
```

\--- /task ---

Most már készen állsz a következő lépésre, csatlakoztasd a Raspberry Pi Pico-d.
