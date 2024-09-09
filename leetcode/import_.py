import bisect
import collections
from typing import Optional
from contextlib import contextmanager
import copy
import gc
from heapq import *
from bisect import bisect_right
from bisect import bisect_left
from itertools import pairwise
from collections import Counter, namedtuple
import itertools
import functools
from functools import cache
import math
import operator
import sys
from typing import List
from typing import Iterable, Protocol
import subprocess
from enum import Enum
from collections.abc import Sequence
from math import inf

from io import StringIO  
from unittest import mock

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def gen_tree(arr):
    def gen(arr, i):
        if i < len(arr):
            tn = TreeNode(arr[i]) if arr[i] is not None else None
            if tn is not None:
                tn.left = gen(arr, 2 * i + 1)
                tn.right = gen(arr, 2 * i + 2)
            return tn
    return gen(arr, 0)