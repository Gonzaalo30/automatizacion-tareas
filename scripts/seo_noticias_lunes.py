import feedparser
import json
from datetime import datetime
from pathlib import Path

def obtener_noticias_seo():
    """
    Recopila noticias de SEO de fuentes RSS gratuitas
    Retorna: lista de noticias con título, enlace y fuente
    """
    
    feeds_seo = {
        'Search Engine Roundtable': 'https://www.seroundtable.com/rss.xml',
        'Search Engine Journal': 'https://www.searchenginejournal.com/feed/',
        'Moz Blog': 'https://moz.com/blog/feed',
        'SEO by the Sea': 'https://www.seobythesea.com/feed/',
        'Google Search Central': 'https://developers.google.com/search/feeds/feed.xml',
    }
    
    noticias_seo = []
    limite_por_feed = 3
    
    print("\n" + "="*60)
    print("🔍 RECOPILANDO NOTICIAS DE SEO...")
    print("="*60 + "\n")
    
    for nombre_fuente, url_feed in feeds_seo.items():
        try:
            print(f"📡 Leyendo: {nombre_fuente}...")
            feed = feedparser.parse(url_feed)
            
            for entry in feed.entries[:limite_por_feed]:
                noticia = {
                    'fuente': nombre_fuente,
                    'titulo': entry.get('title', 'Sin título'),
                    'enlace': entry.get('link', ''),
                    'fecha': entry.get('published', datetime.now().isoformat()),
                    'categoria': 'SEO'
                }
                noticias_seo.append(noticia)
                print(f"   ✓ {noticia['titulo'][:50]}...")
                
        except Exception as e:
            print(f"   ⚠️ Error al leer {nombre_fuente}: {str(e)}")
    
    print(f"\n✅ Total de noticias de SEO: {len(noticias_seo)}")
    return noticias_seo

if __name__ == "__main__":
    noticias = obtener_noticias_seo()
    
    output_path = Path('noticias_seo_lunes.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(noticias, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Noticias guardadas en: {output_path}")
