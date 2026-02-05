# plotly-relayout

Extension of Reflex Plotly graphing component to pass zoom information to event handler in backend until native Reflex support is added.

## Installation

```bash
pip install reflex-plotly-relayout
```

## Usage ##

Instead of using `rx.plotly(...)` to display a Plotly `go.Figure()` in the frontend, you use `plotly_relayout(...)`, i.e.

```python
plotly_relayout(
    data = State.plotly_fig,
    on_click = State.plotly_relayout_click_event,
    on_relayout = State.plotly_relayout_relayout_event,
)
```

The relayout event now accepts a dict, which contains the relayouting info according to the [Plotly documentation](https://plotly.com/javascript/plotlyjs-events/#update-data). According to this [Github discussion](https://github.com/reflex-dev/reflex/issues/4532#issuecomment-3849255924), problems might occur in dev-mode.