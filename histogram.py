import plotly.express as px

# Load restaurant tipping data
df = px.data.tips()

# Create a histogram with marginal rug plots
fig = px.histogram(
    df,
    x="total_bill",
    color="sex",
    nbins=30,
    marginal="rug",  # Adds a distribution rug at the bottom
    title="Distribution of Total Bills by Gender"
)

fig.show()