# noinspection PyUnresolvedReferences
from .. import *
from .. import dispatch as dispatch_original
from ..shape import dispatch_unwrap_dimensions
from ..types import Number, TorchNumeric

dispatch = dispatch_unwrap_dimensions(dispatch_original)

from typing import Union

Numeric = Union[Number, TorchNumeric]

from plum import clear_all_cache as _clear_all_cache

import torch  # Load `torch` to load all new types.

# noinspection PyUnresolvedReferences
from .generic import *
from .linear_algebra import *
from .random import *
from .shaping import *

# Clear cache to make sure that all newly loaded types are available.
_clear_all_cache()

# Alias to actual module.
sys.modules[__name__] = B
