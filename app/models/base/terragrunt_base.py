from pydantic import BaseModel, Field
from typing import Optional


class TerragruntBaseConfig(BaseModel):
    tg_local: bool = Field(False, description="If true, use local backend")
    terraform_version_constraint: str = Field(
        "~> 1.2.0", description="Terraform version constraint"
    )
    terragrunt_version_constraint: str = Field(
        "~> 0.80.4", description="Terragrunt version constraint"
    )
