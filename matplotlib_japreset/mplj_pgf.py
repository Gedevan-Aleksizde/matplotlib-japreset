#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
from matplotlib import rcParams
from .search import find_font

# PGF mode
f = find_font()
# TODO: TeX がインストールされてるかチェック, なければ警告する機能
rcParams.update(matplotlib.rcParamsDefault)
rcParams['pgf.texsystem'] = 'xelatex'
rcParams['font.family'] = f
rcParams["mathtext.fontset"] = 'cm'  # TODO: 数式フォントまで勝手に変えるのは蛇足か?
# TODO: 主要な拡張数式パッケージは全部カバーできているか?
rcParams['pgf.preamble'] =  r'\usepackage{amsmath,amssymb,mathrsfs,cancel,esint,mathdots,mathtools}\usepackage{metalogo}'
matplotlib.use('pgf')
print('matplotlib-japreset PGF mode')
print(f'font: {f}')