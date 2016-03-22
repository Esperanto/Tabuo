# -*- coding: utf-8 -*-

import yaml
import jinja2

def sxargxu():

    kartoj = yaml.load(file('enhavo/kartoj.yml', 'r'))
    return kartoj


def eligu(kartoj):

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader=jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('kartoj.html').render(
      kartoj = kartoj
    )

    with open('eligo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))

def eligu_a4(kartoj):

    env = jinja2.Environment()
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.loader=jinja2.FileSystemLoader('sxablonoj/')

    rendered = env.get_template('a4.html').render(
      kartoj = kartoj
    )

    with open('eligo.html', 'w') as f:
        f.write(rendered.encode('utf-8'))


kartoj = sxargxu()
#eligu(kartoj)
eligu_a4(kartoj)
