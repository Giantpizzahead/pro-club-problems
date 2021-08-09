N = int(input())

links = [int(x) - 1 for x in input().split()]

curr_site = 0
links_followed = 0
while curr_site != N-1:
    curr_site = links[curr_site]
    links_followed += 1

print(links_followed)
