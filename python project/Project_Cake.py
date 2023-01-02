def Equal_Pieces(N, Cake):
    if Cake % N == 0:
        print("Yes, Cake can be cut into", N, "equal pieces")
        print(f"Yes, Cake can be cut into {N} equal pieces")
    else:
        print("No, Cake can't be cut into", N, "equal pieces")
        print(f"No, Cake can't be cut into {N} equal pieces")


def Any_Size_Pieces(N, Cake):
    if N <= Cake:
        print("Yes, Cake can be cut into", N, "pieces of any size")
        print(f"Yes, Cake can be cut into {N} pieces of any size")
    else:
        print("No, Cake can't be cut into", N, "pieces of any size")
        print(f"No, Cake can't be cut into {N} pieces of any size")


def No_Two_Pieces_Equal(N, Cake):
    if N * (N + 1 / 2) <= Cake:
        print("Yes, Cake can be cut into", N, "pieces such that no two of them are equal")
        print(f"Yes, Cake can be cut into {N} pieces such that no two of them are equal")
    else:
        print("No, Cake can't be cut into", N, "pieces such that no two of them are equal")
        print(f"No, Cake can't be cut into {N} pieces such that no two of them are equal")


N = int(input("Enter The Number Of Cuts To be Made: "))
Cake = 360
Equal_Pieces(N, Cake)

Any_Size_Pieces(N, Cake)

No_Two_Pieces_Equal(N,Cake)