from typing import Literal

from pydantic import BaseModel, Field


class Document(BaseModel):
    filename: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    extension: Literal["md", "pdf"]
    size: int = Field(..., ge=0)
