from opensimplex import OpenSimplex
from PIL import Image
import numpy as np
import shutil


shape = (300,300)
tmp = OpenSimplex()
particles=[[150,150]for i in range(100)]
precision=50

for frame in range(10):
	outimage=[[(0,0,0) for j in range(shape[1])] for i in range(shape[0])]
	for p_index, p_val in enumerate(particles):
		nx=tmp.noise2d(x=frame/precision,y=p_index)
		x=int(np.interp(nx,[-1,1],[0,300]))
		ny=tmp.noise2d(x=frame/precision,y=p_index+100)
		y=int(np.interp(ny,[-1,1],[300,0]))
		particles[p_index]=[x,y]


	for p_index, p_val in enumerate(particles):
		outimage[p_val[0]][p_val[1]]=(255,255,255)

	outimage = np.array(outimage, dtype=np.uint8)
	img = Image.fromarray(outimage)
	img.save("images/dotnoise"+str(frame)+".png")

print("DONE")

shutil.make_archive("comimages", 'zip', "images")
