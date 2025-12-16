try:
    while True:
        expr=input("enter numbers and expressions:")
        if expr.lower() == 'E':
            print("Exintg...")
            break
        try:
           print(float(eval(expr)))
        except ZeroDivisionError:
           print("denominator should not be 0")
        except Exception as e:
           print("enter only numbers and math operators!")
finally:
    print("this will executes always")