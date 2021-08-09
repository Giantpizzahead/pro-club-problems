N = int(input())

for i in range(N):
    # Get Elsie's gesture for this game
    gesture = input().strip()
    # Print out the gesture Bessie should play
    if gesture == "hoof":
        print("paper")
    elif gesture == "paper":
        print("scissors")
    else:
        print("hoof")
