from pydantic import BaseModel, Field


class RegionConfig(BaseModel):
    env: str = Field(..., description="Environment name (e.g., dev, staging, prod)")
    env_type: str = Field(..., description="Type of environment (e.g., nonprod, prod)")
    aws_region: str = Field(..., description="AWS region (e.g., eu-west-1)")
    az_number: int = Field(..., description="Number of availability zones to use")
    project_name: str = Field(..., description="Project name for resource naming and tagging")
