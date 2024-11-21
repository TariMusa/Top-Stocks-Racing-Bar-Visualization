# Tech Stock Price Visualization

This project presents a dynamic visualization tool that animates a racing bar chart to show the stock price movements of major technology companies over the past decade. The primary goal was to illustrate the dramatic rise in stock prices of leading tech companies, with a notable surge from Netflix in particular, followed by other industry giants. The visualization highlights the role of emerging technologies in driving these trends. Further development might include adding additional information marking specific events like the Covid-19 pandemic that have been pivotal in not only pushing stock prices but in shifting the podium of top performing stocks. 

The chart also reveals how some tech giants have lost their dominant positions over time. For instance, during the Covid era, companies like Netflix, Zoom, and Adobe experienced significant performance boosts, reshaping the landscape of the tech industry.

To me, this project serves as a ten-year snapshot of how technology companies have evolved in terms of market value, with the rise and fall of key players marking distinct shifts in the market driven by external factors such as the pandemic and the boom in digital technologies.

https://github.com/user-attachments/assets/a172b1e9-000d-48fc-90f4-d3b7e35ccf3d



# Overview

This project creates an animated visualization of stock prices for major tech companies, allowing users to see how different tech stocks have performed relative to each other over the past decade. The animation shows real-time price movements and rankings, making it easy to identify trends and patterns in tech stock performance.
  
**Data Source**
The stock price data is sourced from NASDAQ (nasdaq.com) and includes the following companies:
  
Apple (AAPL)
Microsoft (MSFT)
Amazon (AMZN)
Meta/Facebook (META)
Alphabet/Google (GOOGL)
Netflix (NFLX)
Intel (INTC)
Qualcomm (QCOM)
Adobe (ADBE)
AMD (AMD)
General Electric (GE)
Zoom (ZM)
Cisco (CSCO)
IBM (IBM)
NVIDIA (NVDA)
Palantir (PLTR)
PayPal (PYPL)
Salesforce (CRM)
Starbucks (SBUX)
Tesla (TSLA)

**Prerequisites**
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

**Usage**

Place your NASDAQ stock data CSV file in the data directory
Update the file path in the script to use a relative path:

**Run the script:**

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


Data Source Attribution: NASDAQ

**Known Issues**
The visualization may display "posx and posy should be finite values" error if the data contains NaN or infinite values. Handling these cases resulted in data loss.

Contributing
Feel free to fork this repository and submit pull requests for any improvements.

License
Not Licensed.

Acknowledgments

Data provided by NASDAQ
Visualization created using Matplotlib
Animation handling through Matplotlib's FuncAnimation
