#!/usr/bin/env python3
import sys
import json
from datetime import datetime
from pathlib import Path

print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")

try:
    import feedparser
    print("✅ feedparser importado correctamente")
except ImportError as e:
    print(f"❌ Error importando feedparser: {e}")
    sys.exit(1)

def obtener_todas_noticias():
    """Recopila noticias de todas las categorías"""
    
    feeds = {
        'IA': {
            'The Verge - AI': 'https://www.theverge.com/ai-artificial-intelligence/feed/index.xml',
            'TechCrunch': 'https://feeds.techcrunch.com/TechCrunch/',
            'Hacker News': 'https://news.ycombinator.com/rss',
        },
        'SEO': {
            'Search Engine Roundtable': 'https://www.seroundtable.com/rss.xml',
            'Search Engine Journal': 'https://www.searchenginejournal.com/feed/',
            'Moz Blog': 'https://moz.com/blog/feed',
        },
        'SEO Local': {
            'Bright Local': 'https://www.brightlocal.com/feed/',
            'Google Business': 'https://support.google.com/business/feed/feed.xml',
        },
        'Marketing Digital': {
            'HubSpot Blog': 'https://blog.hubspot.com/marketing/feed',
            'Neil Patel': 'https://neilpatel.com/blog/feed/',
        }
    }
    
    todas_noticias = {}
    
    print("\n" + "="*70)
    print("🚀 RECOPILANDO NOTICIAS PARA LINKEDIN")
    print("="*70 + "\n")
    
    for categoria, fuentes in feeds.items():
        todas_noticias[categoria] = []
        print(f"\n📍 Categoría: {categoria}")
        print("-" * 70)
        
        for nombre_fuente, url_feed in fuentes.items():
            try:
                print(f"   📡 Leyendo: {nombre_fuente}...", end=" ")
                feed = feedparser.parse(url_feed)
                
                count = 0
                for entry in feed.entries[:2]:
                    noticia = {
                        'titulo': entry.get('title', 'Sin título'),
                        'enlace': entry.get('link', ''),
                        'fuente': nombre_fuente,
                        'fecha': entry.get('published', datetime.now().isoformat()),
                        'categoria': categoria
                    }
                    todas_noticias[categoria].append(noticia)
                    count += 1
                
                print(f"✓ ({count} noticias)")
                    
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    # Crear JSON final
    datos_finales = {
        'fecha_generacion': datetime.now().isoformat(),
        'dia_ejecucion': 'Lunes 9:00 AM',
        'noticias_por_categoria': todas_noticias,
        'total_noticias': sum(len(v) for v in todas_noticias.values()),
        'categorias': list(todas_noticias.keys())
    }
    
    return datos_finales

if __name__ == "__main__":
    try:
        print("\n🚀 Iniciando recopilación de noticias...")
        noticias = obtener_todas_noticias()
        
        print(f"\n📊 Total de noticias: {noticias['total_noticias']}")
        
        # Guardar JSON
        output_path = Path('../noticias_lunes.json')
        print(f"\n📁 Guardando en: {output_path}")
        print(f"📁 Ruta absoluta: {output_path.absolute()}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(noticias, f, indent=2, ensure_ascii=False)
        
        print(f"✅ ÉXITO: Archivo guardado correctamente")
        print(f"📊 Noticias generadas: {noticias['total_noticias']}")
        
    except Exception as e:
        print(f"\n❌ ERROR FATAL: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
