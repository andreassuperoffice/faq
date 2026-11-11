#!/usr/bin/env python3
"""Export published SuperOffice community FAQs to Markdown files.

Reads the public FAQ sitemap for each language, opens every FAQ and saves it as
    faq/<lang>/<slug>.md      one file per FAQ, with title, url, lang, updated
    index.tsv                 one line per FAQ (lang, updated, title, url, path)
    EXPORT.json               when the export ran and what happened

Setup (once):   pip install requests beautifulsoup4 markdownify
Trial run:      python faq_export.py --out faq-repo --langs en --limit 5
Full run:       python faq_export.py --out faq-repo
Then publish:   cd faq-repo && git add -A && git commit -m "FAQ export" && git push

The script only reads public pages. It never logs in and never changes the site.
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    from markdownify import markdownify
except ImportError:
    sys.exit("Missing packages. Run: pip install requests beautifulsoup4 markdownify")

BASE = "https://community.superoffice.com"
HOST = urlparse(BASE).netloc
DEFAULT_UA = "SuperOfficeSupportFaqExport/1.0 (internal support tooling)"

# "Updated on" label per language. EN, NO, SV, DA and NL were seen on the live site.
UPDATED_RE = re.compile(
    r"(?:Updated on|Oppdatert på|Uppdaterad på|Opdateret om|Bijgewerkt op|Aktualisiert am)"
    r"\s*:?\s*([^\n]{4,40})"
)
# Everything from this heading down is the language switcher, not FAQ content.
# Only the English label was seen on the live site; the others are guesses.
END_MARKERS = ("available languages", "tilgjengelige språk", "tillgängliga språk")
BLOCK_TITLES = ("just a moment", "access denied", "attention required", "robot", "blocked", "captcha")
MIN_BODY_CHARS = 200          # shorter than this is reported as "thin"
MAX_BLOCKS_IN_A_ROW = 5       # stop a language after this many blocked pages in a row


class Blocked(Exception):
    pass


class NotFound(Exception):
    pass


def looks_blocked(raw):
    m = re.search(rb"<title[^>]*>(.*?)</title>", raw[:20000], re.I | re.S)
    title = m.group(1).decode("utf-8", "ignore").lower() if m else ""
    return any(hint in title for hint in BLOCK_TITLES)


def fetch(session, url, retries=2):
    """Return the page bytes. Raises Blocked, NotFound or RuntimeError."""
    problem = "unknown error"
    blocked = False
    for attempt in range(retries + 1):
        try:
            r = session.get(url, timeout=30)
        except requests.RequestException as e:
            problem, blocked = f"network error: {e}", False
        else:
            if r.status_code == 404:
                raise NotFound(url)
            if r.status_code in (403, 429, 503) or looks_blocked(r.content):
                problem, blocked = f"blocked (HTTP {r.status_code})", True
            elif r.status_code == 200:
                return r.content
            else:
                problem, blocked = f"HTTP {r.status_code}", False
        if attempt < retries:
            time.sleep(5 * (attempt + 1))
    if blocked:
        raise Blocked(problem)
    raise RuntimeError(problem)


def sitemap_links(raw, lang):
    """Return {faq_url: title} for one language's sitemap page."""
    soup = BeautifulSoup(raw, "html.parser")
    prefix = f"/{lang}/support-faqs/faq/"
    found = {}
    for a in soup.find_all("a", href=True):
        p = urlparse(urljoin(f"{BASE}/{lang}/support-faqs/sitemap/faq/", a["href"]))
        if p.netloc != HOST or not p.path.startswith(prefix):
            continue
        slug = p.path[len(prefix):].strip("/")
        if not slug or "/" in slug:
            continue
        url = f"{BASE}{prefix}{slug}/"
        title = a.get_text(" ", strip=True)
        if url not in found or (title and not found[url]):
            found[url] = title
    return found


def find_container(soup, h1, selector):
    """Pick the element that holds the FAQ text."""
    if selector:
        hit = soup.select_one(selector)
        if hit:
            return hit
    if h1 is None:
        return soup.body or soup
    need = len(h1.get_text(strip=True)) + MIN_BODY_CHARS
    # Smallest article/main block that contains the heading and real text.
    for parent in h1.parents:
        if parent.name in ("article", "main") or parent.get("role") == "main":
            if len(parent.get_text(strip=True)) >= need:
                return parent
    # Otherwise climb from the heading until there is real text around it.
    for parent in h1.parents:
        if parent.name in ("body", "html", "[document]"):
            break
        if len(parent.get_text(strip=True)) >= need:
            return parent
    return soup.body or soup


def cut_from_marker(container):
    """Remove the language-switcher heading and everything after it."""
    for node in container.find_all(string=True):
        if node.strip().lower().rstrip(":") in END_MARKERS:
            start = node.parent
            if start is None or start is container:
                return
            # Climb to the container, dropping everything that comes after the marker.
            el = start
            while el is not None and el is not container:
                for sib in list(el.find_next_siblings()):
                    sib.decompose()
                el = el.parent
            start.decompose()
            return


def extract(raw, url, selector=None, fallback_title=""):
    """Return (title, updated, markdown_body) for one FAQ page."""
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "nav", "header", "footer", "form", "iframe"]):
        tag.decompose()
    h1 = soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else fallback_title
    container = find_container(soup, h1, selector)
    cut_from_marker(container)

    m = UPDATED_RE.search(container.get_text("\n"))
    updated = m.group(1).strip() if m else ""

    if h1 is not None and h1 in container.descendants:
        h1.decompose()
    for a in container.find_all("a", href=True):
        a["href"] = urljoin(url, a["href"])
    for img in container.find_all("img"):
        src = img.get("src") or ""
        if (not src or src.startswith("data:")) and img.get("data-src"):
            src = img["data-src"]
        if not src or src.startswith("data:"):
            img.replace_with(img.get("alt") or "[image]")   # no giant inline images
        else:
            img["src"] = urljoin(url, src)

    body = markdownify(str(container), heading_style="ATX", bullets="-")
    body = "\n".join(line.rstrip() for line in body.splitlines()
                     if not re.fullmatch(r"\s*#+\s*", line))
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return title, updated, body


def render(title, url, lang, updated, body):
    head = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"url: {url}",
        f"lang: {lang}",
        f"updated: {json.dumps(updated, ensure_ascii=False)}",
        "---",
    ]
    return "\n".join(head) + f"\n\n# {title}\n\n{body}\n"


def read_front_matter(path):
    meta = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return meta
    for line in lines[1:]:
        if line == "---":
            break
        key, _, value = line.partition(": ")
        try:
            meta[key] = json.loads(value) if value.startswith('"') else value
        except ValueError:
            meta[key] = value
    return meta


def write_index(out):
    rows = []
    for path in sorted((out / "faq").glob("*/*.md")):
        m = read_front_matter(path)
        clean = lambda s: str(s).replace("\t", " ")
        rows.append("\t".join([
            clean(m.get("lang", path.parent.name)), clean(m.get("updated", "")),
            clean(m.get("title", "")), clean(m.get("url", "")), path.relative_to(out).as_posix(),
        ]))
    (out / "index.tsv").write_text(
        "lang\tupdated\ttitle\turl\tpath\n" + "\n".join(rows) + "\n", encoding="utf-8")
    return len(rows)


def export_lang(session, lang, out, args):
    stats = {"in_sitemap": 0, "written": 0, "unchanged": 0, "removed": [],
             "failed": [], "thin": [], "note": ""}
    folder = out / "faq" / lang
    folder.mkdir(parents=True, exist_ok=True)

    try:
        links = sitemap_links(fetch(session, f"{BASE}/{lang}/support-faqs/sitemap/faq/"), lang)
    except (Blocked, NotFound, RuntimeError) as e:
        stats["note"] = f"sitemap not read: {e}. Existing files left as they are."
        print(f"[{lang}] {stats['note']}")
        return stats
    stats["in_sitemap"] = len(links)
    print(f"[{lang}] {len(links)} FAQs in the sitemap")
    if not links:
        stats["note"] = "sitemap opened but no FAQ links found. Existing files left as they are."
        return stats

    todo = sorted(links.items())
    if args.limit:
        todo = todo[:args.limit]
    blocks_in_a_row = 0
    for i, (url, sitemap_title) in enumerate(todo, 1):
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        try:
            raw = fetch(session, url)
            blocks_in_a_row = 0
        except Blocked as e:
            blocks_in_a_row += 1
            stats["failed"].append({"url": url, "why": str(e)})
            print(f"[{lang}] {i}/{len(todo)} BLOCKED {slug}")
            if blocks_in_a_row >= MAX_BLOCKS_IN_A_ROW:
                stats["note"] = f"stopped after {MAX_BLOCKS_IN_A_ROW} blocked pages in a row."
                print(f"[{lang}] {stats['note']}")
                break
            time.sleep(args.delay)
            continue
        except (NotFound, RuntimeError) as e:
            why = "not found (404)" if isinstance(e, NotFound) else str(e)
            stats["failed"].append({"url": url, "why": why})
            print(f"[{lang}] {i}/{len(todo)} FAILED  {slug}: {why}")
            time.sleep(args.delay)
            continue

        title, updated, body = extract(raw, url, args.selector, sitemap_title)
        if len(body) < MIN_BODY_CHARS:
            stats["thin"].append(url)
        text = render(title or sitemap_title or slug, url, lang, updated, body)
        path = folder / f"{slug}.md"
        if path.exists() and path.read_text(encoding="utf-8") == text:
            stats["unchanged"] += 1
        else:
            path.write_text(text, encoding="utf-8")
            stats["written"] += 1
        print(f"[{lang}] {i}/{len(todo)} ok      {slug}")
        time.sleep(args.delay)

    # Remove files for FAQs that are no longer published. Skipped on trial runs,
    # and when the sitemap looks suspiciously short, so a bad day can't empty the repo.
    if not args.limit:
        wanted = {u.rstrip("/").rsplit("/", 1)[-1] for u in links}
        existing = {p.stem: p for p in folder.glob("*.md")}
        gone = sorted(set(existing) - wanted)
        if gone and len(wanted) < 0.5 * len(existing):
            stats["note"] = (stats["note"] + " " if stats["note"] else "") + \
                f"sitemap has {len(wanted)} FAQs but {len(existing)} files exist; nothing removed."
            print(f"[{lang}] {stats['note']}")
        else:
            for slug in gone:
                existing[slug].unlink()
            stats["removed"] = gone
    return stats


def main():
    ap = argparse.ArgumentParser(description="Export SuperOffice community FAQs to Markdown.")
    ap.add_argument("--out", default=".", help="folder to write into (the git repo)")
    ap.add_argument("--langs", nargs="+", default=["en", "no", "sv"])
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between pages")
    ap.add_argument("--limit", type=int, default=0, help="trial run: only the first N FAQs per language")
    ap.add_argument("--selector", default=None, help="CSS selector for the FAQ content, if the automatic pick is wrong")
    ap.add_argument("--user-agent", default=DEFAULT_UA, help="how the script identifies itself to the site")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": args.user_agent, "Accept-Language": "en"})

    report = {
        "exported_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "trial_run": bool(args.limit),
        "languages": {},
    }
    for lang in args.langs:
        report["languages"][lang] = export_lang(session, lang, out, args)

    report["files_in_index"] = write_index(out)
    (out / "EXPORT.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("\nSummary")
    problems = False
    for lang, s in report["languages"].items():
        print(f"  {lang}: {s['in_sitemap']} in sitemap, {s['written']} written, {s['unchanged']} unchanged, "
              f"{len(s['removed'])} removed, {len(s['failed'])} failed, {len(s['thin'])} thin"
              + (f" | {s['note']}" if s["note"] else ""))
        problems = problems or bool(s["failed"] or s["thin"] or s["note"])
    print(f"  {report['files_in_index']} files listed in index.tsv. Details in EXPORT.json.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
