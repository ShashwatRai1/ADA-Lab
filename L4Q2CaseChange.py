#code to print all th permutation 

def permute(input, output):
    if len(input)==0:
        print(output, end=" ")
        return
    ch= input[0].lower()
    ch2= input[0].upper()
    input = input[1:]
    permute(input, output+ch)
    permute(input, output+ch2)

def main():
    input = "A1B"
    permute(input, " ")

main()