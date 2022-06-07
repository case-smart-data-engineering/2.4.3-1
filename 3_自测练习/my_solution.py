#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

#PageRank算法可对所有网页进行重要性排序、实现对网页链接流行度的评估，一个网页的PageRank值越高，代表其链接流行度越高。

import numpy as np

def get_page_rank(IOS, alpha, max_itrs, min_delta):
    """
    :param IOS: 表示网页之间的链接关系的矩阵，值为1表示有链接，0表示无链接
    :param alpha: 阻尼系数
    :max_itrs: 最大迭代数
    :min_delta: 停止迭代时的误差阈值
    """
    PR = [] #记录PageRank值
    times = 0 #记录迭代次数
    N = np.shape(IOS)[0]    # 记录网页数行数
    e = np.ones(shape=(N, 1))   # 创建一个N行1列的全1矩阵
    L = [np.count_nonzero(e) for e in IOS.T]    # 计算每个网页的入度
    # 
    def helps_efunc(ios, l):
        return ios / l

    helps_func = np.frompyfunc(helps_efunc, 2, 1)   # 创建一个函数，用于计算网页的转移矩阵
    helpS = helps_func(IOS, L)  # 计算网页的转移矩阵
    # 计算一般转移矩阵
    A = alpha * helpS + ((1 - alpha) / N) * np.dot(e, e.T)
    raise NotImplementedError('编写使用幂法计算网页的PageRank，并返回最终PageRank值和最终迭代次数。')


# 待测试程序
def solution():
    IOS = np.array([[0, 1, 0, 1], [1, 0, 1, 1], \
        [1, 0, 0, 0], [0, 1, 1, 0]],dtype=float)    # 记录网页链出矩阵

    # 阻尼系数
    alpha = 0.85
    # 最大迭代次数
    max_itrs = 100
    # 停止迭代时的误差阈值
    min_delta = 0.0001

    pr, times = get_page_rank(IOS, alpha, max_itrs, min_delta)
    return pr, times


if __name__ == '__main__':
    pass
