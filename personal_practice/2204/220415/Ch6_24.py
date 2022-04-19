import string as st

upper_case = st.ascii_uppercase
incoding_case = upper_case[3::] + upper_case[0 : 3]
print(upper_case.index("A"))

print(f"{upper_case.index('A')}")
print(incoding_case[upper_case.index("A")])

