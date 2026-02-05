
"""Reflex custom component PlotlyRelayout."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
from reflex.components.plotly.plotly import Plotly
from reflex.event import passthrough_event_spec

class PlotlyRelayout(Plotly):
    """PlotlyRelayout component. It extends the built-in Plotly component and adds a passthrough_event_spec to the on_relayout event so that the axes' ranges can be accessed in the backend, e.g., for downsampling."""

    on_relayout: rx.EventHandler[passthrough_event_spec(dict)]

plotly_relayout = PlotlyRelayout.create
