"""Ülesanne 28. Õpilaste hinnete analüüs"""


def analuusi(hinded):
    return {"keskmine": sum(hinded)/len(hinded) if hinded else None,
            "viisi": hinded.count(5), "kolmesi": hinded.count(3)}
assert analuusi([5,4,3,5]) == {"keskmine": 4.25, "viisi": 2, "kolmesi": 1}
assert analuusi([])["keskmine"] is None
