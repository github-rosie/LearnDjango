# https://docs.djangoproject.com/en/5.0/intro/tutorial02/
# https://docs.djangoproject.com/en/5.0/topics/db/queries/
# https://docs.djangoproject.com/en/5.0/ref/models/relations/
# https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups-intro


from polls.models import Choice, Question
from django.utils import timezone

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.

# objects.all() displays all the questions in the database.
Question.objects.all()

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
q1 = Question(question_text="What's for lunch?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q1.save() 

# Now it has an ID auto generated
q1.id

# Access model field values via Python attributes
q1.question_text
q1.pub_date

# Change values by changing the attributes, then calling save().
q1.question_text = "What's for dinner?"
q1.save()

# filter functions
Question.objects.filter(id=2)
Question.objects.filter(question_text__startswith="What")

# Get the question that was published this year.
current_year = timezone.now().year
print(current_year)
Question.objects.get(pub_date__year=current_year)

# Request an ID that doesn't exist, this will raise an exception.
q4 = Question.objects.get(id=2)
q4.question_text = "What's for lunch?"
q4.save()
q4

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)

# Make sure our custom method worked.
q5 = Question.objects.get(pk=2)
q5.was_published_recently()

# Create three choices 
q5.choice_set.create(choice_text="Steak Sandwich", votes=0)
q5.choice_set.create(choice_text="Pesto Pasta", votes=0)
q5.choice_set.create(choice_text="Greek Salad", votes=0)
q5.choice_set.all()
q5.choice_set.count()

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=current_year)

# Let's delete one of the choices. Use delete() for that.
c1 = q5.choice_set.filter(choice_text__startswith="Greek")
c1
c1.delete()
