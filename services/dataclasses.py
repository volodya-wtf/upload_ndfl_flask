from dataclasses import dataclass, field
from typing import List


@dataclass
class CalculatedItem:
    affiliate: str  # Филиал
    employee: str  # Сотрудник
    tax_base: int  # Налоговая база
    total: int  # Исчислено всего

    total_formula: int  # Исчислено всего по формуле
    deviations: int  # Отклонения


@dataclass
class CalculatedData:
    items: List[CalculatedItem] = field(default_factory=list)

    def add_item(self, item: CalculatedItem):
        self.items.append(item)


@dataclass
class ExtractedItem:
    affiliate: str  # Филиал
    employee: str  # Сотрудник
    accrued: int  # Начислено
    total_deductions: int  # Вычеты всего
    tax_base: int  # Налоговая база
    total: int  # Исчислено всего
    retained_in_total: int  # Удержано всего


@dataclass
class ExtractedData:
    items: List[ExtractedItem] = field(default_factory=list)

    def add_item(self, item: ExtractedItem):
        self.items.append(item)
