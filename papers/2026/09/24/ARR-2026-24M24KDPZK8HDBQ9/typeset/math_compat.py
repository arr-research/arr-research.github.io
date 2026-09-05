"""Compatibility normalization from the preceding manuscript typesetter."""
import re

def clean_math(s):
    s=s.replace(r"\boxed", "")
    s=s.replace(r"\pmod L", r"\ (\mathrm{mod}\ L)")
    s=re.sub(r"\\(?:tfrac|dfrac|frac)([0-9])([0-9])",r"\\frac{\1}{\2}",s)
    s=s.replace(r"\tfrac",r"\frac").replace(r"\dfrac",r"\frac")
    s=re.sub(r"\\(?:big|Big|bigg|Bigg)[lr]?", "",s)
    s=re.sub(r"\\(mathbb|mathcal)\s+([A-Za-z])",r"\\\1{\2}",s)
    # Expand TeX's legal single-token fraction arguments for Mathtext.
    def argument(source,start):
        while source[start].isspace():
            start+=1
        if source[start]=="{":
            depth=1; end=start+1
            while depth:
                depth+=(source[end]=="{")-(source[end]=="}"); end+=1
            return source[start:end],end
        if source[start]=="\\":
            match=re.match(r"\\[A-Za-z]+|\\.",source[start:])
            end=start+len(match[0])
        else:
            end=start+1
        return "{"+source[start:end]+"}",end
    out=""; pos=0
    while True:
        start=s.find(r"\frac",pos)
        if start<0:
            out+=s[pos:]; break
        first,end=argument(s,start+5)
        second,end=argument(s,end)
        out+=s[pos:start]+r"\frac"+first+second; pos=end
    s=out
    return " ".join(s.split())

