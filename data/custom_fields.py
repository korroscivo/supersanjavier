from django.db import models


class CustomCharField(models.CharField):
    description = "CharField"
    is_searchable = False

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomEmailField(models.EmailField):
    description = "EmailField"
    is_searchable = False

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomDateTimeField(models.DateTimeField):
    description = "DateTimeField"
    is_searchable = False

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomAutoField(models.AutoField):
    description = "AutoField"

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        
class CustomIntegerField(models.IntegerField):
    description = "IntegerField"

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomMoneyField(models.IntegerField):
    description = "MoneyField"

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomBooleanField(models.BooleanField):
    description = "BooleanField"

    def __init__(self, hidden=False, is_searchable = False, is_sortable = False, read_only = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hidden = hidden
        self.is_searchable = is_searchable
        self.is_sortable = is_sortable
        self.read_only = read_only
        
class CustomForeignKey(models.ForeignKey):
    description = "ForeignKey"

    def __init__(self, *args, hidden=False, is_sortable = False, **kwargs):
        self.hidden = hidden
        self.is_sortable = is_sortable
        
        super().__init__(*args, **kwargs)
