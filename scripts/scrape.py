import pandas as pd

link = (
    "https://zh.wikipedia.org/wiki/S%26P_500%E6%88%90%E4%BB%BD%E8%82%A1%E5%88%97%E8%A1%A8"
)
df = pd.read_html(link, header=0)[0]

# Write to CSV
df.to_csv("data/constituents.csv", index=False)
