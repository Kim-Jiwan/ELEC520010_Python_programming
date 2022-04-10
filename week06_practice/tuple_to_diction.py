student_tuple = (('191101', '카리나', '010-123-45xx'),
                 ('191102', '김민정', '010-223-45xx'),
                 ('191103', '지젤', '010-323-45xx'),
                 ('191104', '닝닝', '010-313-34xx'))
    
student_list = [['191101', '카리나', '010-123-45xx'],
                ['191102', '김민정', '010-223-45xx'],
                ['191104', '닝닝', '010-313-34xx']]

student_list_to_dict = {num : name for num, name, phone in student_list}
student_tuple_to_dict = {phone : name for num, name, phone in student_tuple}

studuent_dict = dict((student_tuple))

print(student_list_to_dict)
print(student_tuple_to_dict)