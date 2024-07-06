def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Saud", "Lucknow")  # positional argument
# if we change the position of name and location then it will change the output

# so we can use keyword argument to specify the arguments which is not effected by position of input
greet_with(location="Lucknow", name="Saud")
