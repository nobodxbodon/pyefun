import unittest

from .timeUtil import *
from .timeBase import *
from .systemProcessingBase import *


class TestTimeUtil(unittest.TestCase):

    def test_1(self):
        # with 计时器() as t:
        #     延时(1)
        # print(t.取耗时())

        t = 时间统计()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        t.开始()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())

        t = 计时器()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())
        t.开始()
        延时(1.22)
        print(t.取秒())
        print(t.取毫秒())

    def test_2(self):
        for _ in 计时统计(num=1000, verbose=3):
            math.factorial(10000)

    def test_3(self):
        t1 = 计时统计(次数=100, 标签="运行", 取样=20, 显示信息=3, 单位='ms')
        for timer in t1:
            setup_vars = 10000
            with timer:
                延时(0.01 + 取随机数(1, 2)/100)
                math.factorial(setup_vars)
        print('总耗时 = %r' % (t1.取耗时(),))
