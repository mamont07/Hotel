
users = [
    {
        'username': 'lox',
        'password': '1111',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': [],
        'created_at': '2024-09-01'
    },
    {
        'username': 'admin',
        'password': '1234',
        'role': 'admin'
    }
]
services = [
    {'name': 'Номер стандарт', 'price': 2500, 'availability': True, 'booked_count': 0},
    {'name': 'Номер люкс', 'price': 5000, 'availability': True, 'booked_count': 0}
]


def login(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None


def view_services():
    print("Доступные услуги:")
    for service in services:
        print(f"{service['name']} - {service['price']} руб. (Доступно: {'Да' if service['availability'] else 'Нет'})")


def book_service(username, service_name):
    service = next((s for s in services if s['name'] == service_name and s['availability']), None)
    if service:
        user = next(u for u in users if u['username'] == username)
        user['history'].append(service_name)
        service['booked_count'] += 1  # Увеличиваем количество бронирований
        print(f"Услуга '{service_name}' успешно забронирована!")
    else:
        print("Услуга недоступна.")


def update_user_data(username):
    user = next(u for u in users if u['username'] == username)
    new_username = input("Введите новый логин (или оставьте пустым для сохранения): ")
    new_password = input("Введите новый пароль (или оставьте пустым для сохранения): ")

    if new_username:
        user['username'] = new_username
    if new_password:
        user['password'] = new_password

    print("Данные пользователя успешно обновлены.")


def admin_view_users():
    print("Список пользователей:")
    for user in users:
        print(f"- {user['username']} (Роль: {user['role']})")


def add_service(service_name, price):
    new_service = {'name': service_name, 'price': price, 'availability': True, 'booked_count': 0}
    services.append(new_service)
    print(f"Услуга '{service_name}' успешно добавлена.")


def remove_service(service_name):
    global services
    services = [s for s in services if s['name'] != service_name]
    print(f"Услуга '{service_name}' успешно удалена.")


def update_service(service_name):
    service = next((s for s in services if s['name'] == service_name), None)
    if service:
        new_name = input("Введите новое название услуги (или оставьте пустым для сохранения): ")
        new_price = input("Введите новую цену услуги (или оставьте пустым для сохранения): ")

        if new_name:
            service['name'] = new_name
        if new_price:
            service['price'] = float(new_price)

        print(f"Данные об услуге '{service_name}' успешно обновлены.")
    else:
        print("Услуга не найдена.")


def view_statistics():
    print("Статистика по купленным услугам:")
    for service in services:
        print(f"{service['name']} - {service['booked_count']} бронирований")


# Интерфейс для пользователя
def user_interface(user):
    while True:
        print("\nДобро пожаловать!")
        print("Выберите действие:")
        print("1. Просмотреть доступные услуги")
        print("2. Забронировать услугу")
        print("3. Посмотреть историю")
        print("4. Изменить данные")
        print("5. Выйти")

        choice = input("Ваш выбор: ")
        if choice == '1':
            view_services()
        elif choice == '2':
            service_name = input("Введите название услуги для бронирования: ")
            book_service(user['username'], service_name)
        elif choice == '3':
            print("Ваша история бронирований:", user['history'])
        elif choice == '4':
            update_user_data(user['username'])
        elif choice == '5':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


# Интерфейс для администратора
def admin_interface():
    while True:
        print("\nПанель администратора:")
        print("1. Просмотреть пользователей")
        print("2. Добавить услугу")
        print("3. Удалить услугу")
        print("4. Изменить услугу")
        print("5. Просмотреть статистику")
        print("6. Выйти")

        choice = input("Ваш выбор: ")
        if choice == '1':
            admin_view_users()
        elif choice == '2':
            service_name = input("Введите название услуги: ")
            price = float(input("Введите цену услуги: "))
            add_service(service_name, price)
        elif choice == '3':
            service_name = input("Введите название услуги для удаления: ")
            remove_service(service_name)
        elif choice == '4':
            service_name = input("Введите название услуги для изменения: ")
            update_service(service_name)
        elif choice == '5':
            view_statistics()
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


# Основная программа
def main():
    print("Добро пожаловать в онлайн-гостиницу!")
    username = input("Логин: ")
    password = input("Пароль: ")

    user = login(username, password)
    if user:
        if user['role'] == 'admin':
            admin_interface()
        else:
            user_interface(user)
    else:
        print("Неверное имя пользователя или пароль.")


if __name__ == "__main__":
    main()

