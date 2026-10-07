import plotly.io as pio
import plotly.graph_objects as go

pio.templates["course"] = go.layout.Template(
    layout=dict(
        font=dict(family="Arial", size=14),
        colorway=["#2C7FB8", "#41B6C4", "#A1DAB4", "#FDAE61", "#D7191C"],
    )
)
pio.templates.default = "plotly_white+course"