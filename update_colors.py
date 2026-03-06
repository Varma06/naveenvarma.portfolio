import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_replacements = [
    ('slate-', 'zinc-'),
    ('indigo-', 'teal-'),
    ('purple-', 'rose-'),
    ('blue-', 'emerald-'),
    ('cyan-', 'emerald-'),
    ('tranzinc-', 'translate-'),
]

css_replacements = [
    # Hex Colors
    ('#4F46E5', '#14b8a6'), # indigo-600 to teal-500
    ('#A855F7', '#f43f5e'), # purple-500 to rose-500
    ('#06B6D4', '#10b981'), # cyan-500 to emerald-500
    ('#0F172A', '#09090b'), # slate-900 to zinc-950
    ('#1E293B', '#18181b'), # slate-800 to zinc-900
    ('#334155', '#27272a'), # slate-700 to zinc-800
    ('#1A0F3F', '#1c1917'), # dark purple bg to dark stone
    ('#A78BFA', '#5eead4'), # purple-400 to teal-300
    
    # Hex variations (lowercase)
    ('#4f46e5', '#14b8a6'),
    ('#a855f7', '#f43f5e'),
    ('#06b6d4', '#10b981'),
    ('#0f172a', '#09090b'),
    ('#1e293b', '#18181b'),
    ('#334155', '#27272a'),
    ('#1a0f3f', '#1c1917'),
    ('#a78bfa', '#5eead4'),

    # RGBs
    ('79, 70, 229', '20, 184, 166'), # indigo
    ('168, 85, 247', '244, 63, 94'), # purple
    ('6, 182, 212', '16, 185, 129'), # cyan
]

base_dir = r'c:\Users\varma\OneDrive\Desktop\Portfolio'
replace_in_file(os.path.join(base_dir, 'templates', 'index.html'), html_replacements)
replace_in_file(os.path.join(base_dir, 'templates', 'base.html'), html_replacements)
replace_in_file(os.path.join(base_dir, 'static', 'css', 'style.css'), css_replacements)

print("Color theme successfully updated in HTML and CSS files.")
