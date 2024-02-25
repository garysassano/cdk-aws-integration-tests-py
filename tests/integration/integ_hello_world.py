from aws_cdk import App, integ_tests_alpha
from cdk_integ_runner_cwd_fix import fix_cwd

# This needs to be before any import from your CDK app to work around a bug in the CDK
fix_cwd()

from cdk_aws_integration_tests_py.stacks.hello_world_stack import HelloWorldStack

app = App()
stack = HelloWorldStack(app, "HelloWorldIntegTestStack")

# GIVEN
integration_test = integ_tests_alpha.IntegTest(app, "Integ", test_cases=[stack])

# WHEN
function_invoke = integration_test.assertions.invoke_function(
    function_name=stack.function.function_name,
)

# THEN
function_invoke.expect(
    integ_tests_alpha.ExpectedResult.object_like(
        {"StatusCode": 200, "Payload": '"Hello world!"'}
    )
)

app.synth()
