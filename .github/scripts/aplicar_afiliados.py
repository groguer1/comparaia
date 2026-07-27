import json, os, re

MAPA = {}
if os.path.exists('afiliados.json'):
    MAPA = json.load(open('afiliados.json', encoding='utf-8')).get('enlaces', {})

AVISO_AFF = 'Enlaces de afiliado: si te registras a traves de ellos podemos ganar una comision, sin coste adicional para ti. No influye en nuestro veredicto'
AVISO_NEUTRO = 'Enlaces a las webs oficiales de cada herramienta. Ninguna marca paga por aparecer ni influye en nuestro veredicto'

cambios = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(root, fn)
        t = open(p, encoding='utf-8', errors='ignore').read()
        orig = t
        for clave, url in MAPA.items():
            patron = r'(<a\s[^>]*data-aff="' + re.escape(clave) + r'"[^>]*)'
            def sustituir(m):
                etiqueta = m.group(1)
                return re.sub(r'href="[^"]*"', 'href="' + url + '"', etiqueta)
            t = re.sub(patron, sustituir, t)
            patron2 = r'(<a\s[^>]*?)(href="[^"]*")([^>]*data-aff="' + re.escape(clave) + r'")'
            t = re.sub(patron2, lambda m: m.group(1) + 'href="' + url + '"' + m.group(3), t)
        tiene_aff = any(u in t for u in MAPA.values()) if MAPA else False
        if tiene_aff:
            t = t.replace(AVISO_NEUTRO, AVISO_AFF)
        else:
            t = t.replace(AVISO_AFF, AVISO_NEUTRO)
            t = t.replace('Enlaces de afiliado: si te registras a traves de ellos podemos ganar una comision, sin coste adicional para ti. No influye en nuestro veredicto', AVISO_NEUTRO)
        if t != orig:
            open(p, 'w', encoding='utf-8').write(t)
            cambios += 1

print('Archivos actualizados:', cambios)
print('Programas en el mapa:', len(MAPA))
