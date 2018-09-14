import re

dictPseudoState = dict()


def extract_pseudo_state(fline):
    m_obj = re.search(r':[a-zA-Z]+$', fline)
    if m_obj:
        dictPseudoState[m_obj.group(0)] = fline


fstyle = open('style.qss', encoding='utf-8')

for line in fstyle:
    extract_pseudo_state(line)

fstyle.close()

fPseudoState = open('pseudoState.qss', 'w')

for (key, val) in dictPseudoState.items():
    fPseudoState.writelines(key + ' =====> ' + val)

fPseudoState.close()
