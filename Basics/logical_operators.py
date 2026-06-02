has_degree = True
knows_python = True
has_experience = False

print("Has Degree:", has_degree)
print("Knows Python:", knows_python)
print("Has Experience:", has_experience)

if has_degree and knows_python:
    print("\nEligible for Interview")

if knows_python or has_experience:
    print("Can Apply for Internship")

if not has_experience:
    print("Needs More Experience")