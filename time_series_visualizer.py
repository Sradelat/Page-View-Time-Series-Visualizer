import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r"C:\Users\shawn\Desktop\Python Learning\fcc-forum-pageviews.csv", delimiter=",",
                 parse_dates=True, index_col="date")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) &  # only use data between the 2.5 and 97.5 percentiles
     (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(20, 8))
    plt.plot("date", "value", data=df.reset_index(), color="r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.reset_index().copy()
    df_bar["year"] = [d.year for d in df_bar.date]  # parses the date for the year and creates a column for it
    df_bar["month"] = [d.month for d in df_bar.date]  # same as above but for month
    grp = df_bar.groupby(["year", "month"])  # creates a year dimension for months that belong
    agg = grp.aggregate({"value": np.mean})  # gives each month a mean value
    agg = agg.astype({"value": int})  # convert to int for use later

    # Draw bar plot
    fig = plt.figure(figsize=(7, 7))
    ax = plt.subplot(111)

    january = [0, agg.loc[2017, 1][0], agg.loc[2018, 1][0], agg.loc[2019, 1][0]]  # list for each month's values by year
    february = [0, agg.loc[2017, 2][0], agg.loc[2018, 2][0], agg.loc[2019, 2][0]]
    march = [0, agg.loc[2017, 3][0], agg.loc[2018, 3][0], agg.loc[2019, 3][0]]
    april = [0, agg.loc[2017, 4][0], agg.loc[2018, 4][0], agg.loc[2019, 4][0]]
    may = [agg.loc[2016, 5][0], agg.loc[2017, 5][0], agg.loc[2018, 5][0], agg.loc[2019, 5][0]]
    june = [agg.loc[2016, 6][0], agg.loc[2017, 6][0], agg.loc[2018, 6][0], agg.loc[2019, 6][0]]
    july = [agg.loc[2016, 7][0], agg.loc[2017, 7][0], agg.loc[2018, 7][0], agg.loc[2019, 7][0]]
    august = [agg.loc[2016, 8][0], agg.loc[2017, 8][0], agg.loc[2018, 8][0], agg.loc[2019, 8][0]]
    september = [agg.loc[2016, 9][0], agg.loc[2017, 9][0], agg.loc[2018, 9][0], agg.loc[2019, 9][0]]
    october = [agg.loc[2016, 10][0], agg.loc[2017, 10][0], agg.loc[2018, 10][0], agg.loc[2019, 10][0]]
    november = [agg.loc[2016, 11][0], agg.loc[2017, 11][0], agg.loc[2018, 11][0], agg.loc[2019, 11][0]]
    december = [agg.loc[2016, 12][0], agg.loc[2017, 12][0], agg.loc[2018, 12][0], agg.loc[2019, 12][0]]

    years = df_bar["year"].unique()  # for iteration purposes below - list of unique years
    ax.bar(years - 0.15, january, color="tab:blue", width=0.03, align="center")  # x, y, color, width
    ax.bar(years - 0.12, february, color="tab:orange", width=0.03, align="center")
    ax.bar(years - 0.09, march, color="tab:green", width=0.03, align="center")
    ax.bar(years - 0.06, april, color="tab:red", width=0.03, align="center")
    ax.bar(years - 0.03, may, color="tab:purple", width=0.03, align="center")
    ax.bar(years + 0.00, june, color="tab:brown", width=0.03, align="center")
    ax.bar(years + 0.03, july, color="tab:pink", width=0.03, align="center")
    ax.bar(years + 0.06, august, color="tab:gray", width=0.03, align="center")
    ax.bar(years + 0.09, september, color="tab:olive", width=0.03, align="center")
    ax.bar(years + 0.12, october, color="tab:cyan", width=0.03, align="center")
    ax.bar(years + 0.15, november, color="tab:blue", width=0.03, align="center")
    ax.bar(years + 0.18, december, color="tab:orange", width=0.03, align="center")

    color_pairs = {"January": "tab:blue", "February": "tab:orange", "March": "tab:green", "April": "tab:red",
                   "May": "tab:purple", "June": "tab:brown", "July": "tab:pink", "August": "tab:gray",
                   "September": "tab:olive", "October": "tab:cyan", "November": "tab:blue", "December": "tab:orange"}
    plt.legend(color_pairs, title="Months")  # legend uses list above

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_xticks(years)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]  # same as last plot

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(30, 7))
    year1 = df_box.loc[df_box["year"] == 2016]["value"]  # lists of values by year
    year2 = df_box.loc[df_box["year"] == 2017]["value"]
    year3 = df_box.loc[df_box["year"] == 2018]["value"]
    year4 = df_box.loc[df_box["year"] == 2019]["value"]
    data1 = [year1, year2, year3, year4]  # combined data for plotting

    plot1 = ax1.boxplot(data1, patch_artist=True)

    colors = ["tab:blue", "tab:green", "tab:orange", "tab:red"]
    for patch, color in zip(plot1["boxes"], colors):
        patch.set_facecolor(color)

    ax1.set_xticklabels(["2016", "2017", "2018", "2019"])
    ax1.set_ylabel("Page Views")
    ax1.set_xlabel("Year")
    ax1.set_title("Year-wise Box Plot (Trend)")

    jan = df_box.loc[df_box["month"] == "Jan"]["value"]  # lists of data values per month regardless of year
    feb = df_box.loc[df_box["month"] == "Feb"]["value"]
    mar = df_box.loc[df_box["month"] == "Mar"]["value"]
    apr = df_box.loc[df_box["month"] == "Apr"]["value"]
    may = df_box.loc[df_box["month"] == "May"]["value"]
    jun = df_box.loc[df_box["month"] == "Jun"]["value"]
    jul = df_box.loc[df_box["month"] == "Jul"]["value"]
    aug = df_box.loc[df_box["month"] == "Aug"]["value"]
    sep = df_box.loc[df_box["month"] == "Sep"]["value"]
    oct = df_box.loc[df_box["month"] == "Oct"]["value"]
    nov = df_box.loc[df_box["month"] == "Nov"]["value"]
    dec = df_box.loc[df_box["month"] == "Dec"]["value"]
    data2 = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

    ax2.boxplot(data2, patch_artist=True)

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_ylabel("Page Views")
    ax2.set_xlabel("Month")
    ax2.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
