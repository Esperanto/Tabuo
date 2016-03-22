# -*- coding: utf-8 -*-

import yaml
import jinja2

# ŝarĝu kartojn
kartoj = yaml.load(file('enhavo/kartoj.yml', 'r'))
# aldonu la indeksojn
for i in range(0, len(kartoj)):
    kartoj[i]['indekso'] = i + 1


# Kreu printebla HTML enhavanta po 9 kartojn por paĝo.
def eligu_9_po_pagxo(kartoj):

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

    rendered = env.get_template('9_po_pagxo.html').render(
        pagxoj = pagxoj
    )

    with open('eligo/9_po_pagxo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

# Kreu printebla HTML enhavanta po 1 kartojn por paĝo.
# (Eblas decidi ĉe la print-dialogo, kiom da kartoj oni volas havi po printita paĝo.)
def eligu_1_po_pagxo(kartoj):

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader = jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('1_po_pagxo.html').render(
        kartoj = kartoj
    )

    with open('eligo/1_po_pagxo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

eligu_1_po_pagxo(kartoj)
eligu_9_po_pagxo(kartoj)
