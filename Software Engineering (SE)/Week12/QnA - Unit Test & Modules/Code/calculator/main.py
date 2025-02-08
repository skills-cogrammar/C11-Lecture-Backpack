from utils.calc import Calc

calculator = Calc()

def main():
    num_1 = 5
    num_2 = 0
    print(f"The operation add produces: {calculator.add(num_1, num_2)}")
    print(f"The operation mult produces: {calculator.mult(num_1, num_2)}")
    try:
        print(f"The operation div produces: {calculator.div(num_1, num_2)}")
    except ZeroDivisionError as e:
        print("Div by 0")
    print(f"The operation sub produces: {calculator.sub(num_1, num_2)}")

if __name__ == "__main__":
    main()