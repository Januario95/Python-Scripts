import pandas as pd


class School:
    def __init__(self, location, nr_of_students, price_per_student):
        self.location = location
        self.nr_of_students = nr_of_students
        self.price_per_student = price_per_student

    def cost(self):
        return self.nr_of_students * self.price_per_student
    

class CostClass:
    def __init__(self, schools=[]):
        for school in schools:
            if not isinstance(school, School):
                raise TypeError('school must be an instance of School class')
        self.schools = schools

    @property
    def dataframe(self):
        data = []
        for school in self.schools:
            row = {
                'Location': school.location,
                'Nr of students': school.nr_of_students,
                'Price per student': school.price_per_student,
                'Total cost': school.cost()
            }
            data.append(row)
        df = pd.DataFrame(data)
        df = df.append(df.sum(axis=0), ignore_index=True)
        return df

    def total_cost(self):
        total = 0
        for school in self.schools:
            total += school.cost()
        return total

cost = CostClass([
    School(location='Maputo', nr_of_students=150, price_per_student=300),
    School(location='Maputo', nr_of_students=100, price_per_student=300),
    School(location='Lichinga', nr_of_students=300, price_per_student=215),
    School(location='Pemba', nr_of_students=500, price_per_student=215),
    School(location='Quelimane', nr_of_students=200, price_per_student=275),
    School(location='Tete', nr_of_students=200, price_per_student=225)
])
total = cost.total_cost()
print(total * 0.30)
df = cost.dataframe
# print(df['Total cost'].value_counts(normalize=True))
# print(df['Total cost'].sum(axis=0))
# print(df.append(df.sum(axis=0), ignore_index=True))


            