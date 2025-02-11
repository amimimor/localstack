import os
from typing import Final

from tests.integration.stepfunctions.templates.template_loader import TemplateLoader

_THIS_FOLDER: Final[str] = os.path.dirname(os.path.realpath(__file__))


class ServicesTemplates(TemplateLoader):
    # State Machines.
    AWSSDK_LIST_SECRETS: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/aws_sdk_secrestsmaager_list_secrets.json5"
    )
    SQS_SEND_MESSAGE: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/sqs_send_msg.json5")
    LAMBDA_INVOKE: Final[str] = os.path.join(_THIS_FOLDER, "statemachines/lambda_invoke.json5")
    LAMBDA_INVOKE_PIPE: Final[str] = os.path.join(
        _THIS_FOLDER, "statemachines/lambda_invoke_pipe.json5"
    )

    # Lambda Functions.
    LAMBDA_ID_FUNCTION: Final[str] = os.path.join(_THIS_FOLDER, "lambdafunctions/id_function.py")
