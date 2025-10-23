def get_cats_info(path: str) -> list[dict[str, str | int]]:
    cats = []# Initialize empty list
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(',') # Split by comma
            if len(parts) == 3 and parts[2].isdigit():# Check if age is a digit
                cats.append({"id": parts[0], "name": parts[1], "age": int(parts[2])}) # Convert age to int
    return cats
print(get_cats_info("cats_file.txt"))
