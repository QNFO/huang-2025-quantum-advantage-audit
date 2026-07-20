import fitz, os
os.chdir(r'C:\Users\LENOVO\projects\huang-2025-quantum-advantage-audit\papers')
d = fitz.open('out.pdf')
s = os.path.getsize('out.pdf') / 1024
e = sum(1 for p in d if '\ufffd' in p.get_text())
print(f'{len(d)}pp, {s:.0f}KB, {"CLEAN" if e == 0 else f"BLOCKED:{e}"}')
