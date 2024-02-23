def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            cats_info = []

            for line in lines:
                cat_id, name, age = line.strip().split(',')
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)

            return cats_info

    except Exception:
        pass

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)
