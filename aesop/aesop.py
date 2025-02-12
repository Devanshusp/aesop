"""Main app page."""

import reflex as rx
from reflex_clerk import install_signin_page

from aesop.frontend.pages.create import create_page
from aesop.frontend.pages.home import home_page
from aesop.frontend.pages.story import story_page
from aesop.frontend.pages.talk import talk_page

app = rx.App(  # pylint: disable=E1102
    theme=rx.theme(
        appearance="light",
        has_background=True,
        accent_color="orange",
        panel_background="translucent",
    )
)

install_signin_page(app)


app.add_page(story_page, route="/story/[story_id]")
app.add_page(create_page, route="/create")
app.add_page(talk_page, route="/talk")
app.add_page(home_page, route="/")
