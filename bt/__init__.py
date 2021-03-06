import core
import algos
import backtest

from .backtest import Backtest, run
from .core import Strategy, Algo, AlgoStack

import ffn
from ffn import utils, data, get, merge

__version__ = (0, 1, 9)
