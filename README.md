### 解包 JS Eval 混淆过的代码

你可能会见过这种代码
```js
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1 0="2**3 4 5!";6.7(0);',8,8,'i_say|var|f|k|you|Idiot|console|log'.split('|'),0,{}))
```
嗯，它们是被混淆（或是加密？）过的。它的正真结构类似于这种Python代码：
```python
>>>
>>> (lambda p,a,c,k,e,d: print(p,a,c,k,e,d))('H', 'E', 'L', 'L', 'O', '!')
H E L L O !
>>>
```

嗯，因为我不想用Python通过某些包执行JS代码，所以用Python写了一个这样的解包代码。

### 怎么使用呢？
以上面举例的JS Eval代码为例，首先手动取出 `('1 0="2**3 4 5!";6.7(0);',8,8,'i_say|var|f|k|you|Idiot|console|log'.split('|'),0,{})` 这部分，即参数部分。
> 然后
```python
from eval_unpack import eval_unpack
raw_code = eval_unpack('1 0="2**3 4 5!";6.7(0);',8,8,'i_say|var|f|k|you|Idiot|console|log'.split('|'),0,{})
print(raw_code)
```
> 输出结果为
```js
var i_say="f**k you Idiot!";console.log(i_say);
```

## 更新
現在可以自動的解包了，但是請自行注意一些代碼安全問題。
```python
from eval_unpack import unpack
demo_eval = """eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1 0="2**3 4 5!";6.7(0);',8,8,'i_say|var|f|k|you|Idiot|console|log'.split('|'),0,{}))"""
# 輸出解包后的JS代碼
print (unpack(demo_eval))
```

结束。
