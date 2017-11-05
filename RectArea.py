"""
https://leetcode.com/problems/rectangle-area/description/

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
"""

# know right > left
def compute_area(A, B, C, D, E, F, G, H):
    # check if rects overlap 
    overlap = x = y = total = 0
    if E >= C or G <= A:
        overlap = 0
    elif F >= D or H <= B:
        overlap = 0
    else: 
        # 4 cases
        # R1 x inside R2 
        # R1 right x inside R2 
        # R1 left x inside R2
        # R1 x outside R2 
        if A >= E and C <= G:
            x = C - A 
        elif E <= C <= G:
            x = C - E 
        elif E <= A <= G:
            x = G - A
        else:
            x = G - E

        # 4 cases
        # R1 y inside R2 
        # R1 top y inside R2 
        # R1 bottom y inside R2
        # R1 y outside R2 
        if B >= F and D <= H:
            y = D - B
        elif F <= D <= H:
            y = D - F
        elif F <= B <= H:
            y = H - B
        else:
            y = H - F

    overlap = x * y
    total = (C-A)*(D-B) + (G-E)*(H-F) - overlap
    return total

def compute_area_short(A, B, C, D, E, F, G, H):
    # check if rects overlap 
    overlap = x = y = total = 0
    if E >= C or G <= A:
        overlap = 0
    elif F >= D or H <= B:
        overlap = 0
    else: 
        x = min(G, C) - max(E, A)
        y = min(D, H) - max(B, F)
    
    overlap = x * y
    total = (C-A)*(D-B) + (G-E)*(H-F) - overlap
    return total 

def main():
    print(compute_area(-3, 0, 3, 4, 0, -1, 9, 2)) # 45
    print(compute_area(-2, -2, 2, 2, 3, -4, 4, -3)) # 17 
    print(compute_area(-5, 4, 0, 5, -3, -3, 3, 3)) # 41
    print(compute_area_short(-3, 0, 3, 4, 0, -1, 9, 2)) # 45
    print(compute_area_short(-2, -2, 2, 2, 3, -4, 4, -3)) # 17 
    print(compute_area_short(-5, 4, 0, 5, -3, -3, 3, 3)) # 41

if __name__ == '__main__':
    main()
