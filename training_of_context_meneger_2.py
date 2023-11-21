class Example():
    def __init__(self):
        print("Вызов метода __init__")
    def __enter__(self):
        print("Вызов метода __enter__")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вызов метода __exit__")
        if exc_type == Exception:
            print(f"Тип ошибки{exc_type}\nЗначение ошибки{exc_val}\nСлед.ошибки{exc_tb}")
my_obj = Example()
with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')