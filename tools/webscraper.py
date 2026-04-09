import sys
import json
import urllib.request
from html.parser import HTMLParser

class SimpleHTMLScraper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_p = False
        self.title = ""
        self.paragraphs = []
        self.meta_description = ""

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        elif tag == "p":
            self.in_p = True
        elif tag == "meta":
            attrs_dict = dict(attrs)
            if attrs_dict.get("name", "").lower() == "description":
                self.meta_description = attrs_dict.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "p":
            self.in_p = False

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return

        if self.in_title:
            self.title += data
        elif self.in_p:
            # Avoid overly long paragraphs
            if len(self.paragraphs) < 3 and len(data) > 20:
                self.paragraphs.append(data)

def scrape_url(url):
    """
    Scrapes basic information from a given URL and returns
    a dictionary compatible with jules_researcher.py
    """
    try:
        # User-Agent to prevent basic 403 Forbidden errors
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) JulesResearcher/1.0'}
        )

        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8')

        parser = SimpleHTMLScraper()
        parser.feed(html_content)

        # Build description from meta description or paragraphs
        description = parser.meta_description
        if not description:
            description = " ".join(parser.paragraphs)

        if not description:
            description = "Ingen beskrivelse fundet."

        # Try to infer some data or use placeholders
        location_name = parser.title.split('-')[0].split('|')[0].strip()
        if not location_name:
            location_name = "Ukendt_Lokation"

        data = {
            "city": "Ukendt",
            "year": "Ukendt",
            "architect": "Ukendt",
            "style": "Ukendt",
            "area": 1000,
            "foundation_type": "Pælefundering",
            "description": f"Skrabet fra {url}: {description[:500]}...",
            "hidden_infra_type": "Ukendt",
            "status": "Research via Webscraper"
        }

        return location_name, data

    except Exception as e:
        print(f"Fejl ved skrabning af {url}: {e}", file=sys.stderr)
        return None, None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Brug: python webscraper.py <URL>")
        sys.exit(1)

    target_url = sys.argv[1]
    location, scraped_data = scrape_url(target_url)

    if location and scraped_data:
        # Output strictly JSON so it can be piped or read easily
        output = {
            "location": location,
            "data": scraped_data
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))

        print(f"\n# Kan bruges direkte med jules_researcher.py sådan her:", file=sys.stderr)
        print(f"# python tools/jules_researcher.py \"{location}\" '{json.dumps(scraped_data, ensure_ascii=False)}'", file=sys.stderr)
    else:
        sys.exit(1)
