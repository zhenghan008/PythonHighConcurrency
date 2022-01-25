from typing import Generator


# 生成数据的生成器
def gen_data(r: int = 100000000, _s: int = 100000) -> Generator:
    """
    :param _s: size个数
    :param r: 生成的最大数
    :return: s个数的列表
    """

    size = 0
    channel = []
    for i in range(r):
        if size < _s:
            channel.append(i)
            size += 1
        else:
            yield channel
            size = 0
            channel = []
    if channel:
        yield channel


# 处理数据的生成器
def handle_data() -> Generator:
    for each_data in gen_data():
        yield [each + 1 for each in each_data]


def main():
    for i in handle_data():
        print(i)


if __name__ == '__main__':
    main()
