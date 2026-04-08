class ValidYearsConvert:
    #expresion año mayo
    regex=r'^(199[1-9]|20\d{2}|[3-9]\d{3})$'
    
    def to_python(self,value):
        return value

    def to_url(self,value):
        return value