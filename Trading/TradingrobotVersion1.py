import pandas as pd
import pandas_ta as ta

# Beispiel: Daten einlesen (CSV mit 'close'-Preisen)
df = pd.read_csv('preisdaten.csv')
df['sma_200'] = ta.sma(df['close'], length=200)
df['rsi_10'] = ta.rsi(df['close'], length=10)

# Signal-Generierung
df['signal'] = 0
df.loc[df['rsi_10'] < 30, 'signal'] = 1   # Kaufen (Long)
df.loc[df['rsi_10'] > 70, 'signal'] = -1  # Verkaufen (Short)

# Beispielhafte Orderausführung
for index, row in df.iterrows():
    if row['signal'] == 1:
        print(f"{index}: Kaufsignal {row['close']}")
    elif row['signal'] == -1:
        print(f"{index}: Verkaufssignal {row['close']}")

# Risk-Management und Exit-Regeln können etwa auf Stop-Loss/Take-Profit oder Rückkehr zum Mittelwert basieren.
