# hargs
处理命令行参数的工具
## 用法
### New
首先，创建一个 `Hargs` 对象，并且设置一些参数，例如：\
`hargs = Hargs(sys.argv)`

### Hargs.add()
加入参数映射，使用函数`Hargs.add(short:str, long:str, map: str)`\
参数说明：\
`short` 短参数，类似 `-o=output.txt`\
`long` 长参数，类似 `--input-file=input.txt`\
`map` 映射值，为方便调用，随便取。\
举例：
```python
hargs.add('v', 'version', 'v') \
    .add('f', 'file', 'f') \
    .add('o', 'output', 'o') \
    .add('', 'force', 'ff') \
#   ... ...
```
值得注意的是：短参数和长参数不能同时为`''`，映射值不能为`''`

### Hargs.to_dict()
此时可将`hargs`转为`dict`\
`args = hargs.do_dict()`\
例如：\
`./hargs.py -v -o=output.txt --force` 将会变成
```python
{
    'v': '',
    'f': None,
    'o': 'output.txt',
    'ff': ''
}
```