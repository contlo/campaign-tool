import json

from superagi.tools.base_tool import BaseTool
import requests
from pydantic import BaseModel, Field
from typing import Type


class AutonomousEmailInput(BaseModel):
    senderEmail: str = Field(..., description="Email Address of the Sender, default email is 'example@example.com'")
    senderName: str = Field(..., description="Name of the Sender, default is 'example'")
    subject: str = Field(..., description="Subject of the Email to be sent")
    body: str = Field(..., description="Email Body to be sent")
    segmentId: str = Field(..., description="Segment ID")
    time: str = Field(..., description="Campaign schedule time")
    shop_id: str = Field(..., description="Shop ID")
    replyEmail: str = Field(..., description="Email Address for reply, default email is 'example@example.com'")


class AutonomousEmailTool(BaseTool):
    """
        Schedule a campaign tool

        Attributes:
            name : The name.
            description : The description.
            args_schema : The args schema.
    """

    name: str = "Schedule campaign"
    args_schema: Type[AutonomousEmailInput] = AutonomousEmailInput
    description: str = "Send an Email"

    class Config:
        arbitrary_types_allowed = True

    def _execute(self, sender_email: str, sender_name: str, subject: str, body: str, segment_id: str, time: str, shop_id: str, reply_mail: str) -> str:

        api_key = self.get_tool_config("CONTLO_PRIVATE_KEY")
        url = "https://marketing.contlo.com/superagi/new_superagi_campaign"

        data = {'segment_id': segment_id, 'sender_name': sender_name, 'sender_email': sender_email,
                'reply_to_mail': reply_mail, 'subject': subject, 'body': body, 'time': time}

        return requests.post(url=url, data=json.dumps(data), headers={"X-API-KEY": api_key}).text


