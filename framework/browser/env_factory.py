import pytest


class EnvFactory:
    QA_LINK = "https://www.bodum.com/gb/en/"
    DEV_LINK = "https://www.bodum.com/gb/en/"
    PROD_LINK = "https://www.bodum.com/gb/en/"
    __env_type = None

    @staticmethod
    def set_type(env_type):
        if env_type == "qa":
            EnvFactory.__env_type = EnvFactory.QA_LINK
        elif env_type == "dev":
            EnvFactory.__env_type = EnvFactory.DEV_LINK
        elif env_type == "prod":
            EnvFactory.__env_type = EnvFactory.PROD_LINK
        else:
            raise pytest.UsageError("--env should be dev/qa/prod")

    @staticmethod
    def get_type():
        return EnvFactory.__env_type

    @staticmethod
    def clear_env_type():
        if EnvFactory.__env_type is not None:
            EnvFactory.__env_type = None
