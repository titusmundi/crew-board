#!/usr/bin/env python3
"""Prints docs/Crew Board guide.html to docs/Crew Board guide.pdf on Titus Mundi paper.

Usage: python3 scripts/build_guide_pdf.py
Needs Google Chrome (headless print). The HTML carries the page design: brand fonts and logo from docs/assets,
the letterhead header and footer, and the page numbers.
"""
import os, subprocess, sys

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
here = os.path.dirname(os.path.abspath(__file__))
docs = os.path.join(os.path.dirname(here), "docs")
src = os.path.join(docs, "Crew Board guide.html")
out = os.path.join(docs, "Crew Board guide.pdf")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf=" + out, "file://" + src], check=True, capture_output=True)
print("wrote", out)
