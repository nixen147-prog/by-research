# Design Guidelines: Digital Architect / X-Ray Research Style

Denne fil definerer den visuelle stil og de tekniske parametre for "By-Research" projektets 3D-visualiseringer og dokumentation.

## 🎨 Farvepalette (Neon-Grid Noir)
- **Primary (Structure):** `#00ffcc` (Neon Cyan/Turquoise) - Bruges til synlig arkitektur og lineart.
- **Secondary (Hidden):** `#ff3366` (Neon Pink/Red) - Bruges til skjult infrastruktur, fundamenter og hemmelige rum.
- **Background:** `#050505` (Deep Charcoal/Black) - Giver maksimal kontrast.
- **Grid/UI:** `#333333` & `#111111` - Subtile hjælpelinjer.

## 📐 Visuel Stil
- **Lineart:** Altid `LineSegments` eller `EdgesGeometry`. Ingen massive flader (solids).
- **Wireframe Look:** Fokus på bygningens "skelet" og matematiske præcision.
- **Transparency:** Skjulte elementer (pink) skal have en `opacity` på ca. 0.5 for at indikere, at de er under jorden eller bag mure.
- **Typography:** Monospaced skrifttyper (`Courier New`, `Roboto Mono`) for at understøtte "data-crunching" følelsen.

## 🤖 Prompt / Instruks til Gemini (Genskabelse)
Når du beder mig (eller en anden AI) om at bygge noget i denne stil, kan du bruge denne prompt:
> "Generér en interaktiv 3D-visualisering i HTML/Three.js ved brug af 'Digital Architect' stilen: Sort baggrund (#050505), cyan lineart (#00ffcc) for overjordiske strukturer, og semi-transparent neon-pink (#ff3366) for skjult infrastruktur eller fundamenter. Brug et diskret 3D-grid og sørg for at koden inkluderer OrbitControls til interaktion. Stilen skal være ren, teknisk og ligne et røntgenbillede af en bygning."

---
*Sidst opdateret: 24. marts 2026*
*Projekt: Dansk By-Research*
