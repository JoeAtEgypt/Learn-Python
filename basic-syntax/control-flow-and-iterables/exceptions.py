# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass  # Multiple exceptions can be processed jointly.
else:  # Optional clause to the try/except block. Must follow
    # all except blocks.
    print("All good!")  # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print("We can clean up resources here")
