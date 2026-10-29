# -*- coding: utf-8 -*-
from __future__ import annotations

import inspect

from qwenpaw_data.host.core.agent.qwenpaw_data_agent import QwenPawDataAgent


def test_default_react_config_raises_cancelled_error() -> None:
    """The default ReAct config must let cancellation propagate to the host.

    AgentScope swallows asyncio.CancelledError when
    interruption_raise_cancelled_error is False, so reply_stream returns
    normally and ChatRuntime records the run as completed even though the
    user pressed stop. Keeping the flag enabled lets ChatRuntime.cancel()
    interrupt the agent and finish as canceled.
    """

    signature = inspect.signature(QwenPawDataAgent.__init__)
    react_config = signature.parameters["react_config"].default

    assert react_config.interruption_raise_cancelled_error is True
