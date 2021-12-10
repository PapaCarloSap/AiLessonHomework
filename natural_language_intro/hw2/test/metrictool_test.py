# %%
# import plotly.express as px

# df = px.data.gapminder().query("country=='Canada'")
# fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# fig.show()



# %%
from hw2.metrictool import MetricRegressionManager 
y_true = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
y_pred = [0.1, 0.7, 0.85, 0, 0.9, 0.67, 0.15, 0.25, 0.6, 0.4]
target = MetricRegressionManager()
target.apply('test', y_true, y_pred)
target.apply('test 2', 
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
             [0.1, 0.7, 0.5, 0, 0.9, 0.67, 0.15, 0.25, 0.6, 0.4]
             )
target.show_united_auc_interactive()
target.show_united_auc_interactive_v2()

# %%

import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="day", y="total_bill", color="smoker", barmode="group", facet_col="sex",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "smoker": ["Yes", "No"],
                              "sex": ["Male", "Female"]})
fig.show()

# %%
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# create figure with subplots
fig = make_subplots(rows=2, cols=1, subplot_titles = ['title1','title2'], print_grid=True)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6], legendgroup = '1'),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70], legendgroup = '2'),
    row=2, col=1
)

fig.update_layout(
    height=600, 
    width=800, 
    title_text="Subplots", 
    legend_tracegroupgap = 200,
    )

fig.show()

# to change subtitle, address subplot
fig['layout']['annotations'][0].update(text='your text here');

fig.show()



# %%
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", symbol="smoker", facet_col="time",
          labels={"sex": "Gender", "smoker": "Smokes"})
fig.show()

# %%
