# -*- coding: utf-8 -*-

import yaml
import jinja2

# ŝarĝu kartojn
kartoj = yaml.load(file('enhavo/kartoj.yml', 'r'))
# aldonu la indeksojn
for i in range(0, len(kartoj)):
    kartoj[i]['indekso'] = i + 1


# kreu 'kartoj.html'-dosieron (printebla HTML enhavanta po 9 kartojn por paĝo)
def eligu_html(kartoj):

    # kreu liston, en kiu la anoj estas grupitaj per specifa nombro
    def grupigu(listo, nombro):
        grupoj = []
        i = 0;
        while i < len(listo):
            sublisto = []
            for j in range(0, nombro):
                if i < len(listo):
                    sublisto.append(listo[i])
                i += 1
            grupoj.append(sublisto)
        return grupoj

    linioj = grupigu(kartoj, 3)
    pagxoj = grupigu(linioj, 3)

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader = jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('kartoj.html').render(
        pagxoj = pagxoj
    )

    with open('eligo/kartoj.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

# kreu 'a4.html'-dosieron (ĉiu karto estas unu A4-paĝo)
def eligu_a4(kartoj):

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader = jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('a4.html').render(
        kartoj = kartoj
    )

    with open('eligo/a4.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

eligu_html(kartoj)
eligu_a4(kartoj)
