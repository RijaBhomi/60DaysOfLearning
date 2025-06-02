'''
Jan -> January
Feb -> February
'''

monthConversion= {
    "Jan": "January",
    # key: "value"
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Jan"])  # January
print(monthConversion.get("Feb"))  # February

print(type(monthConversion))  # <class 'dict'>



