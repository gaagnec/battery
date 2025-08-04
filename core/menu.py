from admin_tools.menu import items, Menu

class CustomMenu(Menu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.children += [
            items.MenuItem('Главная панель', '/admin/'),
            items.MenuItem('Список клиентов', '/clients/'),
            items.MenuItem('Главная сайта', '/'),
            items.AppList('Все приложения', exclude=('auth.*',)),
        ]
