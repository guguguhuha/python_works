# -*- coding:utf-8 -*-
"""
启动文件入口
"""

import os
import sys

sys.path.append(
    os.path.dirname(__file__)
)

if __name__ == "__main__":
    from core import src

    src.run()
