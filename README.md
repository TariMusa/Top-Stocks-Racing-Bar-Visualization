Tech Stock Price Visualization
A dynamic visualization tool that creates an animated racing bar chart showing the stock price movements of major technology companies over time.
Overview
This project creates an animated visualization of stock prices for major tech companies, allowing users to see how different tech stocks have performed relative to each other over the past decade. The animation shows real-time price movements and rankings, making it easy to identify trends and patterns in tech stock performance.
Data Source
The stock price data is sourced from NASDAQ (nasdaq.com) and includes the following companies:

Apple (AAPL)
Microsoft (MSFT)
Amazon (AMZN)
Meta/Facebook (META)
Alphabet/Google (GOOGL)
Netflix (NFLX)

Prerequisites
Required Python packages:
bashCopypip install matplotlib
pip install pandas
pip install numpy
File Structure
Copyproject_root/
│
├── data/
│   └── faang_prices.csv    # Stock price data
│
├── src/
│   └── stock_visualization.py    # Main visualization script
│
└── README.md
Usage

Place your NASDAQ stock data CSV file in the data directory
Update the file path in the script to use a relative path:

pythonCopy# Instead of absolute path like:
# '/Users/username/Library/CloudStorage/OneDrive-St.LawrenceUniversity/...'

# Use relative path:
stocks_df = pd.read_csv('data/faang_prices.csv')

Run the script:

bashCopypython src/stock_visualization.py
Customization Options

Adjust animation speed: Modify the interval parameter in FuncAnimation (lower value = faster animation)

pythonCopyinterval=50  # Default value, decrease for faster animation

Change frame density: Modify the steps parameter in prepare_data() function

pythonCopysteps=5  # Default value, increase for fewer frames

Modify visualization appearance:

Figure size: Adjust figsize=(10, 6) in plt.subplots()
Bar height: Modify height=0.8 in ax.barh()
Colors: Change colors = plt.cm.Dark2(range(6))


Data Source Attribution: Always credit your data source (in this case, NASDAQ)

Known Issues
The visualization may display "posx and posy should be finite values" error if the data contains NaN or infinite values. Handling these cases resulted in data loss.

Contributing
Feel free to fork this repository and submit pull requests for any improvements.

License
Not Licensed.

Acknowledgments

Data provided by NASDAQ
Visualization created using Matplotlib
Animation handling through Matplotlib's FuncAnimation
