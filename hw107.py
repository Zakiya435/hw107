import pandas as pd, csv, plotly.express as px

df = pd.read_csv("data2.csv")

mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()