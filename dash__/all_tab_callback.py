import dash
from dash import dcc, html, Input, Output, callback
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

# Sample layout with multiple tabs
app.layout = html.Div(
    [
        dcc.Tabs(
            id="tabs-1",
            children=[
                dcc.Tab(label="Tab 1-1", value="tab-1-1"),
                dcc.Tab(label="Tab 1-2", value="tab-1-2"),
            ],
        ),
        html.Div(id="tabs-1-content"),
        dcc.Tabs(
            id="tabs-2",
            children=[
                dcc.Tab(label="Tab 2-1", value="tab-2-1"),
                dcc.Tab(label="Tab 2-2", value="tab-2-2"),
            ],
        ),
        html.Div(id="tabs-2-content"),
        dcc.Tabs(
            id="tabs-3",
            children=[
                dcc.Tab(label="Tab 3-1", value="tab-3-1"),
                dcc.Tab(label="Tab 3-2", value="tab-3-2"),
            ],
        ),
        html.Div(id="tabs-3-content"),
    ]
)


def find_all_tab_ids(layout):
    """Recursively find all Tabs component IDs in the layout"""
    tab_ids = []

    def traverse(component):
        if hasattr(component, "id") and isinstance(component, dcc.Tabs):
            tab_ids.append(component.id)
        if hasattr(component, "children"):
            children = component.children if isinstance(component.children, list) else [component.children]
            for child in children:
                if child is not None:
                    traverse(child)

    traverse(layout)
    return tab_ids


# Get all tab IDs from the layout
all_tab_ids = find_all_tab_ids(app.layout)


# Create a single callback that handles all tabs
@callback(
    [Output(f"{tab_id}-content", "children") for tab_id in all_tab_ids],
    [Input(tab_id, "value") for tab_id in all_tab_ids],
    prevent_initial_call=True,
)
def update_all_tabs(*args):
    # Get the context to see which input triggered the callback
    ctx = dash.callback_context

    if not ctx.triggered:
        raise PreventUpdate

    # Get the ID of the tab that was clicked
    triggered_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # Get the value of the selected tab
    selected_value = ctx.triggered[0]["value"]

    # Create outputs for all tab content divs
    outputs = [None] * len(all_tab_ids)

    # Find which tab was triggered and update its content
    for i, tab_id in enumerate(all_tab_ids):
        if tab_id == triggered_id:
            outputs[i] = f"You've selected {selected_value} from {triggered_id}"

    return outputs


if __name__ == "__main__":
    app.run(debug=True)
