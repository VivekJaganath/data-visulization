import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

path = "C:\\Users\\Vivek\\Downloads\\DataWeierstrass.csv"
df = pd.read_csv(path, sep=";")
df['lecture'] = pd.to_numeric(df['lecture'].str.replace('lecture', ''))

#a) Visualize given data with a scatterplot matrix.
#ref: https://plotly.com/python/splom/
fig = px.scatter_matrix(df, title="Scatter matrix Plot of Professor Ranking",color="professor",dimensions=["lecture", "participants", "professional expertise", "motivation",
                                             "clear presentation", "overall impression"], symbol="overall impression")
fig.update_traces(diagonal_visible=False)
fig.show()

#b) Visualize given data with parallel coordinates.
#ref: https://plotly.com/python/parallel-coordinates-plot/
#ref: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html

# Converting the professor attribute into int datatype
df['professor'] = pd.to_numeric(df['professor'].str.replace('prof', ''))

dimensions = ["lecture", "participants", "professional expertise", "motivation", "clear presentation",
              "overall impression"]

figure = go.Figure(data=
go.Parcoords(
    line=dict(color=df['professor'],
              colorsrc="professor",
              colorscale='rainbow',
              showscale=True),
    dimensions=list([
        dict(range=[(df['professor'].min() - 1), (df['professor'].max() + 1)],
             label="Professor Number", values=df['professor']),
        dict(range=[(df['lecture'].min() - 1), (df['lecture'].max() + 1)],
             label="Lecture Number", values=df['lecture']),
        dict(range=[(df['participants'].min() - 1), (df['participants'].max() + 1)],
             label="Participants", values=df['participants']),
        dict(range=[6, 0],
             tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
             label='Professional Expertise', values=df['professional expertise']),
        dict(range=[6, 0],
             tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
             label='Motivation', values=df['motivation']),
        dict(range=[6, 0],
             tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
             label='Clean Presentation', values=df['clear presentation']),
        dict(range=[6, 0],
             tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6],
             label='Overall impression', values=df['overall impression'])])))

figure.update_layout(title="Parallel Co-ordinates Plot of Professor Ranking")
figure.show()
