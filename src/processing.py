from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает список словарей по значению. По умолчанию 'EXECUTED'"""
    result = []
    for i in data:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(data: List[Dict], sort: bool = True) -> List[Dict]:
    """Функия, сортирующая список по дате"""
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=sort)
    return sorted_list
