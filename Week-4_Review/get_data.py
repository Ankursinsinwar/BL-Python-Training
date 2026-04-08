import requests
import json



def get_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        if response.status_code == 200:
            with open(f'data.json', 'w') as file:
                print(response.json())
                json.dump(response.json(), file, indent=4)
            return response.json()
        else:
            return {"message": " Can't fetch data"}
    except Exception as e:
        return {"error": f"{e}"}



def get_no_of_pic():
    data = []
    try:
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        if users.status_code == 200:
            # print(users)
            if users.status_code == 200:
                # print(users.json())
                for user in users.json():
                    picno = {}
                    picno[user['name']] = get_data_by_id(user['id'])
                    data.append(picno)
                return data
    except Exception as e:
        return {"error": f"{e}"}


def get_data_by_id(user_id):
    try:
        api = f"https://jsonplaceholder.typicode.com/albums?userId={user_id}"
        print(api)
        albums_of_user = requests.get(api)
        # print(albums_of_user)
        no_of_pic = 0
        if albums_of_user.status_code == 200:
            # print(albums_of_user.json())
            for album in albums_of_user.json():
                # print(album)
                no_of_pic = get_pic_by_albumb(album['id'], no_of_pic)
                # print(no_of_pic)
            return no_of_pic
        else:
            return {"message": " Can't fetch data"}
    except Exception as e:
        return {"error": f"{e}"}


def get_pic_by_albumb(album_id, count):
    pic_response = requests.get(f"https://jsonplaceholder.typicode.com/photos?albumId={album_id}")
    if pic_response.status_code == 200:
        # print(pic_response.json())
        for pic in pic_response.json():
            count += 1
        return count
    else:
        return {"message": " Can't fetch data"}