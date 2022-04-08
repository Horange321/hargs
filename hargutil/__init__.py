class Hargs:
    ver = "Python v1.1.3"

    def __init__(self, args: list):
        """
        :param args: sys.argv
        """
        self.__args = args
        self.__ys = {}

    def __startwith(self, x: str, y: str) -> bool:
        """
        Whether the beginning of x is y.
        """
        if len(x) < len(y):
            return False
        for i in range(len(y)):
            if x[i] != y[i]:
                return False
        return True

    def add(self, s: str, l: str, m: str):
        """
        Add  map.
        添加映射
        :param s: short 短参数
        :param l: long 长参数
        :param m: map 映射
        """
        if m == "":
            raise ArgumentError("map can't be empty.")

        if s == "" and l == "":
            raise ArgumentError("s & l can't be empty at the same time")
        self.__ys[m] = (s, l)
        return self

    def to_dict(self):
        r = {}

        for i in self.__ys.keys():
            # 如没有该开关，就为None. 当下面找到该开关时，就被赋值
            r[i] = None
            for j in self.__args:
                # 如果没有参数
                i1 = f"-{self.__ys[i][0]}="
                i2 = f"--{self.__ys[i][1]}="
                j = j + '=' if j[-1] != '=' else j

                if self.__startwith(j, i1) or self.__startwith(j, i2):
                    try:
                        r[i] = j.split("=")[1]
                    except IndexError:
                        # 没有参数
                        r[i] = ''
                    break

        return r


class ArgumentError(Exception):
    pass
