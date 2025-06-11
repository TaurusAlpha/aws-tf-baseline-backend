from pydantic import BaseModel, Field
from typing import Optional


class AccountConfig(BaseModel):
    account_name: str = Field(..., description="Name label for the AWS account (e.g., dev, staging, prod)")
    account_id: str = Field(..., description="12-digit AWS Account ID")
    profile_name: str = Field(..., description="AWS CLI profile name for this account")
    assume_role_arn: Optional[str] = Field(None, description="IAM role ARN to assume when accessing this account")
    external_id: Optional[str] = Field(None, description="External ID used when assuming a cross-account role")
