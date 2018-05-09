import re
import sys
import tempfile
import importlib
from os.path import *


def base10_2_n_string(d, n):
    s, t = "", d
    if t == 0: return "0"
    while t > 0:
        v = t % n
        s += (chr(v + 87), str(v))[v <= 9]
        t = int(t / n)
    return s[::-1]


def eval_unpack(p, a, c, k, e, d):
    def e(c):
        c = int(c)
        if c < a:
            pad = ''
        else:
            pad = e(c/a)
        c = c % a
        if c > 35:
            return pad + chr(c + 29)
        else:
            return pad + base10_2_n_string(c, 36)

    while c:
        c -= 1
        d[e(c)] = k[c] or e(c)

    return re.sub("\w+", lambda e: d.get(e.group()) or e.group(), p)


def get_unpack_args_from_eval_str(data):
    tf = tempfile.TemporaryFile(prefix="unpack", suffix=".py", delete=False)
    tf.file.write(("v = %s" % data).encode())
    tf.close()
    
    imp_name = splitext(basename(tf.name))[0]
    sys.path.append(tempfile.gettempdir())
    m = importlib.import_module(imp_name)
    return m.v


def unpack(eval_text):
    text = re.search("return.*?}(\(.*\))\)", eval_text)
    v = get_unpack_args_from_eval_str(text.group(1))
    return eval_unpack(*v)


if __name__ == "__main__":
    demo_eval = """eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1 0="2**3 4 5!";6.7(0);',8,8,'i_say|var|f|k|you|Idiot|console|log'.split('|'),0,{}))"""
    print (unpack(demo_eval))
