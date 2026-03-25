#!/bin/bash

# auto_research.sh
# Multistep Auto Workflow: Fra Web-URL til færdig Obsidian Markdown fil.
# Trin 1: Data-Indsamling (via webscraper.py)
# Trin 2: Markdown Generering (via jules_researcher.py)

if [ "$#" -ne 1 ]; then
    echo "Brug: ./tools/auto_research.sh <URL>"
    exit 1
fi

URL=$1
echo "🚀 Starter auto-research for: $URL"

# Kør scraperen og gem JSON-output i en midlertidig fil
TEMP_JSON=$(mktemp)
python tools/webscraper.py "$URL" > "$TEMP_JSON"

# Tjek om scraperen fejlede
if [ $? -ne 0 ]; then
    echo "❌ Fejl under data-indsamling fra $URL"
    rm "$TEMP_JSON"
    exit 1
fi

# Udtræk Location og Data vha. python (da jq muligvis ikke er tilgængelig i miljøet)
LOCATION=$(python -c "import sys, json; print(json.load(open(sys.argv[1]))['location'])" "$TEMP_JSON")
DATA_JSON=$(python -c "import sys, json; print(json.dumps(json.load(open(sys.argv[1]))['data']))" "$TEMP_JSON")

echo "✅ Data skrabet succesfuldt for lokation: $LOCATION"

# Kør forsknings-scriptet med de udpakkede data
python tools/jules_researcher.py "$LOCATION" "$DATA_JSON"

# Oprydning
rm "$TEMP_JSON"

echo "🎉 Auto-research fuldført! Tjek Arkitektur-mappen."
