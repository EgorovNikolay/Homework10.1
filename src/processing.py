from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Возвращает список словарей по значению. По умолчанию 'EXECUTED'"""
    result = []
    for i in data:
        if i.get("state") == state:
            result.append(i)
    return result
