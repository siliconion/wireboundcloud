Colletion of patterns and anti-patterns

## return booleans
```
if condition:
    return True
else:
    return False
```

This should be optimized to
```
return condition
```


## early return
```
if condition1:
    if condition2:
        return do_A()
else:
    return do_B()
```

This should be optimized to 
```
if not condtion1:
    return do_B()
if condition2:
    return do_A()
```

## 
