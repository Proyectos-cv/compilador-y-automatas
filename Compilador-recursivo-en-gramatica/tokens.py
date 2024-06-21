
class procedimientos:
    def __init__(self):
        pass

    def split_texto_into_lines(self, text):
        lines = text.split('\n')
        result = [[i+1, line] for i, line in enumerate(lines)]
        a=self.separate_tokens(result)
        return(a)

    def separate_tokens(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            content = content.replace("¿", "¿ ")
            content = content.replace("INT", " INT ")
            content = content.replace("STR", " STR ")
            content = content.replace("FLT", " FLT ")
            content = content.replace("CHR", " CHR ")
            content = content.replace("BOL", " BOL ")
            content = content.replace("SND", " SND ")
            content = content.replace("INS", " INS ")
            content = content.replace(":", " :")
            content = content.replace(",", " , ")
            content = content.replace(";", " ; ")
            content = content.replace("?", " ? ")
            content = content.replace("#", " # ")
            content = content.replace("\"", " \" ")

            split_text[i][1] = content
        a=self.split_into_tokens(split_text)
        return(a)

    def split_into_tokens(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            content = content.split()
            split_text[i][1] = content

        a=self.eliminate_coments(split_text)
        return (a)
    def eliminate_coments(self, split_text):
        for i in range(len(split_text)):
            content = split_text[i][1]
            
            for j in range(len(content)):
                if content[j] == "#":
                    content = content[:j+1]
                    break
            split_text[i][1] = content

        a = self.eliminate_messages(split_text)
        return (a)
    def eliminate_messages(self, split_text):
        for my_list in split_text:
            start = None
            end = None
            for i, word in enumerate(my_list[1]):
                if word == '"' and start is None:
                    start = i
                elif word == '"' and start is not None:
                    end = i
                    break
            if start is not None and end is not None:
                del my_list[1][start+1:end+1]

        return(split_text)