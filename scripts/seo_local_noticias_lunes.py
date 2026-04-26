import feedparser
import json
from datetime import datetime
from pathlib import Path

def obtener_noticias_seo_local():
    """
    Recopila noticias de SEO Local de fuentes RSS gratuitas
    Retorna: lista de noticias con título, enlace y fuente
    """
    
    feeds_seo_local = {
        'Search Engine Roundtable - Local': 'https://www.seroundtable.com/rss.xml',
        'Search Engine Journal': 'https://www.searchenginejournal.com/feed/',
        'Local Search Forum': 'https://www.seroundtable.com/rss.xml',
        'Bright Local Blog': 'https://www.brightlocal.com/feed/',
        'Google Business Profile News': 'https://support.google.com/business/feed/feed.xml',
    }
    
    noticias_seo_local = []
    limite_por_feed = 3
    
    print("\n" + "="*60)
    print("📍 RECOPILANDO NOTICIAS DE SEO LOCAL...")
    print("="*60 + "\n")
    
    for nombre_fuente, url_feed in feeds_seo_local.items():
        try:
            print(f"📡 Leyendo: {nombre_fuente}...")
            feed = feedparser.parse(url_feed)
            
            for entry in feed.entries[:limite_por_feed]:
                noticia = {
                    'fuente': nombre_fuente,
                    'titulo': entry.get('title', 'Sin título'),
                    'enlace': entry.get('link', ''),
                    'fecha': entry.get('published', datetime.now().isoformat()),
                    'categoria': 'SEO Local'
                }
                noticias_seo_local.append(noticia)
                print(f"   ✓ {noticia['titulo'][:50]}...")
                
        except Exception as e:
            print(f"   ⚠️ Error al leer {nombre_fuente}: {str(e)}")
    
    print(f"\n✅ Total de noticias de SEO Local: {len(noticias_seo_local)}")
    return noticias_seo_local

if __name__ == "__main__":
    noticias = obtener_noticias_seo_local()
    
    output_path = Path('noticias_seo_local_lunes.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(noticias, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Noticias guardadas en: {output_path}")
