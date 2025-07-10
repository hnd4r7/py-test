import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(id="live-update-text"),
        dcc.Interval(id="interval-component", interval=1000, n_intervals=0),  # in milliseconds
    ]
)


@app.callback(Output("live-update-text", "children"), Input("interval-component", "n_intervals"))
def update_metrics(n):
    # This function will be called every 1 second
    return f"Number of intervals: {n}"


if __name__ == "__main__":
    app.run_server(debug=True)
