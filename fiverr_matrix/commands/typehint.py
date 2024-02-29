from typing import TYPE_CHECKING

from mautrix.bridge.commands import CommandEvent as BaseCommandEvent

if TYPE_CHECKING:
    from ..__main__ import FiverrBridge
    from ..user import User


class CommandEvent(BaseCommandEvent):
    bridge: "FiverrBridge"
    sender: "User"
