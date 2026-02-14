#!/usr/bin/env python3
import gzip
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Infrastructure source: the latest commit on origin/main that has all the
# infrastructure files (_config.yml, _layouts/, assets/, .github/, etc.)
# plus the media images.  We grab non-page files from this tree.
INFRA_SOURCE = "404588899"  # tip of origin/main

# The original Jekyll conversion commit — used for author/date metadata
# on our synthetic "Convert to Jekyll" commit.
JEKYLL_CONVERT = "a7697c84a"

# Post-migration edit commit hashes — used only for author/date metadata.
# The actual edits are applied programmatically by POST_MIGRATION_EDITS
# (defined later alongside the edit functions).

AUTHOR_MAP = {
    "127.0.0.1": ("DokuWiki System", "system@wiki.csswg.org"),
    "146.82.168.18": ("Anonymous", "anonymous@wiki.csswg.org"),
    "188.143.232.12": ("Anonymous", "anonymous@wiki.csswg.org"),
    "194.246.102.4": ("Anonymous", "anonymous@wiki.csswg.org"),
    "198.246.99.88": ("Anonymous", "anonymous@wiki.csswg.org"),
    "218.108.168.134": ("Anonymous", "anonymous@wiki.csswg.org"),
    "98.248.36.12": ("Anonymous", "anonymous@wiki.csswg.org"),
    "AmeliaBR": ("Amelia Bellamy-Royds", "amelia.bellamy.royds@gmail.com"),
    "AryehGregor": ("Aryeh Gregor", "ayg@aryeh.name"),
    "JohnJansen": ("John Jansen", "2119039+thejohnjansen@users.noreply.github.com"),
    "MaRakow": ("Matt Rakow", "marakow@microsoft.com"),
    "SebastianZ": ("Sebastian Zartner", "sebastianzartner@gmail.com"),
    "SimonSapin": ("Simon Sapin", "simon.sapin@exyr.org"),
    "SteveZilles": ("Steve Zilles", "szilles@adobe.com"),
    "Tantek": ("Tantek Çelik", "tantek@cs.stanford.edu"),
    "acebal": ("César Acebal", "cfacebal@gmail.com"),
    "adam_argyle": ("Adam Argyle", "argyle@google.com"),
    "adenilson": ("Adenilson Cavalcanti", "cavalcantii@gmail.com"),
    "alancutter": ("Alan Cutter", "alancutter@chromium.org"),
    "alexmog": ("Alex Mogilevsky", "alexmog@microsoft.com"),
    "alisonmaher": ("Alison Maher", "almaher@microsoft.com"),
    "amelia_bellamy_royds": ("Amelia Bellamy-Royds", "amelia.bellamy.royds@gmail.com"),
    "andreubotella": ("Andreu Botella", "andreu@andreubotella.com"),
    "andrewfedoniouk": ("Andrew Fedoniouk", "6752794+c-smile@users.noreply.github.com"),
    "anne": ("Anne van Kesteren", "annevk@opera.com"),
    "annevk": ("Anne van Kesteren", "annevk@opera.com"),
    "aprowse": ("Andy Prowse", "33927861+aprowse@users.noreply.github.com"),
    "arno": ("Arno Gourdol", "63460665+gourdol@users.noreply.github.com"),
    "arronei": ("Arron Eicholz", "arron.eicholz@microsoft.com"),
    "arybka": ("Andrey Rybka", "4530160+arybka@users.noreply.github.com"),
    "astearns": ("Alan Stearns", "stearns@adobe.com"),
    "ben": ("Benjamin De Cock", "ben@deaxon.com"),
    "bert": ("Bert Bos", "bert@w3.org"),
    "birtles": ("Brian Birtles", "birtles@gmail.com"),
    "bkardell": ("Brian Kardell", "bkardell@gmail.com"),
    "bkardell2": ("Brian Kardell", "bkardell@gmail.com"),
    "bkemper": ("Brian Kemper", "1335605+bkemper@users.noreply.github.com"),
    "bojcampbell": ("Boj Campbell", "81823204+bojcampbell@users.noreply.github.com"),
    "bokan": ("David Bokan", "bokan@chromium.org"),
    "bramus": ("Bramus", "bramus@bram.us"),
    "brian_birtles": ("Brian Birtles", "birtles@gmail.com"),
    "brunoabinader": ("Bruno de Oliveira Abinader", "bruno.d@partner.samsung.com"),
    "bts": ("Brandon Stewart", "brandonstewart@apple.com"),
    "bzbarsky": ("Boris Zbarsky", "1457979+bzbarsky@users.noreply.github.com"),
    "cabanier": ("Rik Cabanier", "cabanier@adobe.com"),
    "castastrophe": (
        "Cassondra Roberts",
        "1840295+castastrophe@users.noreply.github.com",
    ),
    "cbiesinger": ("Christian Biesinger", "cbiesinger@chromium.org"),
    "ccameron": ("Christopher Cameron", "ccameron@chromium.org"),
    "changseok": ("ChangSeok Oh", "changseok@webkit.org"),
    "chris_harrelson": ("Chris Harrelson", "chrishtr@chromium.org"),
    "chrisl": ("Chris Lilley", "chris@w3.org"),
    "crissov": ("Christoph Päper", "bugzilla@crissov.de"),
    "cwilso": ("Chris Wilson", "cwilso@gmail.com"),
    "dael": ("Dael Jackson", "dael@daelity.com"),
    "daniec": ("Dan Clark", "daniec@microsoft.com"),
    "daniel.weck": ("Daniel Weck", "daniel.weck@gmail.com"),
    "dauwhe": ("Dave Cramer", "dauwhe@gmail.com"),
    "davidleininger": (
        "David Leininger",
        "1840132+davidleininger@users.noreply.github.com",
    ),
    "dazabani": ("Delan Azabani", "delan@azabani.com"),
    "dbaron": ("L. David Baron", "dbaron@dbaron.org"),
    "dcrousso": ("Devin Rousso", "dcrousso@webkit.org"),
    "dgrogan": ("David Grogan", "dgrogan@chromium.org"),
    "dholbert": ("Daniel Holbert", "dholbert@cs.stanford.edu"),
    "dino": ("Dean Jackson", "dino@apple.com"),
    "drott": ("Dominik Röttsches", "drott@chromium.org"),
    "dschulze": ("Dirk Schulze", "dschulze@adobe.com"),
    "dsinger2": ("David Singer", "13665985+dsinger@users.noreply.github.com"),
    "emeyer": ("Eric Meyer", "eric@meyerweb.com"),
    "emil_a_eklund": ("Emil A. Eklund", "1753727+eaenet@users.noreply.github.com"),
    "emilio": ("Emilio Cobos Álvarez", "emilio@crisal.io"),
    "eportis": ("Eric Portis", "e@ericportis.com"),
    "ericwilligers": ("Eric Willigers", "ericwilligers@chromium.org"),
    "esprehn": ("Elliott Sprehn", "esprehn@chromium.org"),
    "fantasai": ("Elika Etemad", "fantasai.bugs@inkedblade.net"),
    "fergal": ("Fergal Daly", "fergal@chromium.org"),
    "flackr": ("Robert Flack", "flackr@chromium.org"),
    "florian": ("Florian Rivoal", "florian@rivoal.net"),
    "fremy": ("François Remy", "frremy@microsoft.com"),
    "fserb": ("Fernando Serboncini", "fserb@chromium.org"),
    "gadams": ("Glenn Adams", "glenn@skynav.com"),
    "glazou": ("Daniel Glazman", "daniel@glazman.org"),
    "gregwhitworth": ("Greg Whitworth", "gregwhitworth@outlook.com"),
    "gsnedders": ("Sam Sneddon", "me@gsnedders.com"),
    "gtalbot": ("Gérard Talbot", "github@gtalbot.org"),
    "heycam": ("Cameron McCormack", "cam@mcc.id.au"),
    "hixie": ("Ian Hickson", "ian@hixie.ch"),
    "hober": ("Theresa O'Connor", "hober@apple.com"),
    "howcome": ("Håkon Wium Lie", "howcome@opera.com"),
    "http://blog.crissov.de/": ("Christoph Päper", "bugzilla@crissov.de"),
    "http://id.annevankesteren.nl/": ("Anne van Kesteren", "annevk@opera.com"),
    "hyojin": ("Hyojin Song", "hyojin22.song@lge.com"),
    "ihilerio": ("Israel Hilerio", "8966941+ihilerio@users.noreply.github.com"),
    "ikilpatrick": ("Ian Kilpatrick", "ikilpatrick@chromium.org"),
    "ishida": ("Richard Ishida", "ishida@w3.org"),
    "itpastorn": ("Lars Gunther", "gunther@keryx.se"),
    "jacobg": ("jacobg", "736985+jacobg@users.noreply.github.com"),
    "jarhar": ("Joey Arhar", "jarhar@chromium.org"),
    "javier_fernandez": ("Javier Fernandez", "jfernandez@igalia.com"),
    "jdaggett": ("John Daggett", "jdaggett@mozilla.com"),
    "jensimmons": ("Jen Simmons", "jensimmons@apple.com"),
    "jetvillegas": ("Jet Villegas", "1307977+jetvillegas@users.noreply.github.com"),
    "jfernandez": ("Javier Fernandez", "jfernandez@igalia.com"),
    "jh.hong": ("Jihye Hong", "jh.hong@lge.com"),
    "jirka_kosek": ("Jirka Kosek", "jirka@kosek.cz"),
    "johanneswilm": ("Johannes Wilm", "mail@johanneswilm.org"),
    "johnjansen": ("John Jansen", "2119039+thejohnjansen@users.noreply.github.com"),
    "jonathan-watt": ("Jonathan Watt", "jwatt@jwatt.org"),
    "jonathan_kew": ("Jonathan Kew", "jfkthame@gmail.com"),
    "joone": ("Joone Hur", "joone@outlook.com"),
    "joshtumath": ("Josh Tumath", "josh.tumath@bbc.co.uk"),
    "kawabata": ("Shinyu Murakami", "murakami@vivliostyle.org"),
    "kbabbitt": ("Kevin Babbitt", "kbabbitt@microsoft.com"),
    "kennyluck": ("Kang-Hao (Kenny) Lu", "588104+kennyluck@users.noreply.github.com"),
    "khushal_sagar": ("Khushal Sagar", "khushalsagar@chromium.org"),
    "kiet_ho": ("Kiet Ho", "kiet.ho@apple.com"),
    "kojiishi": ("Koji Ishii", "kojiishi@gmail.com"),
    "krit": ("Dirk Schulze", "dschulze@adobe.com"),
    "lea": ("Lea Verou", "lea@verou.me"),
    "liam": ("Liam Quin", "8258535+liamquin@users.noreply.github.com"),
    "lstorset": ("Leif Arne Storset", "lstorset@wiki.csswg.org"),
    "macpherson": ("Luke Macpherson", "72672442+Macpherson@users.noreply.github.com"),
    "majidvp": ("Majid Valipour", "majidvp@chromium.org"),
    "masonf": ("Mason Freed", "masonf@chromium.org"),
    "matt_woodrow": ("Matt Woodrow", "matt.woodrow@gmail.com"),
    "matthieu-dubet": ("Matthieu Dubet", "109102217+mdubet@users.noreply.github.com"),
    "megan_gardner": (
        "Megan Gardner",
        "243650270+megan-gardner@users.noreply.github.com",
    ),
    "megra": ("Manuel Rego", "rego@igalia.com"),
    "melanierichards": ("Melanie Richards", "melanie.richards@microsoft.com"),
    "mfreed": ("Mason Freed", "masonf@chromium.org"),
    "miriam": ("Miriam Suzanne", "miriam@oddbird.net"),
    "mirisuzanne": ("Miriam Suzanne", "miriam@oddbird.net"),
    "mmaxfield": ("Myles C. Maxfield", "mmaxfield@apple.com"),
    "mmielke": ("Markus Mielke", "mmielke@microsoft.com"),
    "mnewman": ("Mike Newman", "5278663+mnewman@users.noreply.github.com"),
    "molly": ("Molly E. Holzschlag", "96634835+ThisMissMolly@users.noreply.github.com"),
    "moonira": ("Munira Tursunova", "moonira@google.com"),
    "ms2ger": ("Ms2ger", "111161+Ms2ger@users.noreply.github.com"),
    "mstensho": ("Morten Stenshorne", "mstensho@chromium.org"),
    "myles": ("Myles C. Maxfield", "mmaxfield@apple.com"),
    "nainar": ("Una Kravets", "nainar@google.com"),
    "nhthvhvbh": ("nhthvhvbh", "nhthvhvbh@wiki.csswg.org"),
    "noamr": ("Noam Rosenthal", "noam.j.rosenthal@gmail.com"),
    "nsull": ("Nat McCully", "38678135+nsull@users.noreply.github.com"),
    "ntim": ("Tim Nguyen", "ntim@apple.com"),
    "ojanvafai": ("Ojan Vafai", "1607171+ojanvafai@users.noreply.github.com"),
    "oriol": ("Oriol Brufau", "obrufau@igalia.com"),
    "oyvind": ("Øyvind Stenhaug", "oyvinds@opera.com"),
    "paulirish": ("Paul Irish", "paulirish@google.com"),
    "pcupp": ("Phil Cupp", "pcupp@microsoft.com"),
    "phuangce": ("Ping Huang", "phuang@adobe.com"),
    "pjmclachlan": ("Penelope McLachlan", "28974+b1tr0t@users.noreply.github.com"),
    "plh": ("Philippe Le Hégaret", "plh@w3.org"),
    "plinss": ("Peter Linss", "peter@linss.com"),
    "rachelandrew": ("Rachel Andrew", "rachelandrew@google.com"),
    "rbetts": ("Ryan Betts", "rbetts@adobe.com"),
    "rbyers": ("Rick Byers", "rbyers@chromium.org"),
    "rcaliman": ("Razvan Caliman", "razvan.caliman@gmail.com"),
    "rego": ("Manuel Rego", "rego@igalia.com"),
    "rhauck": ("Rebecca Hauck", "rhauck@adobe.com"),
    "roman_komarov": ("Roman Komarov", "kizmarh@ya.ru"),
    "rossen": ("Rossen Atanassov", "rossen.atanassov@microsoft.com"),
    "rune": ("Rune Lillesveen", "rune@opera.com"),
    "saloni": ("Saloni Mhapsekar", "797414+saloni@users.noreply.github.com"),
    "samomekarajr": (
        "Sam Davis Omekara",
        "59079555+oSamDavis@users.noreply.github.com",
    ),
    "schenney": ("Stephen Chenney", "schenney@chromium.org"),
    "seokho": ("Seokho Song", "seokho@chromium.org"),
    "shans": ("Shane Stephens", "shanestephens@google.com"),
    "simonp": ("Simon Pieters", "simonp@opera.com"),
    "simonsapin": ("Simon Sapin", "simon.sapin@exyr.org"),
    "skk": ("Soonho Kwon", "skk@wiki.csswg.org"),
    "smcgruer2": ("Stephen McGruer", "smcgruer@chromium.org"),
    "smfr": ("Simon Fraser", "simon.fraser@apple.com"),
    "smurakam": ("Shinyu Murakami", "murakami@vivliostyle.org"),
    "spieters": ("Simon Pieters", "simonp@opera.com"),
    "sstephen2": ("Shane Stephens", "shanestephens@google.com"),
    "stantonm": ("Stanton Marcum", "83246723+StantonM@users.noreply.github.com"),
    "stevezilles": ("Steve Zilles", "szilles@adobe.com"),
    "surma": ("Surma", "surma@google.com"),
    "svgeesus": ("Chris Lilley", "chris@w3.org"),
    "sylvaing": ("Sylvain Galineau", "sylvaing@microsoft.com"),
    "tab": ("Tab Atkins-Bittner", "jackalmage@gmail.com"),
    "tabatkins": ("Tab Atkins-Bittner", "jackalmage@gmail.com"),
    "tantek": ("Tantek Çelik", "tantek@cs.stanford.edu"),
    "tclancy": ("Tom Clancy", "67803+tclancy@users.noreply.github.com"),
    "tomharms": ("Tom Harms", "9092076+TomHarms@users.noreply.github.com"),
    "unakravets": ("Una Kravets", "unakravets@google.com"),
    "upsuper": ("Xidorn Quan", "me@upsuper.org"),
    "vhardy": ("Vincent Hardy", "vhardy@adobe.com"),
    "vlevanto": (
        "Vladimir Levantovsky",
        "17148826+vlevantovsky@users.noreply.github.com",
    ),
    "vmpstr": ("Vladimir Levin", "vmpstr@chromium.org"),
    "vollick": ("Ian Vollick", "vollick@chromium.org"),
    "xfq": ("Fuqiao Xue", "xfq@w3.org"),
    "xiaocheng_hu": ("Xiaocheng Hu", "xiaochengh@chromium.org"),
    "ydaniv": ("Yehonatan Daniv", "maggotfish@gmail.com"),
    "zcorpan": ("Simon Pieters", "zcorpan@gmail.com"),
}


def resolve_author(wiki_username):
    """Resolve a DokuWiki username to (name, email)."""
    if wiki_username in AUTHOR_MAP:
        return AUTHOR_MAP[wiki_username]
    key = wiki_username.lower().strip()
    for map_key, value in AUTHOR_MAP.items():
        if map_key.lower() == key:
            return value
    # Generate a dummy email if we don't know the user
    return (wiki_username, f"{wiki_username}@wiki.csswg.org")


def run_git(args, cwd=None, env=None, input_data=None):
    """Run a git command, returning the CompletedProcess."""
    result = subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
        env=env,
        input=input_data,
    )
    if result.returncode != 0 and args[0] not in ("diff",):
        # Don't warn on expected diff non-zero (means "has changes")
        pass
    return result


def make_author_env(name, email, date_iso):
    """Build env dict for git commit with author/committer info."""
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = name
    env["GIT_AUTHOR_EMAIL"] = email
    env["GIT_AUTHOR_DATE"] = date_iso
    env["GIT_COMMITTER_NAME"] = name
    env["GIT_COMMITTER_EMAIL"] = email
    env["GIT_COMMITTER_DATE"] = date_iso
    return env


def get_commit_meta(ref):
    """Extract author/committer metadata and message from a commit."""
    fmt = "%an%x00%ae%x00%aI%x00%cn%x00%ce%x00%cI"
    r = run_git(["log", "-1", f"--format={fmt}", ref])
    parts = r.stdout.strip().split("\x00")
    r2 = run_git(["log", "-1", "--format=%B", ref])
    return {
        "an": parts[0],
        "ae": parts[1],
        "ad": parts[2],
        "cn": parts[3],
        "ce": parts[4],
        "cd": parts[5],
        "msg": r2.stdout.rstrip(),
    }


def commit_tree(tree, parent, message, env):
    """Create a commit object with the given tree, parent, message, and env."""
    r = run_git(["commit-tree", tree, "-p", parent, "-m", message], env=env)
    return r.stdout.strip()


def build_tree_with_renames(base_ref, renames):
    """Build a new tree object by applying renames to an existing tree."""
    run_git(["read-tree", "--empty"])
    run_git(["read-tree", base_ref])

    r = run_git(["ls-tree", "-r", base_ref])
    blob_map = {}
    for line in r.stdout.strip().split("\n"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        parts = meta.split()
        blob_map[path] = (parts[0], parts[2])  # (mode, hash)

    rename_dict = dict(renames)
    remove_paths = [old for old in rename_dict if old in blob_map]

    add_lines = []
    for old_path in remove_paths:
        mode, blob_hash = blob_map[old_path]
        new_path = rename_dict[old_path]
        add_lines.append(f"{mode} {blob_hash}\t{new_path}")

    if remove_paths:
        run_git(["update-index", "--remove"] + remove_paths)

    if add_lines:
        run_git(
            ["update-index", "--index-info"],
            input_data="\n".join(add_lines) + "\n",
        )

    r = run_git(["write-tree"])
    return r.stdout.strip()


def build_tree_with_conversions(base_ref, file_renames, convert_fn):
    """Build a new tree by renaming files AND converting their content.

    Like build_tree_with_renames, but also transforms file content through
    convert_fn(old_path, content) -> new_content.
    """
    import tempfile

    r = run_git(["ls-tree", "-r", base_ref])
    blob_map = {}
    for line in r.stdout.strip().split("\n"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        parts = meta.split()
        blob_map[path] = (parts[0], parts[2])  # (mode, hash)

    rename_dict = dict(file_renames)
    remove_paths = [old for old in rename_dict if old in blob_map]

    # Build new blobs with converted content
    add_lines = []
    for old_path in remove_paths:
        mode, old_blob = blob_map[old_path]
        new_path = rename_dict[old_path]

        if convert_fn:
            # Read old content
            r = run_git(["cat-file", "blob", old_blob])
            old_content = r.stdout

            # Convert
            new_content = convert_fn(old_path, old_content)

            # Hash new content as blob
            r = run_git(["hash-object", "-w", "--stdin"], input_data=new_content)
            new_blob = r.stdout.strip()
            add_lines.append(f"{mode} {new_blob}\t{new_path}")
        else:
            add_lines.append(f"{mode} {old_blob}\t{new_path}")

    # Update index
    run_git(["read-tree", "--empty"])
    run_git(["read-tree", base_ref])

    if remove_paths:
        run_git(["update-index", "--remove"] + remove_paths)

    if add_lines:
        run_git(
            ["update-index", "--index-info"],
            input_data="\n".join(add_lines) + "\n",
        )

    r = run_git(["write-tree"])
    return r.stdout.strip()


# ---------------------------------------------------------------------------
# DokuWiki → Markdown converter
# ---------------------------------------------------------------------------


def dokuwiki_to_markdown(filepath, content):
    """Convert DokuWiki markup to GitHub-Flavored Markdown with Jekyll front matter.

    Args:
        filepath: the file path (e.g. "faq/index.md") — used to derive page title
                  and compute relative image paths
        content: raw DokuWiki markup string

    Returns:
        Markdown string with YAML front matter
    """
    lines = content.split("\n")
    title = _extract_title(lines)

    # Compute relative prefix to repo root for image paths.
    # e.g. "faq/index.md" → depth 1 → "../"
    #      "spec/css3-regions/index.md" → depth 2 → "../../"
    #      "index.md" → depth 0 → "./"
    parts = filepath.split("/")
    depth = len(parts) - 1  # subtract the filename itself
    if depth == 0:
        assets_prefix = "./"
    else:
        assets_prefix = "../" * depth

    body = _convert_body(lines, assets_prefix)

    # Build front matter
    title_escaped = title.replace('"', '\\"')
    front_matter = f'---\ntitle: "{title_escaped}"\n---\n\n'

    return front_matter + body


def _extract_title(lines):
    """Extract page title from the first DokuWiki heading."""
    for line in lines:
        m = re.match(r"^(={2,6})\s*(.+?)\s*=*\s*$", line)
        if m:
            return m.group(2).strip().rstrip("=").strip()
    return "Untitled"


def _convert_body(lines, assets_prefix="./"):
    """Convert DokuWiki body lines to Markdown."""
    result = []
    i = 0
    in_code = False
    code_lang = ""

    while i < len(lines):
        line = lines[i]

        # Code blocks: <code lang> ... </code>
        if not in_code:
            code_open = re.match(r"^(\s*)<code\s*(\w*)\s*>(.*)$", line, re.IGNORECASE)
            if code_open:
                in_code = True
                code_lang = code_open.group(2) or ""
                # Normalize language names
                lang_map = {"html4strict": "html", "html5": "html"}
                code_lang = lang_map.get(code_lang, code_lang)
                result.append(f"```{code_lang}")
                # Content on same line as <code>
                rest = code_open.group(3)
                if rest.rstrip().endswith("</code>"):
                    result.append(rest.rstrip().removesuffix("</code>"))
                    result.append("```")
                    in_code = False
                elif rest:
                    result.append(rest)
                i += 1
                continue

            # Also handle <file> blocks (DokuWiki downloadable code)
            file_open = re.match(
                r"^(\s*)<file\s*(\w*)\s*[^>]*>(.*)$", line, re.IGNORECASE
            )
            if file_open:
                in_code = True
                code_lang = file_open.group(2) or ""
                result.append(f"```{code_lang}")
                rest = file_open.group(3)
                if rest.rstrip().endswith("</file>"):
                    result.append(rest.rstrip().removesuffix("</file>"))
                    result.append("```")
                    in_code = False
                elif rest:
                    result.append(rest)
                i += 1
                continue

        if in_code:
            if re.search(r"</(?:code|file)>", line, re.IGNORECASE):
                content_before = re.sub(
                    r"\s*</(?:code|file)>.*$", "", line, flags=re.IGNORECASE
                )
                if content_before:
                    result.append(content_before)
                result.append("```")
                in_code = False
                i += 1
                continue
            result.append(line)
            i += 1
            continue

        # Headings: ====== H1 ====== to == H5 ==
        heading = re.match(r"^(={2,6})\s*(.+?)\s*=*\s*$", line)
        if heading:
            level = 7 - len(heading.group(1))  # ====== = H1, ===== = H2, etc.
            level = max(1, min(6, level))
            text = heading.group(2).strip().rstrip("=").strip()
            result.append(f"\n{'#' * level} {text}\n")
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^-{4,}\s*$", line):
            result.append("\n---\n")
            i += 1
            continue

        # Note blocks: <note>, <note warning>, <note important>, <note tip>
        note_open = re.match(r"^\s*<note\s*(\w*)\s*>(.*)$", line, re.IGNORECASE)
        if note_open:
            note_type = note_open.group(1) or "NOTE"
            note_type_map = {
                "": "NOTE",
                "warning": "WARNING",
                "important": "IMPORTANT",
                "tip": "TIP",
                "example": "NOTE",
            }
            gfm_type = note_type_map.get(note_type.lower(), "NOTE")
            # Collect note content
            note_lines = []
            rest = note_open.group(2)
            if rest.rstrip().endswith("</note>"):
                note_lines.append(rest.rstrip().removesuffix("</note>"))
            else:
                if rest.strip():
                    note_lines.append(rest)
                i += 1
                while i < len(lines):
                    if re.search(r"</note>", lines[i], re.IGNORECASE):
                        before = re.sub(
                            r"\s*</note>.*$", "", lines[i], flags=re.IGNORECASE
                        )
                        if before.strip():
                            note_lines.append(before)
                        break
                    note_lines.append(lines[i])
                    i += 1
            # Convert note content and format as GFM alert
            result.append(f"\n> [!{gfm_type}]")
            for nl in note_lines:
                converted = _convert_inline(nl.strip(), assets_prefix)
                if converted:
                    result.append(f"> {converted}")
                else:
                    result.append(">")
            result.append("")
            i += 1
            continue

        # Tables: ^ header ^ header ^ or | cell | cell |
        if re.match(r"^\s*[\^|]", line) and ("|" in line or "^" in line):
            table_lines = []
            while i < len(lines) and re.match(r"^\s*[\^|]", lines[i]):
                table_lines.append(lines[i])
                i += 1
            result.extend(_convert_table(table_lines, assets_prefix))
            continue

        # Definition lists: DokuWiki uses ; term : definition
        # or just indented text with ; and :
        defn = re.match(r"^\s*;\s*(.+?)\s*$", line)
        if defn:
            result.append(f"\n{_convert_inline(defn.group(1).strip(), assets_prefix)}")
            i += 1
            while i < len(lines) and re.match(r"^\s*:", lines[i]):
                dm = re.match(r"^\s*:\s*(.+)", lines[i])
                if dm:
                    result.append(
                        f": {_convert_inline(dm.group(1).strip(), assets_prefix)}"
                    )
                i += 1
            result.append("")
            continue

        # Unordered list items
        list_m = re.match(r"^(\s+)\*\s+(.*)", line)
        if list_m:
            indent_level = (len(list_m.group(1)) - 2) // 2
            indent = "  " * max(0, indent_level)
            result.append(
                f"{indent}- {_convert_inline(list_m.group(2), assets_prefix)}"
            )
            i += 1
            continue

        # Ordered list items
        olist_m = re.match(r"^(\s+)-\s+(.*)", line)
        if olist_m:
            indent_level = (len(olist_m.group(1)) - 2) // 2
            indent = "  " * max(0, indent_level)
            result.append(
                f"{indent}1. {_convert_inline(olist_m.group(2), assets_prefix)}"
            )
            i += 1
            continue

        # Regular text
        result.append(_convert_inline(line, assets_prefix))
        i += 1

    text = "\n".join(result)

    # Clean up excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Escape Liquid tags for Jekyll
    text = text.replace("{%", "{% raw %}{%{% endraw %}")
    text = text.replace("{{", "{% raw %}{{{% endraw %}")

    return text.strip() + "\n"


def _convert_inline(text, assets_prefix="./"):
    """Convert DokuWiki inline markup to Markdown."""
    # Bold: **text** -> **text** (same in both!)
    # Italic: //text// -> *text*
    text = re.sub(r"(?<![:/])//(.+?)//", r"*\1*", text)

    # Underline: __text__ -> <u>text</u> (no native MD equivalent)
    text = re.sub(r"__(.+?)__", r"<u>\1</u>", text)

    # Monospace: ''text'' -> `text`
    text = re.sub(r"''(.+?)''", r"`\1`", text)

    # Strikethrough: <del>text</del> -> ~~text~~
    text = re.sub(r"<del>(.*?)</del>", r"~~\1~~", text, flags=re.IGNORECASE)

    # Superscript: <sup>text</sup> (keep as-is, GFM supports it)
    # Subscript: <sub>text</sub> (keep as-is)

    # Nowiki: <nowiki>text</nowiki> -> `text`
    text = re.sub(r"<nowiki>(.*?)</nowiki>", r"`\1`", text, flags=re.IGNORECASE)

    # Internal links: [[page|text]] -> [text](page)
    # External links: [[url|text]] -> [text](url)
    text = _convert_links(text)

    # Images: {{url?size|alt}} -> ![alt](url)
    text = _convert_images(text, assets_prefix)

    # Line break: \\ at end of line -> <br>
    text = re.sub(r"\\\\\s*$", "  ", text)
    # Line break mid-line
    text = re.sub(r"\\\\(\s)", r"<br>\1", text)

    # DokuWiki smileys
    smiley_map = {
        "FIXME": "\U0001f6a7",
        "DELETEME": "\u274c",
    }
    for dw, emoji in smiley_map.items():
        text = text.replace(dw, emoji)

    return text


def _convert_links(text):
    """Convert DokuWiki links to Markdown links."""

    def replace_link(m):
        target = m.group(1)
        label = m.group(3) if m.group(3) else None

        # External URL
        if re.match(r"https?://", target):
            if label:
                return f"[{label}]({target})"
            return f"<{target}>"

        # Internal wiki link — convert namespace:page to /page/
        page_path = target.replace(":", "/").lstrip("/")
        display = label if label else page_path.split("/")[-1]
        return f"[{display}](/{page_path}/)"

    text = re.sub(r"\[\[([^\]|]+)(\|([^\]]*))?\]\]", replace_link, text)
    return text


def _convert_images(text, assets_prefix="./"):
    """Convert DokuWiki image syntax to Markdown."""

    def replace_image(m):
        inner = m.group(1)
        # Split on | for alt text
        parts = inner.split("|", 1)
        src = parts[0].strip()
        alt = parts[1].strip() if len(parts) > 1 else ""

        # Remove DokuWiki parameters (?200x100, ?200, ?nolink, ?direct, ?linkonly,
        # and & combinations like ?nolink&200)
        src = re.sub(r"\?[^|]*$", "", src)
        # Also strip leading colons/spaces
        src = src.lstrip(": ")

        # Check for ?linkonly (download link, not inline image)
        is_link = "linkonly" in inner

        # Convert wiki media paths
        if not re.match(r"https?://", src):
            media_path = src.replace(":", "/").lstrip("/")
            src = f"{assets_prefix}assets/images/{media_path}"

        if is_link:
            label = alt if alt else src.split("/")[-1]
            return f"[{label}]({src})"

        return f"![{alt}]({src})"

    # DokuWiki images: {{src|alt}} but NOT Liquid {{
    # Match {{ that isn't followed by % (Liquid) or another {
    text = re.sub(r"\{\{([^{}]+)\}\}", replace_image, text)
    return text


def _convert_table(table_lines, assets_prefix="./"):
    """Convert DokuWiki table lines to Markdown table."""
    rows = []
    has_header = False

    for line in table_lines:
        line = line.strip()
        if not line:
            continue

        # DokuWiki tables: ^ for header cells, | for regular cells
        # ^H1^H2^H3^ or |C1|C2|C3|
        is_header_row = line.startswith("^")
        if is_header_row:
            has_header = True

        # Split cells — handle both ^ and | as delimiters
        # Replace leading/trailing delimiters
        line = line.strip("^|").strip()

        # Split on ^ or |
        cells = re.split(r"\s*[\^|]\s*", line)
        cells = [_convert_inline(c.strip(), assets_prefix) for c in cells]

        rows.append((is_header_row, cells))

    if not rows:
        return []

    # Determine column count
    max_cols = max(len(r[1]) for r in rows)

    result = []
    header_emitted = False

    for is_header, cells in rows:
        # Pad cells
        while len(cells) < max_cols:
            cells.append("")

        row_str = "| " + " | ".join(cells) + " |"
        result.append(row_str)

        if is_header and not header_emitted:
            sep = "| " + " | ".join(["---"] * max_cols) + " |"
            result.append(sep)
            header_emitted = True

    # If no header row, insert separator after first row
    if not header_emitted and result:
        sep = "| " + " | ".join(["---"] * max_cols) + " |"
        result.insert(1, sep)

    result.insert(0, "")  # blank line before table
    result.append("")  # blank line after table
    return result


def page_id_to_filepath(page_id):
    """Convert a DokuWiki page ID (colon-separated) to a .txt filepath."""
    return page_id.replace(":", "/") + ".txt"


def page_id_to_fspath(page_id):
    """Convert a DokuWiki page ID to filesystem path segments (/ separated)."""
    return page_id.replace(":", "/")


def read_revisions(dump_dir):
    """Read all revisions from the DokuWiki meta/*.changes files.

    Returns a sorted list of revision dicts:
        {timestamp, page, author, summary, type}
    """
    meta_dir = dump_dir / "data" / "meta"
    revisions = []

    for changes_file in meta_dir.rglob("*.changes"):
        # Skip _comments.changes
        if changes_file.name == "_comments.changes":
            continue

        with open(changes_file, encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                fields = line.split("\t")
                if len(fields) < 6:
                    continue

                ts = int(fields[0])
                # fields[1] = IP
                edit_type = fields[2]
                page_id = fields[3]
                author = fields[4]
                summary = fields[5] if len(fields) > 5 else ""

                # Skip comment-related entries (cc, ec, dc)
                if edit_type not in ("C", "c", "E", "e", "R", "D"):
                    continue

                revisions.append(
                    {
                        "timestamp": ts,
                        "page": page_id,
                        "author": author,
                        "summary": summary,
                        "type": edit_type,
                    }
                )

    revisions.sort(key=lambda r: (r["timestamp"], r["page"]))
    return revisions


def get_revision_content(dump_dir, page_id, timestamp, is_latest):
    """Get the content for a specific page revision.

    For historical revisions, reads from data/attic/page.timestamp.txt.gz
    For the latest revision, reads from data/pages/page.txt
    """
    fs_page = page_id_to_fspath(page_id)

    if is_latest:
        current = dump_dir / "data" / "pages" / f"{fs_page}.txt"
        if current.exists():
            return current.read_text(encoding="utf-8", errors="replace")

    # Try attic (gzipped)
    attic = dump_dir / "data" / "attic" / f"{fs_page}.{timestamp}.txt.gz"
    if attic.exists():
        with gzip.open(attic, "rt", encoding="utf-8", errors="replace") as f:
            return f.read()

    return None


def read_acl(dump_dir):
    """Read the DokuWiki ACL file and return namespaces blocked from @ALL.

    DokuWiki ACL format: <page/namespace> <group> <permission>
    Permission 0 = no access. We look for lines that deny @ALL read access.
    Returns a list of page ID prefixes that are private.
    """
    acl_file = dump_dir / "conf" / "acl.auth.php"
    private_prefixes = []

    if not acl_file.exists():
        return private_prefixes

    with open(acl_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue

            target = parts[0]
            group = parts[1]
            perm = int(parts[2])

            # Check for @ALL with permission 0 (no access)
            if group == "@ALL" and perm == 0:
                # Normalize: "csswg:*" -> "csswg:", "csswg" -> "csswg"
                if target.endswith(":*"):
                    private_prefixes.append(target[:-1])  # "csswg:*" -> "csswg:"
                else:
                    private_prefixes.append(target)  # exact page

    return private_prefixes


def is_private(page_id, private_prefixes):
    """Check if a page ID falls under a private ACL prefix."""
    for prefix in private_prefixes:
        if prefix.endswith(":"):
            # Namespace wildcard: matches any page under this namespace
            if page_id.startswith(prefix) or page_id + ":" == prefix:
                return True
        else:
            # Exact page match
            if page_id == prefix:
                return True
    return False


def _meta_to_env(meta):
    """Convert a commit metadata dict to a GIT_* environment dict."""
    env = os.environ.copy()
    env_map = {
        "an": "GIT_AUTHOR_NAME",
        "ae": "GIT_AUTHOR_EMAIL",
        "ad": "GIT_AUTHOR_DATE",
        "cn": "GIT_COMMITTER_NAME",
        "ce": "GIT_COMMITTER_EMAIL",
        "cd": "GIT_COMMITTER_DATE",
    }
    for short, full in env_map.items():
        env[full] = meta[short]
    return env


def add_media_to_tree(dump_dir, base_tree):
    """Add all media files from DokuWiki dump to assets/images/ in a tree.

    Reads binary files from data/media/, hashes them as git blobs, and
    adds them to the index under assets/images/<path>.

    Returns a new tree hash.
    """
    media_dir = dump_dir / "data" / "media"
    if not media_dir.exists():
        return base_tree

    # Start from the base tree
    run_git(["read-tree", "--empty"])
    run_git(["read-tree", base_tree])

    add_lines = []
    media_count = 0

    for media_file in sorted(media_dir.rglob("*")):
        if not media_file.is_file():
            continue
        # Get path relative to data/media/
        rel_path = media_file.relative_to(media_dir)
        dest_path = f"assets/images/{rel_path}"

        # Hash the file as a git blob
        r = run_git(["hash-object", "-w", str(media_file.resolve())])
        blob_hash = r.stdout.strip()
        add_lines.append(f"100644 {blob_hash}\t{dest_path}")
        media_count += 1

    if add_lines:
        run_git(
            ["update-index", "--add", "--index-info"],
            input_data="\n".join(add_lines) + "\n",
        )

    print(f"      Added {media_count} media files to assets/images/")

    r = run_git(["write-tree"])
    return r.stdout.strip()


# ---------------------------------------------------------------------------
# Post-migration edit functions
# Each applies the semantic intent of a GitHub-side edit to our DokuWiki-
# derived Markdown files.  They mutate the working tree in place.
# ---------------------------------------------------------------------------


def _edit_cupertino_in_past():
    """Move Cupertino 2026 F2F from Upcoming to Past Meetings."""
    p = Path("planning/index.md")
    text = p.read_text()
    cupertino_re = re.compile(r"^- 2026-01-27.*Cupertino.*\n", re.MULTILINE)
    m = cupertino_re.search(text)
    if not m:
        return []
    cupertino_line = m.group(0).rstrip("\n")
    text = cupertino_re.sub("", text)
    text = text.replace(
        "## Past Meetings\n",
        "## Past Meetings\n\n### 2026\n\n" + cupertino_line + "\n",
    )
    p.write_text(text)
    return ["planning/index.md"]


def _edit_remove_registration_note():
    """Remove the spam-bots/registration note from index.md."""
    p = Path("index.md")
    text = p.read_text()
    text = re.sub(
        r"\n> \[!NOTE\]\n> Due to abuse by spam bots.*?\n\n",
        "\n",
        text,
        flags=re.DOTALL,
    )
    p.write_text(text)
    return ["index.md"]


def _edit_remove_recent_changes():
    """Remove the 'See recent changes' link from index.md."""
    p = Path("index.md")
    text = p.read_text()
    text = re.sub(
        r"\nSee \[recent changes\]\(http://wiki\.csswg\.org/\?do=recent\)"
        r" for currently active topics\.\n",
        "\n",
        text,
    )
    p.write_text(text)
    return ["index.md"]


def _edit_reorder_scribe_rota():
    """Reorder the scribe rota list to put fantasai first."""
    p = Path("planning/scribing/index.md")
    text = p.read_text()
    old_list = "1. JoshT\n1. kbabbitt\n1. TabAtkins\n1. ydaniv\n1. emilio\n1. fantasai"
    new_list = "1. fantasai\n1. JoshT\n1. kbabbitt\n1. TabAtkins\n1. ydaniv\n1. emilio"
    text = text.replace(old_list, new_list)
    p.write_text(text)
    return ["planning/scribing/index.md"]


def _edit_testing_links():
    """Update test suite link to wpt.fyi and test discussion to WPT GitHub."""
    p = Path("index.md")
    text = p.read_text()
    text = text.replace(
        "[conformance test suites](http://www.w3.org/Style/CSS/Test/)",
        "[conformance test suites](https://wpt.fyi/results/css)",
    )
    text = text.replace(
        "while discussion of our test suites happens on "
        "[public-css-testsuite](http://lists.w3.org/Archives/Public/"
        "public-css-testsuite/). "
        "If you are part of a W3C Member organization, you can also "
        "access our (mostly administrivial) "
        "[internal mailing list](http://lists.w3.org/Archives/Member/"
        "w3c-css-wg/).",
        "while maintenance of our test suites happens on "
        "[WPT GitHub](https://github.com/web-platform-tests/wpt/).",
    )
    p.write_text(text)
    return ["index.md"]


def _edit_contributing_and_coc():
    """Replace wiki contribution policy with Contributing/CoC links."""
    p = Path("index.md")
    text = p.read_text()
    text = text.replace(
        "Contributions to this wiki are governed by the same conditions "
        "as the [W3C Mobile Web Wiki Contribution Policy]"
        "(http://www.w3.org/Consortium/Legal/2006/07-incoming-wiki-"
        "copyright.html).",
        "Contributions to this wiki are governed by the "
        "[Contributor Guidelines](https://github.com/w3c/csswg-drafts/"
        "blob/main/CONTRIBUTING.md) and "
        "[Code of Conduct](https://github.com/w3c/csswg-drafts/"
        "blob/main/CODE_OF_CONDUCT.md).",
    )
    p.write_text(text)
    return ["index.md"]


def _edit_remove_test_mailing_list():
    """Remove the public-css-testsuite mailing list reference."""
    p = Path("test/index.md")
    text = p.read_text()
    text = text.replace(
        " The [public-css-testsuite mailing list]"
        "(http://lists.w3.org/Archives/Public/public-css-testsuite/) "
        "exists for CSS-specific discussion, excluding any policy matters "
        "around the repository, primarily tooling maintained by the CSS WG "
        "(i.e., the CSS testsuites' build system and the CSS test harness).",
        "",
    )
    p.write_text(text)
    return ["test/index.md"]


def _edit_remove_double_obsolete():
    """Remove the doubly-obsolete material from test/index.md."""
    p = Path("test/index.md")
    text = p.read_text()
    marker = "- Contributing a new test file: Ask in #css in W3C IRC"
    idx = text.find(marker)
    if idx >= 0:
        text = text[: idx + len(marker)] + "\n"
    p.write_text(text)
    return ["test/index.md"]


# Map each post-migration commit to the function that applies its intent.
# Order matters — they're applied sequentially.
POST_MIGRATION_EDITS = [
    ("c6feb9427", _edit_cupertino_in_past),
    ("fb5fa74ca", _edit_remove_registration_note),
    ("2306abe47", _edit_remove_recent_changes),
    ("a9433e5a1", _edit_reorder_scribe_rota),
    ("8040603ab", _edit_testing_links),
    ("b34c0c2b7", _edit_contributing_and_coc),
    ("6b80a5f98", _edit_remove_test_mailing_list),
    ("404588899", _edit_remove_double_obsolete),
]


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <dump_dir>")
        sys.exit(1)

    dump_dir = Path(sys.argv[1])
    if not (dump_dir / "data" / "meta").exists():
        print(f"Error: {dump_dir}/data/meta not found")
        sys.exit(1)

    repo_dir = Path("wiki-history")

    # Read ACL to identify private pages
    private_prefixes = read_acl(dump_dir)
    if private_prefixes:
        print("Private namespaces (excluded from history):")
        for p in private_prefixes:
            print(f"  {p}")

    print("\nReading DokuWiki revision history...")
    all_revisions = read_revisions(dump_dir)
    print(f"  {len(all_revisions)} total revisions")

    # Filter out private pages
    revisions = [
        r for r in all_revisions if not is_private(r["page"], private_prefixes)
    ]
    excluded = len(all_revisions) - len(revisions)
    print(f"  {excluded} revisions excluded (private pages)")
    print(f"  {len(revisions)} revisions to replay")

    # Determine the latest revision for each page (to know when to read
    # from pages/ instead of attic/)
    latest_ts = {}
    for rev in revisions:
        page = rev["page"]
        if rev["type"] != "D":
            if page not in latest_ts or rev["timestamp"] > latest_ts[page]:
                latest_ts[page] = rev["timestamp"]

    # Initialize repo
    repo_dir.mkdir(parents=True, exist_ok=True)
    if (repo_dir / ".git").exists():
        print(f"  Removing existing wiki-history repo...")
        import shutil

        shutil.rmtree(repo_dir)
        repo_dir.mkdir()

    run_git(["init"], cwd=repo_dir)
    print(f"  Initialized {repo_dir}")

    # Track which pages currently exist in the repo (for deletes)
    existing_pages = set()

    committed = 0
    skipped = 0
    missing = 0
    deleted = 0
    total = len(revisions)

    for i, rev in enumerate(revisions):
        page = rev["page"]
        ts = rev["timestamp"]
        author = rev["author"]
        summary = rev["summary"]
        edit_type = rev["type"]

        filepath = page_id_to_filepath(page)

        if edit_type == "D":
            # Delete the page
            dest = repo_dir / filepath
            if dest.exists():
                dest.unlink()
                run_git(["add", filepath], cwd=repo_dir)

                result = run_git(["diff", "--cached", "--quiet"], cwd=repo_dir)
                if result.returncode != 0:
                    commit_msg = (
                        f"{page.replace(':', '/')}: {summary}"
                        if summary
                        else f"{page.replace(':', '/')}: deleted"
                    )

                    author_name, author_email = resolve_author(
                        author if author else "127.0.0.1"
                    )
                    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
                    env = make_author_env(author_name, author_email, dt.isoformat())
                    run_git(["commit", "-m", commit_msg], cwd=repo_dir, env=env)
                    committed += 1
                    deleted += 1
            continue

        # C, c, E, e, R — all need content
        is_latest = ts == latest_ts.get(page)
        content = get_revision_content(dump_dir, page, ts, is_latest)

        if content is None:
            missing += 1
            continue

        # Write file
        dest = repo_dir / filepath
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        existing_pages.add(page)

        # Stage
        run_git(["add", filepath], cwd=repo_dir)

        # Check for actual changes
        result = run_git(["diff", "--cached", "--quiet"], cwd=repo_dir)
        if result.returncode == 0:
            skipped += 1
            continue

        # Build commit message
        page_path = page.replace(":", "/")
        if summary:
            commit_msg = f"{page_path}: {summary}"
        else:
            commit_msg = f"{page_path}: edited"

        author_name, author_email = resolve_author(author if author else "127.0.0.1")
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        env = make_author_env(author_name, author_email, dt.isoformat())
        run_git(["commit", "-m", commit_msg], cwd=repo_dir, env=env)
        committed += 1

        if (committed % 500 == 0) or committed == 1:
            print(f"  [{committed}] {dt.strftime('%Y-%m-%d')} {author}: {page_path}")

    print(
        f"\n  Wiki history: {committed} commits "
        f"({skipped} skipped, {missing} missing content, {deleted} deletes)"
    )

    # Get the wiki tip
    wiki_tip = run_git(["rev-parse", "HEAD"], cwd=repo_dir).stdout.strip()
    print(f"  Wiki tip: {wiki_tip[:12]}")

    print("\nGrafting wiki history and inserting rename + conversion commits...")

    # Fetch wiki-history into the main repo
    r = run_git(["remote", "get-url", "wiki-history"])
    if r.returncode != 0:
        run_git(["remote", "add", "wiki-history", str(repo_dir.resolve())])
    else:
        run_git(["remote", "set-url", "wiki-history", str(repo_dir.resolve())])
    run_git(["fetch", "wiki-history"])
    wiki_tip_main = run_git(["rev-parse", "wiki-history/main"]).stdout.strip()

    # Get list of .txt files at wiki tip
    r = run_git(["ls-tree", "--name-only", "-r", wiki_tip_main])
    txt_files = [f for f in r.stdout.strip().split("\n") if f.endswith(".txt")]
    print(f"  {len(txt_files)} wiki .txt files at tip")

    # -----------------------------------------------------------------------
    # Rename step A: foo.txt -> foo/index.txt  (restructure into directories)
    # -----------------------------------------------------------------------
    restructure = []
    for txt in txt_files:
        base = txt.removesuffix(".txt")
        new = "index.txt" if base == "main" else f"{base}/index.txt"
        restructure.append((txt, new))

    # -----------------------------------------------------------------------
    # Rename step B: foo/index.txt -> foo/index.md  (skip .html — not needed)
    # -----------------------------------------------------------------------
    to_md = [(new, new.removesuffix(".txt") + ".md") for _, new in restructure]

    print(f"  Renames: {len(restructure)} restructure, {len(to_md)} .txt->.md")

    # Get metadata for synthetic commits from the original Jekyll conversion
    jekyll_meta = get_commit_meta(JEKYLL_CONVERT)
    jekyll_env = _meta_to_env(jekyll_meta)

    # Build the new commit chain
    print("  Building commit chain...")

    # A: Restructure foo.txt -> foo/index.txt
    tree_a = build_tree_with_renames(wiki_tip_main, restructure)
    commit_a = commit_tree(
        tree_a,
        wiki_tip_main,
        "Restructure wiki pages into directory layout\n\n"
        "Move flat DokuWiki .txt files into directory/index.txt paths.",
        jekyll_env,
    )
    print(f"    A (restructure): {commit_a[:12]}")

    # B: Rename .txt -> .md (pure rename for git log --follow)
    tree_b = build_tree_with_renames(commit_a, to_md)
    commit_b = commit_tree(
        tree_b,
        commit_a,
        "Rename wiki source files to Markdown extension\n\n"
        "Prepare for DokuWiki-to-Markdown content conversion.",
        jekyll_env,
    )
    print(f"    B (.txt->.md): {commit_b[:12]}")

    # C: Convert DokuWiki markup to Markdown + add media + add infrastructure
    print("    Converting DokuWiki markup to Markdown...")

    # Convert all .md files from DokuWiki syntax to Markdown
    all_md = [(md, md) for _, md in to_md]  # same path in, same path out
    tree_c = build_tree_with_conversions(
        commit_b,
        all_md,
        lambda path, content: dokuwiki_to_markdown(path, content),
    )

    # Add media files from DokuWiki dump
    tree_c = add_media_to_tree(dump_dir, tree_c)

    # Overlay infrastructure files from origin/main tip
    # (things like _config.yml, _layouts/, .github/, README.md, assets/*.js, etc.)
    run_git(["read-tree", "--empty"])
    run_git(["read-tree", tree_c])
    r_infra = run_git(["ls-tree", "-r", INFRA_SOURCE])
    infra_lines = []
    for line in r_infra.stdout.strip().split("\n"):
        if not line:
            continue
        meta, path = line.split("\t", 1)
        # Skip page content files — we have our own converted versions
        if path.endswith("/index.md") or path == "index.md":
            continue
        # Skip media images — we added them from the DokuWiki dump (which is
        # a superset of what origin/main had)
        if path.startswith("assets/images/"):
            continue
        # Everything else is infrastructure: add to tree
        parts = meta.split()
        infra_lines.append(f"{parts[0]} {parts[2]}\t{path}")
    if infra_lines:
        run_git(
            ["update-index", "--add", "--index-info"],
            input_data="\n".join(infra_lines) + "\n",
        )
    r_tree_c2 = run_git(["write-tree"])
    tree_c_final = r_tree_c2.stdout.strip()

    commit_c = commit_tree(
        tree_c_final,
        commit_b,
        "Convert to Jekyll with Markdown source files\n\n"
        "Convert DokuWiki markup to GitHub-Flavored Markdown with Jekyll\n"
        "front matter. Add wiki media files and Jekyll site infrastructure.",
        jekyll_env,
    )
    print(f"    C (convert to Jekyll): {commit_c[:12]}")

    # -----------------------------------------------------------------------
    # Apply post-migration edits
    # These are genuine content edits made on the GitHub repo after the wiki
    # was frozen.  Because the scraped-HTML-derived Markdown differs from our
    # DokuWiki-derived Markdown, git cherry-pick can't apply the patches.
    # Instead we apply the *spirit* of each edit programmatically.
    # -----------------------------------------------------------------------
    print("  Applying post-migration edits...")

    # Point HEAD/main at our conversion commit and check out the working tree.
    run_git(["checkout", "main"])
    run_git(["reset", "--hard", commit_c])

    applied = 0
    for ref, edit_fn in POST_MIGRATION_EDITS:
        meta = get_commit_meta(ref)
        env = _meta_to_env(meta)
        msg_line = meta["msg"].split("\n")[0][:60]

        changed_files = edit_fn()  # mutate working-tree files

        if changed_files:
            run_git(["add"] + changed_files)
        result = run_git(["diff", "--cached", "--quiet"])
        if result.returncode != 0:
            run_git(["commit", "-m", meta["msg"]], env=env)
            applied += 1
            print(f"    {msg_line}")
        else:
            print(f"    {msg_line} (no changes)")

    print(f"  Applied {applied} post-migration commits")

    total_commits = run_git(["rev-list", "--count", "HEAD"]).stdout.strip()
    print(f"\nDone! Total commits: {total_commits}")


if __name__ == "__main__":
    main()
