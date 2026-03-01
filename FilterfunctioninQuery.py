from typing import Annotated
from fastapi import FastAPI, Path, Query, APIRouter
from pydantic import BaseModel, Field

app = APIRouter()


# ── Query params grouped in a Pydantic model ──────────────────────────────────

class ProductFilterParams(BaseModel):

    search: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="A keyword to search within the product. Between 3 and 50 characters.",
        alias="search-keyword",
    )

    sort_by: str | None = Field(
        default=None,
        min_length=2,
        max_length=20,
        description="Field to sort results by. E.g. 'price', 'name', 'rating'.",
        alias="sort-by",
    )

    min_price: float | None = Field(
        default=None,
        ge=0.0,
        lt=100000.0,
        description="Filter products with price greater than this value. Must be >= 0.",
    )

    max_price: float | None = Field(
        default=None,
        gt=0.0,
        le=100000.0,
        description="Filter products with price less than or equal to this value.",
    )

    page: int = Field(
        default=1,
        ge=1,
        description="Which page of results to return. Must be 1 or more.",
    )

    page_size: int = Field(
        default=10,
        ge=1,
        le=100,
        description="How many results per page. Between 1 and 100.",
        alias="page-size",
    )

    # Allow alias AND original field name both to work in URL
    model_config = {"populate_by_name": True}


# ── Endpoint ──────────────────────────────────────────────────────────────────
@app.get("/store/{category_id}/products/{product_id}")
async def get_product(

    category_id: Annotated[int,
        Path(
            description="The ID of the product category. Must be between 1 and 500.",
            ge=1,
            le=500,
        ),
    ],

    product_id: Annotated[int,
        Path(
            description="The unique ID of the product. Must be greater than 0.",
            gt=0,
            lt=10000,
        ),
    ],

    # ↓ All query params now come from the model
    filters: Annotated[ProductFilterParams, Query()],
):
    result = {
        "category_id": category_id,
        "product_id": product_id,
        "page": filters.page,
        "page_size": filters.page_size,
    }

    if filters.search:
        result["search"] = filters.search
    if filters.sort_by:
        result["sort_by"] = filters.sort_by
    if filters.min_price is not None:
        result["min_price"] = filters.min_price
    if filters.max_price is not None:
        result["max_price"] = filters.max_price

    return result


'''
Testing :
/store/3/products/452?search-keyword=shoes&sort-by=price&min_price=10.0&max_price=500.0&page=2&page-size=20
'''