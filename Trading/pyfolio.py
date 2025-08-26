pip install pyfolio-reloaded

import pyfolio as pf

perf_stats = pf.from_zipline_csv("backtest_results.csv")
pf.create_full_tear_sheet(perf_stats)

pf.create_full_tear_sheet(zipline_results['returns'])
