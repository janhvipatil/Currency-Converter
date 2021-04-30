with open('salary.txt', 'r') as sal, open('salary_year.txt', 'a') as sal_year:
    for lines in sal:
        sal_year.write(str(int(lines) * 12) + "\n")
