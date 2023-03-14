from django import template

register = template.Library()


@register.filter(name="return_first")
def return_first(value):
    """Turns String into list and Returns first element"""
    return value.split()[0]


@register.filter(name="find_contains")
def find_contains(value, item):
    """Returns True id item is among value"""
    value_users = [i.user.username for i in value]
    if item in value_users:
        return True
    else:
        return False


@register.filter(name="return_img_url")
def return_img_url(value, image_list):
    """Return user's image url"""
    user_image = image_list.filter(user=value).first()
    return user_image.image.url


@register.filter(name="range_filter")
def range_filter(value):
    return range(int(value))


@register.filter(name="access_answer")
def access_answer(value, my_list):
    return my_list[int(value)]["answer"]


@register.filter(name="access_count")
def access_count(value, my_list):
    return my_list[int(value)]["count"]


# ==============================================================
@register.filter(name="labels_by_index")
def labels_by_index(value, my_index):
    value = list(value)
    chosen_list = value[int(my_index)]
    my_labels = [item["answer"] for item in chosen_list]
    return my_labels


@register.filter(name="data_by_index")
def data_by_index(value, my_index):
    chosen_list = value[int(my_index)]
    my_data = [item["count"] for item in chosen_list]
    return my_data


@register.filter(name="check_existence")
def check_existence(value, my_user):
    my_list = list(value)
    if my_user in my_list:
        return True
    else:
        return False
