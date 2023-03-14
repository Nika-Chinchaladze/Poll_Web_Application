class DefineField:
    def __init__(self):
        self.field_name = ""
    
    def get_field_name(self, about_name):
        if about_name == "Workplace":
            self.field_name = "work"
        elif about_name == "University":
            self.field_name = "university"
        elif about_name == "City Name":
            self.field_name = "city"
        elif about_name == "Country Name":
            self.field_name = "country"
        elif about_name == "Relationship Status":
            self.field_name = "love"
        elif about_name == "Phone Number":
            self.field_name = "phone"
        return self.field_name


class ReturnChartData:
    def __init__(self):
        self.hello = "world"
    
    def get_chart_data(self, poll_questions, occurences):
        my_result = []

        for item in range(len(poll_questions)):
            current_question = poll_questions.get(id=(item+1))
            my_result.append([
                {"answer": current_question.answer_1, "count": 0},
                {"answer": current_question.answer_2, "count": 0},
                {"answer": current_question.answer_3, "count": 0},
                {"answer": current_question.answer_4, "count": 0}
            ])
        
        for my_item in occurences:
            for my_list in my_result:
                for my_dict in my_list:
                    if my_dict["answer"] == my_item["answer"]:
                        my_dict["count"] = my_item["count"]
                    else:
                        pass
        
        return my_result
    