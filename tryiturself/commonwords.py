def compare_counts(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read().lower()

    except FileNotFoundError:
        print(f"{filename} not found.")

    else:
        count_the = contents.count('the')
        count_the_space = contents.count('the ')

        print(f"\n{filename}")
        print(f"'the'  : {count_the}")
        print(f"'the ' : {count_the_space}")


files = ['on_shipboard.txt']

for file in files:
    compare_counts(file)