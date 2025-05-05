Erstelle bitte einen Trading-Bot in Python, der abhängig von Chartentwicklung selbstständig Kauf und Verkauf tätigt.

Hier ist ein Beispiel für einen Trading-Bot, der auf Basis gleitender Durchschnitte automatisiert handelt:

```python
import pandas as pd

def trading_bot(prices, window_short=5, window_long=20):
    df = pd.DataFrame(prices, columns=['Close'])
    
    # Berechnung der gleitenden Durchschnitte
    df['SMA_short'] = df['Close'].rolling(window=window_short).mean()
    df['SMA_long'] = df['Close'].rolling(window=window_long).mean()
    
    # Signalgenerierung
    df['Signal'] = 'Hold'
    golden_cross = (df['SMA_short'] > df['SMA_long']) & (df['SMA_short'].shift(1) <= df['SMA_long'].shift(1))
    death_cross = (df['SMA_short'] < df['SMA_long']) & (df['SMA_short'].shift(1) >= df['SMA_long'].shift(1))
    
    df.loc[golden_cross, 'Signal'] = 'Buy'
    df.loc[death_cross, 'Signal'] = 'Sell'
    
    return df[['Close', 'SMA_short', 'SMA_long', 'Signal']]
```

**Funktionsweise des Bots:**
1. Berechnet zwei gleitende Durchschnitte (kurz- und langfristig)
2. Generiert Kaufsignale bei "Golden Cross" (kurzer Durchschnitt kreuzt über langen)
3. Generiert Verkaufssignale bei "Death Cross" (kurzer Durchschnitt kreuzt unter langen)
4. Gibt klare Handelsempfehlungen aus

**Anwendungsbeispiel:**
```python
# Historische Preisdaten (Beispiel)
data = [100, 102, 105, 107, 110, 108, 112, 115, 118, 120, 
        119, 117, 115, 113, 110, 108, 105, 103, 101, 100]

result = trading_bot(data)
print(result.tail(10))
```

**Erweiterungsmöglichkeiten:**
1. Kombination mit weiteren Indikatoren (RSI, MACD)
2. Risikomanagement durch Stop-Loss Orders
3. Volumenanalyse zur Bestätigung von Signalen
4. Backtesting-Funktionalität zur Strategieoptimierung

**Wichtige Hinweise:**
- Dieser Bot dient nur als Beispielbasis
- Echte Handelsentscheidungen erfordern zusätzliche Analysen
- Historische Performance garantiert keine zukünftigen Ergebnisse
- Orderausführung würde zusätzliche Schnittstellen benötigen (z.B. Broker-API)

Für die praktische Anwendung sollten Sie:
1. Echtzeitdatenintegration implementieren
2. Transaktionskosten berücksichtigen
3. Ein Risikomanagement-System einbauen
4. Die Strategie mit historischen Daten backtesten

