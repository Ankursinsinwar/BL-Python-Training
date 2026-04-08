from fastapi import APIRouter
import get_data as request

route = APIRouter()



@route.get("/")
def get_data():
    return request.get_data()


@route.get("/get-count-of-pics/")
def get_data_by_id():
    return request.get_no_of_pic()
    
