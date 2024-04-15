from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_url(self):
        a = self.url.split("/")[3:]
        remainder = "" if not "".join(a) else "/"
        a = "/" + "/".join(a) + remainder
        return a
    
    def get_parent_id(self):
        return None if not self.parent else self.parent.id
