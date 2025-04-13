class HRDatabaseRouter:
    """
    A database router to direct Employee models to PostgreSQL
    and PerformanceReview models to MongoDB.
    """

    def db_for_read(self, model, **hints):
        """Point read queries to the appropriate database."""
        if model._meta.app_label == 'hr_app':
            if model._meta.model_name == 'employee':
                return 'default'  # PostgreSQL
            elif model._meta.model_name == 'performancereview':
                return 'mongodb'  # MongoDB
        return None

    def db_for_write(self, model, **hints):
        """Point write queries to the appropriate database."""
        if model._meta.app_label == 'hr_app':
            if model._meta.model_name == 'employee':
                return 'default'  # PostgreSQL
            elif model._meta.model_name == 'performancereview':
                return 'mongodb'  # MongoDB
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships only within the same database."""
        if obj1._state.db == obj2._state.db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations only happen on the correct database."""
        if app_label == 'hr_app':
            if model_name == 'employee':
                return db == 'default'  # Only migrate Employee in PostgreSQL
            elif model_name == 'performancereview':
                return db == 'mongodb'  # Only migrate PerformanceReview in MongoDB
        return None
