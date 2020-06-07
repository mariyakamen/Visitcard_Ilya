proj_name = "Visitcard_Ilya"

with open(f"src/web/{proj_name}.html") as f:
    html = f.read()

with open(f"src/web/{proj_name}.css") as f:
    css = f.read()

with open(f"src/web/{proj_name}.js") as f:
    js = f.read()


css_tag = f"<style>{css}</style>"
js_tag = f"<script>{js}</script>"

from bs4 import BeautifulSoup

bs = BeautifulSoup(html, features="html.parser")
bs.head.insert(0, BeautifulSoup(css_tag, features="html.parser") )
# bs.body.insert(0, BeautifulSoup(js_tag, features="html.parser") )
blob = str(bs)
