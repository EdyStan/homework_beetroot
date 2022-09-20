def make_country(name, capital):
    my_dict = {"name": name, "capital": capital}
    for i in my_dict.values():
        print(i)


out_name = input("Name: ")
out_capital = input("capital: ")
make_country(out_name, out_capital)
