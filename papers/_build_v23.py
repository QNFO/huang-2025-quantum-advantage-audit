"""Build PDF v2.3 — handle YAML frontmatter separately from body."""
import re, subprocess, os, fitz

os.chdir(r'C:\Users\LENOVO\projects\huang-2025-quantum-advantage-audit\papers')

with open('qc-advantage-keynotes-v2.3.md', 'r', encoding='utf-8') as f:
    raw = f.read()

# Split off YAML frontmatter (between first two '---')
parts = raw.split('---', 2)
if len(parts) < 3:
    print('ERROR: Cannot split YAML frontmatter')
    exit(1)

yaml_header = parts[1]
body = parts[2]

# Strip keywords from YAML header
yaml_header = re.sub(r'\nkeywords:\n(?:  - .+\n)+', '', yaml_header)

# === Math protection: save existing $$...$$ and $...$ blocks in body ===
math_blocks = []
def save_math(m):
    math_blocks.append(m.group(0))
    return f'<<<MATH{len(math_blocks)-1}>>>'
body = re.sub(r'\$\$[^$]+\$\$', save_math, body)
body = re.sub(r'\$[^$]+\$', save_math, body)

# === Unicode→LaTeX on body ===

# Greek
for uni, latex in {'α':'\\alpha','ω':'\\omega','φ':'\\phi','π':'\\pi',
    'ε':'\\varepsilon','ψ':'\\psi','σ':'\\sigma','ℏ':'\\hbar',
    'ℚ':'\\mathbb{Q}','ℝ':'\\mathbb{R}','ℂ':'\\mathbb{C}','ℤ':'\\mathbb{Z}'}.items():
    body = body.replace(uni, '$' + latex + '$')

# Symbols
for uni, latex in {'⊗':'\\otimes','×':'\\times','≈':'\\approx',
    '≥':'\\ge','≤':'\\le','⟨':'\\langle','⟩':'\\rangle',
    '∝':'\\propto','→':'\\to','Φ':'\\Phi','Σ':'\\Sigma'}.items():
    body = body.replace(uni, '$' + latex + '$')

body = body.replace('−', '-')

# Sub/superscript digits
for sub, d in {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9'}.items():
    body = body.replace(sub, '_{' + d + '}')
for sup, d in {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'}.items():
    body = body.replace(sup, '^{' + d + '}')

# cos → \cos (only if not already in math)
body = body.replace('cos ', '$\\cos$ ')

# Restore math blocks
for i, block in enumerate(math_blocks):
    body = body.replace(f'<<<MATH{i}>>>', block)

# Reassemble
content = '---' + yaml_header + '---' + body

with open('build.md', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(
    ['pandoc', 'build.md', '-o', 'out.pdf',
     '--pdf-engine=xelatex', '--metadata', 'date=2026-07-20'],
    capture_output=True, text=True
)

if result.returncode == 0:
    os.remove('build.md')
    doc = fitz.open('out.pdf')
    size = os.path.getsize('out.pdf') / 1024
    errors = [p.number for p in doc if '\ufffd' in p.get_text()]
    if not errors:
        os.replace('out.pdf', 'qc-advantage-keynotes-v2.3.pdf')
        print(f'OK: {len(doc)} pages, {size:.0f} KB, CLEAN')
    else:
        for pn in errors[:3]:
            for line in doc[pn].get_text().split('\n'):
                if '\ufffd' in line:
                    print(f'ERROR p{pn}: {line.strip()[:120]}')
                    break
else:
    print('PDF FAILED')
    print(result.stderr[:800])
