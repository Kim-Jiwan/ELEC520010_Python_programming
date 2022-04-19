import string as st

upper_case = st.ascii_uppercase

print(upper_case)

for i in range(10):
    print(upper_case[i::] + upper_case[0 : i])