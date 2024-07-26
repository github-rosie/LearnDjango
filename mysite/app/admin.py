
from django.contrib import admin
from import_export import resources
from mysite.app.models import Book


# Register your models here.

class BookResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return row["delete"] == "1"

    class Meta:
        """ The model attribute inside the Meta class specifies which Django model the ModelResource should be linked to. In this case, it's the Book model from .models.py
        """
        model = Book
        

def import_data():
    import tablib
    book_resource = resources.modelresource_factory(model=Book)()
    dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
    result = book_resource.import_data(dataset, dry_run=True)
    print(result.has_errors())    
    

def delete_data():
    pass


def export_data():
    dataset = BookResource().export()
    print(dataset.csv)