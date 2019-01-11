# Esperanta Tabuo

Tiu deponejo enhavas esperantlingvajn ludkartojn por la divenludo *Tabuo*.

## Ludo enrete

Ebligas ludi per saĝtelefono / platkompulito. Simpla versio, montras nur la kartojn:

- http://tabuo.esperanto.com

## Uzado

Printu la dosierojn en `eligo`. Elektu ĉu vi volas

- la dosieron [1 por paĝo](eligo/1_por_pagxo.html): Tie vi povos agordi en la printdialogo kiom da kartoj vi efektive volas sur 1 printita paĝo.
- la dosieron [9 por paĝo](eligo/9_por_pagxo.html): Tie vi printos 9 kartoj sur 1 printita paĝo.

## Kreo novajn ludkartojn

### Postuloj

- Python, kun
  - yaml
  - jinja2

### Kreado

1. Aldonu liniojn en [`enhavo/kartoj.yml`](enhavo/kartoj.yml) laŭ la formo de la ekzistantaj linioj.
1. Voku `$ python kreu.py`. La dosieroj en `eligo` aktualiĝos.


