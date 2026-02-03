
"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx
import plotly.graph_objects as go
import numpy as np

from reflex_plotly_relayout import plotly_relayout


class State(rx.State):
    """The app state."""
    fig: go.Figure = go.Figure()

    RAND_SIZE: int = 10

    @rx.var
    def plotly_fig(self) -> go.Figure:
        return self.fig

    @rx.event
    def load_figures(self):
        x = np.arange(self.RAND_SIZE)
        y = np.random.rand(self.RAND_SIZE) 

        self.fig = go.Figure(
            [go.Scattergl(
                x = x, 
                y = y, 
                mode = 'lines',
            ),
            ],
        )
        self.fig.update_layout(
            autosize=True,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(size=25, family='Inter, ui-sans-serif, system-ui'),
        )
        # self.fig = fig

    @rx.event
    def plotly_click_event(self, point: list):
        print("Click event")
        print(point)

    @rx.event
    def plotly_relayout_event(self):
        print("Relayout event")

    @rx.event
    def plotly_relayout_click_event(self, point: list):
        print("Custom click event")
        print(point)

    @rx.event
    def plotly_relayout_relayout_event(self, obj):
        print("Custom relayout event")
        print(obj)




def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to the Plotly relayout demo!", size="9"),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.code(
                            "Default rx.plotly",
                            size = '5',
                        ),
                        rx.plotly(
                            data = State.plotly_fig,
                            on_click = State.plotly_click_event,
                            on_relayout = State.plotly_relayout_event,
                        ),
                        align = 'center',
                    ),
                    size = '4',
                ),
                rx.card(
                    rx.vstack(
                        rx.code(
                            "Custom plotly_relayout",
                            size = '5',
                        ),
                        # rx.plotly(
                        plotly_relayout(
                            data = State.plotly_fig,
                            on_click = State.plotly_relayout_click_event,
                            # on_click = State.plotly_click_event,
                            on_relayout = State.plotly_relayout_relayout_event,
                        ),
                        align = 'center',
                    ),
                    size = '4',
                ),
            ),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(
    index,
    on_load = State.load_figures,
    )
