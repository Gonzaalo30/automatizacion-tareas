import feedparser
import json
from datetime import datetime
from pathlib import Path

def obtener_noticias_ia():
    """
    Recopila noticias de IA de fuentes RSS gratuitas
    Retorna: lista de noticias con título, enlace y fuente
    """
    
    feeds_ia = {
        'The Verge - AI': 'https://www.theverge.com/ai-artificial-intelligence/feed/index.xml',
        'TechCrunch - AI': 'https://feeds.techcrunch.com/TechCrunch/',
        'Hacker News': 'https://news.ycombinator.com/rss',
        'OpenAI Blog': 'https://openai.com/blog/feed/',
        'Anthropic Insights': 'https://www.anthropic.com/news',
    }
    
    noticias_ia = []
    limite_por_feed = 3
    
    print("\n" + "="*60)
    print("🤖 RECOPILANDO NOTICIAS DE IA...")
    print("="*60 + "\n")
    
    for nombre_fuente, url_feed in feeds_ia.items():
        try:
            print(f"📡 Leyendo: {nombre_fuente}...")
            feed = feedparser.parse(url_feed)
            
            for entry in feed.entries[:limite_por_feed]:
                noticia = {
                    'fuente': nombre_fuente,
                    'titulo': entry.get('title', 'Sin título'),
                    'enlace': entry.get('link', ''),
                    'fecha': entry.get('published', datetime.now().isoformat()),
                    'categoria': 'IA'
                }
                noticias_ia.append(noticia)
                print(f"   ✓ {noticia['titulo'][:50]}...")
                
        except Exception as e:
            print(f"   ⚠️ Error al leer {nombre_fuente}: {str(e)}")
    
    print(f"\n✅ Total de noticias de IA: {len(noticias_ia)}")
    return noticias_ia

if __name__ == "__main__":
    noticias = obtener_noticias_ia()
    
    output_path = Path('noticias_ia_lunes.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(noticias, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Noticias guardadas en: {output_path}")


