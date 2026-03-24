# AGENTS.md - By-Research Project Guidelines

Agentic coding agents operating in this Danish architecture/infrastructure research project.

## Project Overview
- **Python** - Scripts for generating research documentation
- **HTML/Three.js** - 3D visualization dashboards
- **Markdown** - Documentation in Obsidian-compatible format
- **GitHub Actions** - Automated research workflow

---

## Build & Run Commands

### Python Scripts
```bash
python tools/jules_researcher.py "Location Name" '{"key": "value"}'
python tools/jules_researcher.py "Aarhus Hovedbanegård" '{"city": "Aarhus", "year": "1927", "area": 1200}'
```

### HTML/Three.js Files
```bash
python -m http.server 8000
# Open http://localhost:8000/index.html
```

### GitHub Actions (Manual Trigger)
```bash
gh workflow run jules-research.yml -f location="Aarhus Hovedbanegård" -f data='{"city": "Aarhus"}'
```

---

## Testing

### Single Test (Python)
No formal test suite - test manually:
```bash
python tools/jules_researcher.py "Test Location" '{"city": "Test", "year": "2024"}'
# Verify output in Arkitektur/ directory
```

### HTML/Three.js Testing
- Open HTML files in browser
- Check console for JavaScript errors
- Verify Three.js scene renders correctly

---

## Code Style Guidelines

### Python Style

**Imports**: Standard library first
```python
import sys
import json
import os
from datetime import datetime
```

**Formatting**: 4-space indentation, max 100 chars, f-strings

**Naming**:
- Classes: `PascalCase` (e.g., `JulesResearcher`)
- Functions/methods: `snake_case` (e.g., `generate_research_entry`)
- Variables: `snake_case` (e.g., `output_dir`)

**Type hints**: Use where beneficial
```python
def generate_research_entry(self, location: str, data: dict) -> str:
```

**Error handling**:
```python
try:
    data_dict = json.loads(raw_data)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
```

### HTML/JavaScript Style

**HTML**: Semantic HTML5, lowercase tags/attributes, 4-space indent

**CSS**: CSS custom properties for colors, monospace fonts (`Courier New`, `Roboto Mono`)

**JavaScript (ES Modules)**:
- Use `import`/`export`
- Use `const` and `let` - avoid `var`
- Arrow functions, template literals

**Three.js Conventions**:
- `LineSegments` with `EdgesGeometry` for wireframe
- Colors: Cyan (`#00ffcc`) visible, Pink (`#ff3366`) hidden
- Background: `#050505`
- Include `OrbitControls` for interaction

### Markdown Style

- Obsidian wiki-links: `[[Byer/By navn]]`
- Tags: `#arkitektur #bygning #research`
- Headers: `#` main, `##` sections, `---` horizontal rules
- Danish language content, **bold** key terms
- Timestamps: `Created: YYYY-MM-DD`

---

## Template Conventions

| Template | Location | Fields |
|----------|----------|--------|
| Bygning | `Templates/Bygning.md` | name, city, year, architect, style |
| By | `Templates/By.md` | name, founded, region, population |
| Infrastruktur | `Templates/Infrastruktur.md` | tunnels, bunkers, utilities |

---

## File Locations

| Type | Directory |
|------|-----------|
| Cities | `Byer/` |
| Architecture | `Arkitektur/` |
| Infrastructure | `Infrastruktur/` |
| Templates | `Templates/` |
| 3D Visualizations | Root (`.html` files) |
| Scripts | `tools/` |

---

## Design Guidelines

See `Templates/Design_Guidelines.md`:
- Neon-Grid Noir palette
- Wireframe/skeletal rendering
- Transparency for underground elements
- Monospace typography

---

## Git Commit Messages

- `Jules: Automatiseret research af [Location]` - automated research
- `Add: [description]` - new features
- `Fix: [description]` - bug fixes
- `Update: [description]` - modifications

---

## Key Files

- `tools/jules_researcher.py` - Main Python script
- `index.html` - Main dashboard with Three.js
- `Templates/Design_Guidelines.md` - Visual style reference
- `.github/workflows/jules-research.yml` - CI/CD workflow
