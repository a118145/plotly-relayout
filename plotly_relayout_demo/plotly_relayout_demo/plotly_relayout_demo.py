
"""Welcome to Reflex! This file showcases the custom component in a basic app."""

import reflex as rx
import plotly.graph_objects as go
import numpy as np

from reflex_plotly_relayout import plotly_relayout


class State(rx.State):
    """The app state."""
    fig: go.Figure = go.Figure()

    relayout_data: str = ""

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
            uirevision = 'zoom',
        )

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
    def plotly_relayout_relayout_event(self, obj: dict):
        print("Custom relayout event")
        self.relayout_data = str(obj)



def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to the Plotly relayout demo!", size="9"),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.center(
                            rx.code(
                                "Default rx.plotly",
                                size = '5',
                            ),
                            width = "100%",
                        ),
                        rx.plotly(
                            data = State.plotly_fig,
                            on_click = State.plotly_click_event,
                            on_relayout = State.plotly_relayout_event,
                        ),
                        rx.text(
                            "The default on_relayout event does not pass through any event data as explained in the ",
                            rx.link(
                            "Plotly documentation", 
                            href="https://plotly.com/javascript/plotlyjs-events/#update-data",
                            external = True,
                            ),
                            '.'
                        ),
                        
                        align = 'start',
                    ),
                    size = '4',
                    width = "50%",
                ),
                rx.card(
                    rx.vstack(
                        rx.center(
                            rx.code(
                                "Custom plotly_relayout",
                                size = '5',
                            ),
                            width = "100%",
                        ),
                        plotly_relayout(
                            data = State.plotly_fig,
                            on_click = State.plotly_relayout_click_event,
                            on_relayout = State.plotly_relayout_relayout_event,
                        ),
                        rx.text(
                            "The custom component the raw event data as dict. Zoom to try out.",
                        ),
                        rx.text(
                            f"on_relayout data: {State.relayout_data}",
                        ),
                        rx.text(
                            'If it does not work, start reflex in production mode. There might still be an issue, cf. ',
                            rx.link(
                            "Github issue", 
                            href="https://github.com/reflex-dev/reflex/issues/4532#issuecomment-3849255924",
                            external = True,
                            ),
                            '.'
                        ),

                        align = 'start',
                    ),
                    size = '4',
                    width = "50%",
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
