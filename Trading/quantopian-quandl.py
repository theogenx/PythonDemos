from zipline import run_algorithm

result = run_algorithm(
    ...,
    bundle='quantopian-quandl'
)

from zipline.data.bundles import load
import os

bundle_data = load('quantopian-quandl', os.environ, None)
