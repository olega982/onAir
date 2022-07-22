import pytest


class EnvManager:
    QA_LINK = "https://www.bodum.com/gb/en/"
    DEV_LINK = "https://www.bodum.com/gb/en/"
    PROD_LINK = "https://www.bodum.com/gb/en/"
    __env_type = None

    @staticmethod
    def set_type(env_type):
        if env_type == "qa":
            EnvManager.__env_type = EnvManager.QA_LINK
        elif env_type == "dev":
            EnvManager.__env_type = EnvManager.DEV_LINK
        elif env_type == "prod":
            EnvManager.__env_type = EnvManager.PROD_LINK
        else:
            raise pytest.UsageError("--env should be dev/qa/prod")

    @staticmethod
    def get_type():
        return EnvManager.__env_type

    @staticmethod
    def clear_env_type():
        if EnvManager.__env_type is not None:
            EnvManager.__env_type = None
