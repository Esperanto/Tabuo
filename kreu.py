# -*- coding: utf-8 -*-

import yaml
import jinja2

# ŝarĝu kartojn
kartoj = yaml.load(file('enhavo/kartoj.yml', 'r'))
# aldonu la indeksojn
for i in range(0, len(kartoj)):
    kartoj[i]['indekso'] = i + 1


# Kreu printeblan HTML-on enhavantan po 9 kartojn por paĝo.
def eligu_9_por_pagxo(kartoj):

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

    rendered = env.get_template('9_por_pagxo.html').render(
        pagxoj = pagxoj
    )

    with open('eligo/9_por_pagxo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

# Kreu printeblan HTML-on enhavantan po 1 karton por paĝo.
# (Eblas decidi ĉe la print-dialogo, kiom da kartoj oni volas havi sur ĉiu printita paĝo.)
def eligu_1_por_pagxo(kartoj):

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader = jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('1_por_pagxo.html').render(
        kartoj = kartoj
    )

    with open('eligo/1_por_pagxo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

eligu_1_por_pagxo(kartoj)
eligu_9_por_pagxo(kartoj)
