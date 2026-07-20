"""Build PDF for Huang response v2.2."""
import re, subprocess, os, fitz

os.chdir(r'C:\Users\LENOVO\projects\huang-2025-quantum-advantage-audit\papers')

with open('qc-advantage-keynotes-v2.2.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'keywords:\n(?:  - .+\n)+', '', content)

with open('build.md', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(
    ['pandoc', 'build.md', '-o', 'qc-advantage-keynotes-v2.2.pdf',
     '--pdf-engine=xelatex', '--metadata', 'date=2026-07-20'],
    capture_output=True, text=True
)

if result.returncode == 0:
    os.remove('build.md')
    doc = fitz.open('qc-advantage-keynotes-v2.2.pdf')
    size = os.path.getsize('qc-advantage-keynotes-v2.2.pdf') / 1024
    errors = [p.number for p in doc if '\ufffd' in p.get_text()]
    status = 'CLEAN' if not errors else f'BLOCKED: pages {errors}'
    print(f'OK: {len(doc)} pages, {size:.0f} KB, {status}')
else:
    print('PDF FAILED')
    print(result.stderr[:500])
