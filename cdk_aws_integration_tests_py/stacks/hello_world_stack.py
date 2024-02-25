import os
from pathlib import Path
from aws_cdk import Stack
from aws_cdk.aws_lambda import Code, Function, Runtime
from constructs import Construct


class HelloWorldStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.function = Function(
            self,
            "HelloWorldLambda",
            code=Code.from_asset(
                str(Path(__file__).parent / ".." / "functions" / "hello-world")
            ),
            handler="index.handler",
            runtime=Runtime.PYTHON_3_12,
        )
