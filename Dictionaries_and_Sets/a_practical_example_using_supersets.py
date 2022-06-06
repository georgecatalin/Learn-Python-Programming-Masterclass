required_skills = ["C++", "Qt", "Linux", "GitHub"]

candidates = {
    "Cornel": { "Java", "Javascript", "C", "Linux"},
    "Mircea": {"Qt", "GitHub", "C++", "Linux", "Windows"},
    "Mirela": {"Python", "Ruby", "Windows"},
    "George": {"C++", "C", "Python", "C#", "SQL", "Linux", "Windows", "GitHub", "Qt"},
}

selected_for_interview = set()

for name, skills in candidates.items():
    #if skills.issuperset(required_skills): # the set methods apply to all kind of iterables, including lists, tuples, etc
    if skills > set(required_skills):   # the set operators only apply to sets
        selected_for_interview.add(name)

print(selected_for_interview)