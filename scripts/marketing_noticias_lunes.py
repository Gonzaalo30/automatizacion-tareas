import feedparser
import json
from datetime import datetime
from pathlib import Path

def obtener_noticias_marketing_digital():
    """
    Recopila noticias de Marketing Digital de fuentes RSS gratuitas
    Retorna: lista de noticias con título, enlace y fuente
    """
    
    feeds_marketing = {
        'HubSpot Blog': 'https://blog.hubspot.com/marketing/feed',
        'Neil Patel': 'https://neilpatel.com/blog/feed/',
        'Copyblogger': 'https://www.copyblogger.com/feed/',
        'Content Marketing Institute': 'https://contentmarketinginstitute.com/feed/',
        'Hootsuite Blog': 'https://blog.hootsuite.com/feed/',
    }
    
    noticias_marketing = []
    limite_por_feed = 3
    
    print("\n" + "="*60)
    print("📊 RECOPILANDO NOTICIAS DE MARKETING DIGITAL...")
    print("="*60 + "\n")
    
    for nombre_fuente, url_feed in feeds_marketing.items():
        try:
            print(f"📡 Leyendo: {nombre_fuente}...")
            feed = feedparser.parse(url_feed)
            
            for entry in feed.entries[:limite_por_feed]:
                noticia = {
                    'fuente': nombre_fuente,
                    'titulo': entry.get('title', 'Sin título'),
                    'enlace': entry.get('link', ''),
                    'fecha': entry.get('published', datetime.now().isoformat()),
                    'categoria': 'Marketing Digital'
                }
                noticias_marketing.append(noticia)
                print(f"   ✓ {noticia['titulo'][:50]}...")
                
        except Exception as e:
            print(f"   ⚠️ Error al leer {nombre_fuente}: {str(e)}")
    
    print(f"\n✅ Total de noticias de Marketing Digital: {len(noticias_marketing)}")
    return noticias_marketing

if __name__ == "__main__":
    noticias = obtener_noticias_marketing_digital()
    
    output_path = Path('noticias_marketing_lunes.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(noticias, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Noticias guardadas en: {output_path}")
