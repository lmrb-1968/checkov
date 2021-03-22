from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck


class PostgreSQLServerHasPublicAccessDisabled(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that PostgreSQL server disables public network access"
        id = "CKV_AZURE_133"
        supported_resources = ['azurerm_postgresql_server']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_block_result=CheckResult.FAILED)

    def get_inspected_key(self):
        return 'public_network_access_enabled'

    def get_expected_value(self):
        return False


check = PostgreSQLServerHasPublicAccessDisabled()
