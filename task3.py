def plural_computer(num: int) -> str:
    if num % 10 in (5, 6, 7, 8, 9, 0) or num in range(11, 20):
        return 'компьютеров'
    elif num % 10 in (2, 3, 4):
        return 'компьютера'
    return 'компьютер'
