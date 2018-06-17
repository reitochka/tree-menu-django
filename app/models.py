from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def menu_items(self):
        return self.menuitem_set.all()


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_ancestors(self):
        if self.parent:
            return self.parent.get_ancestors() + [self.parent]
        else:
            return []

    def get_menu_list(self):
        child = [self.children()[0]] if self.children() else []
        return self.get_ancestors() + [self] + child

    def get_current_level(self):
        if self.parent:
            return self.parent.children()
        else:
            return MenuItem.objects.filter(menu=self.menu, parent__isnull=True)
