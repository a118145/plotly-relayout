
"""Welcome to Reflex! This file showcases the custom component in a basic app."""

from rxconfig import config

import reflex as rx

# from reflex_plotly_relayout import plotly_relayout

filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    pass

def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to the Plotly relayout demo!", size="9"),
            # rx.text(
            #     "Test your custom component by editing ",
            #     rx.code(filename),
            #     font_size="2em",
            # ),
            # plotly_relayout(),
            align="center",
            spacing="7",
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
