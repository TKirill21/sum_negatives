def max_dragon_strength(N):
    if N == 0:
        return 0

    # Максимальное число голов у одного дракона
    max_heads_per_dragon = 7
    
    # Количество полных драконов
    full_dragons = N // max_heads_per_dragon
    
    # Остаток голов
    remainder = N % max_heads_per_dragon
    
    # Если есть остаток, то добавляем его как отдельного дракона
    if remainder > 0:
        full_dragons += 1

    # Произведение
    # Максимальная сила будет равна (7 ^ полные драконы) * (остаток если есть)
    strength = (max_heads_per_dragon ** (full_dragons - (1 if remainder > 0 else 0))) * (remainder if remainder > 0 else 1)
    
    return strength

# Пример использования
N = int(input("Введите количество голов драконьей стаи: "))
result = max_dragon_strength(N)
print("Максимально возможная сила драконьей стаи:", result)
