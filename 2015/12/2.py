import json
import sys


def evaluate_object(obj):
    if isinstance(obj, int):
        return obj
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        return sum(evaluate_object(a) for a in obj.values())
    if isinstance(obj, list):
        return sum(evaluate_object(a) for a in obj)
    return 0


print(evaluate_object(json.loads(sys.stdin.read())))
