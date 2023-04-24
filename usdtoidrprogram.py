def main():
    print("Convert USD to IDR")
    print(18*"=")
    usd = float(input("input your USD : "))
    print("your money :", usd, "USD")
    idr = convert_to_idr(usd)
    print("convert to idr",  idr, "USD")
    print(18*"=")   

def convert_to_idr(usd):
    return usd * 15500.00

main()