from zipline.api import order_target_percent, record, symbol
from zipline import run_algorithm
import pandas as pd
from datetime import datetime
import pytz

def initialize(context):
    context.asset = symbol('AAPL')
    context.window_length = 20  # Tagen für den Mean
    context.threshold = 2  # Standardabweichungen für Extrem
    context.size = 0.5  # Positionsgröße

def handle_data(context, data):
    # Historische Preise abrufen
    hist = data.history(context.asset, 'price', bar_count=context.window_length, frequency="1d")
    mean = hist.mean()
    std = hist.std()
    price = data.current(context.asset, 'price')

    # Mean-Reversion-Bedingungen
    if price > mean + context.threshold * std:
        # Zu hoch: Short
        order_target_percent(context.asset, -context.size)
    elif price < mean - context.threshold * std:
        # Zu niedrig: Long
        order_target_percent(context.asset, context.size)
    else:
        # Keine Position
        order_target_percent(context.asset, 0)

    record(price=price, mean=mean)

# Backtest-Konfiguration
start = pd.Timestamp('2020-01-01', tz=pytz.UTC)
end = pd.Timestamp('2022-01-01', tz=pytz.UTC)

run_algorithm(
    start=start,
    end=end,
    initialize=initialize,
    capital_base=10000,
    handle_data=handle_data,
    data_frequency='daily',
    bundle='quantopian-quandl'  # Beispiel-Bundle
)

# Optional: Ergebnisse visualisieren und analysieren
