
with open('ваша_фамилия.txt', 'w', encoding='utf-8') as file:
    file.write("Иванов\n")
    file.write("Петров\n")
    file.write("Сидоров\n")

with open('ваша_фамилия.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print("Содержимое файла:")
for line in lines:
    print(line.strip())