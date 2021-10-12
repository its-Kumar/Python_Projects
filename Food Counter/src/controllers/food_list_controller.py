from src.services.food_list_service import get_food_list, add_to_food_list, delete_item_to_food_list, get_list_by_date_to_food_list


def get_list():
    return get_food_list()


def send_to_food_list(**kwargs):
    item = kwargs.get('body')
    return add_to_food_list(item)


def delete_item(id):
    id = int(id)
    return delete_item_to_food_list(id)


def get_list_by_date(**kwargs):
    date = kwargs['date']
    return get_list_by_date_to_food_list(date)