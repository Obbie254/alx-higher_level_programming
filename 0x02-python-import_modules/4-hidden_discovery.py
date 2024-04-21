#!bin/usr/python3
if __name__ == "__main__":
    import hidden_4
    nam = dir(hidden_4)
    for i in range(len(nam)):
        if (nam[i][:2] != "__"):
            print(nam[i])
