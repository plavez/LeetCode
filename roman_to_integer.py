class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # Проходим строку справа налево
            current_value = roman_values[char]
            if current_value < prev_value:
                total -= current_value  # Вычитаем, если меньше предыдущего
            else:
                total += current_value  # Добавляем, если больше или равно
            prev_value = current_value

        return total


# Пример использования:
solution = Solution()
print(solution.romanToInt("XX"))  # Вывод: 1994
