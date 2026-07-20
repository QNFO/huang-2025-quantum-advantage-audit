"""Build PDF with Unicode→LaTeX math conversion for XeLaTeX compatibility."""
import re, subprocess, os, fitz

os.chdir(r'C:\Users\LENOVO\projects\huang-2025-quantum-advantage-audit\papers')

with open('qc-advantage-keynotes-v2.2.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Strip keywords YAML block (causes \xmpquote error)
content = re.sub(r'keywords:\n(?:  - .+\n)+', '', content)

# Unicode→LaTeX math conversions (only outside existing math)
# Greek letters
content = content.replace('α', '$\\alpha$')
content = content.replace('ω', '$\\omega$')  
content = content.replace('φ', '$\\phi$')
content = content.replace('π', '$\\pi$')
content = content.replace('ℚ', '$\\mathbb{Q}$')
content = content.replace('ℝ', '$\\mathbb{R}$')
content = content.replace('ℂ', '$\\mathbb{C}$')

# Special symbols
content = content.replace('⊗', '$\\otimes$')
content = content.replace('×', '$\\times$')
content = content.replace('≈', '$\\approx$')
content = content.replace('⟨', '$\\langle$')
content = content.replace('⟩', '$\\rangle$')
content = content.replace('≥', '$\\ge$')
content = content.replace('≤', '$\\le$')  # if present

# Subscript digits — handle patterns like ω₀₁, α, |0⟩
# Subscript 0-9
sub_map = {'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9'}
for sub, digit in sub_map.items():
    content = content.replace(sub, '_{' + digit + '}')

# Superscript digits
sup_map = {'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'}
for sup, digit in sup_map.items():
    content = content.replace(sup, '^{' + digit + '}')

# Bra-ket notation: |0⟩ → $|0\\rangle$  |1⟩ → $|1\\rangle$   |2⟩ → $|2\\rangle$
content = re.sub(r'\|0([0-9]*)\⟩', r'$|0\1\\rangle$', content)
content = re.sub(r'\|([0-9]+)\⟩', r'$|\1\\rangle$', content)
content = re.sub(r'\⟨([0-9]+)\|', r'$\\langle\1|$', content)

# Fix: remove stray standalone $ from mapping conflicts  
# Also fix E_J/EC → $E_J/E_C$ etc
content = re.sub(r'E_J', '$E_J$', content)
content = re.sub(r'E_C', '$E_C$', content)

# Fix: ~ followed by number → $\sim$
content = re.sub(r'~(\d)', r'$\\sim$\1', content)

with open('build.md', 'w', encoding='utf-8') as f:
    f.write(content)

result = subprocess.run(
    ['pandoc', 'build.md', '-o', 'qc-advantage-keynotes-v2.2-fixed.pdf',
     '--pdf-engine=xelatex', '--metadata', 'date=2026-07-20'],
    capture_output=True, text=True
)

if result.returncode == 0:
    os.remove('build.md')
    doc = fitz.open('qc-advantage-keynotes-v2.2-fixed.pdf')
    size = os.path.getsize('qc-advantage-keynotes-v2.2-fixed.pdf') / 1024
    errors = [p.number for p in doc if '\ufffd' in p.get_text()]
    if not errors:
        # Replace the original PDF
        os.replace('qc-advantage-keynotes-v2.2-fixed.pdf', 'qc-advantage-keynotes-v2.2.pdf')
        print(f'OK: {len(doc)} pages, {size:.0f} KB, RENDERING CLEAN')
    else:
        print(f'WARNING: {len(doc)} pages, {size:.0f} KB, replacement chars on pages: {errors}')
else:
    print('PDF FAILED')
    print(result.stderr[:1000])
