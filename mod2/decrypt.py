"3"
def decrypt(s: str) -> str:
    result = []

    for i in s:
        result.append(i)
        if len(result) > 2 and (result[-1], result[-2]) == ('.', '.'):
            result.pop()
            result.pop()
            if result:
                result.pop()
    return "".join(ch for ch in result if ch != '.')