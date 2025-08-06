# dividend-portfolio-tracker

Dividend Portfolio Tracker

## Implementation Plan

1. **Project setup**
   - Create a Python virtual environment and install dependencies (`pandas`, `yfinance`, `SQLAlchemy`, `fastapi` or `streamlit`, `matplotlib/plotly`).
   - Initialize a package structure with models, services, importers, and a UI or API layer.

2. **Data model & storage**
   - Use SQLite through SQLAlchemy.
   - Define models for transactions, holdings, and dividends.

3. **CSV import module**
   - Parse broker CSV files and insert transactions into the database.
   - Provide a CLI command for importing and validating data.

4. **Market and dividend data services**
   - Fetch historical prices, current prices, and dividend information via `yfinance` or another API.
   - Cache responses to limit external calls.

5. **Portfolio calculations**
   - Compute current holdings, cost basis, portfolio value, gains, and dividend metrics from the transactions and market data.

6. **User interface**
   - Offer either a CLI or a simple web interface (FastAPI or Streamlit) to display holdings, portfolio value charts, and dividend streams.

7. **Testing & validation**
   - Write unit tests for CSV parsing, data services, and calculations.

8. **Running locally**
   - Document environment setup, importing transactions, and starting the UI in this repository.

9. **Future enhancements**
   - Schedule periodic updates, support multiple brokers, and add export features.

