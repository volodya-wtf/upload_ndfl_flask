import math

import pandas as pd

from .dataclasses import CalculatedData


class WriteCalculatedDataService:
    @staticmethod
    def _convert_money_to_pretty(value: int) -> float:
        if math.isnan(value):
            return math.isnan(float("nan"))
        else:
            return (value // 100) + ((value - ((value // 100) * 100)) / 100)

    @staticmethod
    def write(data: CalculatedData, path: str):
        to_write = {
            "affiliate": [],
            "employee": [],
            "tax_base": [],
            "total": [],
            "total_formula": [],
            "deviations": [],
        }

        for item in data.items:
            to_write["affiliate"].append(item.affiliate)
            to_write["employee"].append(item.employee)

            to_write["tax_base"].append(
                WriteCalculatedDataService._convert_money_to_pretty(item.tax_base)
            )
            to_write["total"].append(
                WriteCalculatedDataService._convert_money_to_pretty(item.total)
            )
            to_write["total_formula"].append(
                WriteCalculatedDataService._convert_money_to_pretty(item.total_formula)
            )
            to_write["deviations"].append(
                WriteCalculatedDataService._convert_money_to_pretty(item.deviations)
            )

        df = pd.DataFrame(data=to_write)
        df.to_excel(path, index=False)
