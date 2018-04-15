import question_temp
import word_tagging

class Question2Sparql:
    """
    Converter for transforming natural language questions
    to Sparql querys
    """
    def __init__(self, dict_paths):
        """
        load external dict for word tokenizing and tagging,
        and question templates for converting NL to query

        :param dict_paths: paths where user dict located | string
        """
        self.wt = word_tagging.Tagger(dict_paths)
        self.rules = question_temp.rules

    def get_sparql(self, question):
        word_objects = self.wt.get_word_objects(question)
        queries_dict = {}

        for rule in self.rules:
            query, num = rule.apply(word_objects)

            if query:
                queries_dict[num] = query
        
        # print(queries_dict)
        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return list(queries_dict.values())[0]
        else:
            sorted_dict = sorted(list(queries_dict.items()), key=lambda item: item[1])
            return sorted_dict[0][1]