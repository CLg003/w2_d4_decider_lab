from src import task

# 3rd VERSION BASED ON JACOB & MAX'S DICTIONARY SOLUTION:

def task_decider(task1, task2):
    task_options = {
        "Wash Dishes" : ["Cook Dinner", "Wash Clothes"],
        "Cook Dinner" : ["Clean Windows", "Do Ironing"],
        "Do Ironing" : ["Wash Clothes", "Wash Dishes"],
        "Wash Clothes" : ["Cook Dinner", "Clean Windows"],
        "Clean Windows" : ["Wash Dishes", "Do Ironing"]
    }
    if task2.description in task_options[task1.description]:
        return task1
    else:
        return task2


# CLEANED UP AND REFACTORED AFTER DISCUSSING SOLUTIONS:

# def task_decider(task1, task2):
#     if (task1.description == "Wash Dishes") and (task2.description == "Cook Dinner" or task2.description == "Wash Clothes"):
#         return task1
#     elif (task1.description == "Cook Dinner") and (task2.description == "Clean Windows" or task2.description == "Do Ironing"):
#         return task1
#     elif (task1.description == "Do Ironing") and (task2.description == "Wash Clothes" or task2.description == "Wash Dishes"):
#         return task1
#     elif (task1.description == "Wash Clothes") and (task2.description == "Cook Dinner" or task2.description == "Clean Windows"):
#         return task1
#     elif (task1.description == "Clean Windows") and (task2.description == "Wash Dishes" or task2.description == "Do Ironing"):
#         return task1
#     else:
#         return task2

# OUR ORIGINAL SOLUTION (Cordii & me):

# def task_decider(task1, task2):
#     task_options = [task1.description, task2.description]
#     if ("Wash Dishes" in task_options and "Cook Dinner" in task_options) or ("Wash Dishes" in task_options and "Wash Clothes" in task_options):
#         return "Wash Dishes"
#     elif ("Cook Dinner" in task_options and "Clean Windows" in task_options) or ("Cook Dinner" in task_options and "Do Ironing" in task_options):
#         return "Cook Dinner"
#     elif ("Do Ironing" in task_options and "Wash Clothes" in task_options) or ("Do Ironing" in task_options and "Wash Dishes" in task_options):
#         return "Do Ironing"
#     elif ("Wash Clothes" in task_options and "Cook Dinner" in task_options) or ("Wash Clothes" in task_options and "Clean Windows" in task_options):
#         return "Wash Clothes"
#     else:
#         return "Clean Windows"