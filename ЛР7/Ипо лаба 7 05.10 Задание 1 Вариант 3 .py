
months = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль") # Создаем кортеж с названиями месяцев
new_tu = months[:3] # Создаем новый кортеж new_tu из первых трех элементов исходного кортежа
new_tu2 = months[3:]# Создаем новый кортеж new_tu2 из четырех оставшихся элементов исходного кортежа
all_tu = (months, new_tu, new_tu2) # Создаем кортеж all_tu, который содержит все три кортежа
print("Исходный кортеж:", months)
print("new_tu (первые три элемента):", new_tu)
print("new_tu2 (четыре оставшихся элемента):", new_tu2)
print("all_tu (содержит все кортежи):", all_tu)