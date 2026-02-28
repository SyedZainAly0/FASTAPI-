from fastapi import APIRouter, Query
from typing import Annotated

route = APIRouter()

@route.get("/testing2.0")
def system_testing(
    testing_id: int | None,

    testingplace: Annotated[
        str | None,
        Query(
            min_length=5,
            max_length=50,
            alias="test_place",
            description="Reason for testing (5–50 characters)",
            deprecated=True,
            include_in_schema=False,
        )
    ] = "Trying....",

    testingreason: Annotated[
        str | None,
        Query(
            min_length=5,
            max_length=50,
            alias="test_reason",
            description="Reason for testing (5–50 characters)",
            deprecated=True
        )
    ] = "Trying....",

    testingexpense: Annotated[
        int,
        Query(gt=0, title="Testing Expense")
    ] = 1
):
    return {
        "ID": testing_id,
        "Place": testingplace,
        "Reason": testingreason,
        "Expense": testingexpense,
    }