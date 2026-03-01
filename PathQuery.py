from typing import Annotated
from fastapi import FastAPI, Path, Query, APIRouter

app = APIRouter()


@app.get("/store/{category_id}/products/{product_id}")
async def get_product(
    
    category_id: Annotated[int,
        Path(
            description="The ID of the product category. Must be between 1 and 500.",
            ge=1,
            le=500,
        ),
    ],

    product_id: Annotated[
        int,
        Path(
            description="The unique ID of the product. Must be greater than 0.",
            gt=0,
            lt=10000,
        ),
    ],

    search: Annotated[
        str | None,
        Query(
            description="A keyword to search within the product. Between 3 and 50 characters.",
            min_length=3,
            max_length=50,
            alias="search-keyword",
            include_in_schema=True,
        ),
    ] = None,

    sort_by: Annotated[
        str | None,
        Query(
            description="Field to sort results by. E.g. 'price', 'name', 'rating'.",
            min_length=2,
            max_length=20,
            alias="sort-by",
            include_in_schema=True,
        ),
    ] = None,

    min_price: Annotated[
        float | None,
        Query(
            description="Filter products with price greater than this value. Must be >= 0.",
            ge=0.0,
            lt=100000.0,
            include_in_schema=True,
        ),
    ] = None,

    max_price: Annotated[
        float | None,
        Query(
            description="Filter products with price less than or equal to this value.",
            gt=0.0,
            le=100000.0,
            include_in_schema=True,
        ),
    ] = None,

    page: Annotated[
        int,
        Query(
            description="Which page of results to return. Must be 1 or more.",
            ge=1,
            include_in_schema=True,
        ),
    ] = 1,

    page_size: Annotated[
        int,
        Query(
            description="How many results per page. Between 1 and 100.",
            ge=1,
            le=100,
            alias="page-size",
            include_in_schema=True,
        ),
    ] = 10,
):
    result = {
        "category_id": category_id,
        "product_id": product_id,
        "page": page,
        "page_size": page_size,
    }

    if search:
        result["search"] = search
    if sort_by:
        result["sort_by"] = sort_by
    if min_price is not None:
        result["min_price"] = min_price
    if max_price is not None:
        result["max_price"] = max_price

    return result



'''
Testing URL:
/store/3/products/452?search-keyword=shoes&sort-by=price&min_price=10.0&max_price=500.0&page=2&page-size=20
'''