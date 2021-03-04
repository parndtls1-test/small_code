import csv
import pytest
import requests

PEOPLE_URL = 'https://swapi.dev/api/people/'
MAIN_LIST = []

def get_data_from_url(url):
    '''get data from url'''
    response = requests.get(url)
    return response.json()

def get_person_data(data):
    '''parse out person data: name, species, height, len films'''
    for person in data['results']:
        items = (person['name'], person['species'],
                 person['height'], len(person['films']))
        MAIN_LIST.append(items)

def get_species(alist):
    '''get species if url not blank, return new list'''
    newlist = []

    for i in alist:
        x = i[1]

        if x:
            response = requests.get(x[0])
            data = response.json()
            species = data['name']
        else:
            species = ''

        newlist.append((i[0], species, int(i[2]), i[3]))

    return newlist

def create_csv_and_send(alist):
    '''create the csv w/headers and send to httpbin.org/post'''
    with open('characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'species', 'height', 'appearances'])
        writer.writerows(alist)

    myurl = 'https://httpbin.org/post'
    files = {'file': open('characters.csv', 'rb')}
    getdata = requests.post(myurl, files=files)
    return getdata.text

def test_get_data_from_url():
    assert isinstance(get_data_from_url(PEOPLE_URL), dict)

def test_get_species():
    alist = [('Chewbacca', ['http://swapi.dev/api/species/3/'], '228', 4)]
    assert get_species(alist) == [('Chewbacca', 'Wookie', 228, 4)]
    alist = [('Palpatine', [], '170', 5)]
    assert get_species(alist) == [('Palpatine', '', 170, 5)]

def main():
    data = get_data_from_url(PEOPLE_URL)
    get_person_data(data)

    while data['next']:
        data = get_data_from_url(data['next'])
        get_person_data(data)

    most_films_list = sorted(MAIN_LIST, key = lambda x: x[3], reverse=True)[:10]
    height_list = sorted(most_films_list, key = lambda x: int(x[2]), reverse=True)

    final_list = get_species(height_list)
    done = create_csv_and_send(final_list)
    print(done)

if __name__ == '__main__':
    main()