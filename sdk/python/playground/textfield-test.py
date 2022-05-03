import logging
from datetime import datetime
from time import sleep

import flet
from flet import (
    Column,
    Dropdown,
    ElevatedButton,
    Image,
    Page,
    Row,
    Text,
    Theme,
    border_radius,
    dropdown,
    icons,
    padding,
)
from flet.checkbox import Checkbox
from flet.container import Container
from flet.icon import Icon
from flet.list_view import ListView
from flet.progress_bar import ProgressBar
from flet.radio import Radio
from flet.radio_group import RadioGroup
from flet.stack import Stack
from flet.switch import Switch
from flet.textfield import TextField

logging.basicConfig(level=logging.DEBUG)


def main(page: Page):
    page.title = "TextField Examples"
    page.theme_mode = "light"
    page.padding = padding.all(20)

    prgb = ProgressBar(visible=False)

    def chat_submit(e):
        print(f"Submit FieldText: {e.control.value}")
        e.control.value = ""
        form.disabled = True
        prgb.visible = True
        page.update()
        sleep(2)
        form.disabled = False
        prgb.visible = False
        page.update()

    chat_input = TextField(
        hint_text="Say something...",
        shift_enter=True,
        min_lines=1,
        on_submit=chat_submit,
        max_lines=5,
    )

    form = Column(
        [
            prgb,
            Text("Outlined TextField", style="headlineMedium"),
            TextField(),
            Text(
                "Outlined TextField with Label, Hint and Helper text",
                style="headlineSmall",
            ),
            TextField(
                label="Full name",
                hint_text="Enter your full name",
                helper_text="Hint text is visible when TextField is empty and focused",
            ),
            Text(
                "Underlined, filled and multiline TextField",
                style="headlineSmall",
            ),
            TextField(
                label="Comments",
                helper_text="Tell something about us",
                border="underline",
                filled=True,
                multiline=True,
            ),
            Text(
                "New line - Shift + Enter and submit on Enter",
                style="headlineSmall",
            ),
            chat_input,
            Text(
                "Login with email/password",
                style="headlineSmall",
            ),
            TextField(
                label="Email",
                prefix_icon=icons.EMAIL,
                border="underline",
                keyboard_type="email",
                filled=True,
            ),
            TextField(
                label="Password",
                prefix_icon=icons.PASSWORD_SHARP,
                border="underline",
                password=True,
                can_reveal_password=True,
                filled=True,
            ),
        ],
        scroll="adaptive",
        expand=1,
        width=600,
    )

    page.add(form)


flet.app(name="test1", port=8550, target=main, view=flet.WEB_BROWSER)
