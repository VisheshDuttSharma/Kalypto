import pytest

from PySide6.QtWidgets import (
    QApplication
)

from main_interface import (
    KalyptoElite
)


@pytest.mark.gui
def test_gui_launch(qtbot):

    window = KalyptoElite()

    qtbot.addWidget(window)

    window.show()

    assert window.windowTitle() != ""