import math

import pandas as pd

from .dataclasses import ExtractedData, ExtractedItem
from .exceptions import DataError, InputError


class ExtractDataService:
    def _convert_money_to_int(value: float) -> int:
        if not isinstance(value, float):
            raise DataError(value)
        if math.isnan(value):
            return 0
        else:
            floor = math.floor(value)
            return int((floor * 100) + ((value - floor) * 100))

    @staticmethod
    def extract(path: str) -> ExtractedData:
        extracted_data = ExtractedData()

        raw_data = pd.read_excel(path, index_col=1, header=1)
        raw_data = raw_data[:-1]  # remove last element

        for row in raw_data.itertuples():
            if len(row) == 7:
                affiliate = row[0]
                employee = row[1]
                accrued = row[2]
                total_deductions = row[3]
                tax_base = row[4]
                total = row[5]
                retained_in_total = row[6]

                extracted_data.add_item(
                    ExtractedItem(
                        affiliate=affiliate,
                        employee=employee,
                        accrued=ExtractDataService._convert_money_to_int(accrued),
                        total_deductions=ExtractDataService._convert_money_to_int(
                            total_deductions
                        ),
                        tax_base=ExtractDataService._convert_money_to_int(tax_base),
                        total=ExtractDataService._convert_money_to_int(total),
                        retained_in_total=ExtractDataService._convert_money_to_int(
                            retained_in_total
                        ),
                    )
                )

            else:
                raise InputError(row)

        return extracted_data
