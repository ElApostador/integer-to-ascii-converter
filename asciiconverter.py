ascii_codes = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

ascii_characters = [chr(code) for code in ascii_codes]
result = "".join(ascii_characters)

print(result)
