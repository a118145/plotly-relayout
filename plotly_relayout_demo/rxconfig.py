import reflex as rx

config = rx.Config(
    app_name="plotly_relayout_demo",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)