#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import numpy as np
from my_solution import solution


# 测试用例
def test_solution():
    # 正确答案
    correct_solution = np.array([[0.2781110610248023],
                        [0.3245470683213672],
                        [0.155697200935541],
                        [0.24164466971828993]])
    # 程序求解结果
    result, _ = solution()
    assert (correct_solution == result).all()

