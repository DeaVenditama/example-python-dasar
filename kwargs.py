def my_function(**kwargs):
    print("Hello my first name is", kwargs["first_name"],"and my last name is", kwargs["last_name"])

my_function(first_name = "Dea", last_name = "Venditama")
my_function(last_name = "Venditama", first_name = "Dea")