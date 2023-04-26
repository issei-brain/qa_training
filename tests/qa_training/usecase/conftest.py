import pandas as pd
import pytest
from qa_training.utils.boundary.usecase.if_usecase_create_model import (
    IF_UsecaseCreateModel,
)
from qa_training.utils.domain_registry import DomainRegistry


@pytest.fixture
def fixture_create_model(domain_registry: DomainRegistry):
    usecase_create_model = domain_registry.usecase_create_model()
    yield usecase_create_model
    usecase_create_model.initialize()


@pytest.fixture
def fixture_judge_survival(
    domain_registry: DomainRegistry, fixture_create_model: IF_UsecaseCreateModel
):
    fixture_create_model.create_model()

    usecase_judge_survival = domain_registry.usecase_judge_survival()
    df_customer_info = pd.read_csv(
        "./tests/common_data/df_customer_info.csv",
    )
    df_y_pred_expected = pd.read_csv(
        "./tests/common_data/df_y_pred_expected.csv",
    )
    list_survival_expected: list[bool] = df_y_pred_expected["Survived"].to_list()

    yield usecase_judge_survival, df_customer_info, list_survival_expected
    usecase_judge_survival.initialize()
