#Program to split arn

arn = "arn:aws:iam::123456789012:user/David"

print(arn.split("/"))
print(arn.split("/")[1])
print(arn.split("/")[0])

print(arn.upper())