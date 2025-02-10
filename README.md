# Jane-Street-Real-Time-Market-Data-Forecasting

the dataset consists of timeseries data with 79 anonymized features and 9 responders, derived from real market data. The task is to forecast responder_6 for up to six months.

Train Data: Historical data partitioned into ten parts, with columns for date_id, time_id, symbolid, 79 feature{00...78} columns, and 9 responder_{0...8} columns. Test Data: A mock test set structured similarly to the training data, provided in batches via an evaluation API. Lags: Previous day’s responder values, available at the first time_id of each new day.

For this EDA and Statistical analysis i will only be considering the last partition, which might contain more recent data that may align better with the patterns in the unseen test set.