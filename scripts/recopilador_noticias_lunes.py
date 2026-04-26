#!/usr/bin/env python3
import sys
print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")
MAESTRO DE NOTICIAS PARA LINKEDIN
Recopila noticias de IA, SEO, SEO Local y Marketing Digital
Las combina en un único JSON que será leído por Claude para crear posts
"""

import feedparser
import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def obtener_todas_noticias():
    """
    Recopila noticias de todas las categorías
    Prioriza: Si no hay SEO, agrega más IA
    """
    
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
            'SEO by the Sea': 'https://www.seobythesea.com/feed/',
        },
        'SEO Local': {
            'Search Engine Roundtable': 'https://www.seroundtable.com/rss.xml',
            'Bright Local': 'https://www.brightlocal.com/feed/',
            'Google Business': 'https://support.google.com/business/feed/feed.xml',
        },
        'Marketing Digital': {
            'HubSpot Blog': 'https://blog.hubspot.com/marketing/feed',
            'Neil Patel': 'https://neilpatel.com/blog/feed/',
            'Copyblogger': 'https://www.copyblogger.com/feed/',
        }
    }
    
    todas_noticias = defaultdict(list)
    limite_por_feed = 2
    
    print("\n" + "="*70)
    print("🚀 RECOPILANDO NOTICIAS PARA LINKEDIN (Lunes 9:00 AM)")
    print("="*70 + "\n")
    
    for categoria, fuentes in feeds.items():
        print(f"\n📍 Categoría: {categoria}")
        print("-" * 70)
        
        for nombre_fuente, url_feed in fuentes.items():
            try:
                feed = feedparser.parse(url_feed)
                
                for entry in feed.entries[:limite_por_feed]:
                    noticia = {
                        'titulo': entry.get('title', 'Sin título'),
                        'enlace': entry.get('link', ''),
                        'fuente': nombre_fuente,
                        'fecha': entry.get('published', datetime.now().isoformat()),
                        'categoria': categoria
                    }
                    todas_noticias[categoria].append(noticia)
                    print(f"   ✓ {noticia['titulo'][:60]}...")
                    
            except Exception as e:
                print(f"   ⚠️ Error en {nombre_fuente}: {str(e)}")
    
    # Lógica: Si SEO está vacío, agregar más IA
    if not todas_noticias.get('SEO'):
        print("\n⚠️  No hay noticias de SEO. Agregando más de IA...")
        # Intenta buscar más en feeds de IA
        feed_extra = feedparser.parse('https://www.seroundtable.com/rss.xml')
        for entry in feed_extra.entries[2:5]:
            noticia = {
                'titulo': entry.get('title', 'Sin título'),
                'enlace': entry.get('link', ''),
                'fuente': 'Search Engine Roundtable',
                'fecha': entry.get('published', datetime.now().isoformat()),
                'categoria': 'IA'
            }
            todas_noticias['IA'].append(noticia)
    
    # Crear JSON final
    datos_finales = {
        'fecha_generacion': datetime.now().isoformat(),
        'dia_ejecucion': 'Lunes 9:00 AM',
        'noticias_por_categoria': dict(todas_noticias),
        'total_noticias': sum(len(v) for v in todas_noticias.values()),
        'categorias': list(todas_noticias.keys())
    }
    
    return datos_finales

if __name__ == "__main__":
    noticias = obtener_todas_noticias()
    
    # Guardar JSON
    output_path = Path('../noticias_lunes.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(noticias, f, indent=2, ensure_ascii=False)
    
    print("\n" + "="*70)
    print(f"✅ ÉXITO: {noticias['total_noticias']} noticias guardadas")
    print(f"📁 Archivo: {output_path}")
    print(f"📅 Fecha: {noticias['fecha_generacion']}")
    print("="*70 + "\n")
