
"""Reflex custom component PlotlyRelayout."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

from typing import Any, List, Dict, TypedDict

import reflex as rx
from reflex.components.plotly.plotly import Plotly
from reflex.vars.base import Var
# from reflex.event import EventHandler
# from reflex.vars.function import FunctionVar
from reflex.vars.object import ObjectVar
# from dataclasses import dataclass

# Some libraries you want to wrap may require dynamic imports.
# This is because they they may not be compatible with Server-Side Rendering (SSR).
# To handle this in Reflex, all you need to do is subclass `NoSSRComponent` instead.
# For example:
# from reflex.components.component import NoSSRComponent
# class PlotlyRelayout(NoSSRComponent):
#     pass

class _ClickEvent(TypedDict):
    """Defines the shape of the click event passed to onClick by react-plotly.js."""
    # event: Any
    points: List[Dict]

def _on_click_signature(event: ObjectVar[_ClickEvent]) -> List[Any]:
    """Maps the onClick args from javascript to the event handled by the Reflex backend in python."""
    # return [event.point_info]
    return [
        # event.points
        rx.Var(
            _js_expr = f"myExtractPoints({event.points})",
        ),
    ]

class _RelayoutEvent(TypedDict):
    """Defines the shape of the relayout event passed to onRelayout by react-plotly.js."""
    # event: Any
    # points: List[Dict]

def _on_relayout_signature(event: ObjectVar[_RelayoutEvent]) -> List[Any]:
    """Maps the onRelayout args from javascript to the event handled by the Reflex backend in python."""
    # return [event.point_info]
    return [
        # event.points
        'This is a test',
        # rx.Var(
        #     _js_expr = f"console.log({event})",
        # ),
    ]


class PlotlyRelayout(Plotly):
    """PlotlyRelayout component."""

    # The React library to wrap.
    # library = "Fill-Me"

    # The React component tag.
    # tag = "Fill-Me"

    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    # is_default = True

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    # alias = "OtherPlotlyRelayout"

    # The props of the React component.
    # Note: when Reflex compiles the component to Javascript,
    # `snake_case` property names are automatically formatted as `camelCase`.
    # The prop names may be defined in `camelCase` as well.
    # some_prop: rx.Var[str] = "some default value"
    # some_other_prop: rx.Var[int] = 1

    # By default Reflex will install the library you have specified in the library property.
    # However, sometimes you may need to install other libraries to use a component.
    # In this case you can use the lib_dependencies property to specify other libraries to install.
    # lib_dependencies: list[str] = []

    # Event triggers declaration if any.
    # Below is equivalent to merging `{ "on_change": lambda e: [e] }`
    # onto the default event triggers of parent/base Component.
    # The function defined for the `on_change` trigger maps event for the javascript
    # trigger to what will be passed to the backend event handler function.
    # on_change: rx.EventHandler[lambda e: [e]]
    on_click: rx.EventHandler[_on_click_signature]
    # on_click: rx.EventHandler[lambda e: [print(e)]]
    on_relayout: rx.EventHandler[_on_relayout_signature]

    # To add custom code to your component
    def _get_custom_code(self) -> str:
        return """
// extract only relevant data from the points to minimize payload size and workaround circular references
const myExtractPoints = (points) => {
    return points.map(point => {
        return {
            x: point.x,
            y: point.y,
            curveNumber: point.curveNumber,
            pointNumber: point.pointNumber,
            pointIndex: point.pointIndex,
            'marker.color': point['marker.color'],
            'marker.size': point['marker.size'],
            bbox: {
                x0: point.bbox.x0,
                x1: point.bbox.x1,
                y0: point.bbox.y0,
                y1: point.bbox.y1,
            }
        }
    })
}
"""


plotly_relayout = PlotlyRelayout.create
