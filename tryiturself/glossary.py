glossary = {
    "variable": "A container used to store data values.",
    "list": "A collection of items stored in a particular order.",
    "tuple": "A collection of items that cannot be changed after it is created.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A structure that repeats a block of code.",
    "string": "A sequence of characters enclosed in quotes.",
    "integer": "A whole number without a decimal point.",
    "float": "A number that contains a decimal point.",
    "if statement": "A conditional statement used to make decisions in a program.",
    "function": "A reusable block of code that performs a specific task."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")