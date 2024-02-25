from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="10464497+garysassano@users.noreply.github.com",
    author_name="Gary Sassano",
    cdk_version="2.130.0",
    module_name="cdk_aws_integration_tests_py",
    name="cdk-aws-integration-tests-py",
    poetry=True,
    python_exec="python",
    version="0.1.0",
    ###
    deps=["aws_cdk.integ_tests_alpha", "cdk-integ-runner-cwd-fix"],
)

# Set Poetry local configuration for this project
poetry_toml = project.try_find_file("poetry.toml")
poetry_toml.add_override("virtualenvs.create", "true")
poetry_toml.add_override("virtualenvs.in-project", "true")

project.synth()
