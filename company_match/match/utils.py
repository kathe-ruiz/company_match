def get_format_skills(skills):
    data = {}
    if skills:
        data_list = []
        for skill in skills:
            item = {}
            item["skill/role"] = {
                "text": skill["name"],
                "experience": "potential-to-develop",
            }
            data_list.append(item)
    data["or"] = data_list
    return data
