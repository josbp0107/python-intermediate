import json

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Rappi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'NASA',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Globant',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'SENA',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    for worker in all_python_devs:
        print(worker)
    
    print("#"*100)

    all_python_devs_filter = list(filter(lambda worker: worker["language"]== "python", DATA))
    for worker in all_python_devs_filter:
        print(worker)
    
    print("#"*100)

    all_globant_workers = list(filter(lambda worker: worker["organization"]== "Globant", DATA))
    for worker in all_globant_workers:
        print(worker)

    print("#"*100)

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    for worker in adults:
        print(worker)
    
    print("#"*100)

    # | o pipe, nos ayuda a unir un diccionario con otro 
    old_people = list(map(lambda worker: worker | {"old":worker["age"]>70}, DATA))
    for worker in old_people:
        parse_dict = json.dumps(worker, ensure_ascii=False,  indent=4)
        print(parse_dict)

    print("#" * 100)

    old_people_comperhension = [worker["name"] for worker in DATA if worker["age"] > 18]
    print(old_people_comperhension)

if __name__ == '__main__':
    run()