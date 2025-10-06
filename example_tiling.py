from makeGif import *
from patchBasedTextureSynthesis import *

exampleMapPath = "imgs/1.jpg"
outputPath = "out/1/"
patchSize = 50 #size of the patch (without the overlap)
overlapSize = 10 #the width of the overlap region
outputSize = [300,300]

pbts = patchBasedTextureSynthesis(
	exampleMapPath,
	outputPath,
	outputSize,
	patchSize,
	overlapSize,
	in_windowStep = 5,
	in_mirror_hor = True,
	in_mirror_vert = True,
	in_shapshots = True,
	in_live_updates = False,
	in_tiling_hor = True,
	in_tiling_vert = True
)
pbts.resolveAll()
