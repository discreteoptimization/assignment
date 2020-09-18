>>> Path = namedtuple("Path", ['x1', 'x2', 'x3', 'x4'])
>>> paths=[]
>>> for i in range (0,16):
...     path = f"{i:b}".zfill(len(f"{16-1:b}"))
...     paths.append(Path(int(path[0]), int(path[1]), int(path[2]), int(path[3])))
...
>>> print(paths)
