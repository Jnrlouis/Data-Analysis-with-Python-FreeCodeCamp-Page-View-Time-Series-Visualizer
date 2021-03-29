import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = "date", parse_dates = ["date"])

# Clean data
df = df[(df["value"]>=df["value"].quantile(0.025)) & (df["value"]<= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(df.index, df["value"], color = "red", linewidth =2 )
    ax.set_xlabel("Date")
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["month"]= df_bar.index.month
    df_bar["year"]= df_bar.index.year
    df_bar_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    # Draw bar plot
    axes = df_bar_grouped.plot.bar(figsize=(12,12))
    axes.set_xlabel("Years")
    axes.set_ylabel("Average Page Views")
    axes.legend(fontsize = 10, labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    fig = axes.get_figure()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box["month_1"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_1")
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (10,4))
    
    axes[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], data = df_box, ax = axes[0])
    
    axes[0].set(title= "Year-wise Box Plot (Trend)", xlabel='Year', ylabel='Page Views')
    #axes[0] = set_xlabel("Year")
    #axes[0] = set_ylabel("Page Views")

    axes[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], data = df_box, ax = axes[1])

    axes[1].set(title="Month-wise Box Plot (Seasonality)", xlabel='Month', ylabel='Page Views')
    #axes[1] = set_xlabel("Months")
    #axes[1] = set_ylabel("Page Views")
    #axes[0].set_title("Year-wise Box Plot (Trend)")
    #axes[1].set_title("Month-wise Box Plot (Seasonality)")
    







    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
