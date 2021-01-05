
### model
- The makemigrations command looks at all your available models and creates migrations for whichever tables don’t already exist. 
- migrate runs the migrations and creates tables in your database, as well as optionally providing much richer schema control.

### views
- Once one of the URL patterns matches in urls.py, Django calls the given view, which is a Python function. 
- Each view gets passed a request object – which contains request metadata – and the values captured in the pattern.
- Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. 

#### API views
- The @api_view decorator for working with function based views.
- The APIView class for working with class-based views.

#### ViewSets & Routers
- REST framework includes an abstraction for dealing with ViewSets, that allows the developer to concentrate on modeling the state and interactions of the API, and leave the URL construction to be handled automatically, based on common conventions.
- ReadOnlyModelViewSet class automatically provides the default 'read-only' operations (list and retrieve).
- ModelViewSet class provides the complete set of default read and write operations.
- When using ViewSet classes, the conventions for wiring up resources into views and urls can be handled automatically by a Router class.
- ViewSet helps ensure that URL conventions will be consistent across your API, minimizes the amount of code you need to write. But using viewsets is less explicit than building your views individually.

### Serializer
- It's important to remember that ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:
  - An automatically determined set of fields.
  - Simple default implementations for the create() and update() methods.
