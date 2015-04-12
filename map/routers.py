
class CoordinatorRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        "Point all operations on chinook models to 'chinookdb'"
        """
        if model.__name__ == 'Report':
          return 'reports'
        if model._meta.app_label == 'map':
            return 'default'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model.__name__ == 'Report':
          return 'reports'
        if model._meta.app_label == 'map':
            return 'default'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'map' and obj2._meta.app_label == 'map':
            return True
        # Allow if neither is chinook app
        elif 'default' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'default' or model._meta.app_label == "map":
            # we're not using syncdb on our legacy database
            return False
        else:
            # but all other models/databases are fine
            return True