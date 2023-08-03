from superagi.tools.base_tool import BaseTool, BaseToolkit
from abc import ABC
from typing import List
from AutonumousEmailTool import AutonomousEmailTool


class ContloToolkit(BaseToolkit, ABC):
    name: str = "Autonomous Email Toolkit"
    description: str = "Toolkit containing tools for running autonomous email campaigns"

    def get_tools(self) -> List[BaseTool]:
        return [AutonomousEmailTool()]

    def get_env_keys(self) -> List[str]:
        return [
            "CONTLO_PRIVATE_KEY"
        ]