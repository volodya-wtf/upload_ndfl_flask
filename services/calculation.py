from .dataclasses import ExtractedData, CalculatedData, CalculatedItem


class CalculationService:
    @staticmethod
    def calculate(data: ExtractedData) -> CalculatedData:
        calculated_data = CalculatedData()
        for item in data.items:
            affiliate = item.affiliate
            employee = item.employee
            tax_base = item.tax_base
            total = item.total

            if tax_base < (5000000 * 100):
                total_formula = int(tax_base * 0.13)
            else:
                total_formula = int(tax_base * 0.13)

            deviations = total - total_formula

            calculated_data.add_item(
                CalculatedItem(
                    affiliate=affiliate,
                    employee=employee,
                    tax_base=tax_base,
                    total=total,
                    total_formula=total_formula,
                    deviations=deviations,
                ),
            )

        return calculated_data
