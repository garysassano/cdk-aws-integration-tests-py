import os
from aws_cdk import App, Environment
from cdk_aws_integration_tests_py.stacks.hello_world_stack import (
    HelloWorldStack,
)

# for development, use account/region from cdk cli
dev_env = Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)

app = App()

HelloWorldStack(app, "HelloWorldStack", env=dev_env)

app.synth()
