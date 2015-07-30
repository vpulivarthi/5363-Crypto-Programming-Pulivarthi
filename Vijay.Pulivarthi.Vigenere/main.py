import argparse
import sys
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", type=str, default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", type=int, help="Integer seed")

    args = parser.parse_args()

    f = open(args.inputFile,'r')
    message = f.read()
    if(args.mode == 'encrypt'):
        data = rv.encrypt(message,args.seed)
    else:
        data = rv.decrypt(message,args.seed)
    o = open(args.outputFile,'w')
    o.write(str(data))


if __name__ == '__main__':
    main()
