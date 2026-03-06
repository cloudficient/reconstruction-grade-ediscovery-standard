from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


SITEMAP_NAMESPACE = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def on_post_build(config, **kwargs):
    site_dir = Path(config["site_dir"])
    sitemap_xml_path = site_dir / "sitemap.xml"
    sitemap_txt_path = site_dir / "sitemap.txt"

    if not sitemap_xml_path.exists():
        return

    root = ET.fromstring(sitemap_xml_path.read_text(encoding="utf-8"))
    urls = [
        loc.text.strip()
        for loc in root.findall("sm:url/sm:loc", SITEMAP_NAMESPACE)
        if loc.text and loc.text.strip()
    ]

    if not urls:
        return

    sitemap_txt_path.write_text("\n".join(urls) + "\n", encoding="utf-8")
