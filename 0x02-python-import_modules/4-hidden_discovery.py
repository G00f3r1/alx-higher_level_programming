#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    name = dir(hidden_4)
    i = 0

    while(len(name) > i):
        if name[i][:2] != "__":
            print(name[i])
        i += 1
