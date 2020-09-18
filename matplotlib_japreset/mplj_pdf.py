#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
from matplotlib import rcParams
from .search import find_font

# PDF mode
# PNG とかもこれでOK
f = find_font()
rcParams.update(matplotlib.rcParamsDefault)
rcParams['font.family'] = f
rcParams['pdf.fonttype'] = 42
matplotlib.use('pdf')

print('matplotlib-japreset PDF mode')
print(f'font: {f}')