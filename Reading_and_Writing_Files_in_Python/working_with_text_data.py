input_file_name = "country_info.txt"
countries = {}


with open(input_file_name)  as my_file:
    my_file.readline()
    for row in my_file:
        data = row.strip("\n").split("|")
        country, capital, country_code, code3, dialling_code, timezone, currency = data
        # print(country, country_code, code3, dialling_code, timezone, currency, sep="\n\t")
        country_dictionary = {
            "country": country,
            "country_code": country_code,
            "international_code_3": code3,
            "dialling_code": dialling_code,
            "timezone":  timezone,
            "currency": currency
        }
        print(country_dictionary)

        countries[country_code.casefold()] = country_dictionary

print(countries)