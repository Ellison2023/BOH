from testcases.bbb import TestAutoApi


class AutoTest:
    def mi(self, keys):
        token = {keys}
        print(token)


if __name__ == '__main__':
    keys_value = TestAutoApi().keys()   # 获取 keys 的值
    AutoTest().mi(keys_value)   # 将 keys 的值传递给 mi 方法
    # print(AutoTest().mi(keys_value))