import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

# Read and prepare the data
stocks_df = pd.read_csv(
    '/Users/tariromusarandega/Library/CloudStorage/OneDrive-St.LawrenceUniversity/FAANG+ Stock Visualization/Stock Vizualization/faang_prices.csv')
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
stocks_df = stocks_df.set_index('Date')
stocks_df = stocks_df.sort_index()
stocks_df = stocks_df[~stocks_df.index.duplicated(keep='first')]
stocks_df = stocks_df.loc['2014-10-22':'2024-10-22']


def prepare_data(stocks_df, steps=5):  # You can also adjust steps to show fewer frames
    df = stocks_df.reset_index()
    df.index = df.index * steps
    last_idx = df.index[-1] + 1
    df_expanded = df.reindex(range(last_idx))
    df_expanded['Date'] = df_expanded['Date'].ffill()
    df_expanded = df_expanded.set_index('Date')
    df_expanded = df_expanded.interpolate()
    df_rank_expanded = df_expanded.rank(axis=1, method='first')
    return df_expanded, df_rank_expanded


# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6), dpi=144)
df_expanded, df_rank_expanded = prepare_data(stocks_df)


def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=10, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]


colors = plt.cm.Dark2(range(6))


def init():
    ax.clear()
    nice_axes(ax)
    ax.set_ylim(0.5, len(stocks_df.columns) + 0.5)


def update(i):
    ax.clear()
    nice_axes(ax)
    y = df_rank_expanded.iloc[i]
    width = df_expanded.iloc[i]

    # Create the horizontal bars with labels
    bars = ax.barh(y=y, width=width, color=colors, height=0.8)

    # Add the stock labels (company names)
    ax.set_yticks(y)
    ax.set_yticklabels(y.index)

    # Add value labels on the bars
    for bar, value in zip(bars, width):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2,
                f'${width:,.0f}',
                va='center', ha='left', fontsize=8)

    date_str = df_expanded.index[i].strftime('%B %-d, %Y')
    ax.set_title(f'Stock Prices - {date_str}', pad=10, fontsize=12)
    ax.set_xlim(0, df_expanded.max().max() * 1.1)
    ax.set_ylim(0.5, len(stocks_df.columns) + 0.5)


anim = FuncAnimation(
    fig=fig,
    func=update,
    init_func=init,
    frames=len(df_expanded),
    interval=20,
    repeat=False
)

plt.show()