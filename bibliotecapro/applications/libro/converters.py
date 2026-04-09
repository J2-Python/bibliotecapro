class ValidYearsConvert:
    #expresion año mayo
    regex=r'([2-9]\d{3,}|[3-9]\d{2}|199\d)'
    
    def to_python(self,value):
        return value

    def to_url(self,value):
        return value

class TwoDigitsNumber():
        regex='[0-9]+'
        def to_python(self,value):
            #convierte el valor que ingresaron a entero
            
            number=int(value)
            if number > 15:
                return number
            else:
                raise ValueError('error de numero')
            return value
        def to_url(self,value):
            return value