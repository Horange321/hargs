# hargutil
A tool for dealing args.
Read [Chinese version](./README-zh.md) if possible.\
请尽可能看[中文版本](./README-zh.md)。

## Install
The package can be installed through pip (this is the recommended method)\
`pip install hargs`\
Or downloading the release from [Pypi](https://pypi.org/project/hargs/) or Github

## Usage
### New
First, create a `Hargs` class:\
`hargs = Hargs(sys.argv)`

### Hargs.add()
To add some switches, use function `Hargs.add(short:str, long:str, map: str)`\
Args instructions:\
`short` like `-o=output.txt`\
`long` like `--input-file=input.txt`\
`map` For convincing of using. Depend by yourself.\
Example:
```python
hargs.add('v', 'version', 'v') \
    .add('f', 'file', 'f') \
    .add('o', 'output', 'o') \
    .add('', 'force', 'ff') \
#   ... ...
```
It's worth noticing that `short` and `long` can't be `''` at the same time.\
`map` can't be `''`

### Hargs.to_dict()
Then `hargs` can be transformed into `dict`:\
`hargs = hargs.to_dict()`\
Example:\
`./hargs.py -v -o=output.txt --force` will turn into
```python
{
    'v': '',
    'f': None,
    'o': 'output.txt',
    'ff': ''
}
```
