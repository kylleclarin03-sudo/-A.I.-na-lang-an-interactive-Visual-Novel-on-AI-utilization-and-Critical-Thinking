import re, glob, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = ['chapter2.rpy','chapter4.rpy','chapter5.rpy','chapter6.rpy','chapter8.rpy']

for fn in files:
    path = fn
    txt = open(path, encoding='utf-8').read()
    original = txt
    # Replace professors at center with enter_center_rise
    txt = re.sub(r'show (mr_earns|ms_iva) (normal|disappointed) at center with dissolve',
                 r'show \1 \2 at enter_center_rise', txt)
    if txt != original:
        open(path, 'w', encoding='utf-8').write(txt)
        print('Fixed:', fn)
    else:
        print('No changes needed:', fn)