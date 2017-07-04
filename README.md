# A Tutoron that Shows Insights About Java Classes

This Tutoron searches for classes from the core Java API
in code on a web page, and makes insights about those
classes available in a tooltip.

Currently, this only provides toy insights for `ArrayList`
and `LinkedList`, from [Christoph Treude and Martin
Robillard's
paper](https://ctreude.files.wordpress.com/2016/01/icse16a.pdf)
on extracting insightful sentences about API members from
Stack Overflow posts.  Additional insights can be added
easily by adding additional rules to the `insights.py` file.

## Getting started

First, set up the Tutorons server following the instructions
at https://github.com/andrewhead/tutorons-base.

Then, add the Java classes Tutoron as a submodule to the
server:

```bash
git submodule add \
  https://github.com/andrewhead/Tutoron-Java-Classes \
  tutorons/modules/java_classes
```

Add the Tutoron as an "app" to the Tutorons server by adding
the following line to the list of `INSTALLED_APPS` in the
`tutorons/settings/defaults.py` file:

```python
    'tutorons.modules.java_classes',
```

Point the Tutorons server to the URLs from the Java classes
Tutoron.  You can do this by adding these two URL patterns
to the list of URL patterns in `tutorons/urls.py`:

```python
    url(r'^java_classes$', 'tutorons.modules.java_classes.views.scan', name='java_classes'),
    url(r'^java_classes/', include('tutorons.modules.java_classes.urls', namespace='java_classes')),
```

Then you can start playing around with the server!  Start
running the server with this command:

```bash
./rundevserver.sh
```

Go to http://localhost:8002/java_classes/example.  The
`ArrayList` Java class has been detected on the page.  By
clicking on the highlighted word `ArrayList`, you can see
the example explanation for this class.
