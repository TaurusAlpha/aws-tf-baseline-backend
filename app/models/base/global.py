from pydantic import BaseModel, Field


class GlobalConfig(BaseModel):
    management_account_id: str = Field(..., description="AWS account ID of the management/root account")
    management_profile_name: str = Field(..., description="AWS profile name for the management account")
    default_region: str = Field("eu-west-1", description="Default AWS region for organization-wide services")
