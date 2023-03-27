from services import data_extractor, calculation, data_writer


def main():
    extracted = data_extractor.ExtractDataService.extract("data.xlsx")
    calculated = calculation.CalculationService.calculate(extracted.items)
    data_writer.WriteCalculatedDataService.write(calculated, "foo.xlsx")


if __name__ == "__main__":
    main()
