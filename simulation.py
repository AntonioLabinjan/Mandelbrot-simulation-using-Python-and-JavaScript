import matplotlib.pylab as plt
window_size = 300
center = window_size/2
atoms = []
mat = []
for y in range(window_size):
    mat.append([])
    for x in range(window_size):
        mat[y].append(0)
        dx = (x-center)/1000-0.12
        dy = (y-center)/1000-0.82
        a = dx
        b = dy
        for t in range(50):
            d = (a*a)-(b*b)+dx
            b = 2*(a*b)+dy
            a = d
            H = d > 200
            if(H==True):
                mat[y][x] = t
plt.imshow(mat)