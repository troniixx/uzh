def where_is_waldo(list):
     if "Waldo" not in list:
          return None
     else:
          return list.find("Waldo")


print(where_is_waldo(["Peter", "Waldo", "John"]))
